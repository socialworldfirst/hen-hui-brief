"""Producer brief — context + creative territory for the top 3 SEA picks.

Reads finalized.json + slides.json from sea-voice-iterate. /report-style HTML.
A brief, not a checklist: gives the creator the truth, the audience, the constraints,
and open territory. The VO copy is a reference, not a script-as-law.
"""
import json, html, os
esc = html.escape

SRC = '/Users/steven/Documents/Claude/sea-voice-iterate'
fz = json.load(open(f'{SRC}/finalized.json'))
TITLES = {s['slide_id']: s.get('video_title', '') for s in json.load(open(f'{SRC}/slides.json'))}

TOP3 = [('P1-A9-1', 'PH2'), ('P1-A14-1', 'PH2'), ('P2-A8-1', 'PH2')]
by_key = {(e['slide_id'], e['variant_id']): e for e in fz['finalized']}

# Briefing notes per script — the truth, what we're carrying, creative territory
NOTES = {
    ('P1-A9-1', 'PH2'): {
        'shape': 'Story',
        'why': 'Operators feel wire delays as money trouble. They\'re not. They\'re time trouble. The container slips before the money does. We want a viewer who\'s currently watching a "Sent" status to suddenly understand WHY their supplier is silent — and what the real cost is.',
        'truth': 'A delayed wire is not a money problem. It is a container problem, a season problem, a competitor-on-the-shelf problem. The bank app says "Sent" while the factory floor sits idle.',
        'carrying': [
            'The paradox: the app says yes, the supplier says nothing',
            'The chain that nobody told you about — three intermediary banks, conversion windows, AML holds, a Friday holiday in Shenzhen',
            'The escalation: lost the day → lost the week → lost the order',
            'The stakes that hit different in Q4 or on a launch SKU',
            'The reframe: "the wire isn\'t lost. The visibility is."',
        ],
        'anchor_stats': 'Three intermediaries · two days of conversion windows · one surprise AML hold · a Friday public holiday · five-day silence',
        'feel': 'Quiet tension. The energy of refreshing a phone over and over and getting nothing back. Operator-to-operator. Real. Not preachy.',
        'open': [
            'Could be a single-take talking head with the anxiety on the face',
            'Could be a split-screen of operator-side (calm app) vs supplier-side (empty factory, silent WhatsApp)',
            'Could open on the calendar slipping rather than the wire — work backwards',
            'Could be set in a SEA office with familiar visual cues (Bangkok / KL coworking, Friday afternoon light)',
            'The "Friday holiday in Shenzhen" line is gold if she wants to lean into one specific story moment',
        ],
        'locked': [
            'Vertical 9:16',
            '~60 seconds',
            'CTA at end: "Search WorldFirst"',
            'We voice (not "I")',
            'No em-dashes in any captions or supers',
            'WorldFirst proof point: direct CNY rails, same-day, with a tracking reference the supplier can match',
        ],
    },
    ('P1-A14-1', 'PH2'): {
        'shape': 'Math',
        'why': 'Operators know "FX is shady" but can\'t put a number on it. We want them to leave this video with a specific dollar figure burned into their head — and a way to imagine that dollar figure as something tangible (an employee, a container, a product line). Once the math becomes a person, it can\'t be un-seen.',
        'truth': 'Three operators send the same 50K to the same supplier on the same day. They get three different amounts received. The difference isn\'t random and it isn\'t small — it\'s a hire over three years.',
        'carrying': [
            'The setup that feels too tidy to be true (same supplier, same day, same wire)',
            'The reveal (three different received amounts on identical wires)',
            'The compounding (12 wires a year, 600K of sourcing volume)',
            'The translation (7,200 dollar gap a year → 21,600 over three)',
            'The "that\'s an employee / container / product line" moment — abstract becomes tangible',
            'The mechanism in one line: not a fee, the rate',
        ],
        'anchor_stats': '49,250 / 49,700 / 49,850 · 600 dollar spread · 12 wires · 600K volume · 9,000 vs 1,800 annual loss · 7,200 gap · 21,600 over 3 years · 1-2% bank margin · 0.3% specialist margin',
        'feel': 'Confident. Each number lands. The energy of someone showing receipts, not selling. Hormozi-adjacent without the shouting.',
        'open': [
            'Could be pure talking head if the delivery is strong enough to carry the math',
            'Could be a calculator-on-screen treatment where the math is the visual',
            'Could be three split-screen receipts that animate the spread',
            'The "that\'s an employee / container / product line" line opens up a great cutaway sequence — find the strongest image of each and let it breathe',
            'Worth considering: end on a comparison bar that lives on screen long enough for the viewer to screenshot it',
        ],
        'locked': [
            'Vertical 9:16',
            '~60 seconds',
            'CTA at end: "Search WorldFirst"',
            'We voice',
            'No em-dashes',
            'WorldFirst proof point: 0.3% margin on the same wires, same-day to Chinese bank accounts',
        ],
    },
    ('P2-A8-1', 'PH2'): {
        'shape': 'Demo',
        'why': 'This is the script that gives the viewer a hands-on win. They can pause, do the math on their own last wire, and see the hidden fee themselves. Self-discovery beats us telling them every time. The best outcome: they screenshot their own bank receipt and DM it to their accountant.',
        'truth': 'A 30-second exercise anyone with a phone can do, that exposes a fee the bank has every reason not to show on a line item.',
        'carrying': [
            'The challenge framing ("30 seconds, watch")',
            'Step 1: the wire confirmation — "applied rate" is the field that matters',
            'Step 2: Google the mid-market rate for that currency pair',
            'Step 3: the gap IS the margin',
            'Step 4: multiply the gap by the wire amount — that\'s the hidden fee in dollars',
            'The line that bites: "No line item. No receipt. Just hidden inside the rate."',
        ],
        'anchor_stats': '30 seconds total · 5s / 10s / a few seconds to compare / 10s to multiply · 2% gap example · 50K wire example · 1,000 dollars per wire',
        'feel': 'Tutorial-friendly. Slightly conspiratorial — like sharing a trick a finance friend told you. Not "watch me solve a puzzle"; more "you can do this right now, here\'s how."',
        'open': [
            'Could be screen-recording-led with talent narrating over their own phone',
            'Could be talent on camera with a stopwatch ticking in the corner, doing the math on a notepad',
            'Could use a real (anonymized) wire confirmation from a SEA bank for credibility',
            'Could end on a screenshot moment that begs to be shared — make sure the final reveal frame is screenshot-worthy',
            'Stopwatch is optional but plays well with the "30 seconds" promise — director\'s call',
        ],
        'locked': [
            'Vertical 9:16',
            '~30 seconds (matches the promise in the hook)',
            'CTA at end: "Search WorldFirst"',
            'We voice',
            'No em-dashes',
            'No country-specific framing in the body (USD is the wire currency, destination is whatever local currency the viewer wired to)',
            'WorldFirst proof point: near Google mid-market rate = hidden fee disappears',
        ],
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

def list_html(items):
    return ''.join(f'<li>{esc(x)}</li>' for x in items)

def script_panel(num, e, notes):
    title = TITLES.get(e['slide_id'], '')
    body = f'''
    <div class="meta-row">
      <span class="tag">{esc(notes['shape'])}</span>
      <span class="meta-id">{esc(e['slide_id'])}</span>
      <span class="meta-len">~{esc(notes['locked'][1].replace("~","").replace(" seconds","s"))}</span>
    </div>

    <div class="block">
      <div class="block-label">Why we\'re making this</div>
      <p class="prose">{esc(notes['why'])}</p>
    </div>

    <div class="block">
      <div class="block-label">The truth underneath</div>
      <p class="prose strong">{esc(notes['truth'])}</p>
    </div>

    <div class="block">
      <div class="block-label">What the story is carrying</div>
      <ul class="carry">{list_html(notes['carrying'])}</ul>
    </div>

    <div class="grid2">
      <div class="block">
        <div class="block-label">Stats that anchor it</div>
        <p class="prose mono">{esc(notes['anchor_stats'])}</p>
      </div>
      <div class="block">
        <div class="block-label">What it should feel like</div>
        <p class="prose">{esc(notes['feel'])}</p>
      </div>
    </div>

    <div class="grid2">
      <div class="block open">
        <div class="block-label">Open territory · your call</div>
        <ul class="open-list">{list_html(notes['open'])}</ul>
      </div>
      <div class="block locked">
        <div class="block-label">Locked · please keep</div>
        <ul class="locked-list">{list_html(notes['locked'])}</ul>
      </div>
    </div>

    <details class="vo-details">
      <summary><span class="block-label">Reference VO · starting point, not a verbatim read</span></summary>
      <p class="vo">{esc(e['final_vo'])}</p>
    </details>'''
    return panel(num, title, body)

CONTEXT_PANELS = [
    panel(1, 'The brand', '''
    <p class="prose">WorldFirst is a cross-border payments specialist owned by Ant Group. We help small and medium business owners move money between countries — paying suppliers, receiving marketplace payouts, holding multi-currency accounts. We are not a bank. We are the rails between banks that don\'t talk to each other smoothly.</p>
    <p class="prose">For this batch, the product truth is: <strong>direct CNY rails to Chinese suppliers, same-day, near mid-market exchange rates</strong>. The scripts each surface a different way that truth shows up in an operator\'s week.</p>'''),
    panel(2, 'Who we\'re talking to', '''
    <p class="prose">SEA-based SME operators sourcing from China. Priority: Thailand and Malaysia. Secondary: Vietnam, Philippines, Indonesia, Singapore.</p>
    <p class="prose">Small teams. They source on 1688 or Alibaba. They pay suppliers in wires, PayPal, or credit cards depending on the supplier. They know FX margin exists but cannot quantify it. They\'ve had a wire delayed. They\'ve been told no to Visa by a supplier and didn\'t understand why. They are not finance people. Speak to them like a friend who imports, not a bank.</p>
    <p class="prose">Reading level is around 7th-8th grade English. No acronyms without a quick spell-out the first time.</p>'''),
    panel(3, 'Voice + house rules', '''
    <ul class="prose-list">
      <li><strong>We voice.</strong> Official WorldFirst account. Not first-person "I". Not "you guys".</li>
      <li><strong>Direct, modern, practical.</strong> Like a friend who imports, not a bank.</li>
      <li><strong>Value first. Viral second. Brand mentions last.</strong> Teach something real in every script. The brand earns the CTA at the end.</li>
      <li><strong>Numbers, not adjectives.</strong> "Saves money" is weak. "1,000 dollars per wire on a 50K transfer" is strong.</li>
      <li><strong>No em-dashes</strong> (the long horizontal line). Use commas, colons, periods, line breaks.</li>
      <li><strong>One CTA, end of video:</strong> "Search WorldFirst."</li>
    </ul>'''),
    panel(4, 'Three shapes, on purpose', '''
    <p class="prose">The three picks are deliberately different shapes so they don\'t feel like the same video filmed three times. They should land as a small set with internal variety:</p>
    <ul class="prose-list">
      <li><strong>Story</strong> — urgency and time cost. The cost isn\'t the money.</li>
      <li><strong>Math</strong> — compounding numbers. The hidden margin becomes a person.</li>
      <li><strong>Demo</strong> — try it in 30 seconds. The viewer can do the trick themselves.</li>
    </ul>
    <p class="prose">Treat each one as its own film. Different energy, different visual treatment, different rhythm. If they all feel the same on a feed, we\'ve under-shot.</p>'''),
]

SCRIPT_PANELS = ''.join(
    script_panel(i + 5, by_key[k], NOTES[k]) for i, k in enumerate(TOP3) if k in by_key
)

NAV_ITEMS = (
    '<a href="#s1" class="nav-item"><span class="nav-num">01</span><span class="nav-id">The brand</span></a>'
    '<a href="#s2" class="nav-item"><span class="nav-num">02</span><span class="nav-id">Who we\'re talking to</span></a>'
    '<a href="#s3" class="nav-item"><span class="nav-num">03</span><span class="nav-id">Voice + house rules</span></a>'
    '<a href="#s4" class="nav-item"><span class="nav-num">04</span><span class="nav-id">Three shapes, on purpose</span></a>'
)
for i, k in enumerate(TOP3):
    if k not in by_key: continue
    sid = k[0]
    NAV_ITEMS += f'<a href="#s{i+5}" class="nav-item"><span class="nav-num">{i+5:02d}</span><span class="nav-id">{esc(TITLES.get(sid,""))[:48]}</span></a>'

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
.lede { font-size: 16px; color: var(--ink-soft); line-height: 1.6; max-width: 760px; }
.lede + .lede { margin-top: 14px; }

.panel { display: grid; grid-template-columns: 60px 1fr; gap: 24px; padding: 48px 0; border-bottom: 1px solid var(--line-s); }
.panel:last-child { border-bottom: none; }
.panel-num { font-family: var(--mono); font-size: 12px; color: var(--ink-mute); letter-spacing: 0.04em; padding-top: 6px; }
.panel-body { min-width: 0; }

.meta-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: baseline; margin-bottom: 24px; }
.tag { font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--pick); font-weight: 700;
  padding: 3px 8px; border: 1px solid var(--pick); border-radius: 100px; }
.meta-id, .meta-len { font-family: var(--mono); font-size: 10px; color: var(--ink-mute); letter-spacing: 0.04em; text-transform: uppercase; }
.meta-id { color: var(--ink); font-weight: 700; }

h2 { font-size: 24px; line-height: 1.25; letter-spacing: -0.012em; font-weight: 600; margin: 0 0 22px; }

.block { margin-bottom: 24px; }
.block-label { font-family: var(--mono); font-size: 9px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-mute); font-weight: 700; margin-bottom: 8px; }
.prose { font-size: 15px; line-height: 1.65; color: var(--ink); margin: 0; }
.prose + .prose { margin-top: 10px; }
.prose.strong { font-family: var(--serif); font-size: 17px; line-height: 1.55; color: var(--ink); padding: 14px 18px; background: var(--tint); border-left: 3px solid var(--ink); border-radius: 0 6px 6px 0; }
.prose.mono { font-family: var(--mono); font-size: 12px; color: var(--ink); letter-spacing: 0.02em; }
.prose-list { padding-left: 20px; font-size: 15px; line-height: 1.7; color: var(--ink); margin: 0; }
.prose-list li { margin-bottom: 6px; }
.carry { padding-left: 22px; margin: 0; font-size: 15px; line-height: 1.7; color: var(--ink); }
.carry li { margin-bottom: 4px; }
.open-list { padding-left: 22px; margin: 0; font-size: 14px; line-height: 1.65; color: var(--ink-soft); }
.open-list li { margin-bottom: 6px; }
.locked-list { padding-left: 22px; margin: 0; font-size: 14px; line-height: 1.65; color: var(--ink); }
.locked-list li { margin-bottom: 4px; }
.block.open .block-label { color: var(--pick); }
.block.locked .block-label { color: var(--ink); }

.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-bottom: 24px; }
.grid2 .block { margin-bottom: 0; }

.vo-details { margin-top: 18px; padding: 14px 18px; border: 1px solid var(--line); border-radius: 8px; background: var(--bg); }
.vo-details summary { cursor: pointer; list-style: none; }
.vo-details summary::-webkit-details-marker { display: none; }
.vo-details summary::before { content: '▸ '; font-family: var(--mono); color: var(--ink-mute); margin-right: 4px; }
.vo-details[open] summary::before { content: '▾ '; }
.vo-details summary .block-label { display: inline; margin-bottom: 0; }
.vo { font-family: var(--serif); font-size: 15px; line-height: 1.7; color: var(--ink-soft); margin: 14px 0 0; padding: 0; background: none; border: none; }

@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--line); padding: 24px; }
  .main { padding: 32px 24px 80px; }
  .panel { grid-template-columns: 1fr; gap: 12px; }
  .panel-num { padding-top: 0; }
  h1 { font-size: 26px; }
  .grid2 { grid-template-columns: 1fr; gap: 18px; }
}
'''

HTML_PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>SEA Batch 1 - Three to film</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">
    <div class="sb-kicker">Sparkloop · brief</div>
    <div class="sb-title">Three to film</div>
    <div class="sb-meta">SEA brand channel · batch 1</div>
    <div class="sb-nav">{NAV_ITEMS}</div>
  </nav>
  <main class="main">
    <div class="hero">
      <div class="kicker">WorldFirst · SEA brand channel · short-form</div>
      <h1>Three to film</h1>
      <p class="lede">Three picks that earn a slot in the next drop. Each one carries a different shape: a quiet story about lost time, a math piece that turns hidden margin into a hire, and a 30-second demo a viewer can do alongside.</p>
      <p class="lede">This brief gives you the truth underneath each script, the audience we\'re talking to, and the bits we\'d rather not change. The VO copy sits at the bottom of each one as a starting point — not a verbatim read. Bring your treatment.</p>
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
