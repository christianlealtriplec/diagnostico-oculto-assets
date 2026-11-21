"""Escenas de la Parte 10 · La cola (v2 hilo conductor; rama B ganadora en la 09: hervís el agua)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, hallway_door, stairwell_down
from draw3 import wall_clock
from draw4 import hugo, cunado
from draw6 import camping_stove
from t1_p9 import pot_boiling, glass, queue, door_dark, KITCHEN, BEAM_ON, DARK_ROOM

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p10"

LANDING = (wallpaper("#14182a", "#10142a") + floor_tiles(1600, "#201913", "#1a140f") +
           '<rect x="0" y="300" width="140" height="1300" fill="#3a2a1e" stroke="#20170f" stroke-width="14"/>'
           '<path d="M 700 1600 L 1080 1250 L 1080 1600 Z" fill="#1a1510"/>'
           + ''.join(f'<path d="M {700+k*48} {1600-k*44} L {748+k*48} {1600-k*44}" stroke="#3a2d22" stroke-width="10"/>' for k in range(8)) +
           '<path d="M 720 1300 L 1080 960" stroke="#3a1414" stroke-width="18"/>')
DAWN = ('<rect width="1080" height="1920" fill="#1b2440"/>'
        '<rect width="1080" height="900" fill="#3a3f66"/><rect y="600" width="1080" height="400" fill="#7a5a6e" opacity="0.55"/>'
        '<rect y="850" width="1080" height="160" fill="#e8a07a" opacity="0.35"/>')
SIDEWALK = '<rect y="1500" width="1080" height="420" fill="#1a1d26"/><rect y="1500" width="1080" height="14" fill="#2a2e3a"/>'


def dawn_street():
    b = ''.join(f'<rect x="{x}" y="{1500-h}" width="{w}" height="{h}" fill="#141a2c" stroke="#0b0f1c" stroke-width="4"/>'
                for x, w, h in [(-20, 300, 900), (290, 240, 1050), (540, 280, 820), (830, 280, 980)])
    return DAWN + b + SIDEWALK


def breath(x, y, s=1.0):
    return ''.join(f'<circle cx="{x+k*38*s}" cy="{y-k*20*s}" r="{(26+k*12)*s}" fill="#e6edf5" opacity="{0.35-k*0.06:.2f}" filter="url(#blur6)"/>' for k in range(5))


def jug(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-90" y="-260" width="180" height="260" rx="30" fill="#9fd4ff" fill-opacity="0.35" stroke="#dfefff" stroke-width="8"/>'
            '<rect x="-30" y="-310" width="60" height="55" rx="10" fill="#1f6fd1"/>'
            '<path d="M 50 -240 C 110 -240, 110 -150, 50 -150" stroke="#dfefff" stroke-width="16" fill="none"/></g>')


def pot_lid(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -200 -230 L 200 -230 L 180 -20 C 175 10, 150 20, 120 20 L -120 20 C -150 20, -175 10, -180 -20 Z" fill="#8f969f"/>'
            '<ellipse cx="0" cy="-236" rx="215" ry="40" fill="#b8bdc4" stroke="#7a8088" stroke-width="6"/>'
            '<rect x="-40" y="-290" width="80" height="40" rx="12" fill="#3a3f48"/>'
            '<rect x="-270" y="-220" width="80" height="26" rx="12" fill="#3a3f48"/><rect x="190" y="-220" width="80" height="26" rx="12" fill="#3a3f48"/></g>')


def photo_tio():
    """El tío, en primer plano, bañado en rojo: lo buscan."""
    return ('<rect width="1080" height="1920" fill="#120608"/>' + BEAM_ON(540, 900) + tio(540, 1050, 1.25) +
            '<rect width="1080" height="1920" fill="#e10600" opacity="0.16"/>'
            '<circle cx="540" cy="900" r="430" fill="none" stroke="#e10600" stroke-width="14" stroke-dasharray="40 26"/>')


def sleeve_grab():
    """Una mano helada y arrugada agarra tu manga azul marino."""
    return ('<rect width="1080" height="1920" fill="#0e1424"/>' + DAWN.replace('#1b2440', '#141a30') +
            '<path d="M 1100 700 C 900 820, 700 900, 420 1000" stroke="#1c2a48" stroke-width="260" fill="none" stroke-linecap="round"/>'
            '<path d="M 1100 700 C 900 820, 700 900, 420 1000" stroke="#24365c" stroke-width="40" fill="none" opacity="0.6"/>'
            '<path d="M -40 1500 C 120 1350, 260 1200, 420 1080" stroke="#5c6470" stroke-width="210" fill="none" stroke-linecap="round"/>'
            '<g transform="translate(470 1030) rotate(-25)">'
            '<ellipse cx="0" cy="0" rx="120" ry="90" fill="#dcc8bc"/>'
            + ''.join(f'<path d="M {-80+k*50} -60 C {-90+k*50} -150, {-40+k*50} -200, {-20+k*50} -150" stroke="#dcc8bc" stroke-width="44" fill="none" stroke-linecap="round"/>' for k in range(4)) +
            ''.join(f'<path d="M {-80+k*50} -100 l 20 0" stroke="#a89488" stroke-width="5"/>' for k in range(4)) +
            '<ellipse cx="0" cy="0" rx="120" ry="90" fill="#9fb8d8" opacity="0.25"/></g>'
            '<rect width="1080" height="1920" fill="#e10600" opacity="0.08"/>')


scenes = {
    # apertura B: hervís el agua
    "01_hervir": svg(KITCHEN + BEAM_ON(540, 1000) + don_ramon(300, 860, 0.7, mood="serious", radio_hand=False) +
                     pot_boiling(660, 1250, 0.95) + camping_stove(660, 1620, 0.7, low=False)),
    "02_borbotones": svg('<rect width="1080" height="1920" fill="#0d0f16"/>' + BEAM_ON(540, 1000) +
                         pot_boiling(540, 1250, 1.7) + wall_clock(4, 1, 880, 420, 120)),
    "03_tapada": svg(KITCHEN + BEAM_ON(540, 1100) + pot_lid(540, 1350, 1.2) + glass(220, 1550, 0.7) + glass(860, 1550, 0.7)),
    "04_bebeis": svg(KITCHEN + BEAM_ON(540, 1000) + hugo(540, 1000, 0.95, mood="ok") + glass(760, 1300, 0.9, fill=0.7)),
    # la puerta: Protección Civil
    "05_puerta": svg(door_dark(knock=True)),
    "06_voluntario": svg(LANDING + '<polygon points="0,1920 0,1600 300,500 800,520 1080,1100 1080,1920" fill="url(#beam)" opacity="0.7"/>' +
                         voluntario(560, 900, 0.95, mood="serious")),
    "07_traed": svg(LANDING + BEAM_ON(540, 900) + voluntario(540, 980, 1.2, mood="shout") + jug(180, 1700, 0.8) + jug(900, 1700, 0.8)),
    "08_se_va": svg(LANDING + BEAM_ON(800, 1000) + voluntario(860, 1000, 0.75, mood="serious") +
                    '<rect x="0" y="300" width="140" height="1300" fill="#000" opacity="0.4"/>'),
    "09_pregunta": svg('<rect width="1080" height="1920" fill="#0b0d16"/>' + BEAM_ON(540, 900) + voluntario(520, 1150, 1.6, mood="shout", point=False)),
    "10_tio": svg(photo_tio()),
    # hora 80: amanece, la cola
    "11_amanece": svg(dawn_street()),
    "12_bajais": svg(dawn_street() + cunado(380, 1000, 0.8, mood="serious") + jug(720, 1660, 0.9) + jug(900, 1660, 0.9)
                     + breath(470, 900, 1.0)),
    "13_frio": svg(queue().replace('url(#moonsky)', '#3a3f66') + breath(980, 1460, 0.8) + breath(520, 1340, 0.6)),
    "14_senor": svg(dawn_street() + senor_mayor(540, 900, 0.95, mood="shiver") + breath(600, 860, 0.9)),
    "15_zapatillas": svg(dawn_street() + '<rect y="1100" width="1080" height="820" fill="#1a1d26"/>' + slippers(540, 1500, 1.4) +
                         ''.join(f'<path d="M {x} {y} c -10 18, -10 30, 0 36 c 10 -6, 10 -18, 0 -36 Z" fill="#9fd4ff"/>' for x, y in [(380, 1200), (700, 1250), (520, 1300)])),
    "16_senor_habla": svg('<rect width="1080" height="1920" fill="#141a30"/>' + DAWN + senor_mayor(540, 1180, 1.45, mood="talk") + breath(560, 1150, 1.2)),
    "17_cae": svg(dawn_street() + '<g transform="translate(560 1620) rotate(-90) translate(-540 -1085)">' +
                  senor_mayor(540, 900, 0.75, mood="weak") + '</g>' + slippers(860, 1760, 0.6) +
                  '<rect width="1080" height="1920" fill="#e10600" opacity="0.08"/>'),
    "18_voluntario_grita": svg(dawn_street() + voluntario(560, 900, 1.0, mood="shout", point=True) + breath(600, 860, 1.0)),
    "19_petaca": svg('<rect width="1080" height="1920" fill="#141a30"/>' + DAWN + hip_flask(560, 1050, 1.6, rot=-12)),
    "20_cunado": svg(dawn_street() + cunado(540, 950, 1.05, mood="happy", thumb=True) + hip_flask(250, 1480, 0.6, rot=10, hand=False)),
    "21_ya_no": svg(dawn_street() + '<g transform="translate(540 1600) rotate(-90) translate(-540 -1085)">' +
                    senor_mayor(540, 900, 0.75, mood="weak", wet=True) + '</g>' +
                    '<rect width="1080" height="1920" fill="#1f4f9f" opacity="0.12"/>'),
    "22_mala_senal": svg('<rect width="1080" height="1920" fill="#0b1020"/>' + senor_mayor(540, 1200, 1.6, mood="weak") +
                         '<rect width="1080" height="1920" fill="#1f4f9f" opacity="0.18"/><rect width="1080" height="1920" fill="url(#vig)"/>'),
    # decisión: coñac / a cubierto, mantas, algo caliente con azúcar
    "23_decision": svg('<rect width="540" height="1920" fill="#14100c"/><rect x="540" width="540" height="1920" fill="#0e1424"/>'
                       + hip_flask(270, 900, 0.95, rot=-10, hand=False) +
                       '<g transform="translate(810 900) scale(0.55) translate(-540 -900)">' + senor_mayor(540, 900, 1.0, mood="talk", wet=False, blanket=True) + '</g>'
                       '<g transform="translate(900 1230)"><rect x="-60" y="-80" width="120" height="120" rx="14" fill="#e8e8e8"/>'
                       '<path d="M -30 -100 C -50 -150, 0 -170, -20 -220 M 20 -100 C 0 -150, 50 -170, 30 -220" stroke="#e6edf5" stroke-width="10" fill="none" opacity="0.5"/>'
                       '<path d="M 60 -50 C 110 -50, 110 10, 60 10" stroke="#e8e8e8" stroke-width="16" fill="none"/></g>'
                       '<rect x="532" y="0" width="16" height="1280" fill="#e10600"/>'),
    # suspenso
    "24_manga": svg(sleeve_grab()),
    "25_susurra": svg('<rect width="1080" height="1920" fill="#120608"/>' + senor_mayor(540, 1200, 1.6, mood="talk", wet=True) +
                      '<rect width="1080" height="1920" fill="#e10600" opacity="0.14"/><rect width="1080" height="1920" fill="url(#vig)"/>'),
    "26_final": svg(dawn_street() + queue().replace('url(#moonsky)', '#3a3f66')[:0] +
                    '<rect width="1080" height="1920" fill="#000" opacity="0.45"/>' + tio(540, 760, 0.5) +
                    '<rect width="1080" height="1920" fill="#e10600" opacity="0.1"/>'),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
