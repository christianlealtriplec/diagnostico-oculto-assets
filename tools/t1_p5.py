"""Escenas del Capítulo 5 · La nevera (sin textos: se añaden en el montaje)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door, street
from draw3 import fridge, wall_clock
from draw4 import hugo, cunado, candle
from draw5 import tap, burned_hand
from draw6 import (megaphone_car, bathtub, note_under_door, food_items, camping_stove, cans,
                   trash_bin, cloth_hand, ceiling_radio)

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p5"
KITCHEN = wallpaper("#121a22", "#0f161d") + "".join(
    f'<rect x="{x}" y="{y}" width="120" height="120" fill="none" stroke="#1d2a33" stroke-width="4"/>'
    for x in range(0, 1080, 120) for y in range(0, 1300, 120))
BATH = wallpaper("#16222a", "#122028") + "".join(
    f'<rect x="{x}" y="{y}" width="160" height="160" fill="none" stroke="#25363f" stroke-width="5"/>'
    for x in range(0, 1080, 160) for y in range(0, 1100, 160)) + floor_tiles(1350, "#1c2228", "#171c21")
BEAM = '<polygon points="0,1920 0,1600 380,500 900,700" fill="url(#beam)" opacity="0.6"/>'
SHOULDER_HAND = ('<g transform="translate(0 290)"><path d="M 1080 900 C 960 880, 820 900, 720 960 L 700 1030 C 760 1050, 820 1030, 860 1000 C 940 990, 1010 990, 1080 1000 Z" fill="#b98a66"/>'
                 '<path d="M 1080 1010 C 1000 1000, 930 1000, 880 1010 L 900 940 C 960 930, 1030 930, 1080 940 Z" fill="#1c2a48"/></g>')


def split_p5():
    """Pantalla partida: A (oler y comer) / B (a la basura, latas)."""
    left = ('<rect width="540" height="1920" fill="#1a1410"/>'
            + food_items(270, 1100, 0.42) +
            ''.join(f'<path d="M {170+i*60} 1000 C {150+i*60} 940, {200+i*60} 900, {170+i*60} 840" stroke="#9fbf6a" stroke-width="10" fill="none" opacity="0.7"/>' for i in range(4)) +
            '<text x="270" y="760" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#ff3b30" text-anchor="middle" opacity="0.9">A</text>')
    right = ('<rect x="540" width="540" height="1920" fill="#0f1a14"/>'
             + trash_bin(810, 1350, 0.7) + cans(810, 1650, 0.6) +
             '<text x="810" y="760" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#3fd27a" text-anchor="middle" opacity="0.9">B</text>')
    return left + right + '<rect x="532" width="16" height="1920" fill="#000"/>'


scenes = {
    # apertura B: la mano bajo el grifo, veinte minutos
    "01_grifo_mano": svg(KITCHEN + tap(620, 380, drip=False, running=True) +
                         burned_hand(560, 900, 1.2, under_water=True) + BEAM),
    "02_hugo_frio": svg(KITCHEN + tap(860, 420, drip=False, running=True) +
                        '<g transform="translate(-300 -700) scale(1.7)">' + hugo(mood="pain") + '</g>'
                        + '<path d="M 140 520 l -40 -40 M 120 600 l -60 0" stroke="#9fd4ff" stroke-width="10" stroke-linecap="round"/>'),
    "03_aguanta": svg(KITCHEN + '<g transform="translate(-200 -560) scale(1.6)">' + hugo(mood="ok") + '</g>'
                      + SHOULDER_HAND + BEAM),
    # (reloj descartado)
    "05_pano": svg('<rect width="1080" height="1920" fill="#120e0c"/>' +
                   '<ellipse cx="540" cy="960" rx="520" ry="520" fill="#ffb84d" opacity="0.15" filter="url(#blur6)"/>'
                   + cloth_hand(560, 820, 1.55)),
    # hora 60: megáfono, bañera, nota
    "06_megafono": svg(street() + megaphone_car(540, 1620, 0.9)),
    "07_madre_banera": svg(BATH + madre(330, 800, 0.85, mood="shout") +
                           '<g transform="translate(760 1700) scale(0.55) translate(-540 -1250)">' + bathtub(540, 1250, fill=0.0, running=False) + '</g>'),
    "08_banera_llena": svg(BATH + bathtub(540, 1300, fill=0.75, running=True) +
                           '<polygon points="0,1920 0,1650 300,600 900,800" fill="url(#beam)" opacity="0.55"/>'),
    "09_nota": svg(wallpaper("#14182a", "#10142a") +
                   '<rect x="0" y="0" width="1080" height="850" fill="#3a2a1e"/>'
                   '<rect x="80" y="80" width="920" height="700" fill="none" stroke="#2a1f16" stroke-width="12"/>'
                   '<rect x="0" y="850" width="1080" height="30" fill="#05070d"/>'
                   '<rect y="880" width="1080" height="1040" fill="#201913"/>'
                   + note_under_door(540, 1030, 1.2) +
                   '<polygon points="0,1920 0,1300 500,850 1080,950 1080,1920" fill="url(#beam)" opacity="0.7"/>'),
    "10_puerta_4a": svg(hallway_door("4ºA", knock=True) +
                        '<rect x="300" y="1590" width="480" height="20" fill="#05070d"/>'
                        '<circle cx="540" cy="700" r="16" fill="#ffd34d" opacity="0.5"/>'),
    # el hambre y la nevera
    "11_hambre": svg(wallpaper("#1e1a14", "#1a1610") + floor_tiles(1500, "#221a12", "#1c150f") +
                     '<rect x="60" y="1300" width="960" height="50" rx="12" fill="#3a2a1e"/>'
                     '<g transform="translate(-160 -420) scale(1.3)">' + hugo(mood="sick") + '</g>'
                     '<ellipse cx="760" cy="1290" rx="170" ry="34" fill="#e8ecf2"/><ellipse cx="760" cy="1285" rx="120" ry="20" fill="#cfd4dc"/>'
                     + candle(950, 1290, 0.5) +
                     '<ellipse cx="540" cy="1100" rx="460" ry="460" fill="#ffb84d" opacity="0.12" filter="url(#blur6)"/>'),
    "12_nevera_abre": svg(KITCHEN + floor_tiles(1620, "#1c1a18", "#161412") + fridge(open_=True, x=120, y=300) +
                          cunado(860, 980, 0.7, mood="serious") +
                          '<polygon points="0,1920 0,1600 300,700 800,900" fill="url(#beam)" opacity="0.5"/>'),
    "13_comida": svg('<rect width="1080" height="1920" fill="#151922"/>' +
                     ''.join(f'<rect x="60" y="{y}" width="960" height="14" fill="#3a404c"/>' for y in (700, 1200)) +
                     food_items(560, 1060, 0.95) +
                     '<polygon points="0,1920 0,1500 400,600 1000,800" fill="url(#beam)" opacity="0.6"/>'),
    "14_cunado_huele": svg(KITCHEN + floor_tiles(1600, "#1c1a18", "#161412") +
                           cunado(540, 820, 0.95, mood="happy", thumb=True) +
                           '<rect x="0" y="1560" width="1080" height="360" fill="#3a2a1e"/>'
                           '<g transform="translate(540 1600) scale(0.75)">' + food_items(0, 0, 1.0) + '</g>'
                           + ''.join(f'<path d="M {220+i*40} 1540 C {200+i*40} 1490, {240+i*40} 1450, {220+i*40} 1400" stroke="#9fbf6a" stroke-width="8" fill="none" opacity="0.6"/>' for i in range(3))),
    "15_camping_gas": svg(KITCHEN + '<rect y="1450" width="1080" height="470" fill="#2a2018"/>' +
                          camping_stove(600, 1400, 1.25) +
                          '<ellipse cx="600" cy="1250" rx="360" ry="200" fill="#4da3ff" opacity="0.08" filter="url(#blur6)"/>'),
    "16_nevera_cerrada": svg(KITCHEN + floor_tiles(1620, "#1c1a18", "#161412") + fridge(open_=False, x=260, y=300) +
                             '<g transform="translate(540 1050)"><rect x="-120" y="-60" width="240" height="120" rx="14" fill="#111"/>'
                             '<text x="0" y="22" font-family="DejaVu Sans Mono" font-weight="bold" font-size="64" fill="#ff3b30" text-anchor="middle">14°C</text></g>'
                             + BEAM),
    "17_latas": svg(KITCHEN + '<rect y="1350" width="1080" height="570" fill="#2a2018"/>' +
                    '<rect x="0" y="1330" width="1080" height="40" fill="#3a2a1e"/>'
                    + cans(540, 1340, 1.1) +
                    '<polygon points="0,1920 0,1600 340,700 1000,900" fill="url(#beam)" opacity="0.65"/>'),
    "18_decision": svg(split_p5()),
    # suspenso: la radio de arriba
    "19_radio_arriba": svg('<rect width="1080" height="1920" fill="#05060a"/>' + ceiling_radio() +
                           '<g transform="translate(540 1720) scale(0.8) translate(-540 -900)">' + hugo(mood="pain") + '</g>'
                           + candle(860, 1720, 0.5)),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
