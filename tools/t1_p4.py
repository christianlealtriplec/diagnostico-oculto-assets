"""Escenas del Capítulo 4 · La vela (sin textos: se añaden en el montaje)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door
from draw3 import luis, wall_clock
from draw4 import hugo, cunado, generator, candle, gas_swirls
from draw5 import radio, bag_supplies, tap, burned_hand, curtain

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p4"
CANDLE_ROOM = wallpaper("#1e1a14", "#1a1610") + floor_tiles(1500, "#221a12", "#1c150f")


def candle_glow(x, y, r=320, op=0.22):
    return f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r}" fill="#ffb84d" opacity="{op}" filter="url(#blur6)"/>'


def building_wall():
    """Fachada interior del patio con ventanas, de noche."""
    out = '<rect width="1080" height="1500" fill="#10141f"/>'
    for wx in (90, 420, 750):
        for wy in (120, 560):
            out += f'<rect x="{wx}" y="{wy}" width="240" height="300" fill="#1d2a45" stroke="#05070d" stroke-width="14"/>'
    return out + '<rect y="1500" width="1080" height="420" fill="#1f211e"/>'


def split_p4():
    """Pantalla partida: A (hielo directo) / B (agua del grifo sin parar)."""
    left = ('<rect width="540" height="1920" fill="#101a2a"/>'
            '<g transform="translate(270 1050) scale(0.5)">'
            + "".join(f'<rect x="{x}" y="{y}" width="150" height="150" rx="24" fill="#d8f2ff" opacity="0.92" transform="rotate({r} {x+75} {y+75})"/>'
                      for x, y, r in [(-220, -260, -12), (-40, -300, 10), (100, -220, -6), (-140, -100, 18)]) +
            '</g>'
            '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#3fd27a" text-anchor="middle" opacity="0.9">A</text>')
    right = ('<rect x="540" width="540" height="1920" fill="#0f1a1a"/>'
             '<g transform="translate(540 0)">'
             '<g transform="translate(270 820) scale(0.6) translate(-540 -700)">'
             '<rect x="480" y="440" width="120" height="120" rx="20" fill="#9aa0a8"/>'
             '<path d="M 540 560 L 540 660 C 540 760, 580 800, 540 900" stroke="#b8bdc4" stroke-width="56" fill="none" stroke-linecap="round"/>'
             '<rect x="518" y="930" width="44" height="560" fill="#9fd4ff" opacity="0.8"/></g>'
             '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#ff3b30" text-anchor="middle" opacity="0.9">B</text></g>')
    return left + right + '<rect x="532" width="16" height="1920" fill="#000"/>'


scenes = {
    # apertura A: apagas el generador y lo sacáis al patio
    "01_cunado_carga": svg(wallpaper("#121626", "#0f1322") + floor_tiles(1500) +
                           '<rect x="80" y="300" width="380" height="1200" fill="#0a0d16" stroke="#3a2d22" stroke-width="18"/>'
                           + cunado(640, 760, 0.9, mood="serious") +
                           '<path d="M 450 1240 C 480 1180, 560 1170, 600 1200" stroke="#c4621f" stroke-width="66" fill="none" stroke-linecap="round"/>'
                           '<path d="M 830 1240 C 800 1180, 720 1170, 680 1200" stroke="#c4621f" stroke-width="66" fill="none" stroke-linecap="round"/>'
                           + generator(640, 1420, 0.6, running=False) +
                           '<path d="M 0 1600 C 120 1560, 220 1520, 290 1450 L 330 1480 C 260 1560, 160 1620, 0 1680 Z" fill="#b98a66"/>'
                           '<polygon points="0,1920 0,1600 520,520 1000,760" fill="url(#beam)" opacity="0.6"/>'),
    "02_patio": svg(building_wall() +
                    '<path d="M 0 1920 L 0 1500 L 1080 1500 L 1080 1920 Z" fill="#232620"/>'
                    + generator(860, 1700, 0.42, running=True, fumes=False) +
                    '<path d="M 300 1760 L 720 1760" stroke="#3fd27a" stroke-width="12" stroke-dasharray="26 18"/>'
                    '<path d="M 720 1760 l -30 -20 m 30 20 l -30 20" stroke="#3fd27a" stroke-width="12"/>'
                    + "".join(f'<circle cx="{1020-i*10}" cy="{1560-i*90}" r="{30+i*14}" fill="#8a8f9c" opacity="{0.3-i*0.05:.2f}" filter="url(#blur6)"/>' for i in range(5)) +
                    '<polygon points="0,1920 0,1650 600,1500 900,1650" fill="url(#beam)" opacity="0.6"/>'),
    "03_hugo_mejor": svg('<rect width="1080" height="1920" fill="#14182a"/>' + window(620, 260, 360, 520) +
                         '<g transform="translate(-540 -760) scale(2)">' + hugo(mood="ok") + '</g>'
                         '<polygon points="0,1920 0,1500 640,520 1080,800 1080,1920" fill="url(#beam)" opacity="0.5"/>'),
    # hora 41: radio, Luis con velas y pilas
    "04_radio": svg(wallpaper("#121626", "#0f1322") + wall_clock(5, 0, 800, 680, 150) +
                    '<rect y="1300" width="1080" height="620" fill="#2a2018"/>' + radio(500, 1120, 1.15) +
                    '<polygon points="0,1920 0,1650 300,700 900,900" fill="url(#beam)" opacity="0.6"/>'),
    "05_luis_bolsa": svg(hallway_door("2ºA", knock=False) +
                         luis(540, 820, 0.95, mood="calm", box=False) +
                         '<path d="M 680 1180 C 720 1260, 700 1320, 640 1340" stroke="#55603a" stroke-width="66" fill="none" stroke-linecap="round"/>'
                         + bag_supplies(560, 1480, 0.9)),
    "06_velas_luz": svg(CANDLE_ROOM + candle_glow(540, 1000, 520, 0.28) +
                        '<rect x="120" y="1250" width="840" height="60" rx="14" fill="#3a2a1e"/><rect x="160" y="1310" width="40" height="400" fill="#2a1f16"/><rect x="880" y="1310" width="40" height="400" fill="#2a1f16"/>'
                        + candle(330, 1130, 0.7) + candle(540, 1100, 0.9) + candle(750, 1140, 0.65) +
                        '<g transform="translate(830 1220) scale(0.5)"><rect x="-60" y="-60" width="120" height="60" fill="#2a2a2a"/><rect x="-60" y="-60" width="120" height="20" fill="#e0b52a"/></g>'),
    # golpes en el techo, Don Ramón
    "07_techo_hugo": svg(CANDLE_ROOM + candle_glow(540, 1500, 420, 0.2) +
                         '<rect width="1080" height="380" fill="#0c0e14"/>'
                         '<path d="M 420 380 L 470 470 L 440 520 L 500 600 M 470 470 L 560 500" stroke="#05070d" stroke-width="8" fill="none"/>'
                         + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#c9c2b0" opacity="0.7"/>' for x, y, r in [(470, 640, 6), (500, 700, 5), (450, 760, 7), (520, 820, 4), (480, 900, 5)]) +
                         '<path d="M 300 360 l -40 -40 M 340 350 l 0 -50 M 760 360 l 40 -40 M 720 350 l 0 -50" stroke="#ffd34d" stroke-width="10" stroke-linecap="round"/>'
                         '<g transform="translate(560 1250) scale(0.85) rotate(-8 540 900) translate(-540 -900)">' + hugo(mood="ok") + '</g>'
                         + candle(180, 1700, 0.55)),
    "08_madre": svg(CANDLE_ROOM + candle_glow(300, 1500, 380, 0.25) +
                    '<g transform="translate(-540 -720) scale(2)">' + madre(mood="worry") + '</g>'
                    + candle(150, 1780, 0.6)),
    "09_puerta_4a": svg(hallway_door("4ºA", knock=True) +
                        '<path d="M 860 1060 l 60 -30 M 870 1110 l 70 0 M 860 1160 l 60 30" stroke="#ffd34d" stroke-width="10" stroke-linecap="round"/>'),
    # la vela, la quemadura, la cortina
    "10_vela_caida": svg(CANDLE_ROOM +
                         '<rect x="0" y="1260" width="1080" height="60" rx="10" fill="#3a2a1e"/>'
                         + curtain(700, 120, 380, 1140, smoke=True) +
                         '<g transform="translate(560 1250) rotate(-80)">' + candle(0, 0, 0.75) + '</g>'
                         '<path d="M 470 1262 C 420 1300, 360 1290, 320 1330 C 300 1360, 330 1400, 300 1460" stroke="#f1ead8" stroke-width="22" fill="none" stroke-linecap="round"/>'
                         + candle_glow(620, 1150, 300, 0.3) +
                         '<path d="M 160 1400 l -50 -40 M 150 1480 l -60 0" stroke="#ffd34d" stroke-width="10" stroke-linecap="round"/>'),
    "11_mano_quemada": svg('<rect width="1080" height="1920" fill="#120e0c"/>' + candle_glow(540, 960, 520, 0.22) +
                           burned_hand(560, 820, 1.55)),
    "12_toalla_cortina": svg(CANDLE_ROOM + curtain(260, 100, 560, 1400, smoke=True, towel=True) +
                             '<path d="M 1080 1300 C 960 1280, 900 1260, 860 1230 L 880 1180 C 920 1200, 990 1220, 1080 1230 Z" fill="#b98a66"/>'
                             '<path d="M 0 1360 C 120 1330, 200 1300, 230 1260 L 210 1210 C 170 1250, 90 1280, 0 1290 Z" fill="#b98a66"/>'),
    "13_madre_hielo": svg(CANDLE_ROOM + candle_glow(540, 1300, 460, 0.22) +
                          madre(540, 820, 0.95, mood="shout", hold="hielo")),
    "14_tia_pasta": svg(wallpaper("#20182a", "#1b1424") + floor_tiles(1500, "#221a12", "#1c150f") + candle_glow(300, 1400, 380, 0.25) +
                        tia(500, 820, 0.95, mood="shout", hold="pasta")),
    "15_grifo": svg(wallpaper("#121a22", "#0f161d") +
                    "".join(f'<rect x="{x}" y="{y}" width="120" height="120" fill="none" stroke="#1d2a33" stroke-width="4"/>' for x in range(0, 1080, 120) for y in range(0, 1500, 120)) +
                    tap(540, 620, drip=True) +
                    '<polygon points="0,1920 0,1600 380,500 900,700" fill="url(#beam)" opacity="0.65"/>'),
    "16_decision": svg(split_p4()),
    # suspenso: arriba, algo pesado
    "17_arriba": svg('<rect width="1080" height="1920" fill="#05060a"/>' +
                     '<rect width="1080" height="560" fill="#0b0d14"/>'
                     '<path d="M 0 560 L 1080 560" stroke="#1a1e2a" stroke-width="10"/>'
                     '<path d="M 140 470 C 360 440, 620 480, 940 450" stroke="#2a2f3e" stroke-width="40" fill="none" stroke-linecap="round" opacity="0.8"/>'
                     '<path d="M 180 520 C 400 500, 640 520, 900 500" stroke="#2a2f3e" stroke-width="24" fill="none" stroke-linecap="round" opacity="0.6"/>'
                     + "".join(f'<path d="M {x} {y} l {dx} -30" stroke="#ff3b30" stroke-width="10" stroke-linecap="round" opacity="0.8"/>' for x, y, dx in [(220, 640, -30), (540, 650, 0), (860, 640, 30)]) +
                     '<g transform="translate(540 1500) scale(0.8) translate(-540 -900)">' + hugo(mood="pain") + '</g>'
                     + candle(860, 1720, 0.5)),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
