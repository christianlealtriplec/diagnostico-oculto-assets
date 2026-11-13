"""Objetos y escenarios del Capítulo 5 (bañera, megáfono, nota, nevera llena, camping gas, latas)."""
from draw import PAL


def megaphone_car(x=540, y=1560, s=1.0):
    """Coche municipal blanco con franja roja y megáfono en el techo; faros encendidos."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -420 0 L -420 -150 C -400 -190, -360 -200, -300 -205 L -200 -320 C -180 -340, 180 -340, 220 -320 L 320 -205 C 380 -200, 420 -180, 430 -150 L 430 0 Z" fill="#e8ecf2"/>'
            '<rect x="-420" y="-130" width="850" height="40" fill="#e10600"/>'
            '<path d="M -170 -300 L -40 -300 L -40 -210 L -260 -210 Z" fill="#1b2946"/>'
            '<path d="M 10 -300 L 190 -300 L 280 -210 L 10 -210 Z" fill="#1b2946"/>'
            '<circle cx="-250" cy="0" r="80" fill="#111"/><circle cx="-250" cy="0" r="34" fill="#666"/>'
            '<circle cx="270" cy="0" r="80" fill="#111"/><circle cx="270" cy="0" r="34" fill="#666"/>'
            '<ellipse cx="415" cy="-150" rx="22" ry="28" fill="#fff3d1"/>'
            '<polygon points="430,-150 1080,-320 1080,40" fill="#fff3d1" opacity="0.18"/>'
            '<rect x="-30" y="-380" width="60" height="50" fill="#333"/>'
            '<path d="M -20 -400 L -180 -470 L -180 -330 L -20 -380 Z" fill="#cfd4dc" stroke="#666" stroke-width="6"/>'
            '<path d="M 20 -400 L 180 -470 L 180 -330 L 20 -380 Z" fill="#cfd4dc" stroke="#666" stroke-width="6"/>'
            + "".join(f'<path d="M {-220 - i*50} -460 Q {-260 - i*50} -400 {-220 - i*50} -340" stroke="#ff9500" stroke-width="10" fill="none" opacity="{0.9 - i*0.25:.2f}"/>'
                      f'<path d="M {220 + i*50} -460 Q {260 + i*50} -400 {220 + i*50} -340" stroke="#ff9500" stroke-width="10" fill="none" opacity="{0.9 - i*0.25:.2f}"/>'
                      for i in range(3)) +
            '</g>')


def bathtub(x=540, y=1250, fill=0.7, running=True):
    """Bañera blanca vista de frente con grifo; agua a nivel `fill` (0–1)."""
    lvl = int(320 * fill)
    water = (f'<rect x="-430" y="{-lvl}" width="860" height="{lvl}" fill="#6fb6e8" opacity="0.75"/>'
             f'<path d="M -430 {-lvl} Q -215 {-lvl-14} 0 {-lvl} T 430 {-lvl}" stroke="#bfe6ff" stroke-width="8" fill="none"/>') if fill > 0 else ""
    jet = '<rect x="-360" y="-470" width="30" height="500" fill="#9fd4ff" opacity="0.8"/>' if running else ""
    return (f'<g transform="translate({x} {y})">'
            '<rect x="-400" y="-560" width="90" height="70" rx="14" fill="#b8bdc4"/>'
            '<path d="M -360 -490 L -360 -470" stroke="#b8bdc4" stroke-width="40"/>'
            f'{jet}'
            '<path d="M -470 -330 L 470 -330 L 440 40 C 430 80, 400 100, 360 100 L -360 100 C -400 100, -430 80, -440 40 Z" fill="#eef1f5"/>'
            f'<g transform="translate(0 40)"><clipPath id="tubclip"><rect x="-430" y="-360" width="860" height="360"/></clipPath><g clip-path="url(#tubclip)">{water}</g></g>'
            '<path d="M -470 -330 L 470 -330 L 470 -300 L -470 -300 Z" fill="#dfe3e8"/>'
            '<path d="M -440 100 L -400 180 M 440 100 L 400 180" stroke="#9aa1ab" stroke-width="22" stroke-linecap="round"/>'
            '</g>')


def note_under_door(x=540, y=1560, s=1.0, text=("Tengo radio.", "4.º A")):
    """Papel doblado asomando bajo la puerta, letra a mano."""
    t1, t2 = text
    return (f'<g transform="translate({x} {y}) scale({s}) rotate(-6)">'
            '<path d="M -260 -150 L 260 -170 L 280 150 L -250 170 Z" fill="#f4efe2"/>'
            '<path d="M -255 0 L 270 -10" stroke="#d8d0bd" stroke-width="4"/>'
            + "".join(f'<path d="M -220 {yy} L 230 {yy-8}" stroke="#c9d6ea" stroke-width="3"/>' for yy in (-90, -40, 50, 100)) +
            f'<text x="0" y="-55" font-family="DejaVu Serif" font-style="italic" font-weight="bold" font-size="66" fill="#1d2a6b" text-anchor="middle">{t1}</text>'
            f'<text x="0" y="80" font-family="DejaVu Serif" font-style="italic" font-weight="bold" font-size="78" fill="#1d2a6b" text-anchor="middle">{t2}</text>'
            '</g>')


def food_items(x=540, y=1000, s=1.0):
    """Pollo asado, embutido, tortilla y brik de leche en fila."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            # pollo
            '<ellipse cx="-330" cy="40" rx="150" ry="100" fill="#c9893a"/><ellipse cx="-360" cy="10" rx="60" ry="30" fill="#e0a85a" opacity="0.7"/>'
            '<path d="M -460 0 C -520 -40, -540 -10, -510 20" stroke="#c9893a" stroke-width="40" stroke-linecap="round" fill="none"/>'
            '<circle cx="-528" cy="-30" r="20" fill="#f1ead8"/>'
            '<ellipse cx="-330" cy="140" rx="190" ry="26" fill="#d7dbe2"/>'
            # embutido
            '<rect x="-140" y="-40" width="200" height="90" rx="45" fill="#a63a3a"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="8" fill="#f1d6d0"/>' for cx, cy in [(-100, -10), (-60, 20), (-20, -15), (20, 15)]) +
            '<ellipse cx="60" cy="5" rx="22" ry="45" fill="#c96060"/>'
            # tortilla
            '<ellipse cx="190" cy="80" rx="140" ry="60" fill="#e8c05a"/><path d="M 190 80 L 330 80 A 140 60 0 0 1 270 130 Z" fill="#f4e2a0"/>'
            '<ellipse cx="190" cy="125" rx="170" ry="22" fill="#d7dbe2"/>'
            # leche
            '<rect x="370" y="-150" width="120" height="250" fill="#f4f6f8"/><path d="M 370 -150 L 430 -200 L 490 -150 Z" fill="#e0e4ea"/>'
            '<rect x="370" y="-80" width="120" height="70" fill="#2d7fd1"/>'
            '<text x="430" y="-33" font-family="DejaVu Sans" font-weight="bold" font-size="28" fill="#fff" text-anchor="middle">LECHE</text>'
            '</g>')


def camping_stove(x=540, y=1300, s=1.0, low=True):
    """Hornillo de camping gas con cartucho azul y sartén encima; llama débil si low."""
    flame = ("".join(f'<path d="M {fx} -120 C {fx-14} -150, {fx+4} -170, {fx} -190 C {fx+14} -165, {fx+12} -140, {fx} -120 Z" fill="#4da3ff" opacity="0.85"/>'
                     for fx in (-80, -30, 20, 70)) if low else
             "".join(f'<path d="M {fx} -120 C {fx-24} -180, {fx+6} -220, {fx} -260 C {fx+26} -210, {fx+20} -170, {fx} -120 Z" fill="#ff9500"/>'
                     for fx in (-80, -30, 20, 70)))
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<ellipse cx="0" cy="40" rx="260" ry="50" fill="#2a2a2a"/>'
            '<rect x="-230" y="-110" width="460" height="150" rx="20" fill="#3a3f48"/>'
            '<circle cx="0" cy="-110" r="110" fill="#22252b"/>' + flame +
            '<path d="M -320 -220 L 300 -220 C 290 -170, 240 -150, 180 -150 L -200 -150 C -260 -150, -310 -170, -320 -220 Z" fill="#2b2b2b"/>'
            '<rect x="300" y="-215" width="260" height="30" rx="14" fill="#2b2b2b"/>'
            + "".join(f'<path d="M {px} -240 C {px-20} -300, {px+20} -340, {px} -400" stroke="#cfd4dc" stroke-width="10" fill="none" opacity="0.35"/>' for px in (-100, 0, 100)) +
            '<g transform="translate(-380 -60)"><rect x="-80" y="-140" width="160" height="240" rx="30" fill="#1f6fd1"/>'
            '<rect x="-30" y="-180" width="60" height="50" rx="10" fill="#aab"/>'
            '<text x="0" y="-20" font-family="DejaVu Sans" font-weight="bold" font-size="34" fill="#fff" text-anchor="middle">GAS</text>'
            '<rect x="-60" y="20" width="120" height="50" rx="8" fill="#0b2a55"/><rect x="-55" y="25" width="20" height="40" fill="#e10600"/></g>'
            '</g>')


def cans(x=540, y=1300, s=1.0, n=2):
    """Latas de conserva sobre la encimera."""
    out = ""
    for i in range(n):
        cx = (i - (n - 1) / 2) * 260
        out += (f'<g transform="translate({cx} 0)">'
                '<rect x="-100" y="-240" width="200" height="240" fill="#b8bdc4"/>'
                '<ellipse cx="0" cy="-240" rx="100" ry="26" fill="#d6dbe2"/><ellipse cx="0" cy="-240" rx="70" ry="16" fill="#9aa1ab"/>'
                f'<rect x="-100" y="-190" width="200" height="130" fill="{["#c0392b", "#2d7f4a"][i % 2]}"/>'
                f'<text x="0" y="-110" font-family="DejaVu Sans" font-weight="bold" font-size="36" fill="#fff" text-anchor="middle">{["ATÚN", "LENTEJAS"][i % 2] if i < 2 else "MAÍZ"}</text>'
                '<ellipse cx="0" cy="0" rx="100" ry="26" fill="#9aa1ab"/></g>')
    return f'<g transform="translate({x} {y}) scale({s})">{out}</g>'


def trash_bin(x=540, y=1500, s=1.0):
    """Cubo de basura con bolsa negra abierta."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -200 -320 L 200 -320 L 170 0 L -170 0 Z" fill="#2f5a3a"/>'
            '<path d="M -230 -340 L 230 -340 L 220 -300 L -220 -300 Z" fill="#14161b"/>'
            '<path d="M -230 -340 C -260 -400, -200 -420, -170 -380 M 230 -340 C 260 -400, 200 -420, 170 -380" stroke="#14161b" stroke-width="20" fill="none"/>'
            '<path d="M -120 -250 L 120 -250 M -120 -170 L 120 -170 M -120 -90 L 120 -90" stroke="#24452d" stroke-width="10"/>'
            '</g>')


def cloth_hand(x=540, y=1000, s=1.0):
    """Mano de niño envuelta sin apretar en un paño limpio blanco."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -420 260 C -300 200, -200 160, -120 150 L -100 300 C -200 320, -320 360, -420 400 Z" fill="#f2cf4a"/>'
            '<path d="M -130 140 C -40 60, 120 50, 220 90 C 300 120, 330 180, 300 230 C 250 300, 80 330, -110 310 Z" fill="url(#skin)"/>'
            + "".join(f'<path d="M {fx} {fy} C {fx+60} {fy-20}, {fx+130} {fy-10}, {fx+150} {fy+10} C {fx+140} {fy+40}, {fx+60} {fy+45}, {fx} {fy+35} Z" fill="url(#skin)"/>'
                      for fx, fy in [(180, 80), (210, 140), (200, 200), (170, 255)]) +
            '<path d="M -60 90 C 20 40, 200 50, 260 120 C 280 200, 220 290, 60 310 C -40 315, -90 260, -60 90 Z" fill="#f7f8fa" opacity="0.95"/>'
            '<path d="M -40 140 C 60 110, 160 120, 240 160 M -50 220 C 50 200, 160 210, 250 230" stroke="#d4d9e0" stroke-width="6" fill="none"/>'
            '</g>')


def ceiling_radio():
    """Techo oscuro con ondas de radio naranjas que bajan del piso de arriba."""
    return ('<rect width="1080" height="620" fill="#0b0d14"/>'
            '<path d="M 0 620 L 1080 620" stroke="#1a1e2a" stroke-width="12"/>'
            + "".join(f'<path d="M {540-120-i*90} {700+i*70} Q 540 {560+i*120} {540+120+i*90} {700+i*70}" stroke="#ff9500" stroke-width="12" fill="none" opacity="{0.9-i*0.2:.2f}"/>'
                      for i in range(4)) +
            '<rect x="430" y="380" width="220" height="130" rx="20" fill="#1c1c1f" opacity="0.55"/>'
            '<rect x="540" y="400" width="90" height="34" rx="6" fill="#ff9500" opacity="0.6"/>')
