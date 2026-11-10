"""Personajes y escenarios de la Parte 2 (Luis, su mujer, insulina, nevera)."""
from draw import PAL, oxygen_bottle, abuela, window, beam
from draw2 import wallpaper, floor_tiles


def luis(cx=540, cy=900, s=1.0, mood="worry", box=True):
    """Luis, vecino del 2.º: 60 años, pelo canoso rizado, gafas, jersey verde oliva."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    brows = ('<path d="M 470 812 L 520 800" stroke="#5a5a5a" stroke-width="10" stroke-linecap="round"/>'
             '<path d="M 610 812 L 560 800" stroke="#5a5a5a" stroke-width="10" stroke-linecap="round"/>') if mood == "worry" else (
             '<path d="M 470 805 Q 495 795 520 805" stroke="#5a5a5a" stroke-width="10" fill="none"/>'
             '<path d="M 560 805 Q 585 795 610 805" stroke="#5a5a5a" stroke-width="10" fill="none"/>')
    mouth = ('<path d="M 505 960 Q 540 940 575 960" stroke="#5a2a22" stroke-width="8" fill="none" stroke-linecap="round"/>'
             if mood == "worry" else '<ellipse cx="540" cy="955" rx="26" ry="20" fill="#2a1410"/>')
    bx = ('<g transform="rotate(-8 540 1230)">'
          '<rect x="430" y="1160" width="220" height="130" rx="8" fill="#f4f6f8" stroke="#c7ccd3" stroke-width="5"/>'
          '<rect x="430" y="1160" width="220" height="34" fill="#2d7fd1"/>'
          '<text x="540" y="1250" font-family="DejaVu Sans" font-weight="bold" font-size="30" fill="#1d3f6b" text-anchor="middle">INSULINA</text>'
          '<ellipse cx="440" cy="1240" rx="40" ry="28" fill="url(#skin)"/><ellipse cx="640" cy="1240" rx="40" ry="28" fill="url(#skin)"/></g>'
          ) if box else ""
    arms = ('<path d="M 400 1120 C 380 1200, 400 1240, 440 1240" stroke="#55603a" stroke-width="70" fill="none" stroke-linecap="round"/>'
            '<path d="M 680 1120 C 700 1200, 680 1240, 640 1240" stroke="#55603a" stroke-width="70" fill="none" stroke-linecap="round"/>') if box else ""
    return (f'<g {t}>'
            '<path d="M 350 1560 C 350 1180, 430 1070, 540 1060 C 650 1070, 730 1180, 730 1560 Z" fill="#55603a"/>'
            '<path d="M 490 1062 L 540 1120 L 590 1062" fill="none" stroke="#e8e2d6" stroke-width="14"/>'
            f'{arms}<rect x="505" y="960" width="70" height="110" fill="{PAL["skin_d"]}"/>'
            '<ellipse cx="540" cy="880" rx="118" ry="138" fill="url(#skin)"/>'
            '<ellipse cx="422" cy="890" rx="18" ry="30" fill="#b98a66"/><ellipse cx="658" cy="890" rx="18" ry="30" fill="#b98a66"/>'
            '<path d="M 425 850 C 405 740, 470 700, 540 700 C 620 700, 680 740, 655 850 C 645 790, 600 770, 540 775 C 480 770, 440 790, 425 850 Z" fill="#9b9ea6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="#a9acb4"/>' for x, y in [(450, 760), (490, 725), (540, 712), (590, 725), (630, 760)]) +
            '<circle cx="497" cy="860" r="34" fill="#cfe3ff" fill-opacity="0.25" stroke="#222" stroke-width="7"/>'
            '<circle cx="583" cy="860" r="34" fill="#cfe3ff" fill-opacity="0.25" stroke="#222" stroke-width="7"/>'
            '<line x1="531" y1="860" x2="549" y2="860" stroke="#222" stroke-width="7"/>'
            '<circle cx="497" cy="862" r="8" fill="#222"/><circle cx="583" cy="862" r="8" fill="#222"/>'
            f'{brows}<path d="M 540 870 Q 528 905 548 912" stroke="#b98a66" stroke-width="5" fill="none"/>{mouth}'
            f'{bx}</g>')


def mujer_luis(cx=540, cy=900, s=1.0, point=True):
    """Pilar, mujer de Luis: moño oscuro, bata granate, señalando con decisión."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    arm = ('<path d="M 690 1140 C 790 1090, 860 1000, 900 920" stroke="#7a2438" stroke-width="72" fill="none" stroke-linecap="round"/>'
           '<circle cx="905" cy="905" r="38" fill="url(#skin)"/><path d="M 918 892 L 975 835" stroke="#e7c09c" stroke-width="22" stroke-linecap="round"/>') if point else ""
    return (f'<g {t}>'
            '<path d="M 370 1560 C 370 1190, 440 1075, 540 1065 C 640 1075, 710 1190, 710 1560 Z" fill="#7a2438"/>'
            '<path d="M 470 1075 L 540 1300 L 610 1075" fill="none" stroke="#5c1a2a" stroke-width="16"/>'
            f'{arm}<rect x="510" y="965" width="60" height="105" fill="#b98a66"/>'
            '<ellipse cx="540" cy="880" rx="108" ry="132" fill="url(#skin)"/>'
            '<circle cx="540" cy="700" r="62" fill="#2a1d18"/>'
            '<path d="M 432 870 C 420 760, 480 735, 540 735 C 610 735, 665 760, 650 870 C 630 810, 600 790, 540 790 C 480 790, 450 810, 432 870 Z" fill="#2a1d18"/>'
            '<path d="M 478 820 L 522 830" stroke="#2a1d18" stroke-width="9" stroke-linecap="round"/>'
            '<path d="M 602 820 L 558 830" stroke="#2a1d18" stroke-width="9" stroke-linecap="round"/>'
            '<ellipse cx="500" cy="860" rx="10" ry="12" fill="#2b211c"/><ellipse cx="580" cy="860" rx="10" ry="12" fill="#2b211c"/>'
            '<path d="M 540 870 Q 528 900 548 906" stroke="#b98a66" stroke-width="5" fill="none"/>'
            '<ellipse cx="540" cy="950" rx="24" ry="16" fill="#3a1414"/>'
            '<circle cx="434" cy="900" r="9" fill="#d9b44a"/><circle cx="646" cy="900" r="9" fill="#d9b44a"/></g>')


def fridge(open_=True, freezer_open=False, x=260, y=360):
    """Nevera combi sin luz; puerta abierta, interior oscuro."""
    shelves = "".join(f'<rect x="{x+30}" y="{y+yy}" width="500" height="10" fill="#3a404c"/>' for yy in (720, 900, 1080))
    food = (f'<rect x="{x+70}" y="{y+640}" width="90" height="80" rx="10" fill="#c2b07a"/>'
            f'<rect x="{x+200}" y="{y+620}" width="70" height="100" rx="10" fill="#e8eef5"/>'
            f'<ellipse cx="{x+380}" cy="{y+860}" rx="90" ry="40" fill="#d7a24a"/>'
            f'<rect x="{x+100}" y="{y+1000}" width="140" height="80" rx="10" fill="#b84a4a"/>')
    inner = (f'<rect x="{x+20}" y="{y+560}" width="520" height="680" fill="#151922"/>{shelves}{food}'
             f'<circle cx="{x+480}" cy="{y+600}" r="16" fill="#2a2f3a"/>') if open_ else ""
    door = (f'<path d="M {x+560} {y+540} L {x+800} {y+480} L {x+800} {y+1340} L {x+560} {y+1260} Z" fill="#d9dde3"/>'
            f'<path d="M {x+580} {y+620} L {x+780} {y+580} L {x+780} {y+1260} L {x+580} {y+1200} Z" fill="#c4c9d1"/>') if open_ else (
            f'<rect x="{x+20}" y="{y+560}" width="520" height="680" fill="#dfe3e8"/>'
            f'<rect x="{x+480}" y="{y+620}" width="18" height="260" rx="9" fill="#9aa1ab"/>')
    frz = (f'<rect x="{x+20}" y="{y+40}" width="520" height="460" fill="#0f141c"/>'
           + "".join(f'<rect x="{x+60+i*95}" y="{y+330-(i%2)*40}" width="80" height="80" rx="12" fill="#cfefff" opacity="0.85"/>' for i in range(5))
           + f'<path d="M {x+560} {y+40} L {x+800} {y+0} L {x+800} {y+520} L {x+560} {y+500} Z" fill="#d9dde3"/>'
           ) if freezer_open else (
           f'<rect x="{x+20}" y="{y+40}" width="520" height="460" fill="#e3e7ec"/>'
           f'<rect x="{x+480}" y="{y+120}" width="18" height="200" rx="9" fill="#9aa1ab"/>')
    return (f'<rect x="{x}" y="{y}" width="560" height="1260" rx="30" fill="#c8ccd3"/>{frz}'
            f'<rect x="{x}" y="{y+520}" width="560" height="20" fill="#9aa1ab"/>{inner}{door}')


def insulin_box(x=540, y=960, s=1.0, rot=-6):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            '<rect x="-260" y="-150" width="520" height="300" rx="14" fill="#f4f6f8" stroke="#c7ccd3" stroke-width="8"/>'
            '<rect x="-260" y="-150" width="520" height="70" fill="#2d7fd1"/>'
            '<text x="0" y="20" font-family="DejaVu Sans" font-weight="bold" font-size="66" fill="#1d3f6b" text-anchor="middle">INSULINA</text>'
            '<text x="0" y="80" font-family="DejaVu Sans" font-size="30" fill="#556" text-anchor="middle">5 plumas precargadas</text>'
            '<text x="0" y="122" font-family="DejaVu Sans" font-size="24" fill="#889" text-anchor="middle">Conservar en nevera · No congelar</text>'
            '</g>')


def insulin_pen(x=540, y=960, s=1.0, rot=-30, frost=False):
    fr = ('<rect x="-330" y="-60" width="660" height="120" rx="50" fill="#e8f7ff" opacity="0.55"/>'
          + "".join(f'<circle cx="{a}" cy="{b}" r="7" fill="#fff"/>' for a, b in [(-250, -40), (-120, 45), (30, -45), (170, 40), (260, -30)])) if frost else ""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            '<rect x="-300" y="-45" width="460" height="90" rx="40" fill="#e9edf2" stroke="#9aa1ab" stroke-width="5"/>'
            '<rect x="-160" y="-30" width="170" height="60" rx="10" fill="#cfe7ff" opacity="0.8"/>'
            '<rect x="160" y="-40" width="120" height="80" rx="20" fill="#2d7fd1"/>'
            '<rect x="280" y="-22" width="50" height="44" rx="10" fill="#1d3f6b"/>'
            f'<rect x="-330" y="-20" width="40" height="40" rx="8" fill="#9aa1ab"/>{fr}</g>')


def wall_clock(h=3, m=0, x=540, y=820, r=300):
    import math
    ticks = "".join(f'<line x1="{x+math.sin(math.radians(a))*(r-30)}" y1="{y-math.cos(math.radians(a))*(r-30)}" '
                    f'x2="{x+math.sin(math.radians(a))*(r-60)}" y2="{y-math.cos(math.radians(a))*(r-60)}" stroke="#2a2a2a" stroke-width="10"/>'
                    for a in range(0, 360, 30))
    ah = math.radians((h % 12) * 30 + m * 0.5); am = math.radians(m * 6)
    return (f'<circle cx="{x}" cy="{y}" r="{r+20}" fill="#2a2018"/><circle cx="{x}" cy="{y}" r="{r}" fill="#e9e4d8"/>{ticks}'
            f'<line x1="{x}" y1="{y}" x2="{x+math.sin(ah)*r*0.5}" y2="{y-math.cos(ah)*r*0.5}" stroke="#111" stroke-width="18" stroke-linecap="round"/>'
            f'<line x1="{x}" y1="{y}" x2="{x+math.sin(am)*r*0.78}" y2="{y-math.cos(am)*r*0.78}" stroke="#111" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="16" fill="{PAL["red"]}"/>')


def ice_bowl():
    cubes = "".join(f'<rect x="{x}" y="{y}" width="110" height="110" rx="18" fill="#d8f2ff" opacity="0.9" transform="rotate({r} {x+55} {y+55})"/>'
                     f'<rect x="{x+18}" y="{y+16}" width="40" height="18" rx="8" fill="#fff" opacity="0.8" transform="rotate({r} {x+55} {y+55})"/>'
                     for x, y, r in [(260, 860, -10), (380, 820, 12), (510, 850, -4), (640, 830, 18), (330, 960, 6), (470, 950, -15), (600, 960, 9)])
    return (wallpaper("#121826", "#0f1422") +
            '<rect y="1250" width="1080" height="670" fill="#2a2018"/>'
            '<path d="M 180 1000 L 900 1000 C 880 1250, 760 1320, 540 1320 C 320 1320, 200 1250, 180 1000 Z" fill="#4a6fa5"/>'
            + cubes +
            '<ellipse cx="540" cy="1000" rx="360" ry="40" fill="none" stroke="#6b8fc4" stroke-width="12"/>'
            '<polygon points="0,1920 0,1550 420,700 1000,860" fill="url(#beam)" opacity="0.7"/>')


def cool_room():
    """Rincón fresco y en sombra (despensa interior, lejos de ventanas y calor)."""
    return (wallpaper("#101626", "#0d1220") + floor_tiles(1500, "#161310", "#12100d") +
            '<rect x="200" y="380" width="680" height="1120" fill="#1f1a15" stroke="#14100c" stroke-width="16"/>'
            + "".join(f'<rect x="220" y="{y}" width="640" height="16" fill="#3a2d22"/>' for y in (620, 880, 1140, 1400)) +
            '<rect x="260" y="520" width="90" height="100" rx="8" fill="#6b5a3a"/><rect x="370" y="540" width="90" height="80" rx="8" fill="#7a3a2a"/>'
            '<rect x="600" y="780" width="70" height="100" rx="8" fill="#4a5a7a"/><rect x="690" y="800" width="70" height="80" rx="8" fill="#3a4a3a"/>'
            '<rect x="440" y="1040" width="200" height="100" rx="8" fill="#f4f6f8"/><rect x="440" y="1040" width="200" height="26" fill="#2d7fd1"/>'
            '<text x="540" y="1112" font-family="DejaVu Sans" font-weight="bold" font-size="26" fill="#1d3f6b" text-anchor="middle">INSULINA</text>'
            '<circle cx="940" cy="900" r="70" fill="#3d5d92" opacity="0.25"/>'
            '<polygon points="0,1920 0,1650 470,1000 760,1100" fill="url(#beam)" opacity="0.65"/>')


def split_p2():
    """Pantalla partida: A (congelador con hielo) / B (sitio fresco)."""
    left = ('<rect width="540" height="1920" fill="#0d1726"/>'
            '<g transform="translate(-80 260) scale(0.62)">' + fridge(open_=False, freezer_open=True) + '</g>'
            '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#7fd0ff" text-anchor="middle" opacity="0.9">A</text>')
    right = ('<rect x="540" width="540" height="1920" fill="#16110c"/>'
             '<g transform="translate(540 0)">'
             '<rect x="70" y="900" width="400" height="760" fill="#1f1a15" stroke="#14100c" stroke-width="12"/>'
             + "".join(f'<rect x="80" y="{y}" width="380" height="12" fill="#3a2d22"/>' for y in (1080, 1280, 1480)) +
             '<rect x="170" y="1180" width="200" height="100" rx="8" fill="#f4f6f8"/><rect x="170" y="1180" width="200" height="26" fill="#2d7fd1"/>'
             '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#ff3b30" text-anchor="middle" opacity="0.9">B</text></g>')
    return left + right + '<rect x="532" width="16" height="1920" fill="#000"/>'
