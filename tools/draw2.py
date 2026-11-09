"""Escenarios adicionales (temporada 1) con más detalle."""
from draw import PAL, phone_hand, oxygen_bottle, concentrator, tube


def wallpaper(color="#151a2b", stripe="#11162a"):
    s = "".join(f'<rect x="{x}" y="0" width="28" height="1920" fill="{stripe}"/>' for x in range(0, 1080, 70))
    return f'<rect width="1080" height="1920" fill="{color}"/>{s}'


def floor_tiles(y=1450, c1="#1a1512", c2="#15110e"):
    t = "".join(f'<rect x="{x}" y="{y}" width="120" height="470" fill="{c1 if (x//120)%2 else c2}"/>' for x in range(0, 1080, 120))
    return t + f'<rect y="{y}" width="1080" height="12" fill="#0b0907"/>'


def living_room():
    """Salón en el momento del apagón: tele apagada, lámpara, tú en el sofá con el móvil."""
    return (wallpaper() + floor_tiles(1400) +
            '<rect x="620" y="300" width="360" height="520" fill="#2d4a7c" opacity="0.7"/>'
            '<rect x="620" y="300" width="360" height="520" fill="none" stroke="#05070d" stroke-width="16"/>'
            '<line x1="800" y1="300" x2="800" y2="820" stroke="#05070d" stroke-width="10"/>'
            '<rect x="90" y="560" width="440" height="270" rx="10" fill="#050608" stroke="#222634" stroke-width="10"/>'
            '<rect x="250" y="830" width="120" height="40" fill="#222634"/><rect x="70" y="870" width="480" height="40" rx="8" fill="#2a2018"/>'
            '<path d="M 870 1400 L 870 1000" stroke="#2a2a2a" stroke-width="10"/><path d="M 800 1010 L 940 1010 L 900 900 L 840 900 Z" fill="#3a3a40"/>'
            '<path d="M 60 1720 C 60 1450, 140 1380, 300 1380 L 820 1380 C 960 1380, 1020 1450, 1020 1720 Z" fill="#4b2a2a"/>'
            '<rect x="60" y="1560" width="960" height="200" rx="30" fill="#5a3232"/>'
            '<path d="M 420 1560 C 420 1420, 470 1360, 540 1360 C 610 1360, 660 1420, 660 1560 Z" fill="#1c2a48"/>'
            '<circle cx="540" cy="1290" r="70" fill="#1a1a22"/>'
            '<rect x="575" y="1370" width="70" height="120" rx="10" fill="#0e0e10" transform="rotate(20 610 1430)"/>'
            '<rect x="582" y="1380" width="56" height="100" rx="6" fill="#7aa7ff" transform="rotate(20 610 1430)"/>'
            '<ellipse cx="560" cy="1280" rx="110" ry="130" fill="#7aa7ff" opacity="0.18"/>')


def street():
    """Calle a oscuras: semáforos apagados, gente con linternas del móvil."""
    b = ""
    for i, (x, w, h) in enumerate([(-20, 260, 1300), (250, 220, 1150), (480, 300, 1400), (790, 310, 1250)]):
        b += f'<rect x="{x}" y="{1500-h}" width="{w}" height="{h}" fill="#0c1222" stroke="#070b16" stroke-width="4"/>'
        b += "".join(f'<rect x="{wx}" y="{wy}" width="30" height="46" fill="#101830"/>'
                     for wy in range(1500 - h + 50, 1450, 90) for wx in range(x + 25, x + w - 40, 60))
    people = ""
    for x, s in [(200, 1.0), (430, .8), (760, 1.1), (930, .7)]:
        people += (f'<g transform="translate({x} 1560) scale({s})"><circle cx="0" cy="-230" r="34" fill="#05070d"/>'
                   f'<path d="M -50 0 L -45 -180 C -40 -200, 40 -200, 45 -180 L 50 0 Z" fill="#05070d"/>'
                   f'<circle cx="38" cy="-150" r="8" fill="#fff"/><circle cx="38" cy="-150" r="40" fill="url(#glow)" opacity="0.6"/></g>')
    return ('<rect width="1080" height="1000" fill="url(#moonsky)"/>' + b +
            '<rect y="1500" width="1080" height="420" fill="#0d0f16"/>'
            '<rect y="1640" width="1080" height="16" fill="#1d2130"/>'
            '<rect x="900" y="1100" width="16" height="420" fill="#222"/><rect x="872" y="1010" width="72" height="190" rx="12" fill="#151515"/>'
            '<circle cx="908" cy="1050" r="20" fill="#2a0b0b"/><circle cx="908" cy="1105" r="20" fill="#2a240b"/><circle cx="908" cy="1160" r="20" fill="#0b2a12"/>'
            + people)


def hallway_door(label="3ºB", knock=True):
    hand = ('<path d="M 1080 1180 C 950 1150, 860 1120, 800 1100 L 790 1060 C 800 1030, 850 1030, 870 1050 L 900 1080 C 960 1090, 1020 1100, 1080 1110 Z" fill="#b98a66"/>'
            '<path d="M 1080 1230 C 980 1210, 900 1190, 840 1160 L 860 1110 C 940 1140, 1010 1160, 1080 1170 Z" fill="#1c2a48"/>') if knock else ""
    return (wallpaper("#14182a", "#10142a") + floor_tiles(1600, "#201913", "#1a140f") +
            '<rect x="260" y="350" width="560" height="1260" fill="#3a2a1e" stroke="#20170f" stroke-width="18"/>'
            '<rect x="320" y="420" width="440" height="500" fill="none" stroke="#2a1f16" stroke-width="10"/>'
            '<rect x="320" y="980" width="440" height="560" fill="none" stroke="#2a1f16" stroke-width="10"/>'
            '<circle cx="740" cy="1000" r="22" fill="#c9a24a"/><circle cx="540" cy="700" r="12" fill="#0a0a0a"/>'
            '<rect x="455" y="250" width="170" height="70" rx="8" fill="#c9a24a"/>'
            f'<text x="540" y="300" font-family="DejaVu Serif" font-weight="bold" font-size="46" fill="#2a1f16" text-anchor="middle">{label}</text>'
            '<polygon points="0,1920 0,1650 380,350 900,520 1080,900 1080,1920" fill="url(#beam)" opacity="0.75"/>' + hand)


def plug():
    """Primer plano: el enchufe de la pared con el cable de la máquina."""
    return (wallpaper("#171c2e", "#131829") +
            '<rect x="330" y="640" width="420" height="420" rx="40" fill="#e6e6e2" stroke="#b9b9b4" stroke-width="10"/>'
            '<circle cx="540" cy="850" r="150" fill="#d6d6d1" stroke="#b9b9b4" stroke-width="8"/>'
            '<rect x="430" y="780" width="220" height="150" rx="40" fill="#2a2a2e"/>'
            '<path d="M 540 930 C 540 1150, 420 1280, 300 1500 C 220 1650, 180 1800, 160 1920" stroke="#d8d8d8" stroke-width="30" fill="none"/>'
            '<path d="M 540 930 C 540 1150, 420 1280, 300 1500 C 220 1650, 180 1800, 160 1920" stroke="#bdbdbd" stroke-width="10" fill="none"/>'
            '<circle cx="770" cy="560" r="24" fill="#3a0a0a"/><circle cx="770" cy="560" r="10" fill="#5a1010"/>'
            '<polygon points="1080,1920 1080,1500 640,600 300,760 0,1920" fill="url(#beam)" opacity="0.65"/>')


def wardrobe(open_=True):
    clothes = "".join(f'<path d="M {x} 520 L {x-40} 560 L {x-50} {1000+((x*37)%180)} L {x+50} {1000+((x*37)%180)} L {x+40} 560 Z" fill="{c}"/>'
                      f'<path d="M {x} 470 C {x-12} 490, {x+12} 500, {x} 520" stroke="#888" stroke-width="5" fill="none"/>'
                      for x, c in [(330, "#4a3b5c"), (450, "#2f4f6f"), (750, "#6b3a3a")])
    return (wallpaper("#121626", "#0f1322") +
            '<rect x="160" y="300" width="760" height="1460" fill="#2a1f16" stroke="#17110c" stroke-width="20"/>'
            '<rect x="190" y="330" width="700" height="1400" fill="#0d0a08"/>'
            '<line x1="200" y1="470" x2="880" y2="470" stroke="#777" stroke-width="10"/>' + clothes +
            '<g transform="translate(560 1120) scale(0.55) translate(-430 -900)">' + oxygen_bottle(hand=False) + '</g>'
            '<path d="M 160 300 L -40 360 L -40 1720 L 160 1760 Z" fill="#33261b"/>'
            '<path d="M 920 300 L 1120 360 L 1120 1720 L 920 1760 Z" fill="#33261b"/>'
            '<polygon points="0,1920 0,1600 520,800 900,1000" fill="url(#beam)" opacity="0.8"/>')


def stairwell_down():
    """Hueco de escalera visto desde arriba: tres pisos de vértigo."""
    r = ""
    for i in range(9):
        m = 60 + i * 52
        r += f'<rect x="{m}" y="{m*1.75}" width="{1080-2*m}" height="{1920-3.5*m}" fill="none" stroke="{"#3a1414" if i%2 else "#1c2235"}" stroke-width="{26-2*i}"/>'
    return ('<rect width="1080" height="1920" fill="#06070c"/>' + r +
            '<rect x="500" y="900" width="80" height="120" fill="#000"/>'
            '<path d="M 0 0 L 300 0 L 120 600 Z" fill="#b98a66" opacity="0.9"/>'
            '<polygon points="140,0 520,960 560,960 260,0" fill="url(#beam)" opacity="0.6"/>')


def split_decision():
    """Pantalla partida: A (botella) / B (bajar a la calle)."""
    left = ('<rect width="540" height="1920" fill="#0f1a14"/>'
            '<g transform="translate(270 1000) scale(0.75) translate(-430 -900)">' + oxygen_bottle(hand=False) + '</g>'
            '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#3fd27a" text-anchor="middle" opacity="0.9">A</text>')
    right = ('<rect x="540" width="540" height="1920" fill="#1a0f12"/>'
             '<g transform="translate(540 0)">'
             '<polygon points="40,1900 500,1900 460,1500 80,1500" fill="#22263a"/><polygon points="80,1500 460,1500 420,1100 120,1100" fill="#1b1f30"/>'
             '<polygon points="120,1100 420,1100 380,700 160,700" fill="#151826"/>'
             '<circle cx="270" cy="1250" r="44" fill="#05070d"/><path d="M 220 1500 L 225 1300 C 230 1280, 310 1280, 315 1300 L 320 1500 Z" fill="#05070d"/>'
             '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#ff3b30" text-anchor="middle" opacity="0.9">B</text></g>')
    return left + right + '<rect x="532" width="16" height="1920" fill="#000"/>'
