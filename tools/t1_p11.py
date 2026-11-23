"""Escenas de la Parte 11 · Luis (rama B ganadora en la 10: refugio, ropa seca, mantas y caldo con azúcar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door
from draw3 import luis, mujer_luis, insulin_pen, wall_clock
from draw5 import radio
from draw6 import cans
from draw4 import cunado
from t1_p9 import glass, BEAM_ON
from t1_p10 import jug, breath

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p11"

GYM = (wallpaper("#1a1f2e", "#161a28") + floor_tiles(1500, "#2a2118", "#231b14") +
       ''.join(f'<rect x="{x}" y="240" width="150" height="220" fill="#0e1322" stroke="#2a3048" stroke-width="8"/>' for x in (80, 465, 850)) +
       '<rect x="0" y="1380" width="1080" height="20" fill="#3a3f55"/>'
       # catres al fondo
       + ''.join(f'<rect x="{x}" y="1300" width="220" height="50" rx="10" fill="#4a5a3a"/><rect x="{x+10}" y="1350" width="10" height="60" fill="#222"/><rect x="{x+200}" y="1350" width="10" height="60" fill="#222"/>' for x in (40, 820)))
LANTERN = '<circle cx="540" cy="200" r="22" fill="#fff3d1"/><circle cx="540" cy="200" r="260" fill="url(#glow)" opacity="0.22"/>'
STAIRS_LUIS = (wallpaper("#14182a", "#10142a") +
               ''.join(f'<rect x="0" y="{1100+i*120}" width="1080" height="120" fill="{c}" stroke="#0a0c14" stroke-width="6"/>'
                       for i, c in enumerate(["#2a2219", "#251e16", "#211a13", "#1d1711", "#19140f", "#15110c", "#120e0a"])) +
               '<path d="M 80 1100 L 80 300" stroke="#3a1414" stroke-width="20"/><path d="M 80 500 L 1080 500" stroke="#3a1414" stroke-width="18"/>')


def sweat(x, y, s=1.0):
    """Gotas de sudor frío en la frente."""
    return ''.join(f'<path d="M {x+dx*s} {y+dy*s} c {-12*s} {22*s}, {-12*s} {36*s}, 0 {42*s} c {12*s} {-6*s}, {12*s} {-20*s}, 0 {-42*s} Z" fill="#bfe6ff" stroke="#7fb3d9" stroke-width="2"/>'
                   for dx, dy in [(-80, -60), (60, -80), (110, 10), (-120, 20)])


def tremor(x, y, s=1.0):
    return ''.join(f'<path d="M {x+sx*s} {y+k*60*s} q {12*s*sx/abs(sx)} {15*s}, 0 {30*s} q {-12*s*sx/abs(sx)} {15*s}, 0 {30*s}" stroke="#e6edf5" stroke-width="6" fill="none" opacity="0.7"/>'
                   for sx in (-170, 170) for k in range(3))


def blankets_pile(x=540, y=1500, s=1.0):
    """Dos mantas dobladas y la ropa mojada en el suelo, goteando."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<rect x="-380" y="-120" width="360" height="90" rx="30" fill="#7a2c2c"/><rect x="-370" y="-200" width="340" height="85" rx="30" fill="#3d5d92"/>'
            '<path d="M -360 -160 L -40 -160" stroke="#2a3f66" stroke-width="6" stroke-dasharray="20 12"/>'
            '<path d="M 60 -40 C 120 -140, 260 -150, 340 -60 C 380 -10, 300 20, 200 10 C 130 0, 70 10, 60 -40 Z" fill="#3a3f48"/>'
            '<path d="M 120 -60 C 160 -100, 240 -100, 280 -60" stroke="#2a2e36" stroke-width="10" fill="none"/>'
            + ''.join(f'<path d="M {dx} 20 c -8 14, -8 24, 0 28 c 8 -4, 8 -14, 0 -28 Z" fill="#9fd4ff"/>' for dx in (110, 200, 290)) +
            '<ellipse cx="200" cy="60" rx="200" ry="22" fill="#9fd4ff" opacity="0.2"/></g>')


def broth(x=540, y=1100, s=1.0):
    """Taza de caldo humeante y terrones de azúcar."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -190 -180 L 190 -180 L 160 120 C 150 170, 110 190, 60 190 L -60 190 C -110 190, -150 170, -160 120 Z" fill="#e8e8e8" stroke="#b8bdc4" stroke-width="8"/>'
            '<ellipse cx="0" cy="-180" rx="190" ry="40" fill="#c9893a"/>'
            '<path d="M 185 -100 C 290 -100, 290 60, 165 60" stroke="#e8e8e8" stroke-width="34" fill="none"/>'
            + ''.join(f'<path d="M {dx} -230 C {dx-40} -300, {dx+40} -340, {dx} -420" stroke="#e6edf5" stroke-width="14" fill="none" opacity="0.45" stroke-linecap="round"/>' for dx in (-80, 0, 80)) +
            ''.join(f'<rect x="{dx}" y="230" width="80" height="80" rx="6" fill="#f6f6f2" stroke="#cfcfc6" stroke-width="4"/>' for dx in (-300, -200, 260)) +
            '</g>')


def vans_night(people=True):
    """Polideportivo de noche: furgonetas con los faros encendidos se llevan a gente."""
    vans = ''.join(
        f'<g transform="translate({x} 1560) scale({s})"><rect x="-230" y="-260" width="420" height="240" rx="18" fill="#2a2e38"/>'
        '<path d="M 190 -220 L 260 -220 L 290 -130 L 290 -20 L 190 -20 Z" fill="#23262f"/>'
        '<circle cx="-140" cy="-20" r="44" fill="#0a0a0a"/><circle cx="200" cy="-20" r="44" fill="#0a0a0a"/>'
        '<circle cx="285" cy="-90" r="18" fill="#fff3d1"/>'
        '<polygon points="285,-110 1200,-400 1200,200 285,-70" fill="#fff3d1" opacity="0.18"/></g>' for x, s in ((260, 0.95), (720, 0.7)))
    figs = ''.join(f'<g transform="translate({x} 1500) scale({s})"><circle cx="0" cy="-230" r="30" fill="#05070c"/>'
                   '<path d="M -45 0 L -40 -180 C -35 -200, 35 -200, 40 -180 L 45 0 Z" fill="#05070c"/></g>'
                   for x, s in ((520, 0.8), (580, 0.75), (900, 0.6))) if people else ""
    return ('<rect width="1080" height="1920" fill="#070b17"/>'
            '<rect x="40" y="700" width="1000" height="700" fill="#141a2c" stroke="#0b0f1c" stroke-width="10"/>'
            '<path d="M 40 700 Q 540 520 1040 700" fill="#1a2238" stroke="#0b0f1c" stroke-width="10"/>'
            '<rect x="330" y="780" width="420" height="90" fill="#c9a24a"/>'
            '<text x="540" y="842" font-family="DejaVu Sans" font-weight="bold" font-size="44" fill="#2a1f16" text-anchor="middle">POLIDEPORTIVO</text>'
            '<rect x="440" y="1050" width="200" height="350" fill="#2a2a20"/><rect x="440" y="1050" width="200" height="350" fill="#fff3d1" opacity="0.12"/>'
            '<rect y="1400" width="1080" height="520" fill="#0b0d14"/>' + vans + figs)


def luis_sitting(cx=540, cy=900, s=1.0, mood="worry"):
    """Luis sentado en un escalón: piernas dobladas, sudando y temblando."""
    legs = (f'<g transform="translate({cx} {cy}) scale({s}) translate(-540 -900)">'
            '<path d="M 420 1500 L 360 1700 L 300 1720" stroke="#2c3040" stroke-width="90" fill="none" stroke-linecap="round"/>'
            '<path d="M 660 1500 L 720 1700 L 780 1720" stroke="#2c3040" stroke-width="90" fill="none" stroke-linecap="round"/></g>')
    return legs + luis(cx, cy, s, mood=mood, box=False) + sweat(cx, cy - 120 * s, s) + tremor(cx, cy + 300 * s, s)


def dosis_pen(x=540, y=1000, s=1.0, rot=-30):
    """La pluma de insulina en la mano de Pilar, apuntando hacia arriba."""
    return (f'<g transform="translate({x} {y}) scale({s})">' + insulin_pen(0, 0, 1.0, rot=rot) +
            '<ellipse cx="0" cy="80" rx="90" ry="70" fill="url(#skin)"/>'
            '<path d="M -60 60 C -120 140, -130 260, -100 400" stroke="#7a2438" stroke-width="120" fill="none" stroke-linecap="round"/></g>')


def sugar_aid(x=540, y=1100, s=1.0):
    """Azúcar rápido: vaso de zumo, sobres de azúcar y caramelos."""
    return (f'<g transform="translate({x} {y}) scale({s})">' + glass(-90, 120, 1.0, fill=0.8).replace('#9fd4ff', '#ffa630') +
            '<rect x="40" y="-40" width="90" height="140" rx="8" fill="#f6f6f2" stroke="#cfcfc6" stroke-width="5"/>'
            '<text x="85" y="45" font-family="DejaVu Sans" font-weight="bold" font-size="26" fill="#c0392b" text-anchor="middle">AZÚCAR</text>'
            + ''.join(f'<g transform="translate({dx} {dy})"><ellipse cx="0" cy="0" rx="38" ry="26" fill="{c}"/>'
                      f'<path d="M -38 0 L -66 -20 L -66 20 Z" fill="{c}"/><path d="M 38 0 L 66 -20 L 66 20 Z" fill="{c}"/></g>'
                      for dx, dy, c in ((-20, 230, "#e10600"), (120, 250, "#f2c200"))) + '</g>')


def empty_plate(x=540, y=1250, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<ellipse cx="0" cy="0" rx="300" ry="110" fill="#e8e8e8" stroke="#b8bdc4" stroke-width="8"/>'
            '<ellipse cx="0" cy="0" rx="200" ry="70" fill="none" stroke="#cfd4da" stroke-width="6"/>'
            '<path d="M -40 -10 l 30 6 M 50 10 l 18 -4" stroke="#c9a24a" stroke-width="10" stroke-linecap="round"/>'
            '<rect x="330" y="-60" width="18" height="190" rx="8" fill="#9aa1ab" transform="rotate(12 340 30)"/></g>')


scenes = {
    # apertura B: al colegio, seco, mantas, caldo
    "01_colegio_dentro": svg(GYM + LANTERN + voluntario(250, 1020, 0.75, mood="serious") +
                             senor_mayor(700, 980, 0.85, mood="shiver", wet=True) + cunado(1000, 1080, 0.6, mood="serious")),
    "02_mantas": svg(GYM + LANTERN + senor_mayor(540, 1000, 0.95, mood="weak", wet=False, blanket=True) + blankets_pile(540, 1780, 1.1)),
    "03_caldo": svg('<rect width="1080" height="1920" fill="#14100c"/>' + LANTERN + broth(540, 1150, 1.3)),
    "04_tirita": svg(GYM + LANTERN + senor_mayor(540, 1000, 1.1, mood="shiver", wet=False, blanket=True)),
    # el señor habla del polideportivo
    "05_habla": svg('<rect width="1080" height="1920" fill="#141a28"/>' + LANTERN + senor_mayor(540, 1180, 1.45, mood="talk", wet=False, blanket=True)),
    "06_furgonetas": svg(vans_night(True) + '<g opacity="0.95">' +
                         '<rect x="40" y="260" width="440" height="500" rx="24" fill="#141a28" stroke="#c9a24a" stroke-width="8"/>' +
                         '<g transform="translate(260 560) scale(0.38) translate(-540 -900)">' + senor_mayor(540, 900, 1.0, mood="talk", wet=False, blanket=True) + '</g></g>'),
    "07_las_tres": svg('<rect width="1080" height="1920" fill="#120608"/>' + tio(540, 1150, 1.05) +
                       wall_clock(3, 0, 850, 520, 150) + '<rect width="1080" height="1920" fill="#e10600" opacity="0.15"/>' +
                       '<rect x="40" y="260" width="440" height="500" rx="24" fill="#141a28" stroke="#c9a24a" stroke-width="8"/>' +
                       '<g transform="translate(260 560) scale(0.38) translate(-540 -900)">' + senor_mayor(540, 900, 1.0, mood="talk", wet=False, blanket=True) + '</g>'),
    # subes con las garrafas: el 2.º
    "08_subes": svg(STAIRS_LUIS + BEAM_ON(540, 900) + jug(330, 1500, 1.0) + jug(760, 1380, 1.0) + phone_hand(40, 1700, rot=-18)),
    "09_puerta_abierta": svg(hallway_door(label="2º", knock=False) +
                             '<path d="M 280 365 L 520 460 L 520 1520 L 280 1595 Z" fill="#0a0806"/>' +
                             '<path d="M 280 365 L 520 460 L 520 1520 L 280 1595" stroke="#20170f" stroke-width="10" fill="none"/>'),
    "10_luis_escalera": svg(STAIRS_LUIS + BEAM_ON(540, 1000) + luis_sitting(540, 900, 0.85)),
    "11_que_dia": svg('<rect width="1080" height="1920" fill="#0c1020"/>' + BEAM_ON(540, 900) +
                      '<g transform="translate(540 1050) scale(1.6) translate(-540 -900)">' + luis(540, 900, 1.0, mood="worry", box=False) + '</g>' +
                      sweat(540, 720, 1.5)),
    # Pilar y la pluma
    "12_pilar_pluma": svg(STAIRS_LUIS + BEAM_ON(700, 900) + luis_sitting(300, 1000, 0.6) + mujer_luis(720, 960, 0.9, point=False) +
                          insulin_pen(800, 1230, 0.45, rot=-20)),
    "13_pilar_habla": svg('<rect width="1080" height="1920" fill="#120c14"/>' + BEAM_ON(540, 900) + mujer_luis(540, 1050, 1.3, point=False) +
                          insulin_pen(640, 1560, 0.6, rot=-15)),
    "14_otra_dosis": svg('<rect width="1080" height="1920" fill="#120c14"/>' + BEAM_ON(540, 900) + mujer_luis(540, 1080, 1.2, point=True) +
                         '<g transform="translate(900 880)">' + insulin_pen(0, 0, 0.5, rot=-40) + '</g>' +
                         '<rect width="1080" height="1920" fill="#e10600" opacity="0.07"/>'),
    # hora 85: los síntomas
    "15_hora85": svg(wallpaper("#14182a", "#10142a") + BEAM_ON(540, 900) + wall_clock(1, 0, 540, 860, 330)),
    "16_sintomas": svg('<rect width="1080" height="1920" fill="#0a0e1c"/>' +
                       '<g transform="translate(540 1250) scale(2.3) translate(-540 -900)">' + luis(540, 900, 1.0, mood="worry", box=False) + '</g>' +
                       sweat(540, 640, 2.0) + tremor(540, 1300, 1.6) + '<rect width="1080" height="1920" fill="#e10600" opacity="0.1"/>'),
    "17_sin_comer": svg(wallpaper("#151a24", "#11161f") + floor_tiles(1600, "#1d1914", "#17130f") + BEAM_ON(540, 1100) +
                        '<rect x="0" y="1350" width="1080" height="40" fill="#3a2d22"/>' + empty_plate(500, 1300, 1.3) +
                        cans(860, 1340, 0.45, n=1)),
    # decisión
    "18_decision": svg('<rect width="540" height="1920" fill="#14100c"/><rect x="540" width="540" height="1920" fill="#0e1424"/>' +
                       '<g transform="translate(270 950)">' + insulin_pen(0, 0, 0.75, rot=-35) + '</g>' +
                       sugar_aid(800, 880, 1.15) + '<rect x="532" y="0" width="16" height="1280" fill="#e10600"/>'),
    # suspenso: Don Ramón y la radio
    "19_ramon_asoma": svg(STAIRS_LUIS.replace('#14182a', '#0c0f1c') + '<rect y="0" width="1080" height="500" fill="#06080f"/>' +
                          don_ramon(760, 640, 0.75, mood="serious", radio_hand=True) + BEAM_ON(760, 500) +
                          '<rect width="1080" height="1920" fill="#e10600" opacity="0.1"/>'),
    "20_ramon_habla": svg('<rect width="1080" height="1920" fill="#120608"/>' + BEAM_ON(540, 900) +
                          don_ramon(540, 1080, 1.35, mood="shout", radio_hand=True) +
                          '<rect width="1080" height="1920" fill="#e10600" opacity="0.12"/>'),
    "21_final": svg(vans_night(False) + '<rect width="1080" height="1920" fill="#000" opacity="0.35"/>' +
                    '<rect width="1080" height="1920" fill="#e10600" opacity="0.1"/>'),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
