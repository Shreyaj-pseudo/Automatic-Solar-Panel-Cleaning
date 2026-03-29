"""
Conveyor Film System — Minimal Flowchart
3 subsystems: Mechanical, Electrical, Software
Film loop: gear pinions + towel (microfibre cloth proxy) on underpass

Generates: conveyor_flowchart.png

Requirements:
    pip install cairosvg
    # macOS:  brew install cairo
    # Linux:  sudo apt install libcairo2
    # Windows: use WSL or install GTK

Run:
    python3 generate_flowchart.py
"""

import cairosvg

SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 1100" width="640" height="1100">

  <!-- Background -->
  <rect width="640" height="1100" fill="#0d1117"/>
  <radialGradient id="g1" cx="10%" cy="0%" r="55%">
    <stop offset="0%" stop-color="#10b981" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="g2" cx="90%" cy="100%" r="55%">
    <stop offset="0%" stop-color="#a855f7" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
  </radialGradient>
  <rect width="640" height="1100" fill="url(#g1)"/>
  <rect width="640" height="1100" fill="url(#g2)"/>

  <!-- ── TITLE ── -->
  <rect x="140" y="18" width="360" height="22" rx="11" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <text x="320" y="33" text-anchor="middle" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="2">PHASE 3 PROTOTYPE · SYSTEM ARCHITECTURE</text>
  <text x="175" y="70" font-family="sans-serif" font-size="26" font-weight="900" fill="#e6edf3">Conveyor</text>
  <text x="340" y="70" font-family="sans-serif" font-size="26" font-weight="900" fill="#10b981"> Film System</text>
  <text x="320" y="90" text-anchor="middle" font-family="monospace" font-size="10" fill="#7d8590">Signal &amp; mechanical data flow</text>

  <!-- ═══════════════════════════════
       SS-01  Structural   y=108
  ════════════════════════════════ -->
  <rect x="30" y="108" width="580" height="96" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="108" width="5"   height="96" rx="3"  fill="#10b981"/>
  <rect x="35" y="108" width="575" height="50" rx="12" fill="#1c2330"/>
  <rect x="35" y="130" width="575" height="28"          fill="#1c2330"/>
  <rect x="46" y="116" width="36" height="32" rx="9" fill="#041a10"/>
  <text x="64" y="137" text-anchor="middle" font-size="18" fill="#e6edf3">&#x1F3A1;</text>
  <text x="94" y="127" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="1.5">SUBSYSTEM 01 · Structural</text>
  <text x="94" y="146" font-family="sans-serif" font-size="15" font-weight="900" fill="#10b981">Structural Subsystem</text>
  <rect x="486" y="120" width="102" height="20" rx="7" fill="#031208" stroke="#10b981" stroke-width="1"/>
  <text x="537" y="134" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#10b981">TRANSMIT</text>
  <text x="46" y="164" font-family="monospace" font-size="9" fill="#7d8590">Film transport &amp; cleaning via synchronized belt motion</text>
  <line x1="30" y1="172" x2="610" y2="172" stroke="#30363d" stroke-width="1"/>
  <text x="46"  y="190" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">Nema 17</text>
  <text x="46"  y="203" font-family="monospace" font-size="8"  fill="#7d8590">Stepper motor</text>
  <line x1="148" y1="174" x2="148" y2="208" stroke="#30363d" stroke-width="1"/>
  <text x="162" y="190" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">5mm Pinion</text>
  <text x="162" y="203" font-family="monospace" font-size="8"  fill="#7d8590">Drive pulley</text>
  <line x1="270" y1="174" x2="270" y2="208" stroke="#30363d" stroke-width="1"/>
  <text x="284" y="190" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">XL Timing Belt</text>
  <text x="284" y="203" font-family="monospace" font-size="8"  fill="#7d8590">20in / 100T · no-slip</text>
  <line x1="410" y1="174" x2="410" y2="208" stroke="#30363d" stroke-width="1"/>
  <text x="424" y="190" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">Birch Dowels</text>
  <text x="424" y="203" font-family="monospace" font-size="8"  fill="#7d8590">2&#xD7; 5/16&quot; idler rollers</text>

  <!-- Arrow 1 -->
  <line x1="320" y1="210" x2="320" y2="228" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,223 326,223 320,232" fill="#f0a500"/>
  <rect x="140" y="214" width="360" height="18" rx="9" fill="#161b22" stroke="#f0a50055" stroke-width="1"/>
  <circle cx="156" cy="223" r="4" fill="#f0a500"/>
  <text x="320" y="227" text-anchor="middle" font-family="monospace" font-size="9" fill="#f0a500">Motor actuation command &#x2192; Nema 17 coils</text>

  <!-- ═══════════════════════════════
       SS-02  ELECTRICAL   y=234
  ════════════════════════════════ -->
  <rect x="30" y="234" width="580" height="96" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="234" width="5"   height="96" rx="3"  fill="#f0a500"/>
  <rect x="35" y="234" width="575" height="50" rx="12" fill="#1c2330"/>
  <rect x="35" y="256" width="575" height="28"          fill="#1c2330"/>
  <rect x="46" y="242" width="36" height="32" rx="9" fill="#2a1f05"/>
  <text x="64" y="263" text-anchor="middle" font-size="18" fill="#e6edf3">&#x26A1;</text>
  <text x="94" y="253" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="1.5">SUBSYSTEM 02 · ELECTRICAL</text>
  <text x="94" y="272" font-family="sans-serif" font-size="15" font-weight="900" fill="#f0a500">Electrical Subsystem</text>
  <rect x="478" y="246" width="110" height="20" rx="7" fill="#1f1500" stroke="#f0a500" stroke-width="1"/>
  <text x="533" y="260" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#f0a500">ACTUATE</text>
  <text x="46" y="290" font-family="monospace" font-size="9" fill="#7d8590">Controlled actuation via NEMA 17 and A4988 driver</text>
  <line x1="30" y1="298" x2="610" y2="298" stroke="#30363d" stroke-width="1"/>
  <text x="46"  y="316" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">AC-DC 12V 5A</text>
  <text x="46"  y="329" font-family="monospace" font-size="8"  fill="#7d8590">Primary supply</text>
  <line x1="178" y1="300" x2="178" y2="334" stroke="#30363d" stroke-width="1"/>
  <text x="192" y="316" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">Buck Converter</text>
  <text x="192" y="329" font-family="monospace" font-size="8"  fill="#7d8590">12V &#x2192; 5V logic rail</text>
  <line x1="324" y1="300" x2="324" y2="334" stroke="#30363d" stroke-width="1"/>
  <text x="338" y="316" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">A4988 Driver</text>
  <text x="338" y="329" font-family="monospace" font-size="8"  fill="#7d8590">STEP/DIR &#x2192; coil current</text>
  <line x1="468" y1="300" x2="468" y2="334" stroke="#30363d" stroke-width="1"/>
  
  <!-- Arrow 2 -->
  <line x1="320" y1="336" x2="320" y2="354" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,349 326,349 320,358" fill="#a855f7"/>
  <rect x="140" y="340" width="360" height="18" rx="9" fill="#161b22" stroke="#a855f755" stroke-width="1"/>
  <circle cx="156" cy="349" r="4" fill="#a855f7"/>
  <text x="320" y="353" text-anchor="middle" font-family="monospace" font-size="9" fill="#a855f7">STEP + DIR signals &#x2190; Pico W GPIO</text>

  <!-- ═══════════════════════════════
       SS-03  SOFTWARE   y=360
  ════════════════════════════════ -->
  <rect x="30" y="360" width="580" height="96" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="360" width="5"   height="96" rx="3"  fill="#a855f7"/>
  <rect x="35" y="360" width="575" height="50" rx="12" fill="#1c2330"/>
  <rect x="35" y="382" width="575" height="28"          fill="#1c2330"/>
  <rect x="46" y="368" width="36" height="32" rx="9" fill="#1a0d2a"/>
  <text x="64" y="389" text-anchor="middle" font-size="18" fill="#e6edf3">&#x1F4BB;</text>
  <text x="94" y="379" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="1.5">SUBSYSTEM 03 · SOFTWARE</text>
  <text x="94" y="398" font-family="sans-serif" font-size="15" font-weight="900" fill="#a855f7">Software Subsystem</text>
  <rect x="440" y="372" width="158" height="20" rx="7" fill="#170a24" stroke="#a855f7" stroke-width="1"/>
  <text x="519" y="386" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#a855f7">SENSE &amp; CONTROL</text>
  <text x="46" y="416" font-family="monospace" font-size="9" fill="#7d8590">Autonomous activation via photoresistor light sensing</text>
  <line x1="30" y1="424" x2="610" y2="424" stroke="#30363d" stroke-width="1"/>
  <text x="46"  y="442" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">Raspberry Pi Pico W</text>
  <text x="46"  y="455" font-family="monospace" font-size="8"  fill="#7d8590">MCU · ADC + STEP/DIR</text>
  <line x1="216" y1="426" x2="216" y2="460" stroke="#30363d" stroke-width="1"/>
  <text x="230" y="442" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">LDR + 1k&#937; Divider</text>
  <text x="230" y="455" font-family="monospace" font-size="8"  fill="#7d8590">0&#x2013;3.3V &#x2192; ADC pin</text>
  <line x1="386" y1="426" x2="386" y2="460" stroke="#30363d" stroke-width="1"/>
  <text x="400" y="442" font-family="sans-serif" font-size="10" font-weight="700" fill="#e6edf3">Threshold Logic</text>
  <text x="400" y="455" font-family="monospace" font-size="8"  fill="#7d8590">Light&#x2265;threshold &#x2192; RUN</text>

  <!-- Decision diamond -->
  <line x1="320" y1="462" x2="320" y2="480" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,475 326,475 320,484" fill="#a855f7"/>
  <polygon points="320,482 450,512 320,542 190,512" fill="#1c2330" stroke="#a855f7" stroke-width="2"/>
  <text x="320" y="508" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="900" fill="#a855f7">Light &#x2265; Threshold?</text>
  <text x="320" y="524" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="900" fill="#a855f7">(LDR reading)</text>
  <text x="158" y="508" text-anchor="end" font-family="monospace" font-size="9" fill="#7d8590">NO &#x2192;</text>
  <text x="158" y="520" text-anchor="end" font-family="monospace" font-size="9" fill="#7d8590">STANDBY</text>
  <text x="462" y="508" font-family="monospace" font-size="9" fill="#7d8590">&#x2190; YES</text>
  <text x="462" y="520" font-family="monospace" font-size="9" fill="#7d8590">RUN BELT</text>

  <!-- Arrow to film loop -->
  <line x1="320" y1="542" x2="320" y2="562" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,557 326,557 320,566" fill="#10b981"/>
  <rect x="158" y="546" width="324" height="18" rx="9" fill="#161b22" stroke="#10b98155" stroke-width="1"/>
  <circle cx="174" cy="555" r="4" fill="#10b981"/>
  <text x="320" y="559" text-anchor="middle" font-family="monospace" font-size="9" fill="#10b981">Belt enabled &#x2192; film advances over panel</text>

  <!-- ═══════════════════════════════════════════════════
       FILM LOOP DIAGRAM   y=568
       Layout:
         y=568 card background
         y=595 section label
         y=615 top film bar
         y=630 panel proxy bar
         y=645 return / towel bar
         y=680 gear SVGs at x=80 and x=560
  ════════════════════════════════════════════════════ -->
  <rect x="30" y="568" width="580" height="210" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="568" width="5"   height="210" rx="3"  fill="#10b981"/>

  <text x="56" y="586" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="2">FILM LOOP PATH — CROSS SECTION</text>

  <!-- ── GEAR / PINION at left (cx=82, cy=680) ── -->
  <!-- outer ring -->
  <circle cx="82" cy="680" r="26" fill="#0d1117" stroke="#10b981" stroke-width="2"/>
  <!-- hub -->
  <circle cx="82" cy="680" r="10" fill="#041a10" stroke="#10b981" stroke-width="1.5"/>
  <!-- 8 teeth as small rectangles rotated around centre -->
  <g transform="translate(82,680)">
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(0)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(45)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(90)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(135)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(180)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(225)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(270)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(315)"/>
  </g>
  <text x="82" y="724" text-anchor="middle" font-family="monospace" font-size="8" fill="#10b981">5mm pinion</text>

  <!-- ── GEAR / PINION at right (cx=558, cy=680) ── -->
  <circle cx="558" cy="680" r="26" fill="#0d1117" stroke="#10b981" stroke-width="2"/>
  <circle cx="558" cy="680" r="10" fill="#041a10" stroke="#10b981" stroke-width="1.5"/>
  <g transform="translate(558,680)">
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(0)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(45)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(90)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(135)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(180)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(225)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(270)"/>
    <rect x="-4" y="-34" width="8" height="10" rx="2" fill="#10b981" transform="rotate(315)"/>
  </g>
  <text x="558" y="724" text-anchor="middle" font-family="monospace" font-size="8" fill="#10b981">5mm pinion</text>

  <!-- TOP film strip -->
  <rect x="108" y="610" width="424" height="16" rx="4" fill="#041a10" stroke="#10b981" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="320" y="621" text-anchor="middle" font-family="monospace" font-size="8" fill="#10b981">TOP — dust collects here · transparent to light</text>

  <!-- Panel proxy bar -->
  <rect x="108" y="626" width="424" height="14" rx="2" fill="#111111" stroke="#7d8590" stroke-width="1"/>
  <text x="320" y="637" text-anchor="middle" font-family="monospace" font-size="8" fill="#7d8590">BLACK ACRYLIC — solar panel proxy</text>

  <!-- RETURN strip — transparent film on underpass -->
  <rect x="108" y="640" width="424" height="16" rx="4" fill="#170a24" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="320" y="651" text-anchor="middle" font-family="monospace" font-size="8" fill="#a855f7">RETURN — transparent film (underpass)</text>

  <!-- TOWEL / microfibre cloth proxy bar -->
  <rect x="180" y="658" width="280" height="20" rx="6" fill="#1a1000" stroke="#f0a500" stroke-width="1.5"/>
  <!-- hatching lines to look like cloth texture -->
  <line x1="196" y1="658" x2="186" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="210" y1="658" x2="200" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="224" y1="658" x2="214" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="238" y1="658" x2="228" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="252" y1="658" x2="242" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="266" y1="658" x2="256" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="280" y1="658" x2="270" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="294" y1="658" x2="284" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="308" y1="658" x2="298" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="322" y1="658" x2="312" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="336" y1="658" x2="326" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="350" y1="658" x2="340" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="364" y1="658" x2="354" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="378" y1="658" x2="368" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="392" y1="658" x2="382" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="406" y1="658" x2="396" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="420" y1="658" x2="410" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="434" y1="658" x2="424" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="448" y1="658" x2="438" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="460" y1="658" x2="450" y2="678" stroke="#f0a500" stroke-width="1" stroke-opacity="0.4"/>
  <text x="320" y="672" text-anchor="middle" font-family="monospace" font-size="8" font-weight="700" fill="#f0a500">TOWEL — microfibre cloth proxy · cleans film on underpass</text>

  <!-- direction arrows on film loop -->
  <!-- top: left to right arrow -->
  <polygon points="326,604 336,600 336,608" fill="#10b981"/>
  <!-- return: right to left arrow -->
  <polygon points="314,656 304,652 304,660" fill="#a855f7"/>

  <!-- ── LEGEND   y=792 ── -->
  <rect x="30" y="792" width="580" height="22" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <text x="52" y="807" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="1.5">LEGEND</text>
  <line x1="116" y1="803" x2="140" y2="803" stroke="#10b981" stroke-width="2"/>
  <text x="144" y="807" font-family="monospace" font-size="8" fill="#10b981">Structural</text>
  <line x1="230" y1="803" x2="254" y2="803" stroke="#f0a500" stroke-width="2"/>
  <text x="258" y="807" font-family="monospace" font-size="8" fill="#f0a500">Electrical / Cleaning cloth</text>
  <line x1="400" y1="803" x2="424" y2="803" stroke="#a855f7" stroke-width="2"/>
  <text x="428" y="807" font-family="monospace" font-size="8" fill="#a855f7">Software / Film return</text>
  <line x1="556" y1="800" x2="580" y2="800" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="556" y="807" font-family="monospace" font-size="8" fill="#7d8590"></text>

</svg>
"""

cairosvg.svg2png(
    bytestring=SVG.encode("utf-8"),
    write_to="conveyor_flowchart.png",
    output_width=1920,
    output_height=2640,
)

print("Done! Saved as conveyor_flowchart.png  (1920 x 2640px)")