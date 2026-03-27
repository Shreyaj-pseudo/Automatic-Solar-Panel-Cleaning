"""
Conveyor Film System — Two-Column Flowchart
Left column:  subsystem cards + arrows (the flow)
Right column: component details for each subsystem

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
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 1200" width="1100" height="1200">

  <!-- Background -->
  <rect width="1100" height="1200" fill="#0d1117"/>
  <radialGradient id="g1" cx="10%" cy="0%" r="50%">
    <stop offset="0%" stop-color="#f0a500" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="g2" cx="90%" cy="100%" r="50%">
    <stop offset="0%" stop-color="#10b981" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
  </radialGradient>
  <rect width="1100" height="1200" fill="url(#g1)"/>
  <rect width="1100" height="1200" fill="url(#g2)"/>

  <!-- vertical divider -->
  <line x1="490" y1="110" x2="490" y2="1155" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>

  <!-- TITLE -->
  <rect x="300" y="18" width="500" height="22" rx="11" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <text x="550" y="33" text-anchor="middle" font-family="monospace" font-size="10" fill="#7d8590" letter-spacing="2">PHASE 3 PROTOTYPE  ·  SYSTEM ARCHITECTURE</text>
  <text x="380" y="72" font-family="sans-serif" font-size="30" font-weight="900" fill="#e6edf3">Conveyor</text>
  <text x="570" y="72" font-family="sans-serif" font-size="30" font-weight="900" fill="#10b981"> Film System</text>
  <text x="550" y="92" text-anchor="middle" font-family="monospace" font-size="11" fill="#7d8590">Signal &amp; mechanical data flow</text>

  <!-- column headers -->
  <text x="245" y="112" text-anchor="middle" font-family="monospace" font-size="10" fill="#30363d" letter-spacing="2">SUBSYSTEM FLOW</text>
  <text x="790" y="112" text-anchor="middle" font-family="monospace" font-size="10" fill="#30363d" letter-spacing="2">COMPONENTS</text>

  <!-- ══ ROW 1 — SS-01 POWER  y=122 ══ -->
  <rect x="30" y="122" width="440" height="58" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="122" width="5"   height="58" rx="3"  fill="#f0a500"/>
  <rect x="44" y="131" width="32" height="28" rx="7" fill="#2a1f05"/>
  <text x="60" y="150" text-anchor="middle" font-size="16" fill="#e6edf3">&#x26A1;</text>
  <text x="86" y="141" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-01 · POWER SUBSYSTEM</text>
  <text x="86" y="158" font-family="sans-serif" font-size="15" font-weight="900" fill="#f0a500">Power Supply</text>
  <rect x="366" y="133" width="82" height="18" rx="6" fill="#1f1500" stroke="#f0a500" stroke-width="1"/>
  <text x="407" y="146" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#f0a500">SOURCE</text>

  <rect x="506" y="122" width="564" height="58" rx="12" fill="#161b22" stroke="#2a1f05" stroke-width="1"/>
  <text x="522" y="140" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">AC-DC 12V 5A</text>
  <text x="522" y="154" font-family="monospace"  font-size="9"  fill="#7d8590">Primary power source · drives motor + logic</text>
  <text x="700" y="140" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Buck Converter (20W DC-DC)</text>
  <text x="700" y="154" font-family="monospace"  font-size="9"  fill="#7d8590">Steps 12V down to 5V for Arduino logic rail</text>
  <text x="522" y="170" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Dual Rails</text>
  <text x="590" y="170" font-family="monospace"  font-size="9"  fill="#7d8590">12V motor / 5V logic — isolated to prevent MCU noise</text>
  <line x1="470" y1="151" x2="506" y2="151" stroke="#f0a500" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- arrow -->
  <line x1="250" y1="180" x2="250" y2="208" stroke="#30363d" stroke-width="2"/>
  <polygon points="244,202 256,202 250,212" fill="#f0a500"/>
  <rect x="118" y="186" width="264" height="16" rx="8" fill="#161b22" stroke="#f0a50055" stroke-width="1"/>
  <text x="250" y="197" text-anchor="middle" font-family="monospace" font-size="9" fill="#f0a500">5V to Arduino  |  12V to DRV8833</text>

  <!-- ══ ROW 2 — SS-02 INPUT  y=215 ══ -->
  <rect x="30" y="215" width="440" height="58" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="215" width="5"   height="58" rx="3"  fill="#3b82f6"/>
  <rect x="44" y="224" width="32" height="28" rx="7" fill="#071530"/>
  <text x="60" y="243" text-anchor="middle" font-size="16" fill="#e6edf3">&#x2600;</text>
  <text x="86" y="234" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-02 · INPUT SUBSYSTEM</text>
  <text x="86" y="251" font-family="sans-serif" font-size="15" font-weight="900" fill="#3b82f6">Photoresistor Light Sensor</text>
  <rect x="332" y="226" width="116" height="18" rx="6" fill="#05122a" stroke="#3b82f6" stroke-width="1"/>
  <text x="390" y="239" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#3b82f6">TRIGGER</text>

  <rect x="506" y="215" width="564" height="58" rx="12" fill="#161b22" stroke="#05122a" stroke-width="1"/>
  <text x="522" y="233" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Photoresistor (LDR)</text>
  <text x="522" y="247" font-family="monospace"  font-size="9"  fill="#7d8590">Reads ambient light · outputs analog voltage to ADC pin</text>
  <text x="700" y="233" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Voltage Divider</text>
  <text x="700" y="247" font-family="monospace"  font-size="9"  fill="#7d8590">LDR + 10k&#937; resistor · converts to 0-5V signal</text>
  <text x="522" y="263" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Threshold Logic</text>
  <text x="630" y="263" font-family="monospace"  font-size="9"  fill="#7d8590">analogRead() · light &gt;= threshold: RUN  |  dark: STOP</text>
  <line x1="470" y1="244" x2="506" y2="244" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- arrow to decision -->
  <line x1="250" y1="273" x2="250" y2="298" stroke="#30363d" stroke-width="2"/>
  <polygon points="244,292 256,292 250,302" fill="#3b82f6"/>
  <rect x="118" y="279" width="264" height="16" rx="8" fill="#161b22" stroke="#3b82f655" stroke-width="1"/>
  <text x="250" y="290" text-anchor="middle" font-family="monospace" font-size="9" fill="#3b82f6">Analog voltage to Arduino ADC</text>

  <!-- ══ DECISION DIAMOND  y=305 ══ -->
  <polygon points="250,302 390,335 250,368 110,335" fill="#1c2330" stroke="#3b82f6" stroke-width="2"/>
  <text x="250" y="330" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#3b82f6">Light Level</text>
  <text x="250" y="346" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#3b82f6">Above Threshold?</text>
  <text x="250" y="382" text-anchor="middle" font-family="monospace" font-size="9" fill="#7d8590">YES: RUN BELT    |    NO: STANDBY</text>

  <!-- decision right panel -->
  <rect x="506" y="308" width="564" height="58" rx="12" fill="#161b22" stroke="#1c2330" stroke-width="1"/>
  <text x="522" y="328" font-family="sans-serif" font-size="11" font-weight="700" fill="#3b82f6">Light Threshold Decision</text>
  <text x="522" y="344" font-family="monospace"  font-size="9"  fill="#7d8590">Daylight detected: belt enabled, cleaning cycle active</text>
  <text x="522" y="358" font-family="monospace"  font-size="9"  fill="#7d8590">Low light / night: motor halted, system in standby</text>
  <line x1="390" y1="335" x2="506" y2="335" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- arrow to control -->
  <line x1="250" y1="386" x2="250" y2="411" stroke="#30363d" stroke-width="2"/>
  <polygon points="244,405 256,405 250,415" fill="#a855f7"/>
  <rect x="118" y="392" width="264" height="16" rx="8" fill="#161b22" stroke="#a855f755" stroke-width="1"/>
  <text x="250" y="403" text-anchor="middle" font-family="monospace" font-size="9" fill="#a855f7">Run command to firmware logic</text>

  <!-- ══ ROW 3 — SS-03 CONTROL  y=418 ══ -->
  <rect x="30" y="418" width="440" height="58" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="418" width="5"   height="58" rx="3"  fill="#a855f7"/>
  <rect x="44" y="427" width="32" height="28" rx="7" fill="#1a0d2a"/>
  <text x="60" y="446" text-anchor="middle" font-size="16" fill="#e6edf3">&#x1F9E0;</text>
  <text x="86" y="437" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-03 · CONTROL SUBSYSTEM</text>
  <text x="86" y="454" font-family="sans-serif" font-size="15" font-weight="900" fill="#a855f7">Microcontroller</text>
  <rect x="366" y="429" width="82" height="18" rx="6" fill="#170a24" stroke="#a855f7" stroke-width="1"/>
  <text x="407" y="442" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#a855f7">BRAIN</text>

  <rect x="506" y="418" width="564" height="58" rx="12" fill="#161b22" stroke="#1a0d2a" stroke-width="1"/>
  <text x="522" y="436" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Arduino Nano</text>
  <text x="522" y="450" font-family="monospace"  font-size="9"  fill="#7d8590">Central logic unit · reads LDR ADC · drives motor output</text>
  <text x="700" y="436" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">ADC Sampling</text>
  <text x="700" y="450" font-family="monospace"  font-size="9"  fill="#7d8590">Continuous analogRead() · threshold compare</text>
  <text x="522" y="466" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Status LEDs</text>
  <text x="620" y="466" font-family="monospace"  font-size="9"  fill="#7d8590">Red LED = standby   Blue LED = belt running</text>
  <line x1="470" y1="447" x2="506" y2="447" stroke="#a855f7" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- arrow -->
  <line x1="250" y1="476" x2="250" y2="504" stroke="#30363d" stroke-width="2"/>
  <polygon points="244,498 256,498 250,508" fill="#a855f7"/>
  <rect x="100" y="482" width="300" height="16" rx="8" fill="#161b22" stroke="#a855f755" stroke-width="1"/>
  <text x="250" y="493" text-anchor="middle" font-family="monospace" font-size="9" fill="#a855f7">PWM + DIR signals to DRV8833</text>

  <!-- ══ ROW 4 — SS-04 DRIVE  y=511 ══ -->
  <rect x="30" y="511" width="440" height="58" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="511" width="5"   height="58" rx="3"  fill="#10b981"/>
  <rect x="44" y="520" width="32" height="28" rx="7" fill="#041a10"/>
  <text x="60" y="539" text-anchor="middle" font-size="16" fill="#e6edf3">&#x2699;</text>
  <text x="86" y="530" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-04 · DRIVE SUBSYSTEM</text>
  <text x="86" y="547" font-family="sans-serif" font-size="15" font-weight="900" fill="#10b981">Motor &amp; Driver</text>
  <rect x="352" y="522" width="96" height="18" rx="6" fill="#031208" stroke="#10b981" stroke-width="1"/>
  <text x="400" y="535" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#10b981">ACTUATE</text>

  <rect x="506" y="511" width="564" height="58" rx="12" fill="#161b22" stroke="#041a10" stroke-width="1"/>
  <text x="522" y="529" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">DRV8833 Motor Driver</text>
  <text x="522" y="543" font-family="monospace"  font-size="9"  fill="#7d8590">Dual H-bridge · converts PWM to stepper coil current</text>
  <text x="700" y="529" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Mini Stepper Motor Nema 8</text>
  <text x="700" y="543" font-family="monospace"  font-size="9"  fill="#7d8590">Precise step control · low-speed film advance</text>
  <text x="522" y="559" font-family="monospace"  font-size="9"  fill="#7d8590">Built-in overcurrent protection · direct Arduino PWM interface</text>
  <line x1="470" y1="540" x2="506" y2="540" stroke="#10b981" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- arrow -->
  <line x1="250" y1="569" x2="250" y2="597" stroke="#30363d" stroke-width="2"/>
  <polygon points="244,591 256,591 250,601" fill="#10b981"/>
  <rect x="118" y="575" width="264" height="16" rx="8" fill="#161b22" stroke="#10b98155" stroke-width="1"/>
  <text x="250" y="586" text-anchor="middle" font-family="monospace" font-size="9" fill="#10b981">Rotational torque to pinion pulley</text>

  <!-- ══ ROW 5 — SS-05 MECHANICAL  y=604 ══ -->
  <rect x="30" y="604" width="440" height="58" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="604" width="5"   height="58" rx="3"  fill="#0ea5e9"/>
  <rect x="44" y="613" width="32" height="28" rx="7" fill="#031520"/>
  <text x="60" y="632" text-anchor="middle" font-size="16" fill="#e6edf3">&#x1F3A1;</text>
  <text x="86" y="623" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-05 · MECHANICAL SUBSYSTEM</text>
  <text x="86" y="640" font-family="sans-serif" font-size="15" font-weight="900" fill="#0ea5e9">Belt, Pulley &amp; Frame</text>
  <rect x="340" y="615" width="108" height="18" rx="6" fill="#021018" stroke="#0ea5e9" stroke-width="1"/>
  <text x="394" y="628" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#0ea5e9">TRANSMIT</text>

  <rect x="506" y="604" width="564" height="58" rx="12" fill="#161b22" stroke="#021018" stroke-width="1"/>
  <text x="522" y="622" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">4mm 15-Tooth Pinion Pulley</text>
  <text x="522" y="636" font-family="monospace"  font-size="9"  fill="#7d8590">Motor-coupled · engages timing belt teeth precisely</text>
  <text x="700" y="622" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">XL Timing Belt</text>
  <text x="700" y="636" font-family="monospace"  font-size="9"  fill="#7d8590">20in / 100T 3/8in XL · no-slip positive drive</text>
  <text x="522" y="652" font-family="monospace"  font-size="9"  fill="#7d8590">Rigid frame maintains belt tension · guides film path · prevents wrinkling</text>
  <line x1="470" y1="633" x2="506" y2="633" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- arrow -->
  <line x1="250" y1="662" x2="250" y2="690" stroke="#30363d" stroke-width="2"/>
  <polygon points="244,684 256,684 250,694" fill="#0ea5e9"/>
  <rect x="118" y="668" width="264" height="16" rx="8" fill="#161b22" stroke="#0ea5e955" stroke-width="1"/>
  <text x="250" y="679" text-anchor="middle" font-family="monospace" font-size="9" fill="#0ea5e9">Belt tension drives film advance</text>

  <!-- ══ ROW 6 — SS-06 FILM  y=697 ══ -->
  <rect x="30" y="697" width="440" height="58" rx="12" fill="#1c2330" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="697" width="5"   height="58" rx="3"  fill="#f43f5e"/>
  <rect x="44" y="706" width="32" height="28" rx="7" fill="#230810"/>
  <text x="60" y="725" text-anchor="middle" font-size="16" fill="#e6edf3">&#x1F4FD;</text>
  <text x="86" y="716" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="1.5">SS-06 · FILM SUBSYSTEM</text>
  <text x="86" y="733" font-family="sans-serif" font-size="15" font-weight="900" fill="#f43f5e">Conveyor Film Loop</text>
  <rect x="366" y="708" width="82" height="18" rx="6" fill="#1e0409" stroke="#f43f5e" stroke-width="1"/>
  <text x="407" y="721" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#f43f5e">CLEAN</text>

  <rect x="506" y="697" width="564" height="58" rx="12" fill="#161b22" stroke="#1e0409" stroke-width="1"/>
  <text x="522" y="715" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Transparent Film Loop</text>
  <text x="522" y="729" font-family="monospace"  font-size="9"  fill="#7d8590">High-transmittance plastic · loops over panel collecting dust</text>
  <text x="700" y="715" font-family="sans-serif" font-size="11" font-weight="700" fill="#e6edf3">Return Path (Underside)</text>
  <text x="700" y="729" font-family="monospace"  font-size="9"  fill="#7d8590">Under-panel slit · gravity sheds particles at roller</text>
  <text x="522" y="745" font-family="monospace"  font-size="9"  fill="#7d8590">Panel glass never contacted · no scratch risk · clean film continuously re-enters top</text>
  <line x1="470" y1="726" x2="506" y2="726" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- ══ FILM LOOP DIAGRAM  y=773 ══ -->
  <rect x="30" y="773" width="1040" height="128" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <rect x="30" y="773" width="5" height="128" rx="3" fill="#f43f5e"/>
  <text x="60" y="793" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="2">FILM LOOP PATH</text>
  <!-- rollers -->
  <circle cx="130" cy="838" r="22" fill="#041a10" stroke="#10b981" stroke-width="2"/>
  <text x="130" y="844" text-anchor="middle" font-size="13" fill="#e6edf3">&#x1F504;</text>
  <circle cx="980" cy="838" r="22" fill="#041a10" stroke="#10b981" stroke-width="2"/>
  <text x="980" y="844" text-anchor="middle" font-size="13" fill="#e6edf3">&#x1F504;</text>
  <!-- top film -->
  <rect x="152" y="806" width="828" height="24" rx="4" fill="#1e0409" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="566" y="822" text-anchor="middle" font-family="monospace" font-size="10" fill="#f43f5e">TOP SURFACE (Active) — dust collects here · transparent to sunlight</text>
  <!-- panel -->
  <rect x="152" y="830" width="828" height="16" rx="2" fill="#0d2a1a" stroke="#10b981" stroke-width="1"/>
  <text x="566" y="842" text-anchor="middle" font-family="monospace" font-size="9" fill="#10b981">SOLAR PANEL — protected · no direct dust contact · full light transmission</text>
  <!-- return -->
  <rect x="152" y="846" width="828" height="22" rx="4" fill="#031520" stroke="#0ea5e9" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="566" y="861" text-anchor="middle" font-family="monospace" font-size="10" fill="#0ea5e9">RETURN PATH (Underside) — gravity sheds dust particles at roller bend</text>

  <!-- ══ LEGEND  y=918 ══ -->
  <rect x="30" y="916" width="1040" height="24" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1"/>
  <text x="55"  y="932" font-family="monospace" font-size="9" fill="#7d8590" letter-spacing="2">LEGEND</text>
  <line x1="120" y1="928" x2="146" y2="928" stroke="#f0a500" stroke-width="2"/>
  <text x="150" y="932" font-family="monospace" font-size="9" fill="#f0a500">DC Power</text>
  <line x1="232" y1="928" x2="258" y2="928" stroke="#3b82f6" stroke-width="2"/>
  <text x="262" y="932" font-family="monospace" font-size="9" fill="#3b82f6">Sensor Signal</text>
  <line x1="360" y1="928" x2="386" y2="928" stroke="#a855f7" stroke-width="2"/>
  <text x="390" y="932" font-family="monospace" font-size="9" fill="#a855f7">Control / PWM</text>
  <line x1="492" y1="928" x2="518" y2="928" stroke="#10b981" stroke-width="2"/>
  <text x="522" y="932" font-family="monospace" font-size="9" fill="#10b981">Mech. Torque</text>
  <line x1="622" y1="928" x2="648" y2="928" stroke="#0ea5e9" stroke-width="2"/>
  <text x="652" y="932" font-family="monospace" font-size="9" fill="#0ea5e9">Belt Advance</text>
  <line x1="750" y1="925" x2="776" y2="925" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="5,2"/>
  <text x="780" y="932" font-family="monospace" font-size="9" fill="#f43f5e">Film Loop</text>
  <line x1="870" y1="925" x2="896" y2="925" stroke="#7d8590" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="900" y="932" font-family="monospace" font-size="9" fill="#7d8590">SS to Components</text>

</svg>
"""

cairosvg.svg2png(
    bytestring=SVG.encode("utf-8"),
    write_to="conveyor_flowchart.png",
    output_width=2200,
    output_height=2400,
)

print("Done! Saved as conveyor_flowchart.png  (2200 x 2400px)")