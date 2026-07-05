<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>朝の市場ダッシュボード | 雰囲気投資家ひるね</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #10131a;
    --bg-panel: #171b24;
    --bg-panel-hover: #1c212c;
    --border: #262b38;
    --text-primary: #e8eaf0;
    --text-muted: #8890a0;
    --text-faint: #5b6273;
    --accent-good: #5fbf8f;
    --accent-good-bg: rgba(95, 191, 143, 0.12);
    --accent-warn: #e0a458;
    --accent-warn-bg: rgba(224, 164, 88, 0.12);
    --accent-bad: #d9695f;
    --accent-bad-bg: rgba(217, 105, 95, 0.12);
    --accent-gray: #5b6273;
    --accent-gray-bg: rgba(91, 98, 115, 0.12);
    --brand: #8fa6d9;
    --font-display: "Zen Kaku Gothic New", sans-serif;
    --font-mono: "JetBrains Mono", monospace;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--text-primary);
    font-family: var(--font-display);
    -webkit-font-smoothing: antialiased;
  }

  body {
    background-image:
      radial-gradient(ellipse 900px 500px at 15% -10%, rgba(143, 166, 217, 0.10), transparent 60%),
      radial-gradient(ellipse 700px 400px at 100% 0%, rgba(95, 191, 143, 0.06), transparent 60%);
    background-attachment: fixed;
  }

  .wrap {
    max-width: 1120px;
    margin: 0 auto;
    padding: 32px 20px 80px;
  }

  /* ---------- header ---------- */
  .top-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 22px;
    flex-wrap: wrap;
    gap: 8px;
  }
  .site-name {
    font-size: 13px;
    color: var(--text-faint);
    letter-spacing: 0.05em;
  }
  .timestamp {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--text-faint);
  }

  /* ---------- hero: weather ---------- */
  .hero {
    position: relative;
    background: linear-gradient(180deg, var(--bg-panel), var(--bg-panel) 60%, #151922);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 36px 40px;
    margin-bottom: 28px;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 32px;
  }
  .hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 85% 20%, rgba(143,166,217,0.15), transparent 55%);
    pointer-events: none;
  }
  .hero-icon {
    width: 84px;
    height: 84px;
    flex-shrink: 0;
    filter: drop-shadow(0 0 18px rgba(143,166,217,0.35));
  }
  .hero-text .eyebrow {
    font-size: 12px;
    color: var(--text-faint);
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }
  .hero-text h1 {
    font-size: 30px;
    font-weight: 900;
    margin: 0 0 8px;
    letter-spacing: 0.02em;
  }
  .hero-text p.comment {
    font-size: 14px;
    color: var(--text-muted);
    margin: 0;
    line-height: 1.7;
    max-width: 60ch;
  }

  /* ---------- section grid ---------- */
  .section-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--text-muted);
    letter-spacing: 0.06em;
    margin: 30px 0 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .section-title .emoji { font-size: 15px; }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 12px;
  }

  .metric-card {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px 18px;
    transition: border-color 0.15s ease, background 0.15s ease;
  }
  .metric-card:hover {
    background: var(--bg-panel-hover);
    border-color: #313847;
  }

  .metric-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 10px;
  }
  .metric-label {
    font-size: 13px;
    color: var(--text-muted);
    font-weight: 500;
  }
  .badge {
    font-size: 11px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 999px;
    white-space: nowrap;
  }
  .badge.good { color: var(--accent-good); background: var(--accent-good-bg); }
  .badge.warn { color: var(--accent-warn); background: var(--accent-warn-bg); }
  .badge.bad  { color: var(--accent-bad);  background: var(--accent-bad-bg); }
  .badge.gray { color: var(--accent-gray); background: var(--accent-gray-bg); }

  .metric-value {
    font-family: var(--font-mono);
    font-size: 22px;
    font-weight: 700;
    letter-spacing: -0.01em;
  }
  .metric-change {
    font-family: var(--font-mono);
    font-size: 13px;
    margin-left: 8px;
  }
  .metric-change.pos { color: var(--accent-good); }
  .metric-change.neg { color: var(--accent-bad); }

  .stars {
    margin-top: 10px;
    font-size: 13px;
    letter-spacing: 2px;
    color: var(--text-faint);
  }
  .stars .filled { color: var(--brand); }

  .metric-error {
    font-size: 12px;
    color: var(--text-faint);
    font-style: italic;
  }

  /* ---------- news / events panels ---------- */
  .panel {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px 24px;
  }
  .panel + .panel { margin-top: 14px; }
  .panel h3 {
    margin: 0 0 12px;
    font-size: 14px;
    color: var(--text-muted);
    font-weight: 700;
  }
  .headline-row {
    display: flex;
    align-items: baseline;
    gap: 10px;
    padding: 9px 0;
    border-bottom: 1px solid var(--border);
    font-size: 14px;
    line-height: 1.6;
  }
  .headline-row:last-child { border-bottom: none; }
  .headline-source {
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-faint);
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 2px 6px;
    flex-shrink: 0;
    white-space: nowrap;
  }
  .headline-title { color: var(--text-primary); }

  .event-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
    font-size: 14px;
  }
  .event-row:last-child { border-bottom: none; }
  .event-time {
    font-family: var(--font-mono);
    color: var(--text-faint);
    width: 56px;
    flex-shrink: 0;
  }
  .event-importance {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent-warn);
    flex-shrink: 0;
  }
  .no-events {
    font-size: 13px;
    color: var(--text-faint);
  }

  .footer-note {
    margin-top: 36px;
    font-size: 11px;
    color: var(--text-faint);
    text-align: center;
    line-height: 1.8;
  }

  .loading, .load-error {
    text-align: center;
    padding: 80px 20px;
    color: var(--text-faint);
    font-size: 13px;
  }

  @media (max-width: 640px) {
    .hero { flex-direction: column; align-items: flex-start; padding: 28px 24px; }
    .hero-text h1 { font-size: 24px; }
  }
</style>
</head>
<body>

<div class="wrap" id="app">
  <div class="loading" id="loading-msg">読み込み中...</div>
</div>

<script>
const WEATHER_ICONS = {
  sunny: `<svg viewBox="0 0 100 100" fill="none"><circle cx="50" cy="50" r="22" fill="#e0a458"/><g stroke="#e0a458" stroke-width="4" stroke-linecap="round"><line x1="50" y1="8" x2="50" y2="20"/><line x1="50" y1="80" x2="50" y2="92"/><line x1="8" y1="50" x2="20" y2="50"/><line x1="80" y1="50" x2="92" y2="50"/><line x1="19" y1="19" x2="27" y2="27"/><line x1="73" y1="73" x2="81" y2="81"/><line x1="81" y1="19" x2="73" y2="27"/><line x1="27" y1="73" x2="19" y2="81"/></g></svg>`,
  partly_cloudy: `<svg viewBox="0 0 100 100" fill="none"><circle cx="38" cy="42" r="16" fill="#e0a458"/><ellipse cx="58" cy="60" rx="28" ry="18" fill="#8fa6d9" opacity="0.85"/><ellipse cx="40" cy="66" rx="18" ry="12" fill="#8fa6d9" opacity="0.7"/></svg>`,
  cloudy: `<svg viewBox="0 0 100 100" fill="none"><ellipse cx="55" cy="52" rx="30" ry="19" fill="#6c7a94"/><ellipse cx="35" cy="60" rx="20" ry="14" fill="#6c7a94" opacity="0.8"/><ellipse cx="65" cy="62" rx="18" ry="12" fill="#5b6273" opacity="0.9"/></svg>`,
  rain: `<svg viewBox="0 0 100 100" fill="none"><ellipse cx="52" cy="42" rx="28" ry="17" fill="#5b6273"/><ellipse cx="34" cy="50" rx="18" ry="12" fill="#5b6273" opacity="0.85"/><g stroke="#8fa6d9" stroke-width="4" stroke-linecap="round"><line x1="35" y1="70" x2="30" y2="84"/><line x1="52" y1="70" x2="47" y2="84"/><line x1="69" y1="70" x2="64" y2="84"/></g></svg>`,
  storm: `<svg viewBox="0 0 100 100" fill="none"><ellipse cx="50" cy="38" rx="30" ry="17" fill="#3a4050"/><g stroke="#d9695f" stroke-width="4" stroke-linecap="round"><line x1="30" y1="66" x2="26" y2="80"/><line x1="70" y1="66" x2="66" y2="80"/></g><polygon points="52,58 42,78 50,78 44,94 62,70 52,70" fill="#e0a458"/></svg>`,
};

function starString(n) {
  if (n === null || n === undefined) return '<span class="metric-error">評価不可</span>';
  let out = '';
  for (let i = 1; i <= 5; i++) {
    out += i <= n ? '<span class="filled">★</span>' : '☆';
  }
  return out;
}

function badge(judgment) {
  if (!judgment || !judgment.color) return '';
  return `<span class="badge ${judgment.color}">${judgment.label}</span>`;
}

function changeSpan(chg) {
  if (chg === null || chg === undefined) return '';
  const cls = chg > 0 ? 'pos' : (chg < 0 ? 'neg' : '');
  const sign = chg > 0 ? '+' : '';
  return `<span class="metric-change ${cls}">${sign}${chg.toFixed(2)}%</span>`;
}

function metricCard(m) {
  if (!m.ok && m.value === undefined) {
    return `
      <div class="metric-card">
        <div class="metric-top">
          <span class="metric-label">${m.label}</span>
          ${badge(m.judgment)}
        </div>
        <div class="metric-error">データ取得に失敗しました</div>
      </div>`;
  }
  const valueDisplay = (m.value !== null && m.value !== undefined)
    ? m.value.toLocaleString('en-US', {maximumFractionDigits: 2})
    : '—';
  const changeDisplay = m.change_pct !== undefined ? changeSpan(m.change_pct) : (m.change_bp !== undefined ? `<span class="metric-change ${m.change_bp>0?'pos':(m.change_bp<0?'neg':'')}">${m.change_bp>0?'+':''}${m.change_bp}bp</span>` : '');
  return `
    <div class="metric-card">
      <div class="metric-top">
        <span class="metric-label">${m.label}</span>
        ${badge(m.judgment)}
      </div>
      <div><span class="metric-value">${valueDisplay}</span>${changeDisplay}</div>
      <div class="stars">${starString(m.judgment ? m.judgment.stars : null)}</div>
    </div>`;
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

function newsHeadlinesHtml(news) {
  if (!news || !news.headlines || news.headlines.length === 0) {
    return '<div class="no-events">本日は見出しを取得できませんでした。</div>';
  }
  return news.headlines.map(h => `
    <div class="headline-row">
      <span class="headline-source">${escapeHtml(h.source)}</span>
      <span class="headline-title">${escapeHtml(h.title)}</span>
    </div>`).join('');
}

function section(titleEmoji, titleText, entries) {
  const cards = Object.values(entries).map(metricCard).join('');
  return `
    <div class="section-title"><span class="emoji">${titleEmoji}</span>${titleText}</div>
    <div class="card-grid">${cards}</div>`;
}

function render(data) {
  const app = document.getElementById('app');
  const genDate = new Date(data.generated_at);
  const genDateStr = genDate.toLocaleString('ja-JP', { timeZone: 'Asia/Tokyo', hour12: false });

  const weather = data.weather || {};
  const weatherIcon = WEATHER_ICONS[weather.weather] || WEATHER_ICONS.partly_cloudy;

  let eventsHtml = '<div class="no-events">本日の主要指標発表はありません。</div>';
  if (data.events_today && data.events_today.length > 0) {
    eventsHtml = data.events_today.map(e => `
      <div class="event-row">
        <span class="event-time">${e.time || '--:--'}</span>
        <span class="event-importance"></span>
        <span>${e.name}</span>
      </div>`).join('');
  }

  app.innerHTML = `
    <div class="top-row">
      <span class="site-name">雰囲気投資家ひるね ― 朝の市場ダッシュボード</span>
      <span class="timestamp">最終更新: ${genDateStr} JST</span>
    </div>

    <div class="hero">
      <div class="hero-icon">${weatherIcon}</div>
      <div class="hero-text">
        <div class="eyebrow">今朝の空模様</div>
        <h1>${weather.label || '---'}</h1>
        <p class="comment">${weather.comment || ''}</p>
      </div>
    </div>

    ${section('🌍', '世界', data.world)}
    ${section('💴', '為替', data.fx)}
    ${section('📈', '金利', data.rates)}
    ${section('⚡', 'セクター', data.sectors)}
    ${section('🛢', 'コモディティ', data.commodities)}
    ${section('😨', 'リスク', data.risk)}

    <div class="section-title"><span class="emoji">📰</span>ニュース</div>
    <div class="panel">
      <h3>主要見出し(本日 ${data.news ? data.news.headline_count : 0} 件)</h3>
      ${newsHeadlinesHtml(data.news)}
    </div>

    <div class="section-title"><span class="emoji">📅</span>今日のイベント</div>
    <div class="panel">
      ${eventsHtml}
    </div>

    <div class="footer-note">
      本ダッシュボードの判定は機械的なルールに基づく簡易的な目安であり、投資判断を保証するものではありません。<br>
      放置・退屈が正義。地合いが荒れていても、保有方針を急いで変える必要はありません。
    </div>
  `;
}

fetch('data.json?_=' + Date.now())
  .then(res => {
    if (!res.ok) throw new Error('data.json not found');
    return res.json();
  })
  .then(render)
  .catch(err => {
    document.getElementById('app').innerHTML = `
      <div class="load-error">
        data.json の読み込みに失敗しました。<br>
        GitHub Actions がまだ一度も実行されていないか、パスが誤っている可能性があります。<br>
        <span style="font-family: var(--font-mono); font-size: 11px;">${err.message}</span>
      </div>`;
  });
</script>

</body>
</html>
