"""Personajes y escenarios del Capítulo 3 (Hugo, el cuñado, el generador, el gas)."""
from draw import PAL, abuela, window, beam, phone_hand
from draw2 import wallpaper, floor_tiles
from draw3 import insulin_box, luis


def hugo(cx=540, cy=900, s=1.0, mood="ok", hands_head=False):
    """Hugo, sobrino de 7 años: pelo castaño revuelto, pijama amarillo de rayas."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    if mood == "pain":
        eyes = ('<path d="M 482 870 L 518 880" stroke="#3b2d26" stroke-width="9" stroke-linecap="round"/>'
                '<path d="M 598 870 L 562 880" stroke="#3b2d26" stroke-width="9" stroke-linecap="round"/>')
        mouth = '<path d="M 505 975 Q 540 950 575 975" stroke="#5a2a22" stroke-width="9" fill="none" stroke-linecap="round"/>'
        face = "#d9c9a8"
    elif mood == "sick":
        eyes = ('<path d="M 480 875 Q 500 865 520 875" stroke="#3b2d26" stroke-width="8" fill="none"/>'
                '<path d="M 560 875 Q 580 865 600 875" stroke="#3b2d26" stroke-width="8" fill="none"/>')
        mouth = '<ellipse cx="540" cy="970" rx="22" ry="16" fill="#3a1414"/>'
        face = "#c9cfa0"
    else:
        eyes = ('<ellipse cx="500" cy="875" rx="12" ry="14" fill="#2b211c"/><ellipse cx="580" cy="875" rx="12" ry="14" fill="#2b211c"/>'
                '<circle cx="504" cy="870" r="4" fill="#fff"/><circle cx="584" cy="870" r="4" fill="#fff"/>')
        mouth = '<path d="M 512 960 Q 540 980 568 960" stroke="#5a2a22" stroke-width="8" fill="none" stroke-linecap="round"/>'
        face = None
    stripes = "".join(f'<rect x="400" y="{y}" width="280" height="22" fill="#e0b52a"/>' for y in range(1140, 1520, 60))
    arms = ('<path d="M 420 1140 C 360 1060, 380 900, 440 840" stroke="#f2cf4a" stroke-width="56" fill="none" stroke-linecap="round"/>'
            '<path d="M 660 1140 C 720 1060, 700 900, 640 840" stroke="#f2cf4a" stroke-width="56" fill="none" stroke-linecap="round"/>'
            '<circle cx="445" cy="820" r="34" fill="url(#skin)"/><circle cx="635" cy="820" r="34" fill="url(#skin)"/>') if hands_head else (
            '<path d="M 410 1150 C 390 1260, 395 1330, 410 1380" stroke="#f2cf4a" stroke-width="56" fill="none" stroke-linecap="round"/>'
            '<path d="M 670 1150 C 690 1260, 685 1330, 670 1380" stroke="#f2cf4a" stroke-width="56" fill="none" stroke-linecap="round"/>'
            '<circle cx="410" cy="1400" r="30" fill="url(#skin)"/><circle cx="670" cy="1400" r="30" fill="url(#skin)"/>')
    tint = f'<ellipse cx="540" cy="900" rx="100" ry="110" fill="{face}" opacity="0.45"/>' if face else ""
    return (f'<g {t}>'
            '<path d="M 400 1560 C 400 1200, 450 1100, 540 1095 C 630 1100, 680 1200, 680 1560 Z" fill="#f2cf4a"/>' + stripes +
            '<rect x="515" y="1010" width="50" height="90" fill="#b98a66"/>'
            '<ellipse cx="540" cy="900" rx="110" ry="120" fill="url(#skin)"/>' + tint +
            '<ellipse cx="432" cy="905" rx="16" ry="26" fill="#b98a66"/><ellipse cx="648" cy="905" rx="16" ry="26" fill="#b98a66"/>'
            '<path d="M 432 870 C 410 760, 470 720, 540 720 C 620 720, 675 760, 650 870 C 640 810, 610 795, 580 800 L 590 770 L 555 795 L 545 760 L 520 798 L 500 775 L 495 805 C 465 810, 445 830, 432 870 Z" fill="#6b4226"/>'
            f'{eyes}<path d="M 540 890 Q 530 918 548 922" stroke="#b98a66" stroke-width="5" fill="none"/>{mouth}'
            '<ellipse cx="475" cy="930" rx="20" ry="11" fill="#e08f80" opacity="0.4"/><ellipse cx="605" cy="930" rx="20" ry="11" fill="#e08f80" opacity="0.4"/>'
            f'{arms}</g>')


def cunado(cx=540, cy=900, s=1.0, mood="happy", thumb=False):
    """Cuñado: 40 años, pelo negro engominado, bigote, chaqueta de cuadros naranja."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    mouth = ('<path d="M 495 955 Q 540 1000 585 955 Z" fill="#2a1410"/><rect x="505" y="955" width="70" height="10" fill="#f2f2f2"/>'
             if mood == "happy" else '<path d="M 505 965 L 575 965" stroke="#5a2a22" stroke-width="9" stroke-linecap="round"/>')
    plaid = "".join(f'<rect x="{x}" y="1080" width="14" height="480" fill="#7a3a12" opacity="0.6"/>' for x in range(380, 700, 60)) + \
            "".join(f'<rect x="360" y="{y}" width="360" height="14" fill="#7a3a12" opacity="0.6"/>' for y in range(1120, 1560, 60))
    arm = ('<path d="M 690 1150 C 790 1100, 840 1020, 860 940" stroke="#c4621f" stroke-width="76" fill="none" stroke-linecap="round"/>'
           '<circle cx="862" cy="915" r="40" fill="url(#skin)"/><rect x="850" y="850" width="24" height="60" rx="12" fill="#e7c09c"/>') if thumb else ""
    return (f'<g {t}>'
            '<path d="M 350 1560 C 350 1190, 430 1075, 540 1065 C 650 1075, 730 1190, 730 1560 Z" fill="#c4621f"/>' + plaid +
            '<path d="M 480 1068 L 540 1160 L 600 1068" fill="#2b2b2b"/>'
            f'{arm}<rect x="505" y="960" width="70" height="110" fill="{PAL["skin_d"]}"/>'
            '<ellipse cx="540" cy="880" rx="115" ry="135" fill="url(#skin)"/>'
            '<ellipse cx="424" cy="890" rx="17" ry="28" fill="#b98a66"/><ellipse cx="656" cy="890" rx="17" ry="28" fill="#b98a66"/>'
            '<path d="M 428 850 C 410 730, 480 700, 545 700 C 620 700, 675 735, 652 850 C 640 780, 610 760, 560 765 C 500 755, 450 780, 428 850 Z" fill="#141414"/>'
            '<path d="M 470 740 C 520 715, 600 715, 640 750" stroke="#3a3a3a" stroke-width="6" fill="none"/>'
            '<path d="M 475 820 L 522 815" stroke="#141414" stroke-width="12" stroke-linecap="round"/>'
            '<path d="M 605 820 L 558 815" stroke="#141414" stroke-width="12" stroke-linecap="round"/>'
            '<ellipse cx="500" cy="860" rx="11" ry="13" fill="#2b211c"/><ellipse cx="580" cy="860" rx="11" ry="13" fill="#2b211c"/>'
            '<path d="M 540 870 Q 528 905 548 912" stroke="#b98a66" stroke-width="5" fill="none"/>'
            '<path d="M 490 935 C 510 920, 570 920, 590 935 C 570 945, 510 945, 490 935 Z" fill="#141414"/>'
            f'{mouth}</g>')


def generator(x=540, y=1300, s=1.0, running=True, fumes=True):
    """Generador de gasolina rojo con marco negro; humo gris si está en marcha."""
    smoke = "".join(f'<circle cx="{820+i*30}" cy="{1080-i*90}" r="{50+i*22}" fill="#8a8f9c" opacity="{0.35-i*0.05:.2f}" filter="url(#blur6)"/>'
                    for i in range(6)) if (running and fumes) else ""
    shake = ('<path d="M 220 1250 l -30 -10 M 220 1300 l -40 0 M 860 1250 l 30 -10 M 860 1300 l 40 0" stroke="#ffd34d" stroke-width="8" stroke-linecap="round"/>'
             if running else "")
    return (f'<g transform="translate({x} {y}) scale({s}) translate(-540 -1300)">'
            '<ellipse cx="540" cy="1500" rx="360" ry="40" fill="#000" opacity="0.5"/>'
            '<rect x="250" y="1080" width="580" height="400" rx="30" fill="#c81f1f"/>'
            '<rect x="250" y="1080" width="580" height="80" rx="30" fill="#e23a3a"/>'
            '<rect x="230" y="1050" width="620" height="460" rx="20" fill="none" stroke="#1a1a1a" stroke-width="24"/>'
            '<rect x="300" y="1200" width="220" height="200" rx="16" fill="#2a2a2a"/>'
            + "".join(f'<rect x="320" y="{1220+i*36}" width="180" height="16" rx="8" fill="#444"/>' for i in range(5)) +
            '<rect x="560" y="1210" width="220" height="110" rx="10" fill="#1d1d1d"/>'
            '<circle cx="610" cy="1265" r="22" fill="#444"/><circle cx="680" cy="1265" r="22" fill="#444"/>'
            f'<circle cx="745" cy="1265" r="14" fill="{"#5cff9a" if running else "#333"}"/>'
            '<rect x="790" y="1100" width="70" height="40" rx="10" fill="#555"/>'
            '<path d="M 860 1120 C 900 1110, 900 1080, 880 1070" stroke="#555" stroke-width="22" fill="none"/>'
            f'{shake}</g>{smoke}')


def clock_hour(h, m=0):
    from draw3 import wall_clock
    return wall_clock(h, m)


def gas_swirls(op=0.18):
    return "".join(f'<path d="M {x} {y} c 120 -80, 240 80, 360 0 s 240 -80, 360 0" stroke="#c9d1e0" stroke-width="{w}" fill="none" '
                   f'opacity="{op}" filter="url(#blur6)" stroke-linecap="round"/>'
                   for x, y, w in [(-80, 520, 60), (140, 760, 80), (-40, 1000, 70), (200, 1240, 90), (0, 1480, 60), (260, 380, 50)])


def heater(x=780, y=1180, on=True):
    glow = f'<ellipse cx="{x+100}" cy="{y+120}" rx="260" ry="220" fill="#ff7a2a" opacity="0.25" filter="url(#blur6)"/>' if on else ""
    bars = "".join(f'<rect x="{x+30}" y="{y+40+i*50}" width="140" height="22" rx="11" fill="{"#ff5a1f" if on else "#4a2a20"}"/>' for i in range(4))
    return glow + f'<rect x="{x}" y="{y}" width="200" height="260" rx="20" fill="#3a3a3a"/>{bars}'


def candle(x=540, y=1100, s=1.0, lit=True):
    flame = (f'<ellipse cx="0" cy="-230" rx="160" ry="160" fill="#ffb84d" opacity="0.25" filter="url(#blur6)"/>'
             f'<path d="M 0 -270 C 30 -220, 25 -180, 0 -170 C -25 -180, -30 -220, 0 -270 Z" fill="#ffd34d"/>'
             f'<path d="M 0 -240 C 12 -215, 10 -190, 0 -185 C -10 -190, -12 -215, 0 -240 Z" fill="#fff6d0"/>') if lit else ""
    return (f'<g transform="translate({x} {y}) scale({s})">{flame}'
            '<rect x="-4" y="-175" width="8" height="25" fill="#222"/>'
            '<rect x="-50" y="-150" width="100" height="300" rx="10" fill="#f1ead8"/>'
            '<path d="M -50 -140 C -30 -120, -20 -100, -30 -60" stroke="#e2d8c0" stroke-width="12" fill="none"/>'
            '<ellipse cx="0" cy="150" rx="90" ry="22" fill="#8a7a5a"/></g>')


def lit_room():
    """Salón con la luz del generador: bombilla encendida, cálido."""
    return (wallpaper("#2a2418", "#252014") + floor_tiles(1500, "#2a2018", "#241b14") +
            '<line x1="540" y1="0" x2="540" y2="260" stroke="#111" stroke-width="8"/>'
            '<ellipse cx="540" cy="320" rx="420" ry="360" fill="#fff3d1" opacity="0.28" filter="url(#blur6)"/>'
            '<circle cx="540" cy="300" r="60" fill="#fff6d8"/>')
