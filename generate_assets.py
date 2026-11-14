import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "jashan-26-main", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. NAVIGATION BUTTONS
# -------------------------------------------------------------

BTN_PORTFOLIO = '''<svg xmlns="http://www.w3.org/2000/svg" width="168" height="42" viewBox="0 0 168 42" fill="none">
  <rect x="2" y="2" width="164" height="38" rx="12" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>
  <!-- Laptop icon -->
  <g transform="translate(24, 11)">
    <rect x="3" y="1" width="14" height="10" rx="1.5" fill="#25212B"/>
    <rect x="5" y="3" width="10" height="6" rx="0.5" fill="#A8E6CF"/>
    <path d="M0 13H20C20.5 13 21 13.5 21 14.2V15.5C21 16.3 20.3 17 19.5 17H1.5C0.7 17 0 16.3 0 15.5V14.2C0 13.5 0.5 13 0 13Z" fill="#25212B"/>
  </g>
  <text x="56" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="14.5" font-weight="bold" fill="#25212B">Portfolio</text>
</svg>'''

BTN_LINKEDIN = '''<svg xmlns="http://www.w3.org/2000/svg" width="168" height="42" viewBox="0 0 168 42" fill="none">
  <rect x="2" y="2" width="164" height="38" rx="12" fill="#FCD2DC" stroke="#25212B" stroke-width="2.5"/>
  <!-- LinkedIn in box -->
  <g transform="translate(25, 11)">
    <rect x="1" y="1" width="18" height="18" rx="3.5" fill="#25212B"/>
    <text x="4" y="14" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="900" fill="#FCD2DC">in</text>
  </g>
  <text x="56" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="14.5" font-weight="bold" fill="#25212B">LinkedIn</text>
</svg>'''

BTN_GITHUB = '''<svg xmlns="http://www.w3.org/2000/svg" width="168" height="42" viewBox="0 0 168 42" fill="none">
  <rect x="2" y="2" width="164" height="38" rx="12" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>
  <!-- GitHub cat silhouette -->
  <g transform="translate(24, 11)">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M10 0C4.47 0 0 4.48 0 10.01C0 14.43 2.87 18.18 6.84 19.5C7.34 19.6 7.52 19.28 7.52 19.02C7.52 18.78 7.51 17.98 7.51 17.14C4.73 17.75 4.14 15.8 4.14 15.8C3.69 14.64 3.03 14.34 3.03 14.34C2.12 13.72 3.1 13.73 3.1 13.73C4.1 13.8 4.63 14.76 4.63 14.76C5.52 16.29 6.97 15.85 7.54 15.59C7.63 14.94 7.89 14.5 8.18 14.25C5.95 14 3.62 13.14 3.62 9.3C3.62 8.21 4.01 7.32 4.65 6.62C4.55 6.37 4.2 5.35 4.75 3.98C4.75 3.98 5.58 3.71 7.49 5.01C8.29 4.79 9.14 4.68 9.99 4.67C10.84 4.68 11.69 4.79 12.49 5.01C14.39 3.71 15.23 3.98 15.23 3.98C15.78 5.35 15.43 6.37 15.33 6.62C15.97 7.32 16.36 8.21 16.36 9.3C16.36 13.15 14.02 14 11.79 14.24C12.15 14.55 12.47 15.17 12.47 16.11C12.47 17.47 12.46 18.56 12.46 18.84C12.46 19.1 12.64 19.42 13.15 19.32C17.12 17.99 19.98 14.24 19.98 9.81C19.98 4.48 15.52 0 10 0Z" fill="#25212B"/>
  </g>
  <text x="56" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="14.5" font-weight="bold" fill="#25212B">GitHub</text>
</svg>'''

# -------------------------------------------------------------
# 2. STATS BAR
# -------------------------------------------------------------

STATS_BAR = '''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="82" viewBox="0 0 900 82" fill="none">
  <!-- Outer Rounded Container -->
  <rect x="2" y="2" width="896" height="78" rx="20" fill="#1C1A27" stroke="#F6ADC0" stroke-width="1.8"/>

  <!-- Col 1: 04 Major Projects -->
  <g transform="translate(60, 16)">
    <!-- Folder Icon -->
    <g transform="translate(0, 8)">
      <path d="M2 5C2 3.89543 2.89543 3 4 3H12L15 6H30C31.1046 6 32 6.89543 32 8V23C32 24.1046 31.1046 25 30 25H4C2.89543 25 2 24.1046 2 23V5Z" fill="none" stroke="#F6ADC0" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M2 10H32" stroke="#F6ADC0" stroke-width="2"/>
    </g>
    <text x="44" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="28" font-weight="bold" fill="#FFFFFF">04</text>
    <text x="44" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#FCD2DC" letter-spacing="0.3">Major Projects</text>
  </g>

  <!-- Divider 1 -->
  <line x1="250" y1="20" x2="250" y2="62" stroke="#3D3547" stroke-width="1.5" stroke-dasharray="3 3"/>

  <!-- Col 2: 05 Achievements -->
  <g transform="translate(285, 16)">
    <!-- Trophy Icon -->
    <g transform="translate(0, 7)">
      <path d="M6 3H26V13C26 18.5228 21.5228 23 16 23C10.4772 23 6 18.5228 6 13V3Z" fill="none" stroke="#F6ADC0" stroke-width="2.2"/>
      <path d="M6 6H2C0.89543 6 0 6.89543 0 8V10C0 12.2091 1.79086 14 4 14H6" stroke="#F6ADC0" stroke-width="2"/>
      <path d="M26 6H30C31.1046 6 32 6.89543 32 8V10C32 12.2091 30.2091 14 28 14H26" stroke="#F6ADC0" stroke-width="2"/>
      <path d="M16 23V27M10 27H22" stroke="#F6ADC0" stroke-width="2.2" stroke-linecap="round"/>
    </g>
    <text x="44" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="28" font-weight="bold" fill="#FFFFFF">05</text>
    <text x="44" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#FCD2DC" letter-spacing="0.3">Achievements</text>
  </g>

  <!-- Divider 2 -->
  <line x1="475" y1="20" x2="475" y2="62" stroke="#3D3547" stroke-width="1.5" stroke-dasharray="3 3"/>

  <!-- Col 3: 03 Hackathons -->
  <g transform="translate(510, 16)">
    <!-- Code </> Icon -->
    <g transform="translate(0, 10)">
      <text x="0" y="20" font-family="'Courier New', Courier, Consolas, monospace" font-size="20" font-weight="bold" fill="#F6ADC0">&lt;/&gt;</text>
    </g>
    <text x="44" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="28" font-weight="bold" fill="#FFFFFF">03</text>
    <text x="44" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#FCD2DC" letter-spacing="0.3">Hackathons</text>
  </g>

  <!-- Divider 3 -->
  <line x1="695" y1="20" x2="695" y2="62" stroke="#3D3547" stroke-width="1.5" stroke-dasharray="3 3"/>

  <!-- Col 4: 01+ Certification -->
  <g transform="translate(730, 16)">
    <!-- Certificate Badge Icon -->
    <g transform="translate(0, 7)">
      <circle cx="15" cy="12" r="9" fill="none" stroke="#F6ADC0" stroke-width="2.2"/>
      <path d="M11 20L8 28L15 24L22 28L19 20" fill="none" stroke="#F6ADC0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M12 12L14 14L18 10" stroke="#F6ADC0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="44" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="28" font-weight="bold" fill="#FFFFFF">01+</text>
    <text x="44" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="500" fill="#FCD2DC" letter-spacing="0.3">Certification</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. LEFT COLUMN: about_me.txt
# -------------------------------------------------------------

CARD_ABOUT_ME = '''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="205" viewBox="0 0 360 205" fill="none">
  <!-- Window Outline -->
  <rect x="2" y="2" width="356" height="201" rx="14" fill="#FFF8F8" stroke="#25212B" stroke-width="2.5"/>
  
  <!-- Title bar -->
  <path d="M2 14C2 7.37258 7.37258 2 14 2H346C352.627 2 358 7.37258 358 14V34H2V14Z" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>
  <line x1="2" y1="34" x2="358" y2="34" stroke="#25212B" stroke-width="2"/>

  <!-- Page Icon -->
  <g transform="translate(14, 10)">
    <rect x="0" y="0" width="13" height="15" rx="2" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <line x1="3" y1="4" x2="10" y2="4" stroke="#25212B" stroke-width="1.2"/>
    <line x1="3" y1="7" x2="10" y2="7" stroke="#25212B" stroke-width="1.2"/>
    <line x1="3" y1="10" x2="8" y2="10" stroke="#25212B" stroke-width="1.2"/>
  </g>

  <!-- Title -->
  <text x="35" y="23" font-family="'Courier New', Courier, Consolas, monospace" font-size="14" font-weight="bold" fill="#25212B">about_me.txt</text>

  <!-- Window controls -->
  <g transform="translate(288, 8)">
    <!-- Minimize -->
    <rect x="0" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="12" y2="10" stroke="#25212B" stroke-width="1.8"/>
    <!-- Maximize -->
    <rect x="22" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <rect x="26" y="6" width="8" height="7" stroke="#25212B" stroke-width="1.5" fill="none"/>
    <!-- Close -->
    <rect x="44" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="48" y1="6" x2="56" y2="13" stroke="#25212B" stroke-width="1.5"/>
    <line x1="56" y1="6" x2="48" y2="13" stroke="#25212B" stroke-width="1.5"/>
  </g>

  <!-- Body Text -->
  <g transform="translate(18, 52)">
    <text font-family="'Courier New', Courier, Consolas, monospace" font-size="13.2" fill="#2E2533" font-weight="600" letter-spacing="-0.2">
      <tspan x="0" y="16">An AIML undergraduate who enjoys</tspan>
      <tspan x="0" y="38">building practical AI solutions,</tspan>
      <tspan x="0" y="60">experimenting with new technologies,</tspan>
      <tspan x="0" y="82">and solving real-world problems.</tspan>
    </text>
  </g>

  <!-- Cute Peeking Pixel Cat in Bottom-Right -->
  <g transform="translate(290, 142)">
    <!-- Cat Ears -->
    <path d="M6 14L12 4L17 14H6Z" fill="#FFFFFF" stroke="#25212B" stroke-width="1.8"/>
    <path d="M8 12L12 6L15 12H8Z" fill="#FCD2DC"/>
    <path d="M33 14L38 4L44 14H33Z" fill="#FFFFFF" stroke="#25212B" stroke-width="1.8"/>
    <path d="M35 12L38 6L42 12H35Z" fill="#FCD2DC"/>
    <!-- Cat Head -->
    <ellipse cx="25" cy="24" rx="22" ry="18" fill="#FFFFFF" stroke="#25212B" stroke-width="1.8"/>
    <!-- Cat Eyes -->
    <circle cx="16" cy="22" r="2.5" fill="#25212B"/>
    <circle cx="34" cy="22" r="2.5" fill="#25212B"/>
    <circle cx="15" cy="21" r="0.8" fill="#FFFFFF"/>
    <circle cx="33" cy="21" r="0.8" fill="#FFFFFF"/>
    <!-- Blushing Cheeks -->
    <ellipse cx="11" cy="27" rx="3.5" ry="1.8" fill="#FCD2DC"/>
    <ellipse cx="39" cy="27" rx="3.5" ry="1.8" fill="#FCD2DC"/>
    <!-- Cute Nose & Mouth -->
    <path d="M23 26L25 28L27 26" stroke="#25212B" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M22 29C23.5 31 25 31 25 29C25 31 26.5 31 28 29" stroke="#25212B" stroke-width="1.5" stroke-linecap="round" fill="none"/>
    <!-- Whiskers -->
    <line x1="4" y1="23" x2="0" y2="21" stroke="#25212B" stroke-width="1.2"/>
    <line x1="4" y1="27" x2="0" y2="29" stroke="#25212B" stroke-width="1.2"/>
    <line x1="46" y1="23" x2="50" y2="21" stroke="#25212B" stroke-width="1.2"/>
    <line x1="46" y1="27" x2="50" y2="29" stroke="#25212B" stroke-width="1.2"/>
    <!-- Little Paws on Border -->
    <ellipse cx="12" cy="40" rx="4" ry="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <ellipse cx="38" cy="40" rx="4" ry="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. LEFT COLUMN: tech_stack.exe
# -------------------------------------------------------------

CARD_TECH_STACK = '''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="235" viewBox="0 0 360 235" fill="none">
  <!-- Window Outline -->
  <rect x="2" y="2" width="356" height="231" rx="14" fill="#FFF8F8" stroke="#25212B" stroke-width="2.5"/>
  
  <!-- Title bar -->
  <path d="M2 14C2 7.37258 7.37258 2 14 2H346C352.627 2 358 7.37258 358 14V34H2V14Z" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>
  <line x1="2" y1="34" x2="358" y2="34" stroke="#25212B" stroke-width="2"/>

  <!-- Folder Icon -->
  <g transform="translate(14, 10)">
    <path d="M1 3C1 1.89543 1.89543 1 3 1H7L9 3H15C16.1046 3 17 3.89543 17 5V13C17 14.1046 16.1046 15 15 15H3C1.89543 15 1 14.1046 1 13V3Z" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
  </g>

  <!-- Title -->
  <text x="38" y="23" font-family="'Courier New', Courier, Consolas, monospace" font-size="14" font-weight="bold" fill="#25212B">tech_stack.exe</text>

  <!-- Window controls -->
  <g transform="translate(288, 8)">
    <rect x="0" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="12" y2="10" stroke="#25212B" stroke-width="1.8"/>
    <rect x="22" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <rect x="26" y="6" width="8" height="7" stroke="#25212B" stroke-width="1.5" fill="none"/>
    <rect x="44" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="48" y1="6" x2="56" y2="13" stroke="#25212B" stroke-width="1.5"/>
    <line x1="56" y1="6" x2="48" y2="13" stroke="#25212B" stroke-width="1.5"/>
  </g>

  <!-- Badges Grid (4 rows x 3 cols) -->
  <!-- Helper macro: Pill at (x,y), width, text -->
  
  <!-- Row 1: Python (104), C (98), C++ (102) -->
  <g transform="translate(16, 48)">
    <!-- Python -->
    <rect x="0" y="0" width="102" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="1.8" fill="#25212B"/>
    <text x="28" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">Python</text>

    <!-- C -->
    <rect x="112" y="0" width="98" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="1.8" fill="#25212B"/>
    <text x="146" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">C</text>

    <!-- C++ -->
    <rect x="220" y="0" width="106" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="236" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="236" cy="17" r="1.8" fill="#25212B"/>
    <text x="252" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">C++</text>
  </g>

  <!-- Row 2: ML, DL, Streamlit -->
  <g transform="translate(16, 92)">
    <!-- ML -->
    <rect x="0" y="0" width="102" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="1.8" fill="#25212B"/>
    <text x="36" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">ML</text>

    <!-- DL -->
    <rect x="112" y="0" width="98" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="1.8" fill="#25212B"/>
    <text x="144" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">DL</text>

    <!-- Streamlit -->
    <rect x="220" y="0" width="106" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="234" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="234" cy="17" r="1.8" fill="#25212B"/>
    <text x="246" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="11.5" font-weight="bold" fill="#25212B">Streamlit</text>
  </g>

  <!-- Row 3: Gradio, MySQL, MongoDB -->
  <g transform="translate(16, 136)">
    <!-- Gradio -->
    <rect x="0" y="0" width="102" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="1.8" fill="#25212B"/>
    <text x="27" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="12" font-weight="bold" fill="#25212B">Gradio</text>

    <!-- MySQL -->
    <rect x="112" y="0" width="98" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="1.8" fill="#25212B"/>
    <text x="138" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="12" font-weight="bold" fill="#25212B">MySQL</text>

    <!-- MongoDB -->
    <rect x="220" y="0" width="106" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="234" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="234" cy="17" r="1.8" fill="#25212B"/>
    <text x="248" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="12" font-weight="bold" fill="#25212B">MongoDB</text>
  </g>

  <!-- Row 4: Git, GitHub, VS Code -->
  <g transform="translate(16, 180)">
    <!-- Git -->
    <rect x="0" y="0" width="102" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="16" cy="17" r="1.8" fill="#25212B"/>
    <text x="35" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">Git</text>

    <!-- GitHub -->
    <rect x="112" y="0" width="98" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="128" cy="17" r="1.8" fill="#25212B"/>
    <text x="138" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="12.5" font-weight="bold" fill="#25212B">GitHub</text>

    <!-- VS Code -->
    <rect x="220" y="0" width="106" height="34" rx="17" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.5"/>
    <circle cx="234" cy="17" r="4.5" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <circle cx="234" cy="17" r="1.8" fill="#25212B"/>
    <text x="248" y="22" font-family="'Courier New', Courier, Consolas, monospace" font-size="11.5" font-weight="bold" fill="#25212B">VS Code</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. RIGHT COLUMN: featured_projects (Complete Window)
# -------------------------------------------------------------

WINDOW_FEATURED_PROJECTS = '''<svg xmlns="http://www.w3.org/2000/svg" width="620" height="448" viewBox="0 0 620 448" fill="none">
  <!-- Window Outline -->
  <rect x="2" y="2" width="616" height="444" rx="14" fill="#FFF8F8" stroke="#25212B" stroke-width="2.5"/>
  
  <!-- Title bar -->
  <path d="M2 14C2 7.37258 7.37258 2 14 2H606C612.627 2 618 7.37258 618 14V34H2V14Z" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>
  <line x1="2" y1="34" x2="618" y2="34" stroke="#25212B" stroke-width="2"/>

  <!-- Folder Icon -->
  <g transform="translate(14, 10)">
    <path d="M1 3C1 1.89543 1.89543 1 3 1H7L9 3H15C16.1046 3 17 3.89543 17 5V13C17 14.1046 16.1046 15 15 15H3C1.89543 15 1 14.1046 1 13V3Z" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
  </g>

  <!-- Title -->
  <text x="38" y="23" font-family="'Courier New', Courier, Consolas, monospace" font-size="14" font-weight="bold" fill="#25212B">featured_projects</text>

  <!-- Window controls -->
  <g transform="translate(548, 8)">
    <rect x="0" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="12" y2="10" stroke="#25212B" stroke-width="1.8"/>
    <rect x="22" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <rect x="26" y="6" width="8" height="7" stroke="#25212B" stroke-width="1.5" fill="none"/>
    <rect x="44" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="48" y1="6" x2="56" y2="13" stroke="#25212B" stroke-width="1.5"/>
    <line x1="56" y1="6" x2="48" y2="13" stroke="#25212B" stroke-width="1.5"/>
  </g>

  <!-- ==================== PROJECT 1 (Top-Left) ==================== -->
  <g transform="translate(14, 46)">
    <!-- Card Border -->
    <rect x="0" y="0" width="288" height="186" rx="12" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.8"/>
    
    <!-- Retro Chart Icon in Pink Box -->
    <rect x="12" y="14" width="46" height="46" rx="10" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <g transform="translate(20, 22)">
      <!-- Monitor & Chart -->
      <rect x="2" y="2" width="26" height="18" rx="2" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <path d="M6 14L11 9L16 13L24 6" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M12 20V24M8 24H16" stroke="#25212B" stroke-width="1.5" stroke-linecap="round"/>
    </g>

    <!-- External Link Icon ↗ -->
    <path d="M266 18H274V26M274 18L265 27" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Project Title -->
    <text x="68" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="12" font-weight="bold" fill="#25212B">
      <tspan x="68" y="26">Autonomous Social Media</tspan>
      <tspan x="68" y="42">Content Creator &amp; Sched.</tspan>
    </text>

    <!-- Description -->
    <text x="14" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="#584D60" font-weight="500">
      <tspan x="14" y="80">AI-powered content creation and</tspan>
      <tspan x="14" y="98">scheduling using Generative AI.</tspan>
    </text>

    <!-- Tech Tag Pills -->
    <g transform="translate(14, 138)">
      <!-- Tag 1: Python -->
      <rect x="0" y="0" width="66" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="12" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Python</text>
      <!-- Tag 2: Streamlit -->
      <rect x="74" y="0" width="80" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="82" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Streamlit</text>
      <!-- Tag 3: GenAI -->
      <rect x="162" y="0" width="60" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="171" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">GenAI</text>
    </g>
  </g>

  <!-- ==================== PROJECT 2 (Top-Right) ==================== -->
  <g transform="translate(318, 46)">
    <!-- Card Border -->
    <rect x="0" y="0" width="288" height="186" rx="12" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.8"/>
    
    <!-- Coins Icon in Pink Box -->
    <rect x="12" y="14" width="46" height="46" rx="10" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <g transform="translate(22, 22)">
      <!-- Coin Stacks -->
      <ellipse cx="10" cy="8" rx="8" ry="3.5" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <path d="M2 8V14C2 16 5.5 17.5 10 17.5C14.5 17.5 18 16 18 14V8" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <ellipse cx="18" cy="15" rx="7" ry="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <path d="M11 15V21C11 22.5 14 24 18 24C22 24 25 22.5 25 21V15" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    </g>

    <!-- External Link Icon ↗ -->
    <path d="M266 18H274V26M274 18L265 27" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Project Title -->
    <text x="68" y="32" font-family="'Courier New', Courier, Consolas, monospace" font-size="14.5" font-weight="bold" fill="#25212B">SmartSpend AI</text>

    <!-- Description -->
    <text x="14" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="#584D60" font-weight="500">
      <tspan x="14" y="80">Personal expense analyzer and</tspan>
      <tspan x="14" y="98">budgeting application with ML.</tspan>
    </text>

    <!-- Tech Tag Pills -->
    <g transform="translate(14, 138)">
      <!-- Tag 1: Python -->
      <rect x="0" y="0" width="66" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="12" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Python</text>
      <!-- Tag 2: Machine Learning -->
      <rect x="74" y="0" width="134" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="82" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Machine Learning</text>
    </g>
  </g>

  <!-- ==================== PROJECT 3 (Bottom-Left) ==================== -->
  <g transform="translate(14, 246)">
    <!-- Card Border -->
    <rect x="0" y="0" width="288" height="186" rx="12" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.8"/>
    
    <!-- Cyclone Spiral Icon in Pink Box -->
    <rect x="12" y="14" width="46" height="46" rx="10" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <g transform="translate(20, 22)">
      <!-- Cyclone Spirals -->
      <path d="M14 6C8 6 4 11 4 16C4 21 8 26 14 26C12 23 11 19 14 16C16 14 19 14 21 16C23 18 21 21 18 22" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" fill="none"/>
      <circle cx="14" cy="16" r="2.5" fill="#25212B"/>
    </g>

    <!-- External Link Icon ↗ -->
    <path d="M266 18H274V26M274 18L265 27" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Project Title -->
    <text x="68" y="28" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">
      <tspan x="68" y="28">Cyclone Intensity</tspan>
      <tspan x="68" y="44">Classifier</tspan>
    </text>

    <!-- Description -->
    <text x="14" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="#584D60" font-weight="500">
      <tspan x="14" y="80">AI/ML system to classify tropical</tspan>
      <tspan x="14" y="98">cyclone patterns using satellite data.</tspan>
    </text>

    <!-- Tech Tag Pills -->
    <g transform="translate(14, 138)">
      <!-- Tag 1: Python -->
      <rect x="0" y="0" width="66" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="12" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Python</text>
      <!-- Tag 2: PyTorch -->
      <rect x="74" y="0" width="70" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="82" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">PyTorch</text>
      <!-- Tag 3: EfficientNet -->
      <rect x="152" y="0" width="102" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="160" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">EfficientNet</text>
    </g>
  </g>

  <!-- ==================== PROJECT 4 (Bottom-Right) ==================== -->
  <g transform="translate(318, 246)">
    <!-- Card Border -->
    <rect x="0" y="0" width="288" height="186" rx="12" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="1.8"/>
    
    <!-- Medical Cross Monitor Icon in Pink Box -->
    <rect x="12" y="14" width="46" height="46" rx="10" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
    <g transform="translate(20, 22)">
      <!-- Monitor & Cross -->
      <rect x="2" y="2" width="26" height="18" rx="2" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <path d="M15 6V16M10 11H20" stroke="#25212B" stroke-width="2" stroke-linecap="round"/>
      <path d="M12 20V24M8 24H16" stroke="#25212B" stroke-width="1.5" stroke-linecap="round"/>
    </g>

    <!-- External Link Icon ↗ -->
    <path d="M266 18H274V26M274 18L265 27" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Project Title -->
    <text x="68" y="32" font-family="'Courier New', Courier, Consolas, monospace" font-size="15" font-weight="bold" fill="#25212B">MedSight</text>

    <!-- Description -->
    <text x="14" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="#584D60" font-weight="500">
      <tspan x="14" y="80">Deep learning-based medical image</tspan>
      <tspan x="14" y="98">screening with Grad-CAM explanations.</tspan>
    </text>

    <!-- Tech Tag Pills -->
    <g transform="translate(14, 138)">
      <!-- Tag 1: Python -->
      <rect x="0" y="0" width="66" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="12" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Python</text>
      <!-- Tag 2: Deep Learning -->
      <rect x="74" y="0" width="108" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="82" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Deep Learning</text>
      <!-- Tag 3: Grad-CAM -->
      <rect x="190" y="0" width="76" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
      <text x="198" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">Grad-CAM</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. INDIVIDUAL PROJECT CARDS (for interactive clickable links)
# -------------------------------------------------------------

def make_project_card(title1, title2, desc1, desc2, tags, icon_type):
    # Generates a 290x186 standalone card
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="292" height="190" viewBox="0 0 292 190" fill="none">
  <!-- Card Outline -->
  <rect x="2" y="2" width="288" height="186" rx="12" fill="#FFFFFF" stroke="#F6ADC0" stroke-width="2"/>
  
  <!-- Icon in Pink Box -->
  <rect x="14" y="14" width="46" height="46" rx="10" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
'''
    if icon_type == "chart":
        svg += '''  <g transform="translate(22, 22)">
    <rect x="2" y="2" width="26" height="18" rx="2" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <path d="M6 14L11 9L16 13L24 6" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M12 20V24M8 24H16" stroke="#25212B" stroke-width="1.5" stroke-linecap="round"/>
  </g>'''
    elif icon_type == "coins":
        svg += '''  <g transform="translate(24, 22)">
    <ellipse cx="10" cy="8" rx="8" ry="3.5" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <path d="M2 8V14C2 16 5.5 17.5 10 17.5C14.5 17.5 18 16 18 14V8" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <ellipse cx="18" cy="15" rx="7" ry="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <path d="M11 15V21C11 22.5 14 24 18 24C22 24 25 22.5 25 21V15" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
  </g>'''
    elif icon_type == "cyclone":
        svg += '''  <g transform="translate(22, 22)">
    <path d="M14 6C8 6 4 11 4 16C4 21 8 26 14 26C12 23 11 19 14 16C16 14 19 14 21 16C23 18 21 21 18 22" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" fill="none"/>
    <circle cx="14" cy="16" r="2.5" fill="#25212B"/>
  </g>'''
    elif icon_type == "medical":
        svg += '''  <g transform="translate(22, 22)">
    <rect x="2" y="2" width="26" height="18" rx="2" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <path d="M15 6V16M10 11H20" stroke="#25212B" stroke-width="2" stroke-linecap="round"/>
    <path d="M12 20V24M8 24H16" stroke="#25212B" stroke-width="1.5" stroke-linecap="round"/>
  </g>'''

    svg += '''
  <!-- External Link Icon ↗ -->
  <path d="M268 18H276V26M276 18L267 27" stroke="#25212B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
'''
    if title2:
        svg += f'''
  <!-- Project Title (2 lines) -->
  <text x="70" y="26" font-family="'Courier New', Courier, Consolas, monospace" font-size="12" font-weight="bold" fill="#25212B">
    <tspan x="70" y="26">{title1}</tspan>
    <tspan x="70" y="42">{title2}</tspan>
  </text>'''
    else:
        svg += f'''
  <!-- Project Title (1 line) -->
  <text x="70" y="32" font-family="'Courier New', Courier, Consolas, monospace" font-size="14.5" font-weight="bold" fill="#25212B">{title1}</text>'''

    svg += f'''
  <!-- Description -->
  <text x="14" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="#584D60" font-weight="500">
    <tspan x="14" y="80">{desc1}</tspan>
    <tspan x="14" y="98">{desc2}</tspan>
  </text>
  
  <!-- Tech Tag Pills -->
  <g transform="translate(14, 138)">
'''
    curr_x = 0
    for tag in tags:
        tag_width = len(tag) * 8 + 24
        svg += f'''    <rect x="{curr_x}" y="0" width="{tag_width}" height="24" rx="12" fill="#FCD2DC" stroke="#F6ADC0" stroke-width="1.2"/>
    <text x="{curr_x + 12}" y="16" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">{tag}</text>
'''
        curr_x += tag_width + 8

    svg += '''  </g>
</svg>'''
    return svg

# -------------------------------------------------------------
# 7. FEATURED HEADER (for modular layout)
# -------------------------------------------------------------

HEADER_FEATURED = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="36" viewBox="0 0 600 36" fill="none">
  <!-- Title bar -->
  <path d="M2 14C2 7.37258 7.37258 2 14 2H586C592.627 2 598 7.37258 598 14V34H2V14Z" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>
  <line x1="2" y1="34" x2="598" y2="34" stroke="#25212B" stroke-width="2"/>

  <!-- Folder Icon -->
  <g transform="translate(14, 10)">
    <path d="M1 3C1 1.89543 1.89543 1 3 1H7L9 3H15C16.1046 3 17 3.89543 17 5V13C17 14.1046 16.1046 15 15 15H3C1.89543 15 1 14.1046 1 13V3Z" fill="#FCD2DC" stroke="#25212B" stroke-width="1.5"/>
  </g>

  <!-- Title -->
  <text x="38" y="23" font-family="'Courier New', Courier, Consolas, monospace" font-size="14" font-weight="bold" fill="#25212B">featured_projects</text>

  <!-- Window controls -->
  <g transform="translate(528, 8)">
    <rect x="0" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="12" y2="10" stroke="#25212B" stroke-width="1.8"/>
    <rect x="22" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <rect x="26" y="6" width="8" height="7" stroke="#25212B" stroke-width="1.5" fill="none"/>
    <rect x="44" y="2" width="16" height="15" rx="3" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
    <line x1="48" y1="6" x2="56" y2="13" stroke="#25212B" stroke-width="1.5"/>
    <line x1="56" y1="6" x2="48" y2="13" stroke="#25212B" stroke-width="1.5"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# 8. BOTTOM BAR: Currently Exploring + Battery + Sleeping Cat
# -------------------------------------------------------------

FOOTER_BAR = '''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="52" viewBox="0 0 900 52" fill="none">
  <!-- Pill Container -->
  <rect x="2" y="2" width="896" height="48" rx="24" fill="#A8E6CF" stroke="#25212B" stroke-width="2.5"/>

  <!-- Left: Currently Exploring Pink Badge -->
  <g transform="translate(10, 8)">
    <rect x="0" y="0" width="186" height="32" rx="16" fill="#FCD2DC" stroke="#25212B" stroke-width="1.8"/>
    <!-- Star icon -->
    <path d="M18 10L20 14L24 14.5L21 17.5L22 22L18 19.5L14 22L15 17.5L12 14.5L16 14L18 10Z" fill="#25212B"/>
    <text x="30" y="21" font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">Currently Exploring</text>
  </g>

  <!-- Center Text -->
  <g transform="translate(216, 29)">
    <text font-family="'Courier New', Courier, Consolas, monospace" font-size="13" font-weight="bold" fill="#25212B">
      AI/ML <tspan fill="#685B72">|</tspan> Deep Learning <tspan fill="#685B72">|</tspan> Generative AI <tspan fill="#685B72">|</tspan> DSA <tspan fill="#685B72">|</tspan> System Design
    </text>
  </g>

  <!-- Right: Battery & Sleeping Cat -->
  <g transform="translate(740, 11)">
    <!-- Battery Level Indicator -->
    <g transform="translate(0, 7)">
      <rect x="0" y="0" width="58" height="16" rx="4" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <rect x="3" y="3" width="9" height="10" rx="1" fill="#FCD2DC"/>
      <rect x="14" y="3" width="9" height="10" rx="1" fill="#FCD2DC"/>
      <rect x="25" y="3" width="9" height="10" rx="1" fill="#FCD2DC"/>
      <rect x="36" y="3" width="9" height="10" rx="1" fill="#FCD2DC"/>
      <rect x="47" y="3" width="8" height="10" rx="1" fill="#F9EEF1"/>
      <!-- Battery terminal -->
      <path d="M58 5H60V11H58" fill="#25212B"/>
    </g>

    <!-- Sleeping Cat with z z z -->
    <g transform="translate(74, -2)">
      <!-- zzz text -->
      <text x="-12" y="8" font-family="'Courier New', Courier, Consolas, monospace" font-size="11" font-weight="bold" fill="#25212B">z<tspan font-size="9">z</tspan><tspan font-size="7">z</tspan></text>
      <!-- Cat Body -->
      <ellipse cx="28" cy="18" rx="20" ry="12" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <!-- Cat Head -->
      <ellipse cx="14" cy="16" rx="10" ry="9" fill="#FFFFFF" stroke="#25212B" stroke-width="1.5"/>
      <!-- Ears -->
      <path d="M8 10L11 4L14 10H8Z" fill="#FFFFFF" stroke="#25212B" stroke-width="1.2"/>
      <path d="M14 9L17 4L19 10H14Z" fill="#FFFFFF" stroke="#25212B" stroke-width="1.2"/>
      <path d="M9 9L11 6L13 9H9Z" fill="#FCD2DC"/>
      <path d="M15 8L17 6L18 8H15Z" fill="#FCD2DC"/>
      <!-- Sleeping Eyes (- -) -->
      <path d="M9 16C10 17 11 17 12 16" stroke="#25212B" stroke-width="1.2" stroke-linecap="round" fill="none"/>
      <path d="M14 16C15 17 16 17 17 16" stroke="#25212B" stroke-width="1.2" stroke-linecap="round" fill="none"/>
      <!-- Pink Blush -->
      <ellipse cx="8" cy="18" rx="1.5" ry="1" fill="#FCD2DC"/>
      <!-- Tail wrapped around -->
      <path d="M46 17C48 20 44 24 38 23" stroke="#25212B" stroke-width="2" stroke-linecap="round" fill="none"/>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# WRITE ASSETS TO DISK
# -------------------------------------------------------------

files_to_write = {
    "btn-portfolio.svg": BTN_PORTFOLIO,
    "btn-linkedin.svg": BTN_LINKEDIN,
    "btn-github.svg": BTN_GITHUB,
    "stats-bar.svg": STATS_BAR,
    "card-about-me.svg": CARD_ABOUT_ME,
    "card-tech-stack.svg": CARD_TECH_STACK,
    "window-featured-projects.svg": WINDOW_FEATURED_PROJECTS,
    "header-featured-projects.svg": HEADER_FEATURED,
    "card-project-1.svg": make_project_card(
        "Autonomous Social Media", "Content Creator &amp; Sched.",
        "AI-powered content creation and", "scheduling using Generative AI.",
        ["Python", "Streamlit", "GenAI"], "chart"
    ),
    "card-project-2.svg": make_project_card(
        "SmartSpend AI", "",
        "Personal expense analyzer and", "budgeting application with ML.",
        ["Python", "Machine Learning"], "coins"
    ),
    "card-project-3.svg": make_project_card(
        "Cyclone Intensity", "Classifier",
        "AI/ML system to classify tropical", "cyclone patterns using satellite data.",
        ["Python", "PyTorch", "EfficientNet"], "cyclone"
    ),
    "card-project-4.svg": make_project_card(
        "MedSight", "",
        "Deep learning-based medical image", "screening with Grad-CAM explanations.",
        ["Python", "Deep Learning", "Grad-CAM"], "medical"
    ),
    "footer-bar.svg": FOOTER_BAR,
}

for name, content in files_to_write.items():
    p = os.path.join(ASSETS_DIR, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {name}")

print("All assets generated successfully!")
