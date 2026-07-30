"""
配当利回り・配当支払月の自動取得スクリプト

codes.json に記載した銘柄コード一覧をもとに yfinance で配当情報を取得し、
dividends.json に出力する。JPX400スクリーナー等と同じ構成
（GitHub Actions で定期実行 → GitHub Pages で公開）を想定。

codes.json の書式:
  ["7203", "9432", "1489", "AAPL", "VYM"]
  - 日本株/JP-ETFは4桁の証券コードのみでOK（内部で ".T" を付与）
  - 米国株/ETFはティッカーそのまま

出力される dividends.json の書式:
  {
    "7203": {"yield": 3.2, "months": [3, 9], "updated": "2026-07-30"},
    "AAPL": {"yield": 0.5, "months": [2, 5, 8, 11], "updated": "2026-07-30"}
  }
"""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("yfinance がインストールされていません: pip install yfinance", file=sys.stderr)
    sys.exit(1)

CODES_FILE = Path(__file__).parent / "codes.json"
OUTPUT_FILE = Path(__file__).parent / "dividends.json"


def to_yf_symbol(code: str) -> str:
    """日本株の4桁コードには .T を付与。それ以外(米国株ティッカー等)はそのまま。"""
    code = code.strip()
    if code.isdigit() and len(code) == 4:
        return f"{code}.T"
    return code


def fetch_one(code: str) -> dict | None:
    symbol = to_yf_symbol(code)
    try:
        t = yf.Ticker(symbol)
        info = t.info or {}
        yield_pct = None
        # yfinanceのバージョンによりキー名が異なるため両方試す
        for key in ("dividendYield", "trailingAnnualDividendYield"):
            v = info.get(key)
            if v:
                yield_pct = round(v * 100, 2) if v < 1 else round(v, 2)
                break

        months = []
        try:
            divs = t.dividends
            if divs is not None and len(divs) > 0:
                cutoff = datetime.now(divs.index.tz) - timedelta(days=400)
                recent = divs[divs.index >= cutoff]
                months = sorted(set(int(d.month) for d in recent.index))
        except Exception:
            pass

        if yield_pct is None and not months:
            return None
        return {
            "yield": yield_pct or 0,
            "months": months,
            "updated": datetime.now().strftime("%Y-%m-%d"),
        }
    except Exception as e:
        print(f"  [warn] {code} ({symbol}) 取得失敗: {e}", file=sys.stderr)
        return None


def main():
    if not CODES_FILE.exists():
        print(f"{CODES_FILE} が見つかりません。銘柄コードの配列をJSONで用意してください。", file=sys.stderr)
        sys.exit(1)

    codes = json.loads(CODES_FILE.read_text(encoding="utf-8"))
    result = {}
    for code in codes:
        print(f"取得中: {code}")
        data = fetch_one(code)
        if data:
            result[code] = data

    OUTPUT_FILE.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"完了: {len(result)}/{len(codes)} 件を {OUTPUT_FILE} に出力しました")


if __name__ == "__main__":
    main()
