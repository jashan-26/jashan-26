import os

ASSETS = "assets"
os.makedirs(ASSETS, exist_ok=True)

# ── Palette (Exact match to user's retro OS reference) ──────────────
BG          = "#1A1826"   # dark navy
FRAME       = "#25212B"   # window stroke
MINT        = "#A8E6CF"   # title bar & buttons
PINK        = "#FCD2DC"   # blush pink badges & dots
PINK_BORDER = "#F6ADC0"   # pink border accent
CREAM       = "#FFF5F0"   # inner cream body
WHITE       = "#FFFFFF"
TEXT_DARK   = "#25212B"
TEXT_MUTED  = "#584D60"
GREEN_VINE  = "#7ec89a"

def window_chrome(title, icon_svg="", w=1200, bar_h=42):
    return f'''
  <!-- Title bar -->
  <rect x="16" y="16" width="{w-32}" height="{bar_h}" rx="14" fill="{MINT}" stroke="{FRAME}" stroke-width="2.5"/>
  <rect x="16" y="38" width="{w-32}" height="20" fill="{MINT}"/>
  <line x1="16" y1="58" x2="{w-16}" y2="58" stroke="{FRAME}" stroke-width="2"/>
  <!-- Traffic light dots -->
  <circle cx="42" cy="38" r="7" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
  <circle cx="64" cy="38" r="7" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
  <circle cx="86" cy="38" r="7" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
  {icon_svg}
  <text x="136" y="44" font-family="'Courier New', Courier, monospace" font-size="16" font-weight="bold" fill="{TEXT_DARK}">{title}</text>
  <!-- Window buttons [-] [□] [✕] -->
  <g transform="translate({w - 96}, 30)">
    <rect x="0" y="0" width="16" height="16" rx="3" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.2"/>
    <line x1="4" y1="8" x2="12" y2="8" stroke="{FRAME}" stroke-width="1.5"/>
    <rect x="24" y="0" width="16" height="16" rx="3" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.2"/>
    <rect x="28" y="4" width="8" height="8" stroke="{FRAME}" stroke-width="1.2" fill="none"/>
    <rect x="48" y="0" width="16" height="16" rx="3" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.2"/>
    <line x1="52" y1="4" x2="60" y2="12" stroke="{FRAME}" stroke-width="1.2"/>
    <line x1="60" y1="4" x2="52" y2="12" stroke="{FRAME}" stroke-width="1.2"/>
  </g>
'''

def sparkle(x, y, size=12, color=PINK):
    s = size
    return f'''<g transform="translate({x},{y})">
    <path d="M{s/2} 0 L{s*0.6} {s*0.4} L{s} {s/2} L{s*0.6} {s*0.6} L{s/2} {s} L{s*0.4} {s*0.6} L0 {s/2} L{s*0.4} {s*0.4} Z" fill="{color}" opacity="0.85"/>
  </g>'''

def sleeping_cat(x, y, scale=1.0):
    return f'''<g transform="translate({x},{y}) scale({scale})">
    <text x="-6" y="4" font-family="'Courier New', monospace" font-size="14" font-weight="bold" fill="{FRAME}">z</text>
    <text x="2" y="-4" font-family="'Courier New', monospace" font-size="11" font-weight="bold" fill="{FRAME}">z</text>
    <text x="8" y="-10" font-family="'Courier New', monospace" font-size="8" font-weight="bold" fill="{FRAME}">z</text>
    <ellipse cx="30" cy="20" rx="24" ry="14" fill="{WHITE}" stroke="{FRAME}" stroke-width="2"/>
    <ellipse cx="12" cy="18" rx="14" ry="12" fill="{WHITE}" stroke="{FRAME}" stroke-width="2"/>
    <path d="M4 10L8 2L12 10Z" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
    <path d="M6 9L8 4L10 9Z" fill="{PINK}"/>
    <path d="M12 9L16 2L19 10Z" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
    <path d="M13 8L16 4L18 9Z" fill="{PINK}"/>
    <path d="M6 18C7.5 19.5 9 19.5 10 18" stroke="{FRAME}" stroke-width="1.5" stroke-linecap="round" fill="none"/>
    <path d="M14 18C15.5 19.5 17 19.5 18 18" stroke="{FRAME}" stroke-width="1.5" stroke-linecap="round" fill="none"/>
    <ellipse cx="5" cy="22" rx="2" ry="1.2" fill="{PINK}"/>
    <path d="M52 18C56 22 52 28 44 26" stroke="{FRAME}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  </g>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. STATS BANNER (1200 x 200)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_stats():
    w, h = 1200, 200
    icon = '''<g transform="translate(104, 26)">
      <rect x="0" y="2" width="18" height="18" rx="3" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
      <line x1="4" y1="14" x2="8" y2="8" stroke="{FRAME}" stroke-width="1.5"/>
      <line x1="8" y1="8" x2="12" y2="12" stroke="{FRAME}" stroke-width="1.5"/>
      <line x1="12" y1="12" x2="16" y2="6" stroke="{FRAME}" stroke-width="1.5"/>
    </g>'''.format(PINK=PINK, FRAME=FRAME)

    chrome = window_chrome("stats_overview.exe", icon, w, 42)
    cols = [
        (60, "03", "Patent Applications", "filed &amp; innovations"),
        (350, "04", "Major AI/ML Builds", "end-to-end systems"),
        (640, "03", "Hackathons &amp; Honours", "SIH finalist · SheFi S16"),
        (930, "#AWS", "Cloud Practitioner", "Amazon Web Services"),
    ]

    items_svg = []
    for x, val, label1, label2 in cols:
        items_svg.append(f'''
    <g transform="translate({x}, 80)">
      <text x="0" y="38" font-family="'Courier New', Courier, monospace" font-size="44" font-weight="bold" fill="{TEXT_DARK}">{val}</text>
      <text x="0" y="66" font-family="'Courier New', Courier, monospace" font-size="14" font-weight="bold" fill="{TEXT_DARK}">{label1}</text>
      <text x="0" y="86" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" fill="{TEXT_MUTED}">{label2}</text>
    </g>''')

    dividers = f'''
    <line x1="310" y1="80" x2="310" y2="175" stroke="{PINK_BORDER}" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="600" y1="80" x2="600" y2="175" stroke="{PINK_BORDER}" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="890" y1="80" x2="890" y2="175" stroke="{PINK_BORDER}" stroke-width="1.5" stroke-dasharray="3 3"/>
'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="16" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>
  {chrome}
  {dividers}
  {''.join(items_svg)}
  {sparkle(1140, 75, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION HEADER BANNER (1200 x 74)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_section_header(num, title, icon_type="folder"):
    w, h = 1200, 74
    icon_svg = ""
    if icon_type == "folder":
        icon_svg = f'''<g transform="translate(104, 26)">
          <path d="M1 3C1 1.9 1.9 1 3 1H7L9 3H17C18.1 3 19 3.9 19 5V15C19 16.1 18.1 17 17 17H3C1.9 17 1 16.1 1 15V3Z" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
        </g>'''
    elif icon_type == "atom":
        icon_svg = f'''<g transform="translate(104, 26)">
          <circle cx="9" cy="9" r="4" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
          <ellipse cx="9" cy="9" rx="10" ry="4" fill="none" stroke="{FRAME}" stroke-width="1.2" transform="rotate(30 9 9)"/>
          <ellipse cx="9" cy="9" rx="10" ry="4" fill="none" stroke="{FRAME}" stroke-width="1.2" transform="rotate(-30 9 9)"/>
        </g>'''
    elif icon_type == "trophy":
        icon_svg = f'''<g transform="translate(104, 26)">
          <path d="M4 2H14V8C14 11 11 13 9 13C7 13 4 11 4 8V2Z" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
          <path d="M4 4H1V7C1 8.5 2.5 9 4 9" stroke="{FRAME}" stroke-width="1.5" fill="none"/>
          <path d="M14 4H17V7C17 8.5 15.5 9 14 9" stroke="{FRAME}" stroke-width="1.5" fill="none"/>
          <line x1="9" y1="13" x2="9" y2="16" stroke="{FRAME}" stroke-width="1.5"/>
          <rect x="5" y="16" width="8" height="2" fill="{FRAME}"/>
        </g>'''
    elif icon_type == "code":
        icon_svg = f'''<text x="104" y="42" font-family="'Courier New', monospace" font-size="18" font-weight="bold" fill="{TEXT_DARK}">&lt;/&gt;</text>'''

    chrome = window_chrome(f"§ {num}  {title}", icon_svg, w, 44)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="14" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>
  {chrome}
  {sparkle(1130, 26, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROJECT CARD (600 x 380)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_project_card(num, category, title, stack, desc_lines, tags, icon_type="chart"):
    w, h = 600, 380

    icon_svg = ""
    if icon_type == "chart":
        icon_svg = f'''
      <rect x="4" y="4" width="34" height="24" rx="3" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
      <path d="M8 20L15 13L21 18L32 9" stroke="{FRAME}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M17 28V33M11 33H23" stroke="{FRAME}" stroke-width="1.8" stroke-linecap="round"/>
'''
    elif icon_type == "cyclone":
        icon_svg = f'''
      <path d="M21 8C13 8 7 15 7 23C7 31 13 38 21 38C18 34 17 29 21 23C24 20 28 20 31 23C33 26 31 31 27 32" stroke="{FRAME}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
      <circle cx="21" cy="23" r="4" fill="{FRAME}"/>
'''
    elif icon_type == "coins":
        icon_svg = f'''
      <ellipse cx="21" cy="14" rx="14" ry="6" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
      <path d="M7 14V23C7 26.5 13 29 21 29C29 29 35 26.5 35 23V14" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
      <ellipse cx="25" cy="26" rx="10" ry="4.5" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
'''
    elif icon_type == "medical":
        icon_svg = f'''
      <rect x="4" y="4" width="34" height="24" rx="3" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
      <path d="M21 9V23M14 16H28" stroke="{FRAME}" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M17 28V33M11 33H23" stroke="{FRAME}" stroke-width="1.8" stroke-linecap="round"/>
'''

    tag_pills = []
    cur_x = 36.0
    for t in tags:
        tw = len(t) * 8.5 + 24
        tag_pills.append(f'''
    <rect x="{cur_x:.1f}" y="318" width="{tw:.1f}" height="28" rx="14" fill="{PINK}" stroke="{PINK_BORDER}" stroke-width="1.5"/>
    <text x="{cur_x + tw/2:.1f}" y="337" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" font-weight="bold" fill="{TEXT_DARK}">{t}</text>
''')
        cur_x += tw + 10

    desc_svg = []
    y_d = 210
    for line in desc_lines:
        desc_svg.append(f'<text x="36" y="{y_d}" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="14" fill="{TEXT_MUTED}">{line}</text>')
        y_d += 24

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="16" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>

  <!-- Top bar -->
  <rect x="16" y="16" width="{w-32}" height="38" rx="16" fill="{MINT}" stroke="{FRAME}" stroke-width="2.5"/>
  <rect x="16" y="34" width="{w-32}" height="20" fill="{MINT}"/>
  <line x1="16" y1="54" x2="{w-16}" y2="54" stroke="{FRAME}" stroke-width="2"/>
  <circle cx="38" cy="35" r="6" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
  <circle cx="56" cy="35" r="6" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
  <circle cx="74" cy="35" r="6" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
  <text x="96" y="40" font-family="'Courier New', monospace" font-size="13" font-weight="bold" fill="{TEXT_DARK}">{num} · {category}</text>
  <!-- Link arrow -->
  <path d="M{w-44} 28H{w-34}V38M{w-34} 28L{w-46} 40" stroke="{FRAME}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Icon box -->
  <g transform="translate(36, 76)">
    <rect x="0" y="0" width="46" height="46" rx="10" fill="{PINK}" stroke="{FRAME}" stroke-width="1.8"/>
    {icon_svg}
  </g>

  <!-- Title & Stack -->
  <text x="96" y="96" font-family="'Courier New', monospace" font-size="19" font-weight="bold" fill="{TEXT_DARK}">{title}</text>
  <text x="96" y="118" font-family="'Courier New', monospace" font-size="13" font-weight="bold" fill="{TEXT_MUTED}">{stack}</text>

  <line x1="36" y1="145" x2="{w-36}" y2="145" stroke="{PINK_BORDER}" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Description -->
  {''.join(desc_svg)}

  <!-- Tag pills -->
  {''.join(tag_pills)}

  {sparkle(w-48, 80, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. INVENTIONS / PATENTS BANNER (1200 x 440) - PICTURE 4 INCLUDED!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_patents():
    w, h = 1200, 440
    icon = f'''<g transform="translate(104, 26)">
      <circle cx="9" cy="9" r="4" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
      <ellipse cx="9" cy="9" rx="10" ry="4" fill="none" stroke="{FRAME}" stroke-width="1.2" transform="rotate(30 9 9)"/>
    </g>'''
    chrome = window_chrome("inventions_and_patents.doc", icon, w, 42)

    patents = [
        (
            "I", "AI DRIVEN NANO BIO ECO TREE",
            "Self-Sustaining Environment Intelligence System · AI Controller, Nano-MOF &amp; Swarm Coordination",
            "Prototype verified: Nano-MOF CO2 capture, HEPA purification, water harvesting &amp; solar/piezo renewable power.",
            "clean-tech"
        ),
        (
            "II", "NEUROSCAN HELMET",
            "AI-Assisted Cranial Trauma Screening · Non-Ionizing Acoustic Ultrasound Transducer Arrays",
            "Rapid on-field diagnostic helmet screening for suspected skull fractures &amp; intracranial injury.",
            "medtech"
        ),
        (
            "III", "CARHSRS PROPULSION HEALTH",
            "Cognitive Autonomous Rocket Engine Health Management · Predictive Propulsion Diagnostics",
            "Telemetry-driven anomaly forecasting and automated parameter adjustments for aerospace rocket engines.",
            "aerospace ai"
        ),
    ]

    rows_svg = []
    y_start = 80
    for roman, title, subtitle, desc, tag in patents:
        tw = len(tag) * 8.5 + 28
        tag_x = w - 48 - tw
        rows_svg.append(f'''
    <!-- Row {roman} -->
    <g transform="translate(48, {y_start})">
      <!-- Roman pill -->
      <rect x="0" y="4" width="36" height="36" rx="8" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
      <text x="18" y="27" text-anchor="middle" font-family="'Courier New', monospace" font-size="16" font-weight="bold" fill="{TEXT_DARK}">{roman}</text>

      <!-- Title & Details -->
      <text x="50" y="22" font-family="'Courier New', monospace" font-size="17" font-weight="bold" fill="{TEXT_DARK}">{title}</text>
      <text x="50" y="42" font-family="'Courier New', monospace" font-size="13" font-weight="bold" fill="{TEXT_MUTED}">{subtitle}</text>
      <text x="50" y="62" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" fill="{TEXT_MUTED}">{desc}</text>
    </g>

    <!-- Tag -->
    <rect x="{tag_x:.1f}" y="{y_start + 12}" width="{tw:.1f}" height="26" rx="13" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.2"/>
    <text x="{tag_x + tw/2:.1f}" y="{y_start + 29}" text-anchor="middle" font-family="'Courier New', monospace" font-size="11.5" font-weight="bold" fill="{TEXT_DARK}">{tag}</text>

    <line x1="48" y1="{y_start + 100}" x2="{w-48}" y2="{y_start + 100}" stroke="{PINK_BORDER}" stroke-width="1" stroke-dasharray="3 3"/>
''')
        y_start += 112

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="16" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>
  {chrome}
  {''.join(rows_svg)}
  {sparkle(w-44, 75, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. RECOGNITION & HONOURS BANNER (1200 x 480)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_recognition():
    w, h = 1200, 480
    icon = f'''<g transform="translate(104, 26)">
      <path d="M4 2H14V8C14 11 11 13 9 13C7 13 4 11 4 8V2Z" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
    </g>'''
    chrome = window_chrome("achievements_and_leadership.exe", icon, w, 42)

    honours = [
        ("SheFi Scholar (Season 16)", "Global Web3 &amp; Frontier Technology Leadership Scholar", "Fellowship"),
        ("AWS Certified Cloud Practitioner", "Amazon Web Services Official Cloud Architecture Certification", "Certification"),
        ("Smart India Hackathon (SIH)", "National Finalist &amp; Participant · AI/ML Solution Domain", "National Finalist"),
        ("Public Collaboration Head — Emergence Club", "Anchor &amp; Event Host for GDG Cloud Chandigarh &amp; AI Bootcamp 2K26", "Leadership"),
        ("Technical Hackathons &amp; Ideathons", "Multiple AI/ML Hackathons — Top 10 Finishes in Computer Vision &amp; GenAI", "Competitions"),
    ]

    rows_svg = []
    y_start = 76
    for title, desc, badge in honours:
        bw = len(badge) * 8.5 + 24
        bx = w - 48 - bw
        rows_svg.append(f'''
    <g transform="translate(48, {y_start})">
      <circle cx="10" cy="18" r="4" fill="{MINT}" stroke="{FRAME}" stroke-width="1.5"/>
      <text x="28" y="22" font-family="'Courier New', monospace" font-size="16" font-weight="bold" fill="{TEXT_DARK}">{title}</text>
      <text x="28" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" fill="{TEXT_MUTED}">{desc}</text>
    </g>

    <rect x="{bx:.1f}" y="{y_start + 10}" width="{bw:.1f}" height="26" rx="13" fill="{PINK}" stroke="{FRAME}" stroke-width="1.2"/>
    <text x="{bx + bw/2:.1f}" y="{y_start + 27}" text-anchor="middle" font-family="'Courier New', monospace" font-size="11.5" font-weight="bold" fill="{TEXT_DARK}">{badge}</text>

    <line x1="48" y1="{y_start + 65}" x2="{w-48}" y2="{y_start + 65}" stroke="{PINK_BORDER}" stroke-width="1" stroke-dasharray="3 3"/>
''')
        y_start += 76

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="16" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>
  {chrome}
  {''.join(rows_svg)}
  {sparkle(w-44, 75, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. TOOLKIT BANNER (1200 x 360)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_toolkit():
    w, h = 1200, 360
    icon = f'''<text x="104" y="42" font-family="'Courier New', monospace" font-size="18" font-weight="bold" fill="{TEXT_DARK}">&lt;/&gt;</text>'''
    chrome = window_chrome("tech_stack_toolkit.exe", icon, w, 42)

    cats = [
        ("LANGUAGES", ["Python", "C", "C++", "SQL", "JavaScript", "HTML/CSS"]),
        ("ML &amp; AI", ["PyTorch", "TensorFlow", "scikit-learn", "OpenCV", "Hugging Face", "GenAI", "Grad-CAM", "EfficientNet"]),
        ("BACKEND &amp; WEB", ["Streamlit", "Gradio", "FastAPI", "Node.js", "Express", "React"]),
        ("DATA &amp; INFRA", ["PostgreSQL", "MongoDB", "MySQL", "Git", "GitHub Actions", "AWS", "NumPy", "Pandas"]),
    ]

    rows_svg = []
    y_start = 76
    for label, pills in cats:
        pills_svg = []
        cur_x = 240.0
        for p in pills:
            pw = len(p) * 9.0 + 24
            pills_svg.append(f'''
      <rect x="{cur_x:.1f}" y="{y_start + 8}" width="{pw:.1f}" height="32" rx="16" fill="{WHITE}" stroke="{PINK_BORDER}" stroke-width="1.5"/>
      <text x="{cur_x + pw/2:.1f}" y="{y_start + 29}" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" font-weight="bold" fill="{TEXT_DARK}">{p}</text>
''')
            cur_x += pw + 10

        rows_svg.append(f'''
    <g transform="translate(48, {y_start})">
      <rect x="0" y="8" width="165" height="32" rx="16" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
      <text x="82" y="29" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" font-weight="bold" fill="{TEXT_DARK}">{label}</text>
    </g>
    {''.join(pills_svg)}
    <line x1="48" y1="{y_start + 56}" x2="{w-48}" y2="{y_start + 56}" stroke="{PINK_BORDER}" stroke-width="1" stroke-dasharray="3 3"/>
''')
        y_start += 66

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="16" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>
  {chrome}
  {''.join(rows_svg)}
  {sparkle(w-44, 75, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. CONTACT / SIGN-OFF BANNER (1200 x 200)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def make_contact():
    w, h = 1200, 200
    icon = f'''<g transform="translate(104, 26)">
      <rect x="0" y="2" width="20" height="14" rx="2" fill="{PINK}" stroke="{FRAME}" stroke-width="1.5"/>
      <path d="M0 4L10 11L20 4" stroke="{FRAME}" stroke-width="1.5" fill="none"/>
    </g>'''
    chrome = window_chrome("contact_and_connect.txt", icon, w, 42)

    cat_svg = sleeping_cat(1010, 95, 1.25)

    battery_svg = f'''
    <g transform="translate(930, 115)">
      <rect x="0" y="0" width="50" height="16" rx="4" fill="{WHITE}" stroke="{FRAME}" stroke-width="1.5"/>
      <rect x="3" y="3" width="8" height="10" rx="1" fill="{PINK}"/>
      <rect x="13" y="3" width="8" height="10" rx="1" fill="{PINK}"/>
      <rect x="23" y="3" width="8" height="10" rx="1" fill="{PINK}"/>
      <rect x="33" y="3" width="8" height="10" rx="1" fill="{PINK}"/>
      <path d="M50 5H52V11H50" fill="{FRAME}"/>
    </g>
'''

    buttons_svg = f'''
    <g transform="translate(48, 115)">
      <rect x="0" y="0" width="140" height="38" rx="12" fill="{MINT}" stroke="{FRAME}" stroke-width="2"/>
      <text x="70" y="24" text-anchor="middle" font-family="'Courier New', monospace" font-size="13" font-weight="bold" fill="{TEXT_DARK}">💻 Portfolio</text>

      <rect x="160" y="0" width="140" height="38" rx="12" fill="{PINK}" stroke="{FRAME}" stroke-width="2"/>
      <text x="230" y="24" text-anchor="middle" font-family="'Courier New', monospace" font-size="13" font-weight="bold" fill="{TEXT_DARK}">🔗 LinkedIn</text>

      <rect x="320" y="0" width="140" height="38" rx="12" fill="{MINT}" stroke="{FRAME}" stroke-width="2"/>
      <text x="390" y="24" text-anchor="middle" font-family="'Courier New', monospace" font-size="13" font-weight="bold" fill="{TEXT_DARK}">🐙 GitHub</text>
    </g>
'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="16" fill="{CREAM}" stroke="{FRAME}" stroke-width="2.5"/>
  {chrome}
  <text x="48" y="92" font-family="'Courier New', monospace" font-size="16" font-weight="bold" fill="{TEXT_DARK}">Let's connect and build something impactful together.</text>
  {buttons_svg}
  {battery_svg}
  {cat_svg}
  {sparkle(w-44, 75, 10, PINK)}
</svg>'''

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WRITE ALL ASSETS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
files = {
    "stats.svg": make_stats(),
    "s01-builds.svg": make_section_header("01", "Selected Builds", "folder"),
    "p-social.svg": make_project_card(
        "01", "LLM · AUTOMATION",
        "Autonomous Scheduler",
        "Python · Streamlit · GenAI",
        [
            "AI-powered multi-platform content creation and scheduling",
            "system synthesizing targeted posts, hashtags, and media",
            "calendars autonomously using Generative AI."
        ],
        ["solo build", "GenAI", "Streamlit"], "chart"
    ),
    "p-cyclone.svg": make_project_card(
        "02", "VISION · FORECASTING",
        "Cyclone Classifier",
        "PyTorch · EfficientNet · SatData",
        [
            "Computer vision deep learning model grading tropical",
            "cyclone intensities and storm paths from multi-source",
            "satellite imagery with Grad-CAM feature validation."
        ],
        ["SIH finalist", "satellite", "PyTorch"], "cyclone"
    ),
    "p-smartspend.svg": make_project_card(
        "03", "FINTECH · PREDICTIVE ML",
        "SmartSpend AI",
        "Python · Scikit-Learn · ML",
        [
            "Personal expense intelligence platform classifying expenses,",
            "detecting recurring spikes, and forecasting monthly budget",
            "variances with adaptive savings insights."
        ],
        ["fintech", "ML analytics", "budgeting"], "coins"
    ),
    "p-medsight.svg": make_project_card(
        "04", "MEDICAL · EXPLAINABILITY",
        "MedSight",
        "Python · Deep Learning · Grad-CAM",
        [
            "Deep learning medical image screening system delivering",
            "visual Grad-CAM diagnostic heatmaps for transparent,",
            "clinician-interpretable radiological assessments."
        ],
        ["medical AI", "Grad-CAM", "deep learning"], "medical"
    ),
    "s02-inventions.svg": make_section_header("02", "Inventions &amp; Patents", "atom"),
    "patents.svg": make_patents(),
    "s03-recognition.svg": make_section_header("03", "Recognition &amp; Honours", "trophy"),
    "recognition.svg": make_recognition(),
    "s04-toolkit.svg": make_section_header("04", "Toolkit &amp; Technologies", "code"),
    "toolkit.svg": make_toolkit(),
    "contact.svg": make_contact(),
}

for name, content in files.items():
    p = os.path.join(ASSETS, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {p}")

print("\nAll retro pixel OS portfolio assets generated successfully!")
