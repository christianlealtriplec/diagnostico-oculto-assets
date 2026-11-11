"""Escenas del Capítulo 3 · El generador (sin textos: se añaden en el montaje)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles
from draw3 import luis, insulin_box, wall_clock
from draw4 import hugo, cunado, generator, gas_swirls, heater, candle, lit_room

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p3"
DARK_SALON = wallpaper("#121626", "#0f1322") + floor_tiles(1500)


def split_p3():
    """Pantalla partida: A (generador fuera, lejos de ventanas) / B (generador dentro, ventanas abiertas)."""
    left = ('<rect width="540" height="1920" fill="#0d1a14"/>'
            '<rect x="60" y="700" width="160" height="240" fill="#2d4a7c" opacity="0.6" stroke="#05070d" stroke-width="10"/>'
            '<rect y="1500" width="540" height="420" fill="#1a2418"/>'
            '<g transform="translate(380 1500) scale(0.42) translate(-540 -1300)">' + generator(fumes=False) + '</g>'
            '<path d="M 300 1300 L 140 1300" stroke="#3fd27a" stroke-width="10" stroke-dasharray="20 14"/>'
            '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#3fd27a" text-anchor="middle" opacity="0.9">A</text>')
    right = ('<rect x="540" width="540" height="1920" fill="#1a0f12"/>'
             '<g transform="translate(540 0)">'
             '<rect x="140" y="700" width="260" height="360" fill="#2d4a7c" opacity="0.6" stroke="#05070d" stroke-width="10"/>'
             '<path d="M 140 700 L 60 760 L 60 1120 L 140 1060 Z" fill="#3a4f75" opacity="0.8"/>'
             '<g transform="translate(270 1520) scale(0.45) translate(-540 -1300)">' + generator() + '</g>'
             '<text x="270" y="560" font-family="DejaVu Sans" font-weight="bold" font-size="220" fill="#ff3b30" text-anchor="middle" opacity="0.9">B</text></g>')
    return left + right + '<rect x="532" width="16" height="1920" fill="#000"/>'


scenes = {
    # apertura B: insulina al armario del pasillo
    "01_armario_pasillo": svg(wallpaper("#101626", "#0d1220") +
                              '<rect x="180" y="300" width="720" height="1300" fill="#2a2018" stroke="#1a140f" stroke-width="20"/>'
                              '<rect x="220" y="340" width="640" height="1220" fill="#151110"/>'
                              + "".join(f'<rect x="220" y="{y}" width="640" height="16" fill="#3a2d22"/>' for y in (700, 1060, 1400)) +
                              '<rect x="260" y="600" width="120" height="100" rx="10" fill="#5a6a7a"/><rect x="640" y="960" width="160" height="100" rx="10" fill="#6b5a3a"/>'
                              + insulin_box(560, 1000, 1.0, rot=0) +
                              '<path d="M 1080 1100 C 900 1060, 780 1040, 700 1030 L 700 1000 C 780 990, 900 1000, 1080 1020 Z" fill="#1c2a48"/>'
                              '<polygon points="0,1920 0,1600 420,500 960,700" fill="url(#beam)" opacity="0.7"/>'),
    "02_luis_alivio": svg('<rect width="1080" height="1920" fill="#0d1120"/>' +
                          '<g transform="translate(-540 -600) scale(2)">' + luis(540, 900, 1.0, mood="calm", box=False) + '</g>' +
                          '<polygon points="0,1920 0,1500 700,500 1080,760 1080,1920" fill="url(#beam)" opacity="0.6"/>'),
    # hora 26 (23:00), frío
    "03_reloj_26": svg(wallpaper("#121626", "#0f1322") + wall_clock(11, 0) +
                       '<polygon points="0,1920 0,1600 380,700 900,900" fill="url(#beam)" opacity="0.7"/>'),
    "04_frio": svg(DARK_SALON + window(250, 300, 580, 800) +
                   "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e6f2ff" opacity="0.35"/>' for x, y, r in
                           [(300, 360, 50), (780, 380, 60), (280, 1050, 70), (800, 1060, 55), (540, 340, 30)]) +
                   '<g transform="translate(540 1500) scale(0.9) translate(-540 -900)">' + hugo(mood="ok") + '</g>'
                   '<ellipse cx="660" cy="1560" rx="80" ry="35" fill="#e6f2ff" opacity="0.5" filter="url(#blur6)"/>'
                   '<path d="M 330 1700 C 360 1560, 720 1560, 750 1700 L 780 1920 L 300 1920 Z" fill="#8f1414"/>'),
    "05_cunado_garaje": svg('<rect width="1080" height="1920" fill="#0e1018"/>'
                            '<polygon points="0,1920 1080,1920 1080,1500 0,1600" fill="#1a1a20"/>' +
                            cunado(540, 820, 0.95, mood="happy") +
                            '<g transform="translate(540 1520) scale(0.55) translate(-540 -1300)">' + generator(running=False) + '</g>'
                            '<polygon points="0,1920 0,1650 460,500 1000,700" fill="url(#beam)" opacity="0.55"/>'),
    "06_generador_salon": svg(DARK_SALON +
                              '<rect x="620" y="300" width="360" height="520" fill="#2d4a7c" opacity="0.5" stroke="#05070d" stroke-width="16"/>'
                              + generator(540, 1320, 1.05) +
                              '<path d="M 830 1430 C 950 1500, 980 1650, 1080 1700" stroke="#111" stroke-width="12" fill="none"/>'
                              '<polygon points="0,1920 0,1600 420,700 960,900" fill="url(#beam)" opacity="0.5"/>'),
    "07_luz_estufa": svg(lit_room() + heater(720, 1150) + generator(330, 1450, 0.5, fumes=False) +
                         '<rect x="430" y="1580" width="60" height="110" rx="10" fill="#0e0e10"/><rect x="438" y="1590" width="44" height="90" rx="6" fill="#7aa7ff"/>'
                         '<rect x="520" y="1600" width="60" height="110" rx="10" fill="#0e0e10"/><rect x="528" y="1610" width="44" height="90" rx="6" fill="#7aa7ff"/>'
                         '<path d="M 460 1690 C 460 1760, 400 1760, 360 1740 M 550 1710 C 550 1780, 420 1780, 380 1750" stroke="#ddd" stroke-width="6" fill="none"/>'),
    "08_cunado_orgulloso": svg(lit_room() + cunado(540, 900, 1.0, mood="happy", thumb=True) +
                               generator(540, 1640, 0.55, fumes=False)),
    "09_hugo_cabeza": svg('<rect width="1080" height="1920" fill="#1e1a14"/>' +
                          '<g transform="translate(-540 -720) scale(2)">' + hugo(mood="pain", hands_head=True) + '</g>' +
                          gas_swirls(0.12)),
    "10_abuela_mareada": svg(wallpaper("#2a2418", "#252014") +
                             '<g transform="translate(-180 -420) scale(1.55)">' + abuela(mood="ahogo", lips="#b07a7a") + '</g>'
                             + "".join(f'<path d="M {x} 380 a 40 40 0 1 1 30 30" stroke="#ffd34d" stroke-width="8" fill="none" opacity="0.8"/>' for x in (250, 420, 600)) +
                             gas_swirls(0.12)),
    "11_rendija": svg(lit_room() +
                      '<rect x="240" y="420" width="600" height="820" fill="#0b1426" stroke="#05070d" stroke-width="18"/>'
                      '<path d="M 540 420 L 610 470 L 610 1190 L 540 1240 Z" fill="#2d4a7c" opacity="0.8"/>'
                      '<line x1="540" y1="420" x2="540" y2="1240" stroke="#05070d" stroke-width="12"/>'
                      '<path d="M 1080 900 C 900 880, 760 860, 640 860 L 630 820 C 660 800, 700 810, 720 830 C 820 830, 960 840, 1080 850 Z" fill="#e7c09c"/>'
                      '<path d="M 1080 900 C 980 900, 880 880, 800 870 L 820 830 C 900 840, 1000 850, 1080 850 Z" fill="#c4621f"/>' +
                      gas_swirls(0.14)),
    "12_hugo_vomita": svg('<rect width="1080" height="1920" fill="#1a1812"/>' + floor_tiles(1500, "#2a2018", "#241b14") +
                          '<g transform="translate(-232 389) scale(0.8) rotate(40 540 1560)">' + hugo(mood="sick") + '</g>'
                          '<path d="M 380 1500 L 420 1760 L 760 1760 L 800 1500 Z" fill="#3a6fb0"/>'
                          '<ellipse cx="590" cy="1500" rx="210" ry="36" fill="#26507f"/>' + gas_swirls(0.16)),
    "13_gas_invisible": svg('<rect width="1080" height="1920" fill="#0a0c12"/>' + generator(540, 1500, 0.8) + gas_swirls(0.32) +
                            '<text x="540" y="760" font-family="DejaVu Sans" font-weight="bold" font-size="260" fill="#c9d1e0" opacity="0.18" text-anchor="middle">CO</text>'),
    "14_decision": svg(split_p3()),
    "15_vela": svg('<rect width="1080" height="1920" fill="#06080f"/>' +
                   '<g transform="translate(420 900) scale(0.95) translate(-540 -900)">' + hugo(mood="ok") + '</g>'
                   + candle(800, 1560, 0.9)),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
