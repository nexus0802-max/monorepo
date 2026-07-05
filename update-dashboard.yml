#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
朝の市場ダッシュボード用データ取得スクリプト
- yfinance: 指数/セクター/コモディティ/VIX/為替
- FRED CSV (無料・APIキー不要): 米10年・2年金利
- RSS + Claude API: ニュースAI要約
- events.json: 手動キュレーションの経済指標カレンダー(当日分を抽出)

出力: data.json (index.html が読み込む)
"""

import json
import time
import traceback
from datetime import datetime
from zoneinfo import ZoneInfo

import requests
import yfinance as yf

JST = ZoneInfo("Asia/Tokyo")

# ------------------------------------------------------------
# ティッカー定義
# ------------------------------------------------------------
WORLD_TICKERS = {
    "sp500": {"label": "S&P500", "symbol": "^GSPC"},
    "nasdaq100": {"label": "NASDAQ100", "symbol": "^NDX"},
    "russell2000": {"label": "ラッセル2000", "symbol": "^RUT"},
    "nikkei_fut": {"label": "日経225先物", "symbol": "NIY=F"},
    "topix": {"label": "TOPIX(1306連動)", "symbol": "1306.T"},
}

FX_TICKERS = {
    "usdjpy": {"label": "ドル円", "symbol": "JPY=X"},
    "dxy": {"label": "ドルインデックス", "symbol": "DX-Y.NYB"},
}

SECTOR_TICKERS = {
    "sox": {"label": "SOX(半導体)", "symbol": "^SOX"},
    "banks": {"label": "銀行(KBE)", "symbol": "KBE"},
    "energy": {"label": "エネルギー(XLE)", "symbol": "XLE"},
}

COMMODITY_TICKERS = {
    "oil": {"label": "原油(WTI)", "symbol": "CL=F"},
    "gold": {"label": "金", "symbol": "GC=F"},
    "copper": {"label": "銅", "symbol": "HG=F"},
}

RISK_TICKERS = {
    "vix": {"label": "VIX", "symbol": "^VIX"},
}

# FRED (APIキー不要のCSVエンドポイント)
FRED_SERIES = {
    "us10y": "DGS10",
    "us2y": "DGS2",
}
FRED_CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"


# ------------------------------------------------------------
# ユーティリティ
# ------------------------------------------------------------
def safe_round(x, nd=2):
    try:
        return round(float(x), nd)
    except (TypeError, ValueError):
        return None


def fetch_yf_metric(symbol, ma_windows=(20, 50)):
    """直近値・前日比・移動平均乖離を取得"""
    try:
        hist = yf.Ticker(symbol).history(period="4mo", interval="1d")
        if hist.empty or len(hist) < 3:
            raise ValueError("empty history")
        closes = hist["Close"].dropna()
        last = closes.iloc[-1]
        prev = closes.iloc[-2]
        change_pct = (last - prev) / prev * 100

        ma_status = {}
        for w in ma_windows:
            if len(closes) >= w:
                ma = closes.rolling(w).mean().iloc[-1]
                ma_status[f"above_ma{w}"] = bool(last > ma)
            else:
                ma_status[f"above_ma{w}"] = None

        return {
            "value": safe_round(last, 2),
            "change_pct": safe_round(change_pct, 2),
            **ma_status,
            "ok": True,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def fetch_fred_yield(series_id):
    """FREDから金利を取得(直近2営業日分の変化を計算)"""
    try:
        url = FRED_CSV_URL.format(series=series_id)
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        lines = [l for l in resp.text.strip().splitlines() if l]
        rows = [l.split(",") for l in lines[1:]]  # header除く
        # 欠損値(".")を除外
        rows = [r for r in rows if len(r) == 2 and r[1] != "."]
        if len(rows) < 2:
            raise ValueError("not enough data")
        last_val = float(rows[-1][1])
        prev_val = float(rows[-2][1])
        change_bp = (last_val - prev_val) * 100  # %ポイント→bp
        return {
            "value": safe_round(last_val, 3),
            "change_bp": safe_round(change_bp, 1),
            "date": rows[-1][0],
            "ok": True,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


# ------------------------------------------------------------
# 判定(★スコア + 色)ロジック
# ------------------------------------------------------------
def judge_trend(metric):
    """指数/セクター系: 騰落 + 移動平均で5段階判定"""
    if not metric.get("ok"):
        return {"stars": None, "color": "gray", "label": "取得失敗"}

    chg = metric["change_pct"]
    above20 = metric.get("above_ma20")
    above50 = metric.get("above_ma50")
    ma_score = sum(1 for v in (above20, above50) if v is True)

    if chg is None:
        return {"stars": None, "color": "gray", "label": "データ不足"}

    if chg > 1.0 and ma_score == 2:
        stars, color, label = 5, "good", "絶好調"
    elif chg > 0 and ma_score == 2:
        stars, color, label = 4, "good", "良好"
    elif (chg > 0 and ma_score >= 1) or (chg <= 0 and ma_score == 2):
        stars, color, label = 3, "warn", "中立"
    elif chg <= 0 and ma_score == 1:
        stars, color, label = 2, "warn", "軟調"
    else:
        stars, color, label = 1, "bad", "警戒"

    return {"stars": stars, "color": color, "label": label}


def judge_volatility_flag(metric, threshold=2.5):
    """為替/コモディティ: 良し悪しでなく変動幅で注意喚起"""
    if not metric.get("ok"):
        return {"stars": None, "color": "gray", "label": "取得失敗"}
    chg = metric["change_pct"]
    if chg is None:
        return {"stars": None, "color": "gray", "label": "データ不足"}
    abs_chg = abs(chg)
    if abs_chg >= threshold * 1.6:
        return {"stars": 1, "color": "bad", "label": "急変動"}
    elif abs_chg >= threshold:
        return {"stars": 2, "color": "warn", "label": "やや荒い"}
    else:
        return {"stars": 4, "color": "good", "label": "平常"}


def judge_vix(metric):
    if not metric.get("ok"):
        return {"stars": None, "color": "gray", "label": "取得失敗"}
    v = metric["value"]
    if v is None:
        return {"stars": None, "color": "gray", "label": "データ不足"}
    if v < 15:
        return {"stars": 5, "color": "good", "label": "落ち着いている"}
    elif v < 18:
        return {"stars": 4, "color": "good", "label": "平常"}
    elif v < 22:
        return {"stars": 3, "color": "warn", "label": "やや神経質"}
    elif v < 28:
        return {"stars": 2, "color": "warn", "label": "警戒"}
    else:
        return {"stars": 1, "color": "bad", "label": "リスクオフ"}


def judge_rate_move(metric):
    if not metric.get("ok"):
        return {"stars": None, "color": "gray", "label": "取得失敗"}
    bp = metric["change_bp"]
    if bp is None:
        return {"stars": None, "color": "gray", "label": "データ不足"}
    abs_bp = abs(bp)
    if abs_bp < 3:
        return {"stars": 4, "color": "good", "label": "安定"}
    elif abs_bp < 7:
        return {"stars": 3, "color": "warn", "label": "やや動意"}
    elif abs_bp < 12:
        return {"stars": 2, "color": "warn", "label": "荒い動き"}
    else:
        return {"stars": 1, "color": "bad", "label": "急変動"}


def judge_spread(spread_value):
    if spread_value is None:
        return {"stars": None, "color": "gray", "label": "データ不足"}
    if spread_value > 0.5:
        return {"stars": 5, "color": "good", "label": "健全な順イールド"}
    elif spread_value > 0:
        return {"stars": 4, "color": "good", "label": "順イールド"}
    elif spread_value > -0.3:
        return {"stars": 2, "color": "warn", "label": "逆イールド"}
    else:
        return {"stars": 1, "color": "bad", "label": "深い逆イールド"}


# ------------------------------------------------------------
# 全体の空模様(天気)判定
# ------------------------------------------------------------
def judge_weather(vix_metric, world_judgments, spread_value):
    if not vix_metric.get("ok"):
        return {"weather": "cloudy", "label": "データ取得不調", "comment": "一部データが取得できませんでした。手動で確認してください。"}

    vix = vix_metric["value"]
    good_count = sum(1 for j in world_judgments if j.get("color") == "good")
    bad_count = sum(1 for j in world_judgments if j.get("color") == "bad")
    total = len(world_judgments) or 1

    deep_inversion = spread_value is not None and spread_value < -0.3

    if vix is not None and vix > 32 and bad_count >= total / 2:
        return {"weather": "storm", "label": "嵐", "comment": "リスクオフ色が強い朝です。無理にポジションを動かす必要はありません。"}
    if vix is not None and vix > 26 or bad_count > total / 2:
        return {"weather": "rain", "label": "雨", "comment": "やや荒れ模様。保有株は放置でOK、システム系はフィルター条件を再確認。"}
    if deep_inversion or (vix is not None and 20 <= vix <= 26):
        return {"weather": "cloudy", "label": "曇り", "comment": "神経質な地合い。急いで動く場面ではなさそうです。"}
    if vix is not None and vix < 18 and good_count >= total / 2:
        return {"weather": "sunny", "label": "晴れ", "comment": "落ち着いた地合い。普段どおりで大丈夫です。"}
    return {"weather": "partly_cloudy", "label": "薄曇り", "comment": "強弱まちまち。いつもどおり淡々と。"}


# ------------------------------------------------------------
# ニュース見出し取得 (RSS)
# API不使用: 取得した見出しをそのまま重複除去・整形して表示する
# ------------------------------------------------------------
NEWS_RSS_FEEDS = [
    {"name": "WSJ Markets", "url": "https://feeds.a.dj.com/rss/RSSMarketsMain.xml"},
    {"name": "Reuters Business", "url": "https://www.reutersagency.com/feed/?best-topics=business-finance"},
]


def fetch_news_headlines(max_per_feed=8, max_total=12):
    import xml.etree.ElementTree as ET

    headlines = []
    seen = set()
    for feed in NEWS_RSS_FEEDS:
        try:
            resp = requests.get(feed["url"], timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            for item in root.findall(".//item")[:max_per_feed]:
                title = item.findtext("title")
                if not title:
                    continue
                title = title.strip()
                key = title.lower()
                if key in seen:
                    continue
                seen.add(key)
                headlines.append({"source": feed["name"], "title": title})
        except Exception:
            continue
    return headlines[:max_total]


# ------------------------------------------------------------
# 今日のイベント(手動キュレーションJSONから当日分抽出)
# ------------------------------------------------------------
def load_todays_events(path="events.json"):
    try:
        with open(path, encoding="utf-8") as f:
            events = json.load(f)
    except Exception:
        events = []
    today_str = datetime.now(JST).strftime("%Y-%m-%d")
    return [e for e in events if e.get("date") == today_str]


# ------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------
def build_section(tickers, judge_func):
    out = {}
    for key, meta in tickers.items():
        metric = fetch_yf_metric(meta["symbol"])
        judgment = judge_func(metric)
        out[key] = {"label": meta["label"], "symbol": meta["symbol"], **metric, **{"judgment": judgment}}
    return out


def main():
    world = build_section(WORLD_TICKERS, judge_trend)
    fx = build_section(FX_TICKERS, judge_volatility_flag)
    sectors = build_section(SECTOR_TICKERS, judge_trend)
    commodities = build_section(COMMODITY_TICKERS, judge_volatility_flag)
    risk = build_section(RISK_TICKERS, judge_vix)

    us10y = fetch_fred_yield(FRED_SERIES["us10y"])
    us2y = fetch_fred_yield(FRED_SERIES["us2y"])
    spread_value = None
    if us10y.get("ok") and us2y.get("ok"):
        spread_value = safe_round(us10y["value"] - us2y["value"], 3)

    rates = {
        "us10y": {"label": "米10年債", **us10y, "judgment": judge_rate_move(us10y)},
        "us2y": {"label": "米2年債", **us2y, "judgment": judge_rate_move(us2y)},
        "spread": {
            "label": "10Y-2Yスプレッド",
            "value": spread_value,
            "judgment": judge_spread(spread_value),
        },
    }

    world_judgments = [v["judgment"] for v in world.values()]
    weather = judge_weather(risk["vix"], world_judgments, spread_value)

    headlines = fetch_news_headlines()

    events_today = load_todays_events()

    data = {
        "generated_at": datetime.now(JST).isoformat(),
        "weather": weather,
        "world": world,
        "fx": fx,
        "rates": rates,
        "sectors": sectors,
        "commodities": commodities,
        "risk": risk,
        "news": {"headlines": headlines, "headline_count": len(headlines)},
        "events_today": events_today,
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("data.json を出力しました。")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        raise
