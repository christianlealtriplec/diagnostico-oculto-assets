"""Escenas de la Parte 13 · El tío (rama B ganadora en la 12: golpes en la espalda y compresiones; Hugo respira)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, street
from draw4 import hugo, cunado
from t1_p9 import BEAM_ON
from t1_p11 import vans_night
from t1_p12 import candy, queue_poli, poli_facade

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p13"

RED = lambda op: f'<rect width="1080" height="1920" fill="#e10600" opacity="{op}"/>'
DARK = lambda c: f'<rect width="1080" height="1920" fill="{c}"/>'
SHADE = lambda op: f'<rect width="1080" height="1920" fill="#000" opacity="{op}"/>'


def hugo_bent(x, y, s=1.0, mood="choke"):
    """Hugo inclinado hacia delante (tronco a 60°)."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<g transform="rotate(60) scale(0.75) translate(-540 -1150)">' + hugo(540, 900, 1.0, mood=mood) + '</g></g>')


def open_hand(x, y, s=1.0, rot=-30, sleeve="#2c3550"):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M 0 -20 L 0 -300" stroke="{sleeve}" stroke-width="80" stroke-linecap="round"/>'
            '<ellipse cx="0" cy="0" rx="75" ry="55" fill="url(#skin)"/>'
            + "".join(f'<rect x="{-60 + i*30}" y="20" width="24" height="70" rx="12" fill="url(#skin)"/>' for i in range(4)) + '</g>')


def impact(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            + "".join(f'<path d="M {dx} {dy} l {ex} {ey}" stroke="#ffd400" stroke-width="14" stroke-linecap="round"/>'
                      for dx, dy, ex, ey in ((-90, -40, -60, -20), (0, -90, 0, -60), (90, -40, 60, -20), (-70, 50, -50, 30), (70, 50, 50, 30)))
            + '</g>')


def heimlich():
    """Abrazo por detrás: Hugo de frente, tus brazos rodeándole y el puño sobre la tripa; flecha hacia dentro y arriba."""
    return (hugo(540, 880, 1.05, mood="choke") +
            '<path d="M 120 1250 C 260 1300, 380 1330, 470 1330" stroke="#2c3550" stroke-width="80" fill="none" stroke-linecap="round"/>'
            '<path d="M 960 1250 C 820 1300, 700 1330, 610 1330" stroke="#2c3550" stroke-width="80" fill="none" stroke-linecap="round"/>'
            '<circle cx="540" cy="1330" r="70" fill="url(#skin)" stroke="#b98a66" stroke-width="6"/>'
            '<path d="M 490 1310 L 590 1310 M 490 1340 L 590 1340" stroke="#b98a66" stroke-width="6"/>'
            '<path d="M 540 1460 C 560 1400, 560 1340, 540 1250" stroke="#ffd400" stroke-width="16" fill="none" stroke-linecap="round"/>'
            '<path d="M 505 1290 L 540 1240 L 575 1290" stroke="#ffd400" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


def tears(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -40 0 C -45 30, -50 60, -42 80" stroke="#9fd4ff" stroke-width="12" fill="none" stroke-linecap="round"/>'
            '<path d="M 40 0 C 45 30, 50 60, 42 80" stroke="#9fd4ff" stroke-width="12" fill="none" stroke-linecap="round"/>'
            '<ellipse cx="-42" cy="96" rx="10" ry="14" fill="#9fd4ff"/><ellipse cx="42" cy="96" rx="10" ry="14" fill="#9fd4ff"/></g>')


def walkers():
    """Familia volviendo a casa por la calle a oscuras, de espaldas."""
    return "".join(
        f'<g transform="translate({x} 1640) scale({s})"><circle cx="0" cy="-230" r="34" fill="#05070d"/>'
        '<path d="M -50 0 L -45 -180 C -40 -200, 40 -200, 45 -180 L 50 0 Z" fill="#05070d"/>'
        '<path d="M -30 0 L -36 90 M 30 0 L 36 90" stroke="#05070d" stroke-width="30" stroke-linecap="round"/></g>'
        for x, s in ((420, 1.1), (560, 0.7), (680, 1.05)))


def portal(lit=False, sitter=True, blood=False):
    """Portal del edificio de noche: puerta de hierro y cristal, dos escalones y portero automático apagado."""
    sit = ('<g opacity="0.95"><circle cx="380" cy="1300" r="48" fill="#05070d"/>'
           '<path d="M 310 1520 C 300 1420, 330 1360, 380 1355 C 440 1360, 470 1420, 460 1520 Z" fill="#05070d"/>'
           '<path d="M 330 1520 L 520 1530 L 540 1640" stroke="#05070d" stroke-width="56" fill="none" stroke-linecap="round"/></g>') if sitter else ""
    drops = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.6:.0f}" fill="#8f0a0a"/>'
                    for x, y, r in ((470, 1560, 18), (500, 1575, 10), (440, 1590, 12), (520, 1700, 22), (480, 1715, 9))) if blood else ""
    return ('<rect width="1080" height="1920" fill="#0b1020"/>'
            + "".join(f'<rect x="{x}" y="{y}" width="120" height="70" fill="#141b2e" stroke="#0a0d18" stroke-width="4"/>'
                      for y in range(60, 520, 110) for x in range(30, 1080, 140)) +
            '<rect x="200" y="560" width="680" height="980" fill="#1b2236" stroke="#0a0d18" stroke-width="12"/>'
            '<rect x="250" y="610" width="580" height="930" fill="#0f1424"/>'
            '<rect x="290" y="650" width="230" height="860" fill="#1a2440" opacity="0.8"/><rect x="560" y="650" width="230" height="860" fill="#1a2440" opacity="0.8"/>'
            + "".join(f'<path d="M {x} 650 L {x} 1510" stroke="#0a0d18" stroke-width="10"/>' for x in (350, 405, 460, 620, 675, 730)) +
            '<circle cx="540" cy="1100" r="14" fill="#c9a24a"/>'
            '<rect x="895" y="900" width="90" height="160" rx="8" fill="#2a2e3a"/>'
            + "".join(f'<circle cx="940" cy="{y}" r="10" fill="#555b6a"/>' for y in (940, 980, 1020)) +
            '<rect x="440" y="470" width="200" height="70" rx="6" fill="#c9a24a"/>'
            '<text x="540" y="520" font-family="DejaVu Serif" font-weight="bold" font-size="44" fill="#2a1f16" text-anchor="middle">Nº 14</text>'
            '<rect x="140" y="1540" width="800" height="80" fill="#2a2e3a"/><rect x="100" y="1620" width="880" height="90" fill="#232631"/>'
            '<rect y="1710" width="1080" height="210" fill="#0d0f16"/>'
            + (BEAM_ON(400, 1350) if lit else "") + sit + drops)


def blood_step(x=540, y=1300, s=1.0):
    """Primer plano del escalón con gotas de sangre que caen."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<rect x="-560" y="0" width="1120" height="160" fill="#2a2e3a"/><rect x="-560" y="160" width="1120" height="200" fill="#1e212b"/>'
            '<rect x="-560" y="-6" width="1120" height="14" fill="#3a3f4f"/>'
            + "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="{r}" ry="{r*0.55:.0f}" fill="#8f0a0a"/>'
                      for dx, dy, r in ((-60, 60, 50), (40, 80, 26), (-140, 100, 20), (110, 40, 16), (-10, 120, 34)))
            + "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="12" ry="20" fill="#b30d0d"/>' for dx, dy in ((-20, -300), (-30, -160), (10, -60)))
            + '</g>')


def wrapped_arm(x=540, y=1000, s=1.0):
    """Primer plano: antebrazo envuelto en una camiseta clara empapada de sangre; gotea."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -600 -40 L -200 -40" stroke="#2f4f86" stroke-width="210" stroke-linecap="butt"/>'
            '<path d="M -220 -130 C -60 -160, 160 -150, 280 -120 L 290 60 C 170 90, -60 90, -220 60 Z" fill="#e9e4da"/>'
            '<path d="M -200 -110 C -40 -140, 140 -130, 270 -100 L 275 50 C 160 75, -40 75, -200 45 Z" fill="#b30d0d" opacity="0.88"/>'
            '<ellipse cx="40" cy="-30" rx="150" ry="70" fill="#7a0505"/>'
            '<path d="M -150 -100 C -100 -30, -120 40, -150 60 M 120 -120 C 160 -40, 150 30, 120 70" stroke="#d9d2c4" stroke-width="10" fill="none" opacity="0.6"/>'
            '<ellipse cx="380" cy="-20" rx="110" ry="90" fill="url(#skin)"/>'
            + "".join(f'<rect x="{440}" y="{-90 + i*40}" width="110" height="32" rx="16" fill="url(#skin)"/>' for i in range(4)) +
            '<path d="M 20 70 C 15 140, 25 200, 20 260" stroke="#b30d0d" stroke-width="18" fill="none" stroke-linecap="round"/>'
            '<ellipse cx="20" cy="300" rx="16" ry="26" fill="#b30d0d"/><ellipse cx="20" cy="420" rx="12" ry="20" fill="#b30d0d"/>'
            '</g>')


def belt_hands(x=540, y=1350, s=1.0):
    """Manos del cuñado sujetando un cinturón de cuero estirado con la hebilla."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -300 0 C -150 -40, 150 -40, 300 0" stroke="#4a2a14" stroke-width="46" fill="none"/>'
            '<path d="M -300 0 C -150 -40, 150 -40, 300 0" stroke="#6b3d1e" stroke-width="10" fill="none" stroke-dasharray="20 18"/>'
            '<rect x="250" y="-45" width="80" height="90" rx="10" fill="none" stroke="#c9ccd2" stroke-width="14"/>'
            '<circle cx="-320" cy="0" r="56" fill="url(#skin)"/><circle cx="340" cy="0" r="56" fill="url(#skin)"/>'
            '<path d="M -340 40 L -460 200 M 360 40 L 480 200" stroke="#c4621f" stroke-width="80" stroke-linecap="round"/></g>')


def grab_hand(x=540, y=1100, s=1.0):
    """La mano del tío agarra tu antebrazo (primer plano)."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -620 60 L 620 60" stroke="#2c3550" stroke-width="170"/>'
            '<path d="M 500 -400 C 380 -250, 250 -120, 160 -60" stroke="#2f4f86" stroke-width="120" stroke-linecap="round" fill="none"/>'
            '<path d="M 60 -60 C 120 -90, 240 -80, 260 -20 L 250 150 C 180 190, 60 180, 30 140 Z" fill="url(#skin)" stroke="#b98a66" stroke-width="6"/>'
            + "".join(f'<path d="M {fx} -40 C {fx-10} 40, {fx-10} 120, {fx+10} 170" stroke="#b98a66" stroke-width="8" fill="none"/>' for fx in (90, 140, 190))
            + '<path d="M 230 -30 C 150 0, 100 20, 60 30" stroke="#b98a66" stroke-width="8" fill="none"/>'
            '</g>')


def decision_split():
    """A: cinturón apretado como torniquete (tachado mental) · B: dos manos presionando la herida."""
    left = ('<g transform="translate(270 950) scale(0.75)">'
            '<path d="M -320 -40 L 320 -40" stroke="#2f4f86" stroke-width="200"/>'
            '<rect x="-40" y="-150" width="80" height="220" fill="#4a2a14"/>'
            '<rect x="-56" y="-60" width="112" height="80" rx="8" fill="none" stroke="#c9ccd2" stroke-width="14"/></g>')
    right = ('<g transform="translate(810 1000) scale(0.75)">'
             '<path d="M -360 0 L 360 0" stroke="#2f4f86" stroke-width="200"/>'
             '<path d="M -120 -90 C -40 -110, 60 -110, 130 -90 L 130 90 C 60 110, -40 110, -120 90 Z" fill="#e9e4da"/>'
             '<ellipse cx="0" cy="0" rx="80" ry="50" fill="#b30d0d" opacity="0.7"/>'
             '<ellipse cx="0" cy="-60" rx="170" ry="110" fill="url(#skin)" stroke="#b98a66" stroke-width="6"/>'
             '<ellipse cx="20" cy="-130" rx="150" ry="90" fill="url(#skin)" stroke="#b98a66" stroke-width="6"/>'
             '<path d="M 0 -380 L 0 -260 M -40 -300 L 0 -250 L 40 -300" stroke="#ffd400" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return ('<rect width="540" height="1920" fill="#0e1424"/><rect x="540" width="540" height="1920" fill="#14100c"/>'
            + left + right + '<rect x="532" y="0" width="16" height="1280" fill="#e10600"/>')


scenes = {
    # apertura B: golpes en la espalda y compresiones; el caramelo sale
    "01_inclinas": svg(queue_poli() + SHADE(0.45) + BEAM_ON(540, 1000) + hugo_bent(540, 1250, 1.0) +
                       open_hand(450, 1110, 0.8, rot=-20)),
    "02_golpes": svg(DARK("#0c1020") + BEAM_ON(540, 900) + hugo_bent(560, 1350, 1.35) +
                     open_hand(420, 1140, 1.05, rot=-20) + impact(430, 1230, 1.3)),
    "03_compresion": svg(DARK("#0e0c18") + BEAM_ON(540, 900) + heimlich()),
    "04_caramelo_sale": svg(DARK("#0c1020") + BEAM_ON(540, 900) +
                            '<g transform="translate(380 1150) scale(1.4) translate(-540 -900)">' + hugo(540, 900, 1.0, mood="sick") + '</g>' +
                            candy(820, 760, 1.6) +
                            '<path d="M 520 1000 C 620 900, 700 830, 740 800" stroke="#ffd400" stroke-width="10" fill="none" stroke-dasharray="20 20"/>'),
    "05_hugo_llora": svg(queue_poli() + SHADE(0.5) + BEAM_ON(540, 900) +
                         '<g transform="translate(540 1100) scale(1.5) translate(-540 -900)">' + hugo(540, 900, 1.0, mood="pain") + '</g>' +
                         tears(540, 1030, 1.5)),
    # vuelta a casa
    "06_poli_noche": svg(vans_night(people=False) + SHADE(0.25)),
    "07_vuelta_casa": svg(street() + SHADE(0.35) + walkers()),
    "08_portal_lejos": svg(portal(lit=False, sitter=True) + SHADE(0.25)),
    "09_portal_linterna": svg(portal(lit=True, sitter=True)),
    # es el tío
    "10_calvo_barba": svg(DARK("#0a0d18") + BEAM_ON(540, 900) +
                          '<g transform="translate(540 1350) scale(1.9) translate(-540 -900)">' + tio(540, 900, 1.0, mood="pain", point=False) + '</g>'),
    "11_tu_tio": svg(portal(lit=True, sitter=False, blood=True) + tio(500, 1020, 0.95, mood="pain", point=False, wounded=True) + RED(0.12)),
    "12_primera_noche": svg(door() + tio(540, 920, 1.05) + '<rect width="1080" height="1920" fill="#3a2a10" opacity="0.45"/>' +
                            '<rect x="40" y="40" width="1000" height="1840" fill="none" stroke="#d9c9a0" stroke-width="10" opacity="0.5"/>'),
    "13_brazo": svg(DARK("#120808") + BEAM_ON(540, 900) + wrapped_arm(560, 950, 1.0) + RED(0.1)),
    "14_tio_habla": svg(DARK("#0c0f1c") + BEAM_ON(540, 900) + tio(560, 1000, 1.15, mood="pain", point=False, wounded=True)),
    "15_gotea": svg(DARK("#0a0c14") + BEAM_ON(540, 1100) + blood_step(540, 1250, 1.0)),
    "16_cinturon": svg(portal(lit=True, sitter=False, blood=True) + SHADE(0.35) + cunado(560, 950, 1.0, mood="serious") +
                       belt_hands(560, 1380, 0.8)),
    # decisión
    "17_decision": svg(decision_split()),
    # suspenso
    "18_agarra": svg(DARK("#0c0a12") + BEAM_ON(540, 900) + grab_hand(540, 1050, 1.1) + RED(0.1)),
    "19_secreto": svg(DARK("#08090f") + '<g transform="translate(540 1250) scale(1.7) translate(-540 -900)">' +
                      tio(540, 900, 1.0, mood="whisper", point=False) + '</g>' +
                      '<polygon points="0,1920 0,1500 300,700 820,750 1080,1400 1080,1920" fill="url(#beam)" opacity="0.5"/>'),
    "20_final": svg(portal(lit=False, sitter=False, blood=True) + SHADE(0.45) + RED(0.1)),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
