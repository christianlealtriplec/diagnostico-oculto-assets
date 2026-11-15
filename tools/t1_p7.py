"""Escenas del Capítulo 7 · Epílogo (rama B ganadora en el Capítulo 6: uno pide ayuda y tú comprimes; <10 votos)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door
from draw3 import wall_clock, insulin_pen, ice_bowl
from draw4 import hugo, cunado, candle, generator, lit_room
from draw5 import radio, tap, burned_hand
from draw6 import food_items, trash_bin
from draw7 import abuela_suelo, compress_hands, bedroom

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p7"
SALON = wallpaper("#1e1a14", "#1a1610") + floor_tiles(1500, "#221a12", "#1c150f")
TABLE = '<rect x="40" y="1300" width="1000" height="60" rx="12" fill="#3a2a1e"/><rect x="80" y="1360" width="40" height="400" fill="#2a1f16"/><rect x="960" y="1360" width="40" height="400" fill="#2a1f16"/>'
STAIR = ''.join(f'<polygon points="{80+i*10},{1900-i*120} {1000-i*10},{1900-i*120} {980-i*10},{1840-i*120} {100+i*10},{1840-i*120}" fill="{c}"/>'
                for i, c in enumerate(["#1d2235", "#181c2d", "#151927", "#121521", "#0f121c", "#0d0f18", "#0b0d14", "#090b11", "#08090e", "#06070b"]))
KNOCK = ''.join(f'<path d="M 860 1000 m {dx} {dy} l {dx*0.6} {dy*0.6}" stroke="#ff3b30" stroke-width="12" stroke-linecap="round"/>'
                for dx, dy in [(60, -60), (80, 0), (60, 60)])
BLUE = '<rect width="1080" height="1920" fill="#2a6bff" opacity="0.16"/><ellipse cx="540" cy="300" rx="600" ry="300" fill="#3f86ff" opacity="0.25" filter="url(#blur6)"/>'
ICON_FRAME = lambda c: f'<circle cx="540" cy="900" r="400" fill="none" stroke="{c}" stroke-width="12" opacity="0.6"/>'


def sanitario(x, y, s=1.0):
    """Sanitario en silueta con chaleco reflectante y maletín."""
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-330" r="62" fill="#0b0d14"/>'
            '<path d="M -110 0 L -100 -250 C -90 -280, 90 -280, 100 -250 L 110 0 Z" fill="#c8d63a"/>'
            '<rect x="-100" y="-170" width="200" height="22" fill="#e9eef5"/><rect x="-100" y="-110" width="200" height="22" fill="#e9eef5"/>'
            '<rect x="120" y="-140" width="110" height="90" rx="10" fill="#d23"/><path d="M 175 -125 v 60 M 145 -95 h 60" stroke="#fff" stroke-width="14"/>'
            '<rect x="-90" y="0" width="70" height="200" fill="#1c2a48"/><rect x="20" y="0" width="70" height="200" fill="#1c2a48"/></g>')


scenes = {
    # apertura B
    "01_aporrea": svg(hallway_door("4ºA", knock=False) + cunado(380, 860, 0.85, mood="serious") +
                      '<g transform="translate(820 1000)"><ellipse cx="0" cy="0" rx="62" ry="54" fill="url(#skin)"/></g>'
                      '<path d="M 560 1080 C 650 1050, 740 1020, 790 1000" stroke="#3a6aa8" stroke-width="60" stroke-linecap="round" fill="none"/>' + KNOCK),
    "02_ramon_abre": svg(wallpaper("#14182a", "#10142a") + floor_tiles(1600, "#201913", "#1a140f") +
                         '<rect x="170" y="280" width="740" height="1340" fill="#2a1e14"/><rect x="200" y="310" width="680" height="1310" fill="#ffb84d" opacity="0.22"/>'
                         + don_ramon(540, 820, 0.95) +
                         '<text x="540" y="250" font-family="DejaVu Sans" font-weight="bold" font-size="70" fill="#c9a24a" text-anchor="middle">4ºA</text>'),
    "03_ramon_radio": svg('<rect width="1080" height="1920" fill="#120e0a"/>' + don_ramon(540, 720, 1.35, mood="shout") +
                          ''.join(f'<path d="M 860 {520-i*50} a {60+i*50} {60+i*50} 0 0 1 0 {120+i*100}" stroke="#ffb84d" stroke-width="10" fill="none" opacity="{0.8-i*0.2}"/>' for i in range(3))),
    "04_comprimes": svg(bedroom(lit=False) + abuela_suelo(560, 1500, 0.9) + compress_hands(560, 1420, 0.6) +
                        '<polygon points="0,1920 0,1500 300,1100 1080,1300 1080,1920" fill="url(#beam)" opacity="0.6"/>'),
    "05_ritmo": svg('<rect width="1080" height="1920" fill="#120e0c"/>' + abuela_suelo(260, 1050, 2.2) + compress_hands(540, 1180, 1.25) +
                    ''.join(f'<path d="M {200+i*110} 1700 l 40 -60 l 40 60" stroke="#ff3b30" stroke-width="10" fill="none" opacity="0.8"/>' for i in range(7))),
    "06_sanitarios": svg('<rect width="1080" height="1920" fill="#06070b"/>' + STAIR + BLUE +
                         sanitario(380, 1250, 1.1) + sanitario(720, 1150, 0.95) +
                         '<path d="M 120 1700 L 380 300" stroke="#3a1414" stroke-width="22"/><path d="M 960 1700 L 700 300" stroke="#3a1414" stroke-width="22"/>'),
    "07_carmen_vive": svg(bedroom(lit=False) + bed(150, 880) + abuela(470, 830, 1.05, mood="ok", lips="#c46a6a") + blanket(150, 1180) +
                          '<g transform="translate(770 980) scale(0.7)">' + sanitario(0, 0, 1.0) + '</g>' + BLUE),
    # cierre: vuelve la luz
    "08_hora72": svg('<rect width="1080" height="1920" fill="#05060a"/>' + wall_clock(12, 0, 540, 900, 330) +
                     '<text x="540" y="1420" font-family="DejaVu Sans" font-weight="bold" font-size="120" fill="#ffd400" text-anchor="middle">72</text>'),
    "09_vuelve_luz": svg(lit_room() + TABLE + madre(220, 860, 0.7, mood="ok") + hugo(540, 1000, 0.75, mood="ok")
                         + cunado(870, 860, 0.7, mood="happy")),
    "10_repaso": svg(lit_room() + '<rect x="200" y="700" width="680" height="900" rx="20" fill="#f3ead2"/>'
                     + ''.join(f'<rect x="270" y="{800+i*130}" width="60" height="60" rx="8" fill="none" stroke="#3a2a1e" stroke-width="8"/>'
                               f'<path d="M 280 {830+i*130} l 18 18 l 30 -40" stroke="#2e9e5a" stroke-width="12" fill="none"/>'
                               f'<rect x="370" y="{815+i*130}" width="{420-i*40}" height="26" rx="8" fill="#b8ab8c"/>' for i in range(6))),
    "11_oxigeno": svg(lit_room() + oxygen_bottle(430, 520, 1.25, hand=False) + ICON_FRAME("#3fd27a")),
    "12_insulina": svg('<rect width="1080" height="1920" fill="#0e1a22"/>' + ice_bowl() + insulin_pen(540, 760, 1.4, rot=-30) + ICON_FRAME("#3fd27a")),
    "13_generador": svg('<rect width="1080" height="1100" fill="url(#moonsky)"/><rect y="1100" width="1080" height="820" fill="#1a1d24"/>'
                        '<rect x="0" y="300" width="380" height="800" fill="#10131c"/><rect x="80" y="420" width="120" height="160" fill="#ffe7a8" opacity="0.8"/>'
                        + generator(700, 1450, 0.9) + '<path d="M 420 1300 L 560 1300" stroke="#3fd27a" stroke-width="14" marker-end=""/>'),
    "14_quemadura": svg('<rect width="1080" height="1920" fill="#101820"/>' + tap(540, 520, drip=False, running=True) + burned_hand(540, 1050, 1.2, under_water=True)),
    "15_basura": svg(wallpaper("#121a22", "#0f161d") + floor_tiles(1600, "#1c1a18", "#161412") + trash_bin(540, 1650, 1.25) +
                     '<g transform="translate(540 1000) scale(0.6)">' + food_items(0, 0, 1.0) + '</g>' + ICON_FRAME("#3fd27a")),
    "16_parpadea": svg(lit_room() + '<rect width="1080" height="1920" fill="#000" opacity="0.6"/>' +
                       '<path d="M 470 230 l -60 -50 M 610 230 l 60 -50 M 540 200 l 0 -80" stroke="#ff3b30" stroke-width="12" stroke-linecap="round"/>'
                       + madre(300, 900, 0.7, mood="worry") + cunado(780, 900, 0.7, mood="serious")),
    "17_radio_aviso": svg('<rect width="1080" height="1920" fill="#120a0a"/>' + radio(540, 1050, 1.3) +
                          '<rect width="1080" height="1920" fill="#ff3b30" opacity="0.07"/>'),
    "18_guardalo": svg(lit_room() + '<g transform="translate(540 1000) rotate(-8)"><ellipse cx="60" cy="330" rx="170" ry="230" fill="url(#skin)"/>'
                      '<rect x="-170" y="-380" width="340" height="680" rx="44" fill="#111"/><rect x="-148" y="-340" width="296" height="600" rx="24" fill="#2b6fd6"/>'
                      '<path d="M 0 -200 L 0 20 M -70 -130 L 0 -200 L 70 -130" stroke="#fff" stroke-width="22" fill="none" stroke-linecap="round"/>'
                      '<path d="M -90 -40 L -90 90 L 90 90 L 90 -40" stroke="#fff" stroke-width="18" fill="none" stroke-linejoin="round"/>'
                      '<path d="M -40 180 L 40 180 L 40 240 L 0 215 L -40 240 Z" fill="#ffd400"/></g>'),
    "19_otra_vez": svg(city_night() + '<rect width="1080" height="1920" fill="#000" opacity="0.25"/>'),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
