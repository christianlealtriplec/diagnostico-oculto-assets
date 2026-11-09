"""Escenas de la Parte 1 · Se va la luz (sin textos: se añaden en el montaje)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p1"

scenes = {
    "01_apagon": svg(city_night() + silhouette_window_person()),
    "02_sin_servicio": svg('<rect width="1080" height="1920" fill="#0a0e1a"/>'
                           '<g transform="translate(-180 -900) scale(2.1)">' + phone_hand(330, 560, -8, screen=True) + '</g>'),
    "03_escalera": svg(stairs()),
    "04_abuela_plano": svg(window() + bed() + concentrator() +
                           tube("M 900 1080 C 880 900, 640 980, 470 905") +
                           abuela() + blanket() + beam() + phone_hand()),
    "05_abuela_cara": svg(window(720, 200, 300, 470) +
                          '<g transform="translate(-200 -430) scale(1.6)">' + abuela() + '</g>' +
                          '<polygon points="0,1920 0,1500 760,520 1080,800 1080,1920" fill="url(#beam)" opacity="0.7"/>'),
    "06_maquina_off": svg('<rect y="1500" width="1080" height="420" fill="#120f0c"/>' +
                          concentrator(250, 380, 2.4) +
                          '<polygon points="0,1920 0,1650 700,500 1080,700 1080,1920" fill="url(#beam)" opacity="0.8"/>'),
    "07_botella": svg('<rect x="180" y="200" width="720" height="1560" fill="#1a140f" stroke="#2a2018" stroke-width="20"/>' +
                      oxygen_bottle() +
                      '<polygon points="0,1920 0,1600 520,300 1000,500" fill="url(#beam)" opacity="0.8"/>'),
    "08_tio_grita": svg(door() + tio(540, 920, 1.05) +
                        '<polygon points="0,1920 0,1700 420,700 900,820" fill="url(#beam)" opacity="0.6"/>'),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
