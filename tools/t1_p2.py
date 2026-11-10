"""Escenas de la Parte 2 · La insulina (sin textos: se añaden en el montaje)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door
from draw3 import luis, mujer_luis, fridge, insulin_box, insulin_pen, wall_clock, ice_bowl, cool_room, split_p2

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p2"

scenes = {
    # apertura A: botella abierta, Carmen recupera el color
    "01_botella_abierta": svg('<rect x="180" y="200" width="720" height="1560" fill="#1a140f" stroke="#2a2018" stroke-width="20"/>' +
                              oxygen_bottle(open_=True) +
                              '<polygon points="0,1920 0,1600 520,300 1000,500" fill="url(#beam)" opacity="0.8"/>'),
    "02_abuela_recupera": svg(window(720, 200, 300, 470) +
                              '<g transform="translate(-200 -430) scale(1.6)">' + abuela(mood="calma", lips="#c46a6a") + '</g>' +
                              '<polygon points="0,1920 0,1500 760,520 1080,800 1080,1920" fill="url(#beam)" opacity="0.7"/>'),
    "03_abuela_cama_botella": svg(window() + bed() +
                                  '<g transform="translate(830 1000) scale(0.42) translate(-430 -900)">' + oxygen_bottle(hand=False, open_=True) + '</g>' +
                                  tube("M 880 820 C 860 760, 640 980, 470 905") +
                                  abuela(mood="calma", lips="#c46a6a") + blanket() + beam()),
    # gancho / hora tres
    "04_reloj": svg(wallpaper("#121626", "#0f1322") + wall_clock(3, 0) +
                    '<polygon points="0,1920 0,1600 380,700 900,900" fill="url(#beam)" opacity="0.7"/>'),
    "05_llaman": svg(hallway_door("3ºB", knock=False) +
                     '<g transform="translate(540 1120) scale(0.7) translate(-540 -1120)">' +
                     '<path d="M 1080 1150 C 950 1120, 860 1090, 800 1070 L 790 1030 C 800 1000, 850 1000, 870 1020 L 900 1050 C 960 1060, 1020 1070, 1080 1080 Z" fill="#b98a66"/></g>'),
    "06_luis_puerta": svg(door(220, 300, 640, 1400) + luis(540, 980, 0.95) +
                          '<polygon points="0,1920 0,1700 420,600 960,760" fill="url(#beam)" opacity="0.55"/>'),
    "07_luis_cara": svg('<rect width="1080" height="1920" fill="#0d1120"/>' +
                        '<g transform="translate(-540 -620) scale(2)">' + luis(540, 900, 1.0, box=False) + '</g>' +
                        '<polygon points="0,1920 0,1500 700,500 1080,760 1080,1920" fill="url(#beam)" opacity="0.6"/>'),
    "08_caja_insulina": svg('<rect width="1080" height="1920" fill="#0b0f1b"/>' + insulin_box(540, 900, 1.25) +
                            '<ellipse cx="170" cy="1120" rx="100" ry="64" fill="url(#skin)"/><ellipse cx="910" cy="1060" rx="100" ry="64" fill="url(#skin)"/>' +
                            '<polygon points="0,1920 0,1600 480,500 1080,700" fill="url(#beam)" opacity="0.7"/>'),
    "09_nevera_off": svg(wallpaper("#121826", "#0f1422") + floor_tiles(1620) + fridge(open_=True) +
                         '<polygon points="0,1920 0,1650 500,700 960,900" fill="url(#beam)" opacity="0.6"/>'),
    "10_mujer_congelador": svg(wallpaper("#121826", "#0f1422") +
                               '<g transform="translate(560 200) scale(0.7)">' + fridge(open_=False, freezer_open=True) + '</g>' +
                               mujer_luis(380, 1000, 0.95) +
                               '<polygon points="0,1920 0,1700 300,700 900,800" fill="url(#beam)" opacity="0.5"/>'),
    "11_hielo": svg(ice_bowl()),
    "12_pluma": svg('<rect width="1080" height="1920" fill="#0b0f1b"/>' + insulin_pen(540, 900, 1.2, -25) +
                    '<polygon points="0,1920 0,1600 460,520 1080,760" fill="url(#beam)" opacity="0.7"/>'),
    "13_sitio_fresco": svg(cool_room()),
    "14_movil_duda": svg('<rect width="1080" height="1920" fill="#0a0e1a"/>' +
                         '<text x="800" y="520" font-family="DejaVu Sans" font-weight="bold" font-size="300" fill="#7aa7ff" opacity="0.4" text-anchor="middle">?</text>'
                         '<g transform="translate(-180 -900) scale(2.1)">' + phone_hand(330, 560, -8, screen=True) + '</g>'),
    "15_decision": svg(split_p2()),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
