"""
Conveyor Film System — Minimal Flowchart
Single column · subsystem cards · pill-labelled arrows

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
    <stop offset="0%" stop-color="#f0a500" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="g2" cx="90%" cy="100%" r="55%">
    <stop offset="0%" stop-color="#10b981" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
  </radialGradient>
  <rect width="640" height="1100" fill="url(#g1)"/>
  <rect width="640" height="1100" fill="url(#g2)"/>

  <!-- TITLE -->
  <rect x="140" y="18" width="360" height="22" rx="11" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <text x="320" y="33" text-anchor="middle" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="2">PHASE 3 PROTOTYPE · SYSTEM ARCHITECTURE</text>
  <text x="175" y="70" font-family="sans-serif" font-size="26" font-weight="900" fill="#e6edf3">Conveyor</text>
  <text x="340" y="70" font-family="sans-serif" font-size="26" font-weight="900" fill="#10b981"> Film System</text>
  <text x="320" y="90" text-anchor="middle" font-family="monospace" font-size="10" fill="#7d8590">Signal &amp; mechanical data flow</text>

  <!-- ═══ SS-01 POWER  y=108 ═══ -->
  <rect x="30" y="108" width="580" height="68" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="108" width="5"   height="68" rx="3"  fill="#f0a500"/>
  <rect x="46" y="118" width="34" height="30" rx="8" fill="#2a1f05"/>
  <text x="63" y="138" text-anchor="middle" font-size="17" fill="#e6edf3">&#x26A1;</text>
  <text x="92" y="129" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-01 · POWER SUBSYSTEM</text>
  <text x="92" y="148" font-family="sans-serif" font-size="15" font-weight="900" fill="#f0a500">Power Supply</text>
  <rect x="504" y="120" width="84" height="20" rx="7" fill="#1f1500" stroke="#f0a500" stroke-width="1"/>
  <text x="546" y="134" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#f0a500">SOURCE</text>
  <text x="92" y="166" font-family="monospace" font-size="9" fill="#7d8590">AC-DC 12V 5A  ·  20W Buck Converter  ·  Dual 12V/5V Rails</text>

  <!-- Arrow 1 -->
  <line x1="320" y1="176" x2="320" y2="196" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,191 326,191 320,200" fill="#f0a500"/>
  <rect x="162" y="180" width="316" height="18" rx="9" fill="#161b22" stroke="#f0a50055" stroke-width="1"/>
  <circle cx="178" cy="189" r="4" fill="#f0a500"/>
  <text x="320" y="193" text-anchor="middle" font-family="monospace" font-size="9" fill="#f0a500">5V &#x2192; Pico W  |  12V &#x2192; A4988 Driver</text>

  <!-- ═══ SS-02 INPUT  y=202 ═══ -->
  <rect x="30" y="202" width="580" height="68" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="202" width="5"   height="68" rx="3"  fill="#3b82f6"/>
  <rect x="46" y="212" width="34" height="30" rx="8" fill="#071530"/>
  <text x="63" y="232" text-anchor="middle" font-size="17" fill="#e6edf3">&#x2600;</text>
  <text x="92" y="223" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-02 · INPUT SUBSYSTEM</text>
  <text x="92" y="242" font-family="sans-serif" font-size="15" font-weight="900" fill="#3b82f6">Photoresistor Light Sensor</text>
  <rect x="488" y="214" width="100" height="20" rx="7" fill="#05122a" stroke="#3b82f6" stroke-width="1"/>
  <text x="538" y="228" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#3b82f6">TRIGGER</text>
  <text x="92" y="260" font-family="monospace" font-size="9" fill="#7d8590">LDR + 1k&#937; Voltage Divider  ·  ADC Threshold Logic (0&#x2013;3.3V)</text>

  <!-- Arrow 2 -->
  <line x1="320" y1="270" x2="320" y2="290" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,285 326,285 320,294" fill="#3b82f6"/>
  <rect x="158" y="274" width="324" height="18" rx="9" fill="#161b22" stroke="#3b82f655" stroke-width="1"/>
  <circle cx="174" cy="283" r="4" fill="#3b82f6"/>
  <text x="320" y="287" text-anchor="middle" font-family="monospace" font-size="9" fill="#3b82f6">Analog voltage &#x2192; Pico W ADC pin (GP26)</text>

  <!-- ═══ DECISION  y=296 ═══ -->
  <polygon points="320,294 480,330 320,366 160,330" fill="#1c2330" stroke="#3b82f6" stroke-width="2"/>
  <text x="320" y="325" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="900" fill="#3b82f6">Light Level</text>
  <text x="320" y="342" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="900" fill="#3b82f6">Above Threshold?</text>
  <text x="128" y="326" text-anchor="end" font-family="monospace" font-size="9" fill="#7d8590">NO</text>
  <text x="128" y="338" text-anchor="end" font-family="monospace" font-size="9" fill="#7d8590">STANDBY</text>
  <text x="512" y="326" font-family="monospace" font-size="9" fill="#7d8590">YES</text>
  <text x="512" y="338" font-family="monospace" font-size="9" fill="#7d8590">RUN</text>

  <!-- Arrow 3 -->
  <line x1="320" y1="366" x2="320" y2="386" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,381 326,381 320,390" fill="#a855f7"/>
  <rect x="158" y="370" width="324" height="18" rx="9" fill="#161b22" stroke="#a855f755" stroke-width="1"/>
  <circle cx="174" cy="379" r="4" fill="#a855f7"/>
  <text x="320" y="383" text-anchor="middle" font-family="monospace" font-size="9" fill="#a855f7">Run command &#x2192; firmware step logic</text>

  <!-- ═══ SS-03 CONTROL  y=392 ═══ -->
  <rect x="30" y="392" width="580" height="68" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="392" width="5"   height="68" rx="3"  fill="#a855f7"/>
  <rect x="46" y="402" width="34" height="30" rx="8" fill="#1a0d2a"/>
  <text x="63" y="422" text-anchor="middle" font-size="17" fill="#e6edf3">&#x1F9E0;</text>
  <text x="92" y="413" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-03 · CONTROL SUBSYSTEM</text>
  <text x="92" y="432" font-family="sans-serif" font-size="15" font-weight="900" fill="#a855f7">Microcontroller</text>
  <rect x="516" y="404" width="72" height="20" rx="7" fill="#170a24" stroke="#a855f7" stroke-width="1"/>
  <text x="552" y="418" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#a855f7">BRAIN</text>
  <text x="92" y="450" font-family="monospace" font-size="9" fill="#7d8590">Raspberry Pi Pico W  ·  ADC sampling  ·  Red/Blue status LEDs</text>

  <!-- Arrow 4 -->
  <line x1="320" y1="460" x2="320" y2="480" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,475 326,475 320,484" fill="#a855f7"/>
  <rect x="140" y="464" width="360" height="18" rx="9" fill="#161b22" stroke="#a855f755" stroke-width="1"/>
  <circle cx="156" cy="473" r="4" fill="#a855f7"/>
  <text x="320" y="477" text-anchor="middle" font-family="monospace" font-size="9" fill="#a855f7">STEP + DIR pulses &#x2192; A4988 input pins</text>

  <!-- ═══ SS-04 DRIVE  y=486 ═══ -->
  <rect x="30" y="486" width="580" height="68" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="486" width="5"   height="68" rx="3"  fill="#10b981"/>
  <rect x="46" y="496" width="34" height="30" rx="8" fill="#041a10"/>
  <text x="63" y="516" text-anchor="middle" font-size="17" fill="#e6edf3">&#x2699;</text>
  <text x="92" y="507" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-04 · DRIVE SUBSYSTEM</text>
  <text x="92" y="526" font-family="sans-serif" font-size="15" font-weight="900" fill="#10b981">Motor &amp; Driver</text>
  <rect x="500" y="498" width="98" height="20" rx="7" fill="#031208" stroke="#10b981" stroke-width="1"/>
  <text x="549" y="512" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#10b981">ACTUATE</text>
  <text x="92" y="544" font-family="monospace" font-size="9" fill="#7d8590">A4988 Driver Carrier  ·  Nema 17 Stepper Motor</text>

  <!-- Arrow 5 -->
  <line x1="320" y1="554" x2="320" y2="574" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,569 326,569 320,578" fill="#10b981"/>
  <rect x="140" y="558" width="360" height="18" rx="9" fill="#161b22" stroke="#10b98155" stroke-width="1"/>
  <circle cx="156" cy="567" r="4" fill="#10b981"/>
  <text x="320" y="571" text-anchor="middle" font-family="monospace" font-size="9" fill="#10b981">Shaft torque &#x2192; 5mm pinion pulley &#x2192; XL belt</text>

  <!-- ═══ SS-05 MECHANICAL  y=580 ═══ -->
  <rect x="30" y="580" width="580" height="68" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="580" width="5"   height="68" rx="3"  fill="#0ea5e9"/>
  <rect x="46" y="590" width="34" height="30" rx="8" fill="#031520"/>
  <text x="63" y="610" text-anchor="middle" font-size="17" fill="#e6edf3">&#x1F3A1;</text>
  <text x="92" y="601" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-05 · MECHANICAL SUBSYSTEM</text>
  <text x="92" y="620" font-family="sans-serif" font-size="15" font-weight="900" fill="#0ea5e9">Belt, Pulley &amp; Frame</text>
  <rect x="486" y="592" width="112" height="20" rx="7" fill="#021018" stroke="#0ea5e9" stroke-width="1"/>
  <text x="542" y="606" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#0ea5e9">TRANSMIT</text>
  <text x="92" y="638" font-family="monospace" font-size="9" fill="#7d8590">5mm Pinion  ·  20in XL Belt  ·  2&#xD7; 5/16&quot; Birch Dowel Idlers  ·  Frame</text>

  <!-- Arrow 6 -->
  <line x1="320" y1="648" x2="320" y2="668" stroke="#30363d" stroke-width="2"/>
  <polygon points="314,663 326,663 320,672" fill="#0ea5e9"/>
  <rect x="158" y="652" width="324" height="18" rx="9" fill="#161b22" stroke="#0ea5e955" stroke-width="1"/>
  <circle cx="174" cy="661" r="4" fill="#0ea5e9"/>
  <text x="320" y="665" text-anchor="middle" font-family="monospace" font-size="9" fill="#0ea5e9">Belt tension &#x2192; film advance over panel</text>

  <!-- ═══ SS-06 FILM  y=674 ═══ -->
  <rect x="30" y="674" width="580" height="68" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="674" width="5"   height="68" rx="3"  fill="#f43f5e"/>
  <rect x="46" y="684" width="34" height="30" rx="8" fill="#230810"/>
  <text x="63" y="704" text-anchor="middle" font-size="17" fill="#e6edf3">&#x1F4FD;</text>
  <text x="92" y="695" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-06 · FILM SUBSYSTEM</text>
  <text x="92" y="714" font-family="sans-serif" font-size="15" font-weight="900" fill="#f43f5e">Conveyor Film Loop</text>
  <rect x="516" y="686" width="72" height="20" rx="7" fill="#1e0409" stroke="#f43f5e" stroke-width="1"/>
  <text x="552" y="700" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#f43f5e">CLEAN</text>
  <text x="92" y="732" font-family="monospace" font-size="9" fill="#7d8590">Transparent film over black acrylic proxy  ·  loops via birch dowel idlers  ·  gravity sheds dust</text>

  <!-- ═══ FILM LOOP DIAGRAM  y=758 ═══ -->
  <rect x="30" y="758" width="580" height="112" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="758" width="5" height="112" rx="3" fill="#f43f5e"/>
  <text x="56" y="776" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="2">FILM LOOP PATH</text>
  <!-- dowel rollers -->
  <circle cx="90"  cy="830" r="18" fill="#1a0f05" stroke="#10b981" stroke-width="2"/>
  <text x="90"  y="835" text-anchor="middle" font-size="11" fill="#e6edf3">&#x1FAB5;</text>
  <circle cx="550" cy="830" r="18" fill="#1a0f05" stroke="#10b981" stroke-width="2"/>
  <text x="550" y="835" text-anchor="middle" font-size="11" fill="#e6edf3">&#x1FAB5;</text>
  <!-- labels under rollers -->
  <text x="90"  y="856" text-anchor="middle" font-family="monospace" font-size="7" fill="#7d8590">5/16&quot; birch</text>
  <text x="550" y="856" text-anchor="middle" font-family="monospace" font-size="7" fill="#7d8590">5/16&quot; birch</text>
  <!-- top film -->
  <rect x="108" y="804" width="442" height="16" rx="4" fill="#1e0409" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="329" y="815" text-anchor="middle" font-family="monospace" font-size="8" fill="#f43f5e">TOP — dust collects here · transparent to light</text>
  <!-- panel proxy -->
  <rect x="108" y="820" width="442" height="14" rx="2" fill="#111" stroke="#10b981" stroke-width="1"/>
  <text x="329" y="831" text-anchor="middle" font-family="monospace" font-size="8" fill="#10b981">BLACK ACRYLIC (solar panel proxy) — protected surface</text>
  <!-- return -->
  <rect x="108" y="834" width="442" height="16" rx="4" fill="#031520" stroke="#0ea5e9" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="329" y="845" text-anchor="middle" font-family="monospace" font-size="8" fill="#0ea5e9">RETURN — gravity sheds dust at dowel roller bend</text>

  <!-- ═══ LEGEND  y=880 ═══ -->
  <rect x="30" y="880" width="580" height="22" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <text x="50"  y="895" font-family="monospace" font-size="8" fill="#7d8590" letter-spacing="1.5">LEGEND</text>
  <line x1="108" y1="891" x2="128" y2="891" stroke="#f0a500" stroke-width="2"/>
  <text x="132" y="895" font-family="monospace" font-size="8" fill="#f0a500">DC Power</text>
  <line x1="198" y1="891" x2="218" y2="891" stroke="#3b82f6" stroke-width="2"/>
  <text x="222" y="895" font-family="monospace" font-size="8" fill="#3b82f6">Sensor</text>
  <line x1="264" y1="891" x2="284" y2="891" stroke="#a855f7" stroke-width="2"/>
  <text x="288" y="895" font-family="monospace" font-size="8" fill="#a855f7">Control/STEP</text>
  <line x1="374" y1="891" x2="394" y2="891" stroke="#10b981" stroke-width="2"/>
  <text x="398" y="895" font-family="monospace" font-size="8" fill="#10b981">Torque</text>
  <line x1="444" y1="891" x2="464" y2="891" stroke="#0ea5e9" stroke-width="2"/>
  <text x="468" y="895" font-family="monospace" font-size="8" fill="#0ea5e9">Belt</text>
  <line x1="498" y1="888" x2="518" y2="888" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="522" y="895" font-family="monospace" font-size="8" fill="#f43f5e">Film Loop</text>

</svg>
"""

cairosvg.svg2png(
    bytestring=SVG.encode("utf-8"),
    write_to="conveyor_flowchart.png",
    output_width=1920,
    output_height=3300,
)

print("Done! Saved as conveyor_flowchart.png  (1920 x 3300px)")