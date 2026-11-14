"""Escenas del Capítulo 6 · La abuela no responde (rama B ganadora en el Capítulo 5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door
from draw3 import wall_clock
from draw4 import hugo, cunado, candle
from draw5 import radio
from draw6 import food_items, cans, trash_bin
from draw7 import abuela_suelo, hands_shoulders, compress_hands, keys_hand, bedroom

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p6"
KITCHEN = wallpaper("#121a22", "#0f161d") + "".join(
    f'<rect x="{x}" y="{y}" width="120" height="120" fill="none" stroke="#1d2a33" stroke-width="4"/>'
    for x in range(0, 1080, 120) for y in range(0, 1300, 120))
BEAM = '<polygon points="0,1920 0,1600 380,500 900,700" fill="url(#beam)" opacity="0.6"/>'
SALON = wallpaper("#1e1a14", "#1a1610") + floor_tiles(1500, "#221a12", "#1c150f")
TABLE = '<rect x="40" y="1300" width="1000" height="60" rx="12" fill="#3a2a1e"/><rect x="80" y="1360" width="40" height="400" fill="#2a1f16"/><rect x="960" y="1360" width="40" height="400" fill="#2a1f16"/>'
GLOW = '<ellipse cx="540" cy="1100" rx="460" ry="460" fill="#ffb84d" opacity="0.12" filter="url(#blur6)"/>'
STAIR = ''.join(f'<polygon points="{80+i*10},{1900-i*120} {1000-i*10},{1900-i*120} {980-i*10},{1840-i*120} {100+i*10},{1840-i*120}" fill="{c}"/>'
                for i, c in enumerate(["#1d2235", "#181c2d", "#151927", "#121521", "#0f121c", "#0d0f18", "#0b0d14", "#090b11", "#08090e", "#06070b"]))
IMPACT = ''.join(f'<path d="M 540 1350 L {540+dx} {1350+dy}" stroke="#ff3b30" stroke-width="14" stroke-linecap="round"/>'
                 for dx, dy in [(-260, -120), (260, -120), (-200, -260), (200, -260), (0, -300), (-300, 20), (300, 20)])


def split_p6():
    """Pantalla partida: A (todos salen por la puerta) / B (uno sale y tú comprimes)."""
    run = lambda x, s: (f'<g transform="translate({x} 1500) scale({s})"><circle cx="0" cy="-230" r="34" fill="#05070d"/>'
                        f'<path d="M -50 0 L -45 -180 C -40 -200, 40 -200, 45 -180 L 50 0 Z" fill="#05070d"/></g>')
    left = ('<rect width="540" height="1920" fill="#1a1410"/>'
            '<rect x="120" y="820" width="300" height="760" fill="#0a0c14" stroke="#3a2a1e" stroke-width="16"/>'
            + run(200, 1.0) + run(300, 0.8) + run(380, 0.9) +
            '<text x="270" y="680" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#ff3b30" text-anchor="middle" opacity="0.9">A</text>')
    right = ('<rect x="540" width="540" height="1920" fill="#0f1a14"/>'
             '<g transform="translate(540 0)"><g transform="translate(270 1500) scale(0.45) translate(-540 -1350)">' + abuela_suelo() + '</g>'
             '<g transform="translate(315 1510) scale(0.5) translate(-540 -1100)">' + compress_hands() + '</g></g>'
             '<text x="810" y="680" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#3fd27a" text-anchor="middle" opacity="0.9">B</text>')
    return left + right + '<rect x="532" width="16" height="1920" fill="#000"/>'


scenes = {
    # apertura B: a la basura
    "01_basura": svg(KITCHEN + floor_tiles(1600, "#1c1a18", "#161412") + trash_bin(540, 1650, 1.25) +
                     '<g transform="translate(540 1050) scale(0.6)">' + food_items(0, 0, 1.0) + '</g>'
                     '<path d="M 540 1250 L 540 1360" stroke="#fff" stroke-width="10" stroke-dasharray="20 20" opacity="0.5"/>' + BEAM),
    "02_cunado_loco": svg(KITCHEN + floor_tiles(1600, "#1c1a18", "#161412") + cunado(540, 820, 0.95, mood="serious") +
                          '<path d="M 300 560 l -60 -60 M 780 560 l 60 -60 M 540 470 l 0 -80" stroke="#ff3b30" stroke-width="14" stroke-linecap="round"/>'),
    "03_garbanzos": svg(SALON + TABLE + '<g transform="translate(-220 -380) scale(1.25)">' + hugo(mood="ok") + '</g>'
                        + cans(760, 1300, 0.55) +
                        '<ellipse cx="440" cy="1295" rx="150" ry="30" fill="#e8ecf2"/>'
                        + ''.join(f'<circle cx="{380+i*24}" cy="{1282-(i%2)*8}" r="13" fill="#d9b86a"/>' for i in range(6)) +
                        '<path d="M 900 1270 C 900 1230, 1010 1230, 1010 1270 Z" fill="#c9954a"/>' + candle(160, 1300, 0.5) + GLOW),
    # hora 70: la radio y el cuñado bajando del cuarto
    "04_radio_hora70": svg(SALON + TABLE + radio(540, 1120, 0.95) + madre(860, 760, 0.6, mood="worry") + candle(200, 1300, 0.5) + GLOW),
    "05_cunado_baja": svg('<rect width="1080" height="1920" fill="#06070b"/>' + STAIR +
                          '<path d="M 120 1700 L 380 300" stroke="#3a1414" stroke-width="22"/><path d="M 960 1700 L 700 300" stroke="#3a1414" stroke-width="22"/>'
                          + cunado(540, 760, 0.8, mood="serious") +
                          '<polygon points="140,1880 100,1760 470,700 820,760" fill="url(#beam)"/>'
                          '<g transform="translate(540 160) scale(0.35)">' + radio(0, 0, 1.0) + '</g>'),
    # el golpe
    "06_golpe": svg(bedroom() + IMPACT),
    "07_abuela_suelo": svg(bedroom(lit=False) + abuela_suelo(560, 1500, 0.9) +
                           '<polygon points="0,1920 0,1500 300,1100 1080,1300 1080,1920" fill="url(#beam)" opacity="0.7"/>'),
    "08_sacudir": svg('<rect width="1080" height="1920" fill="#1f1813"/>' + abuela_suelo(420, 1150, 1.7) + hands_shoulders(560, 1300, 1.0)),
    "09_pecho": svg('<rect width="1080" height="1920" fill="#120e0c"/>' + abuela_suelo(260, 1000, 2.2) +
                    '<circle cx="540" cy="1000" r="230" fill="none" stroke="#ff3b30" stroke-width="10" stroke-dasharray="40 24"/>'
                    '<path d="M 300 1500 L 420 1500 L 450 1440 L 480 1560 L 510 1500 L 780 1500" stroke="#ff3b30" stroke-width="10" fill="none"/>'),
    "10_sin_cobertura": svg(bedroom(lit=False) + '<g transform="translate(320 500) scale(2.2) translate(-60 -1560)">' + phone_hand(60, 1560, -8, screen=True) + '</g>'),
    "11_cunado_llaves": svg(hallway_door("3ºB", knock=False) + cunado(420, 860, 0.85, mood="serious") + keys_hand(780, 1000, 1.2)),
    "12_hugo_puerta": svg(door(240, 380, 600, 1300) + '<rect x="240" y="380" width="600" height="1300" fill="#2a2018" opacity="0.5"/>'
                          + '<g transform="translate(540 1100) scale(1.1) translate(-540 -900)">' + hugo(mood="pain", hands_head=True) + '</g>'
                          + '<path d="M 450 1020 l -6 40 M 630 1020 l 6 40" stroke="#9fd4ff" stroke-width="10" stroke-linecap="round"/>'),
    "13_minutos": svg('<rect width="1080" height="1920" fill="#05060a"/>' + wall_clock(9, 50, 540, 900, 330) +
                      '<path d="M 540 900 m -380 0 a 380 380 0 0 1 380 -380" stroke="#ff3b30" stroke-width="22" fill="none"/>'),
    "14_decision": svg(split_p6()),
    # suspenso: la radio de arriba se calla
    "15_radio_calla": svg('<rect width="1080" height="1920" fill="#05060a"/>'
                          '<rect width="1080" height="620" fill="#0b0d14"/><path d="M 0 620 L 1080 620" stroke="#1a1e2a" stroke-width="12"/>'
                          '<rect x="430" y="380" width="220" height="130" rx="20" fill="#1c1c1f" opacity="0.55"/>'
                          '<rect x="540" y="400" width="90" height="34" rx="6" fill="#333" opacity="0.8"/>'
                          '<g transform="translate(540 1400) scale(0.9) translate(-540 -900)">' + hugo(mood="pain") + '</g>'
                          + candle(860, 1720, 0.5, lit=False)),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
