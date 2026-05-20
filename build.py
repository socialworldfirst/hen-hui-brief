"""Producer brief for Hen Hui — context + delivery notes for the top 3 SEA picks.

Reads finalized.json + slides.json from sea-voice-iterate. /report-style HTML.
"""
import json, html, os
esc = html.escape

SRC = '/Users/steven/Documents/Claude/sea-voice-iterate'
fz = json.load(open(f'{SRC}/finalized.json'))
TITLES = {s['slide_id']: s.get('video_title', '') for s in json.load(open(f'{SRC}/slides.json'))}

TOP3 = [('P1-A9-1', 'PH2'), ('P1-A14-1', 'PH2'), ('P2-A8-1', 'PH2')]
by_key = {(e['slide_id'], e['variant_id']): e for e in fz['finalized']}

# Producer notes per script — hand-written context for Hen Hui
NOTES = {
    ('P1-A9-1', 'PH2'): {
        'shape': 'Story',
        'angle': 'The cost of a wire isn\'t the money. It\'s the time. A delayed wire = a delayed container = a missed Q4 = a competitor on the shelf.',
        'hook_power': 'Opens with a paradox — "lose a container without losing the money." Curiosity gap. Forces the viewer to keep watching to resolve the contradiction.',
        'beats': [
            'Paradox (sent on the app vs nothing in supplier\'s WhatsApp)',
            'Escalation (lost the day → the week → the order)',
            'Mechanism (supplier won\'t load raw materials until CNY hits)',
            'Compounding cost (3 intermediaries + AML + Friday holiday = 5 days)',
            'Stakes (Q4 container, launch SKU, competitor beats you to shelf)',
            'Reframe ("the wire isn\'t lost. The visibility is.")',
            'WF positioning (direct rail, same-day, tracking reference)',
        ],
        'numbers': 'Three intermediaries · two days of conversion windows · one AML hold · Friday public holiday in Shenzhen · five-day silence',
        'tone': 'Urgent but controlled. Operator-to-operator. Slight tension build. Not lecturing.',
        'visual_ideas': [
            'Talking head + B-roll: business owner refreshing bank app, no notification',
            'Factory floor with raw materials NOT being loaded (cuts to empty crates)',
            'Calendar animation: days slipping by, weekend shaded',
            'Quick screen recording: "Sent" status vs no incoming on supplier side',
            'End card: a closed container on a truck driving away (the missed shipment)',
        ],
        'length': '60 seconds',
        'cta': 'Search WorldFirst',
    },
    ('P1-A14-1', 'PH2'): {
        'shape': 'Math',
        'angle': 'Same wire, same supplier, same day, three different amounts received. The variation IS the lesson. Then compound it across a year and three years.',
        'hook_power': '"Three operators, same wire, three amounts" — promise of a clean factual reveal. Audience leans in for the numbers.',
        'beats': [
            'Setup (3 owners, same supplier, same day, same 50K wire)',
            'Reveal (49,250 / 49,700 / 49,850 — 600 dollar spread)',
            'Annual compounding (12 wires/year, 600K volume)',
            'Per-operator loss (9K bank vs 1.8K specialist)',
            'Three-year math (21,600 dollar gap)',
            'Reframe ("That\'s an employee. That\'s a container. That\'s the next product line.")',
            'Mechanism ("Not a fee. It\'s the exchange rate margin. Banks bake 1 to 2% in.")',
            'WF positioning (0.3% on same wires, same-day to Chinese banks)',
        ],
        'numbers': '49,250 / 49,700 / 49,850 · 600 · 50K · 12 wires · 600,000 volume · 9,000 loss · 1,800 loss · 7,200 gap · 21,600 over 3 years · 1-2% bank margin · 0.3% WF margin',
        'tone': 'Confident, mathematical, slightly intense. Hormozi PAS energy. Each number lands like a punch.',
        'visual_ideas': [
            'Three split-screen wire receipts showing the three different received amounts',
            'Calculator on-screen as the math unfolds (12 × 50K, multiplied by margin)',
            'Stacks of bills growing as the 3-year loss builds to 21,600',
            'Cutaway at the "employee / container / product line" line: job posting, container photo, product launch',
            'Final beat: a clean comparison bar chart — bank margin vs WF margin',
        ],
        'length': '60 seconds',
        'cta': 'Search WorldFirst',
    },
    ('P2-A8-1', 'PH2'): {
        'shape': 'Demo',
        'angle': 'Interactive challenge. The viewer can do this WITH the talent in real time. 30-second hands-on tutorial = proof of value via demonstration.',
        'hook_power': '"Can a business owner find a hidden FX fee in 30 seconds? Watch." — challenge framing + tutorial promise. Forces engagement.',
        'beats': [
            'Challenge frame ("30 seconds, watch")',
            'Step 1 (5s — pull up wire confirmation, find "applied rate")',
            'Step 2 (10s — Google "USD to local currency", note the mid-market rate)',
            'Step 3 (compare — the gap is the hidden margin)',
            'Step 4 (multiply — gap × wire amount = the hidden fee in dollars)',
            'Reveal ("No line item. No receipt. Just hidden inside the rate.")',
            'Scale ("2% gap on a 50K wire = 1,000 dollars. Per wire.")',
            'WF positioning (near Google\'s mid-market = hidden fee disappears)',
        ],
        'numbers': '30 seconds total · 5s/10s/20s/10s breakdown · 50K-100K wire range · 2% gap · 1,000 dollars per wire',
        'tone': 'Tutorial-friendly. Slightly conspiratorial ("they don\'t want you to know"). Hands-on, direct.',
        'visual_ideas': [
            'Stopwatch overlay through all 30 seconds, ticking',
            'Screen recording: anonymized bank wire confirmation, "applied rate" highlighted',
            'Cut to Google search: "USD to MYR" (or THB, depending on cut region) — mid-market rate visible',
            'Side-by-side comparison: bank rate vs Google rate, the gap highlighted',
            'Calculator showing gap × 50,000 = the hidden fee number',
            'Final beat: bank receipt with the hidden fee circled in red',
        ],
        'length': '30 seconds (matches the "30 seconds" promise in the hook)',
        'cta': 'Search WorldFirst',
    },
}

def panel(num, title, body_html):
    return f'''
<section id="s{num}" class="panel">
  <div class="panel-num">{num:02d}</div>
  <div class="panel-body">
    <h2>{esc(title)}</h2>
    {body_html}
  </div>
</section>'''

def script_panel(num, e, notes):
    title = TITLES.get(e['slide_id'], '')
    bullets = ''.join(f'<li>{esc(b)}</li>' for b in notes['beats'])
    visuals = ''.join(f'<li>{esc(v)}</li>' for v in notes['visual_ideas'])
    body = f'''
    <div class="meta-row">
      <span class="tag">{esc(notes['shape'])}</span>
      <span class="meta-id">{esc(e['slide_id'])} · {esc(e['variant_id'])}</span>
      <span class="meta-version">{esc(e['version'])}</span>
      <span class="meta-len">{esc(notes['length'])}</span>
      <span class="meta-words">{e['word_count']} words</span>
    </div>

    <div class="block">
      <div class="block-label">Final VO (read this verbatim)</div>
      <p class="vo">{esc(e['final_vo'])}</p>
    </div>

    <div class="grid2">
      <div class="block">
        <div class="block-label">Angle</div>
        <p class="prose">{esc(notes['angle'])}</p>
      </div>
      <div class="block">
        <div class="block-label">Why the hook works</div>
        <p class="prose">{esc(notes['hook_power'])}</p>
      </div>
    </div>

    <div class="block">
      <div class="block-label">Story beats (in order)</div>
      <ol class="beats">{bullets}</ol>
    </div>

    <div class="grid2">
      <div class="block">
        <div class="block-label">Numbers to nail (deliver exactly)</div>
        <p class="prose mono">{esc(notes['numbers'])}</p>
      </div>
      <div class="block">
        <div class="block-label">Tone &amp; pacing</div>
        <p class="prose">{esc(notes['tone'])}</p>
      </div>
    </div>

    <div class="block">
      <div class="block-label">Visual / B-roll ideas (director\'s call, these are starting points)</div>
      <ul class="visuals">{visuals}</ul>
    </div>

    <div class="grid2">
      <div class="block">
        <div class="block-label">Format</div>
        <p class="prose">{esc(notes['length'])} · vertical 9:16 · SEA short-form (TikTok / IG Reels / FB Reels / YT Shorts)</p>
      </div>
      <div class="block">
        <div class="block-label">CTA</div>
        <p class="prose">{esc(notes['cta'])}</p>
      </div>
    </div>'''
    return panel(num, f'{num-3}. {title}' if num > 3 else title, body)

CONTEXT_PANELS = [
    panel(1, 'The brand', '''
    <p class="prose">WorldFirst is a cross-border payments specialist owned by Ant Group. We help small and medium business owners move money between countries — paying suppliers, receiving marketplace payouts, holding multi-currency accounts. We are not a bank. We are the rails between banks that don\'t talk to each other smoothly.</p>
    <p class="prose">For this batch, the product hero is: <strong>direct CNY rails to Chinese suppliers, same-day, near mid-market exchange rates</strong>. That is the proof point every script lands on.</p>'''),
    panel(2, 'The audience', '''
    <p class="prose">SEA-based SME operators sourcing from China. Priority markets: Thailand and Malaysia. Secondary: Vietnam, Philippines, Indonesia, Singapore.</p>
    <p class="prose">They have small teams. They source on 1688 or Alibaba. They pay suppliers in wires or PayPal or credit cards. They know FX margin exists but cannot quantify it. They\'ve had a wire delayed. They\'ve been told no to Visa by a supplier and didn\'t understand why. They are not finance people. Speak plain.</p>
    <p class="prose">They use English at a 7th-8th grade reading level on average. No jargon without a quick definition. No acronyms without a spell-out.</p>'''),
    panel(3, 'The voice', '''
    <p class="prose"><strong>We voice.</strong> Official WorldFirst account. Not first-person "I". Not "you guys".</p>
    <p class="prose"><strong>Direct, modern, practical.</strong> Like a friend who imports, not a bank.</p>
    <p class="prose"><strong>Value first, viral second, brand mentions last.</strong> Teach something concrete in every script. The brand earns the CTA at the end.</p>
    <p class="prose"><strong>Numbers, not adjectives.</strong> "Saves money" is weak. "1,000 dollars per wire on a 50K transfer" is strong.</p>
    <p class="prose"><strong>No em-dashes</strong> (the long horizontal line —). Use commas, colons, periods, line breaks.</p>'''),
]

SCRIPT_PANELS = ''.join(
    script_panel(i + 4, by_key[k], NOTES[k]) for i, k in enumerate(TOP3) if k in by_key
)

NAV_ITEMS = (
    '<a href="#s1" class="nav-item"><span class="nav-num">01</span><span class="nav-id">The brand</span></a>'
    '<a href="#s2" class="nav-item"><span class="nav-num">02</span><span class="nav-id">The audience</span></a>'
    '<a href="#s3" class="nav-item"><span class="nav-num">03</span><span class="nav-id">The voice</span></a>'
)
for i, k in enumerate(TOP3):
    if k not in by_key: continue
    sid = k[0]
    NAV_ITEMS += f'<a href="#s{i+4}" class="nav-item"><span class="nav-num">{i+4:02d}</span><span class="nav-id">{esc(TITLES.get(sid,""))[:48]}</span></a>'

CSS = '''
:root {
  --ink: #0a0a0a;
  --ink-soft: #3a3a3a;
  --ink-mute: #6a6a6a;
  --line: #d8d8d8;
  --line-s: #ececec;
  --bg: #fff;
  --tint: #f7f7f5;
  --pick: #0a6d2f;
  --serif: ui-serif, "New York", "Iowan Old Style", Georgia, serif;
  --mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", sans-serif;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--ink); font-family: var(--sans); -webkit-font-smoothing: antialiased; }
.layout { display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; max-width: 1400px; margin: 0 auto; }

.sidebar { position: sticky; top: 0; height: 100vh; border-right: 1px solid var(--line); padding: 28px 20px 28px 32px; overflow-y: auto; }
.sb-kicker { font-family: var(--mono); font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-mute); margin-bottom: 6px; }
.sb-title { font-size: 17px; font-weight: 700; letter-spacing: -0.01em; margin-bottom: 4px; }
.sb-meta { font-family: var(--mono); font-size: 10px; color: var(--ink-mute); margin-bottom: 24px; }
.sb-nav { display: flex; flex-direction: column; gap: 1px; }
.nav-item { display: grid; grid-template-columns: 28px 1fr; gap: 8px; padding: 8px 10px;
  border: 1px solid transparent; border-radius: 5px; text-decoration: none; color: var(--ink-soft);
  font-size: 12px; transition: all 0.15s; align-items: baseline; }
.nav-item:hover { border-color: var(--line); background: var(--tint); color: var(--ink); }
.nav-num { font-family: var(--mono); font-size: 10px; color: var(--ink-mute); }
.nav-id { font-family: var(--sans); font-size: 12px; font-weight: 500; color: var(--ink); }

.main { padding: 60px 56px 120px; }
.hero { padding-bottom: 32px; border-bottom: 1px solid var(--line); margin-bottom: 48px; }
.kicker { font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-mute); margin-bottom: 14px; }
h1 { font-size: 36px; line-height: 1.15; letter-spacing: -0.022em; font-weight: 600; margin: 0 0 12px; }
.lede { font-size: 16px; color: var(--ink-soft); line-height: 1.55; max-width: 760px; }
.lede + .lede { margin-top: 12px; }
.stats { display: flex; gap: 36px; margin-top: 28px; }
.stat-block { display: flex; flex-direction: column; gap: 4px; }
.stat-num { font-family: var(--serif); font-size: 30px; font-weight: 500; letter-spacing: -0.01em; }
.stat-label { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-mute); }

.panel { display: grid; grid-template-columns: 60px 1fr; gap: 24px; padding: 44px 0; border-bottom: 1px solid var(--line-s); }
.panel:last-child { border-bottom: none; }
.panel-num { font-family: var(--mono); font-size: 12px; color: var(--ink-mute); letter-spacing: 0.04em; padding-top: 6px; }
.panel-body { min-width: 0; }

.meta-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: baseline; margin-bottom: 24px; }
.tag { font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--pick); font-weight: 700;
  padding: 3px 8px; border: 1px solid var(--pick); border-radius: 100px; }
.meta-id { font-family: var(--mono); font-size: 12px; font-weight: 700; color: var(--ink); letter-spacing: 0.04em; }
.meta-version, .meta-len, .meta-words { font-family: var(--mono); font-size: 10px; color: var(--ink-mute); letter-spacing: 0.04em; text-transform: uppercase; }

h2 { font-size: 23px; line-height: 1.25; letter-spacing: -0.012em; font-weight: 600; margin: 0 0 18px; }

.block { margin-bottom: 22px; }
.block-label { font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-mute); font-weight: 700; margin-bottom: 8px; }
.vo { font-family: var(--serif); font-size: 16px; line-height: 1.7; color: var(--ink); margin: 0;
  padding: 18px 22px; background: var(--tint); border-left: 3px solid var(--ink); border-radius: 0 6px 6px 0; }
.prose { font-size: 14px; line-height: 1.6; color: var(--ink); margin: 0; }
.prose.mono { font-family: var(--mono); font-size: 12px; color: var(--ink); letter-spacing: 0.02em; }
.beats { padding-left: 22px; margin: 0; font-size: 14px; line-height: 1.7; color: var(--ink); }
.beats li { margin-bottom: 4px; }
.visuals { padding-left: 22px; margin: 0; font-size: 14px; line-height: 1.7; color: var(--ink-soft); }
.visuals li { margin-bottom: 4px; }

.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-bottom: 22px; }
.grid2 .block { margin-bottom: 0; }

@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--line); padding: 24px; }
  .main { padding: 32px 24px 80px; }
  .panel { grid-template-columns: 1fr; gap: 12px; }
  .panel-num { padding-top: 0; }
  h1 { font-size: 26px; }
  .stats { gap: 24px; flex-wrap: wrap; }
  .stat-num { font-size: 24px; }
  .grid2 { grid-template-columns: 1fr; gap: 18px; }
}
'''

HTML_PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>SEA Batch 1 - Top 3 Producer Brief</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">
    <div class="sb-kicker">Sparkloop · producer brief</div>
    <div class="sb-title">SEA Batch 1 - Top 3</div>
    <div class="sb-meta">For Hen Hui</div>
    <div class="sb-nav">{NAV_ITEMS}</div>
  </nav>
  <main class="main">
    <div class="hero">
      <div class="kicker">WorldFirst · SEA brand channel · short-form batch 1</div>
      <h1>Top 3 producer brief</h1>
      <p class="lede">Three picks ready to film. Each one carries clean VO copy you can read verbatim, plus context on the angle, story beats, numbers to nail, tone, and visual starting points.</p>
      <p class="lede">Three different shapes on purpose: a <strong>story</strong> (urgency / time cost), a <strong>math</strong> (compounding numbers), and a <strong>demo</strong> (try it in 30 seconds). They should not feel like the same video three times.</p>
      <div class="stats">
        <div class="stat-block"><div class="stat-num">3</div><div class="stat-label">Scripts</div></div>
        <div class="stat-block"><div class="stat-num">150s</div><div class="stat-label">Total runtime</div></div>
        <div class="stat-block"><div class="stat-num">SEA</div><div class="stat-label">Region focus</div></div>
        <div class="stat-block"><div class="stat-num">9:16</div><div class="stat-label">Format</div></div>
      </div>
    </div>
    {''.join(CONTEXT_PANELS)}
    {SCRIPT_PANELS}
  </main>
</div>
</body>
</html>
'''

with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'w') as f:
    f.write(HTML_PAGE)
print('Built: index.html')
