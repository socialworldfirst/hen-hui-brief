"""Producer brief — context + creative territory for the top 3 SEA picks.

Reads finalized.json + slides.json from sea-voice-iterate. /report-style HTML.
Password-gated (wf) for internal team viewing.
"""
import json, html, os, base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
esc = html.escape

PASSWORD = 'wf'
PBKDF2_ITER = 100_000
STORAGE_KEY = 'hen_hui_brief_pw'

def encrypt_payload(plaintext: str, password: str = PASSWORD) -> dict:
    salt = os.urandom(16); iv = os.urandom(12)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=PBKDF2_ITER).derive(password.encode('utf-8'))
    ct = AESGCM(key).encrypt(iv, plaintext.encode('utf-8'), None)
    return {
        'v': 1,
        'salt': base64.b64encode(salt).decode('ascii'),
        'iv': base64.b64encode(iv).decode('ascii'),
        'iterations': PBKDF2_ITER,
        'ciphertext': base64.b64encode(ct).decode('ascii'),
    }

SRC = '/Users/steven/Documents/Claude/sea-voice-iterate'
fz = json.load(open(f'{SRC}/finalized.json'))
TITLES = {s['slide_id']: s.get('video_title', '') for s in json.load(open(f'{SRC}/slides.json'))}

TOP3 = [('P1-A9-1', 'PH2'), ('P1-A14-1', 'PH2'), ('P2-A8-1', 'PH2')]
by_key = {(e['slide_id'], e['variant_id']): e for e in fz['finalized']}

# Briefing notes per script — the truth, what we're carrying, creative territory
NOTES = {
    ('P1-A9-1', 'PH2'): {
        'shape': 'Story',
        'why_this_one': 'Anyone who\'s wired money to China has felt this silence. It\'s the most universal pain in the batch, and it lets us open the set without selling anything. Earn the listen first.',
        'what_this_is_for': 'The trust piece. It doesn\'t sell WorldFirst, it shows we understand the actual problem. If a viewer walks away thinking "they get it," this script did its job.',
        'truth': 'A delayed wire is not a money problem. It\'s a container problem, a season problem, a competitor-on-the-shelf problem. The bank app says "Sent" while the factory floor sits idle.',
        'carrying': 'The paradox lands first: the app shows Sent, the supplier shows nothing. Then the chain nobody told them about, the intermediary banks, the conversion windows, the AML hold above some threshold, a Friday holiday in Shenzhen. The escalation matters: lost the day, then the week, then the order. Land it on the reframe: the wire isn\'t lost, the visibility is.',
        'anchor_stats': 'three intermediaries · two conversion days · one surprise AML hold · Friday holiday in Shenzhen · five-day silence',
        'feel': 'Quiet tension. Refreshing a phone, getting nothing. Operator-to-operator, not preachy.',
        'open': 'Single talking head if the delivery carries it. Split-screen of operator-side calm and supplier-side empty floor if she wants visual contrast. Could work the calendar slipping into the cold open. The Friday-in-Shenzhen beat is the strongest specific if she wants one moment to lean into.',
        'locked': 'Vertical 9:16, ~60 seconds, we voice, no em-dashes, CTA "Search WorldFirst." Land the proof point: direct CNY rails, same-day, with a tracking reference the supplier can match.',
    },
    ('P1-A14-1', 'PH2'): {
        'shape': 'Math',
        'why_this_one': 'Operators know FX margin exists, they can\'t name a number. This one names three: 49,250, 49,700, 49,850. Then it compounds. By the end, the hidden margin becomes "an employee" or "a container," and that doesn\'t un-see.',
        'what_this_is_for': 'The proof piece. After the story script earns trust, this one gives them a number to remember. Best case: someone pauses to do the math on their own volume.',
        'truth': 'Three operators send the same 50K to the same supplier on the same day. They get three different amounts back. The difference is a hire over three years.',
        'carrying': 'The setup is almost too tidy to be true, that\'s the hook. Then the reveal of the three received amounts. Then the compounding: 12 wires a year on 600K of volume, the gap year-on-year, the three-year total. The translation moment is the one to protect: "that\'s an employee, that\'s a container, that\'s the next product line." Close on the mechanism in one line: it\'s not a fee, it\'s the rate.',
        'anchor_stats': '49,250 / 49,700 / 49,850 · 600 dollar spread · 12 wires · 600K volume · 7,200 annual gap · 21,600 over 3 years',
        'feel': 'Confident, mathematical. Showing receipts, not selling. Hormozi-adjacent without the shouting.',
        'open': 'Pure talking head if the delivery is strong. Calculator-on-screen treatment if she wants the math to be the visual. Three split receipts is the obvious move — only worth it if the design lands. The "employee / container / product line" beat opens a cutaway sequence, find the strongest image of each and let each one breathe.',
        'locked': 'Vertical 9:16, ~60 seconds, we voice, no em-dashes, CTA "Search WorldFirst." Land the proof point: 0.3% on the same wires, same-day to Chinese bank accounts.',
    },
    ('P2-A8-1', 'PH2'): {
        'shape': 'Demo',
        'why_this_one': 'Most "hidden fee" content gets tuned out. This one turns the claim into a 30-second exercise the viewer can do on their own bank receipt. Self-discovery hits harder than us telling them.',
        'what_this_is_for': 'The conversion piece. The viewer finds their own number, then the WorldFirst positioning at the end answers a question they\'re already asking. Best case: they screenshot their own receipt and send it to their accountant.',
        'truth': 'A 30-second exercise anyone with a phone can do, that exposes a fee the bank has every reason not to put on a line item.',
        'carrying': 'Open on the challenge. Step one is the wire confirmation, point them at the "applied rate" field. Step two is Google for the mid-market rate. Step three is the comparison, the gap is the margin. Step four is the multiplication, the gap times the wire amount. Land the line: no line item, no receipt, just hidden inside the rate. Close on the scale: a 2 percent gap on a 50K wire is 1,000 dollars, every time.',
        'anchor_stats': '30 seconds · 4 steps · 2% gap example · 50K wire example · 1,000 dollars hidden per wire',
        'feel': 'Tutorial-friendly, slightly conspiratorial. Like a finance friend showing a trick.',
        'open': 'Screen-recording with talent narrating over the phone is the obvious version. Could be talent on camera with a stopwatch in the corner, doing the math longhand. Real anonymized wire confirmation from a SEA bank would land harder than a mock. The final reveal frame should be screenshot-worthy on purpose.',
        'locked': 'Vertical 9:16, ~30 seconds (it has to match the promise), we voice, no em-dashes, CTA "Search WorldFirst." Body stays generic — USD is the wire currency, destination is whatever local currency the viewer wired to. Land the proof point: near Google mid-market rate, hidden fee disappears.',
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
    </div>

    <div class="block">
      <div class="block-label">Why this one</div>
      <p class="prose">{esc(notes['why_this_one'])}</p>
    </div>

    <div class="block">
      <div class="block-label">What it\'s for</div>
      <p class="prose">{esc(notes['what_this_is_for'])}</p>
    </div>

    <div class="block">
      <p class="prose strong">{esc(notes['truth'])}</p>
    </div>

    <div class="block">
      <div class="block-label">What the story carries</div>
      <p class="prose">{esc(notes['carrying'])}</p>
    </div>

    <div class="block">
      <div class="block-label">Numbers that anchor it</div>
      <p class="prose mono">{esc(notes['anchor_stats'])}</p>
    </div>

    <div class="block">
      <div class="block-label">Feel</div>
      <p class="prose">{esc(notes['feel'])}</p>
    </div>

    <div class="block">
      <div class="block-label">Open territory · your call</div>
      <p class="prose">{esc(notes['open'])}</p>
    </div>

    <div class="block">
      <div class="block-label">Locked · please keep</div>
      <p class="prose">{esc(notes['locked'])}</p>
    </div>

    <div class="block">
      <div class="block-label">Story suggestion · rewrite it in your tone</div>
      <p class="vo">{esc(e['final_vo'])}</p>
    </div>'''
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
.for-line { font-family: var(--serif); font-size: 28px; font-weight: 500; letter-spacing: -0.01em; color: var(--pick); margin: 0 0 6px; line-height: 1.1; }
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
.vo { font-family: var(--serif); font-size: 15px; line-height: 1.7; color: var(--ink); margin: 0; padding: 18px 22px; background: var(--tint); border-left: 3px solid var(--pick); border-radius: 0 6px 6px 0; }

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

INNER_HTML = f'''
<div class="layout">
  <nav class="sidebar">
    <div class="sb-kicker">Creator brief · for Hen Hui</div>
    <div class="sb-title">Three to film</div>
    <div class="sb-meta">SEA brand channel · batch 1</div>
    <div class="sb-nav">{NAV_ITEMS}</div>
  </nav>
  <main class="main">
    <div class="hero">
      <div class="kicker">WorldFirst · SEA brand channel · short-form · creator brief</div>
      <div class="for-line">For Hen Hui</div>
      <h1>Three to film</h1>
      <p class="lede">Three picks that earn a slot in the next drop. Each one carries a different shape on purpose: a quiet story about lost time, a math piece that turns hidden margin into a hire, and a 30-second demo a viewer can do alongside.</p>
      <p class="lede">Each script comes with the why (why this story over the other nine for the same idea), what it\'s for (the role it plays in the small-batch set), the truth underneath it, and the bits we\'d rather not change. The story suggestion sits at the bottom of each one as a direction — rewrite it in your tone, your treatment, your rhythm.</p>
    </div>
    {''.join(CONTEXT_PANELS)}
    {SCRIPT_PANELS}
    <footer class="footer">
      <a href="#" onclick="localStorage.removeItem('{STORAGE_KEY}');location.reload();return false;">lock device</a>
    </footer>
  </main>
</div>
'''

payload_json = json.dumps(encrypt_payload(INNER_HTML))

GATE_CSS = '''
body.locked { overflow: hidden; }
#gate { position: fixed; inset: 0; background: var(--bg, #fff); display: flex; align-items: center; justify-content: center; z-index: 9999; }
#gate-card { width: min(360px, 92vw); padding: 40px 32px; border: 1px solid #d8d8d8; border-radius: 10px; background: #fff; text-align: center; }
#gate-card h2 { font-size: 18px; font-weight: 600; margin: 0 0 22px; color: #0a0a0a; letter-spacing: -0.01em; }
#gate-form { display: flex; flex-direction: column; gap: 10px; }
#gate-input { padding: 12px 14px; font-size: 14px; border: 1px solid #d8d8d8; border-radius: 6px; outline: none; font-family: inherit; }
#gate-input:focus { border-color: #0a0a0a; }
#gate-btn { padding: 12px 14px; font-size: 13px; font-weight: 600; letter-spacing: 0.02em; background: #0a0a0a; color: #fff; border: 0; border-radius: 6px; cursor: pointer; }
#gate-btn:hover { background: #2a2a2a; }
#gate-err { font-size: 12px; color: #b03060; margin-top: 8px; min-height: 16px; }
.footer { margin-top: 80px; padding-top: 24px; border-top: 1px solid #ececec; font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 11px; color: #6a6a6a; }
.footer a { color: #6a6a6a; text-decoration: none; }
.footer a:hover { color: #0a0a0a; text-decoration: underline; }
'''

HTML_PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>Three to film - for Hen Hui</title>
<style>{CSS}{GATE_CSS}</style>
</head>
<body class="locked">
<div id="gate">
  <div id="gate-card">
    <h2>Three to film · for Hen Hui</h2>
    <form id="gate-form" onsubmit="return gateSubmit(event)">
      <input id="gate-input" type="password" placeholder="password" autocomplete="off" autofocus>
      <button id="gate-btn" type="submit">Enter</button>
    </form>
    <div id="gate-err"></div>
  </div>
</div>
<div id="content" hidden></div>
<script type="application/json" id="payload">{payload_json}</script>
<script>
const STORAGE_KEY = '{STORAGE_KEY}';
function b64ToBytes(b64) {{
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return bytes;
}}
async function deriveKey(password, salt, iterations) {{
  const enc = new TextEncoder();
  const baseKey = await crypto.subtle.importKey('raw', enc.encode(password), 'PBKDF2', false, ['deriveKey']);
  return crypto.subtle.deriveKey(
    {{ name: 'PBKDF2', salt, iterations, hash: 'SHA-256' }},
    baseKey,
    {{ name: 'AES-GCM', length: 256 }},
    false, ['decrypt']
  );
}}
async function decryptPayload(password) {{
  const blob = JSON.parse(document.getElementById('payload').textContent);
  const salt = b64ToBytes(blob.salt);
  const iv = b64ToBytes(blob.iv);
  const ct = b64ToBytes(blob.ciphertext);
  const key = await deriveKey(password, salt, blob.iterations);
  const plain = await crypto.subtle.decrypt({{ name: 'AES-GCM', iv }}, key, ct);
  return new TextDecoder().decode(plain);
}}
async function gateSubmit(e) {{
  e.preventDefault();
  const inp = document.getElementById('gate-input');
  const err = document.getElementById('gate-err');
  err.textContent = '';
  try {{
    const innerHtml = await decryptPayload(inp.value);
    document.getElementById('content').innerHTML = innerHtml;
    document.getElementById('content').hidden = false;
    document.getElementById('gate').style.display = 'none';
    document.body.classList.remove('locked');
    try {{ localStorage.setItem(STORAGE_KEY, inp.value); }} catch (_) {{}}
  }} catch (ex) {{
    err.textContent = 'wrong password';
    inp.value = '';
    inp.focus();
  }}
  return false;
}}
(async () => {{
  try {{
    const cached = localStorage.getItem(STORAGE_KEY);
    if (cached) {{
      const innerHtml = await decryptPayload(cached);
      document.getElementById('content').innerHTML = innerHtml;
      document.getElementById('content').hidden = false;
      document.getElementById('gate').style.display = 'none';
      document.body.classList.remove('locked');
    }}
  }} catch (_) {{
    try {{ localStorage.removeItem(STORAGE_KEY); }} catch (_) {{}}
  }}
}})();
</script>
</body>
</html>
'''

with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'w') as f:
    f.write(HTML_PAGE)
print('Built: index.html (gated with wf)')
