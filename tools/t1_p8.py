"""Escenas de la Parte 08 · Vuelve a irse (arco «Sin fecha de fin»; sin votación previa)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, street
from draw3 import wall_clock
from draw4 import hugo, cunado, lit_room
from draw5 import radio

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p8"

DARK_ROOM = wallpaper("#121626", "#0f1322") + floor_tiles(1500, "#17130f", "#120f0c")
DEAD_BULB = ('<line x1="540" y1="0" x2="540" y2="260" stroke="#111" stroke-width="8"/>'
             '<circle cx="540" cy="300" r="60" fill="#2a2a30" stroke="#3a3a44" stroke-width="6"/>'
             '<path d="M 515 300 q 12 -30 25 0 q 12 30 25 0" stroke="#55555f" stroke-width="5" fill="none"/>')
FLICKER = ('<path d="M 470 230 l -60 -50 M 610 230 l 60 -50 M 540 200 l 0 -80 M 440 320 l -80 0 M 640 320 l 80 0" '
           'stroke="#ffd400" stroke-width="12" stroke-linecap="round"/>')
LANDING = (wallpaper("#10142a", "#0d1124") + floor_tiles(1450, "#1c1813", "#16120e") +
           '<rect x="0" y="1450" width="1080" height="40" fill="#2a2018"/>'
           '<path d="M 80 1450 L 80 700 M 80 700 L 1000 700" stroke="#3a1414" stroke-width="22"/>'
           + ''.join(f'<rect x="{90+i*80}" y="700" width="10" height="750" fill="#2a0f0f"/>' for i in range(12)) +
           '<text x="900" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="60" fill="#3a3f55">2.º</text>')
BEAM_ON = lambda x, y: f'<polygon points="0,1920 0,1600 {x-250},{y-300} {x+300},{y-250} 1080,1500 1080,1920" fill="url(#beam)" opacity="0.8"/>'
STATIC = ''.join(f'<rect x="{(i*137)%1080}" y="{(i*271)%1920}" width="{20+(i*7)%60}" height="4" fill="#cfd6e6" opacity="0.18"/>' for i in range(160))


def bump_hugo(cx, cy, s, mood="pain", hands_head=True):
    """Hugo con un chichón morado en la frente (mismas coordenadas que hugo())."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    return (hugo(cx, cy, s, mood=mood, hands_head=hands_head) +
            f'<g {t}><ellipse cx="575" cy="808" rx="38" ry="30" fill="#8a3a6a"/>'
            f'<ellipse cx="568" cy="800" rx="16" ry="10" fill="#c46a9a" opacity="0.7"/></g>')


def flashlight(x, y, rot=-30, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            '<rect x="-40" y="0" width="80" height="260" rx="20" fill="#2b2b30"/><rect x="-55" y="-60" width="110" height="80" rx="14" fill="#3a3a40"/>'
            '<ellipse cx="0" cy="-60" rx="55" ry="14" fill="#fff6d8"/>'
            '<ellipse cx="-10" cy="180" rx="70" ry="90" fill="url(#skin)"/></g>')


def ambulance(x=540, y=1560, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<rect x="-330" y="-380" width="560" height="340" rx="24" fill="#e9eef5"/><path d="M 230 -300 L 330 -300 L 380 -180 L 380 -40 L 230 -40 Z" fill="#dfe5ee"/>'
            '<path d="M 245 -285 L 320 -285 L 360 -190 L 245 -190 Z" fill="#1a2a44"/>'
            '<rect x="-330" y="-180" width="710" height="40" fill="#d23"/><path d="M -100 -320 v 110 M -155 -265 h 110" stroke="#2a6bff" stroke-width="30"/>'
            '<circle cx="-200" cy="-30" r="58" fill="#111"/><circle cx="260" cy="-30" r="58" fill="#111"/>'
            '<rect x="-60" y="-420" width="120" height="40" rx="10" fill="#2a6bff"/>'
            '<ellipse cx="0" cy="-400" rx="320" ry="120" fill="#3f86ff" opacity="0.35" filter="url(#blur6)"/></g>')


def memory_frame(inner):
    """Foto antigua: marco blanco ladeado con un recuerdo dentro."""
    return ('<g transform="translate(540 900) rotate(-5)"><rect x="-380" y="-460" width="760" height="900" fill="#e8e2d6"/>'
            '<rect x="-340" y="-420" width="680" height="720" fill="#1a2238"/>'
            '<clipPath id="mem"><rect x="-340" y="-420" width="680" height="720"/></clipPath>'
            f'<g clip-path="url(#mem)">{inner}</g>'
            '<text x="0" y="390" font-family="DejaVu Sans" font-size="44" fill="#5a4a3a" text-anchor="middle">LA PRIMERA NOCHE</text></g>')


scenes = {
    # apertura
    "01_parpadea": svg(lit_room() + '<rect width="1080" height="1920" fill="#000" opacity="0.45"/>' + FLICKER +
                       cunado(300, 960, 0.7, mood="serious") + hugo(770, 1080, 0.6, mood="ok")),
    "02_una_dos": svg(DARK_ROOM + DEAD_BULB + '<ellipse cx="540" cy="320" rx="300" ry="260" fill="#fff3d1" opacity="0.10" filter="url(#blur6)"/>'
                      + cunado(300, 960, 0.7, mood="serious") + hugo(770, 1080, 0.6, mood="pain")),
    "03_se_va": svg('<rect width="1080" height="1920" fill="#030409"/>' + DEAD_BULB +
                    '<g opacity="0.35">' + cunado(300, 960, 0.7, mood="serious") + hugo(770, 1080, 0.6, mood="pain") + '</g>'),
    # Hugo en la escalera
    "04_hugo_grita": svg(LANDING + '<rect width="1080" height="1920" fill="#000" opacity="0.35"/>'
                         + ''.join(f'<path d="M {660+i*20} {880+i*70} l 90 {-30+i*30}" stroke="#ff3b30" stroke-width="12" stroke-linecap="round"/>' for i in range(3))
                         + '<g opacity="0.55">' + bump_hugo(560, 1150, 0.5) + '</g>'),
    "05_bajas_linterna": svg(stairs()),
    "06_hugo_rellano": svg(LANDING + BEAM_ON(560, 1000) + bump_hugo(560, 1050, 0.85)),
    "07_chichon": svg('<rect width="1080" height="1920" fill="#0e0a0c"/>' + BEAM_ON(540, 900) + bump_hugo(540, 1150, 1.7, hands_head=False)),
    # arriba: Don Ramón y la radio
    "08_ramon_dial": svg(wallpaper("#1a1612", "#15110e") + floor_tiles(1600, "#201913", "#1a140f") +
                         '<ellipse cx="540" cy="1000" rx="520" ry="600" fill="#ffb84d" opacity="0.10" filter="url(#blur6)"/>'
                         + don_ramon(540, 900, 1.1, mood="serious") +
                         ''.join(f'<path d="M 860 {720-i*50} a {60+i*50} {60+i*50} 0 0 1 0 {120+i*100}" stroke="#ffb84d" stroke-width="10" fill="none" opacity="{0.8-i*0.2:.1f}"/>' for i in range(3))),
    "09_ambulancia": svg(street() + '<rect width="1080" height="1920" fill="#2a6bff" opacity="0.12"/>' + ambulance(540, 1640, 0.95)),
    "10_mandas_tu": svg(DARK_ROOM + BEAM_ON(540, 1000) + flashlight(880, 1500, rot=-25) +
                        cunado(330, 980, 0.75, mood="serious") + hugo(700, 1120, 0.6, mood="pain")),
    "11_estatica": svg('<rect width="1080" height="1920" fill="#0c0a10"/>' + radio(540, 1100, 1.3) + STATIC +
                       '<path d="M 120 650 l 60 -40 l 60 70 l 60 -90 l 60 110 l 60 -60 l 60 30 l 60 -80 l 60 100 l 60 -50 l 60 20 l 60 -40 l 60 30" stroke="#ffb84d" stroke-width="8" fill="none" opacity="0.8"/>'),
    "12_voz_tio": svg('<rect width="1080" height="1920" fill="#08070c"/>' + radio(540, 1380, 0.9, waves=True) +
                      '<g opacity="0.45">' + tio(540, 640, 0.75) + '</g>' + STATIC),
    "13_recuerdo_tio": svg('<rect width="1080" height="1920" fill="#05060a"/>' +
                           memory_frame('<g transform="translate(-540 -900)">' + city_night() + tio(540, 1000, 0.8) + '</g>')),
    # Hugo tiene sueño
    "14_hugo_bosteza": svg(DARK_ROOM + BEAM_ON(540, 1000) + bump_hugo(540, 1050, 1.0, mood="sick", hands_head=False)),
    "15_cunado_dormir": svg(DARK_ROOM + BEAM_ON(540, 900) + cunado(540, 950, 1.05, mood="serious", thumb=True)),
    # decisión
    "16_decision": svg('<rect width="540" height="1920" fill="#0a0c16"/><rect x="540" width="540" height="1920" fill="#14100c"/>'
                       '<g transform="translate(-103 400) scale(0.65)">' + bed(220, 760) + '</g>'
                       + '<g transform="translate(-103 400) scale(0.65)">' + bump_hugo(450, 980, 0.55, mood="sick", hands_head=False) + blanket(220, 1150) + '</g>'
                       + '<text x="300" y="760" font-family="DejaVu Sans" font-weight="bold" font-size="90" fill="#7a86a8" text-anchor="middle">Zzz</text>'
                       + wall_clock(3, 0, 810, 780, 190) + flashlight(810, 1420, rot=-10, s=0.9) +
                       '<polygon points="760,1360 860,1360 1040,1000 600,1000" fill="url(#beam)" opacity="0.5"/>'
                       '<rect x="532" y="0" width="16" height="1920" fill="#e10600"/>'),
    "17_no_vengais": svg('<rect width="1080" height="1920" fill="#120808"/>' + radio(540, 1000, 1.4) + STATIC +
                         '<rect width="1080" height="1920" fill="#ff3b30" opacity="0.08"/>'),
    "18_final": svg(stairs() + '<rect width="1080" height="1920" fill="#000" opacity="0.35"/>'),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
