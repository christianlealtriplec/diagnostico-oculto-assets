"""Escenas de la Parte 12 · El polideportivo (rama B ganadora en la 11: zumo y caramelos, Luis vuelve)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles
from draw3 import luis, mujer_luis, wall_clock
from draw4 import hugo
from t1_p9 import BEAM_ON
from t1_p11 import STAIRS_LUIS, GYM, LANTERN, sugar_aid, sweat

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p12"


def candy(x, y, s=1.0, c="#e10600"):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="0" cy="0" rx="38" ry="26" fill="{c}"/>'
            f'<path d="M -38 0 L -66 -20 L -66 20 Z" fill="{c}"/><path d="M 38 0 L 66 -20 L 66 20 Z" fill="{c}"/>'
            '<path d="M -18 -10 Q 0 -20 18 -10" stroke="#fff" stroke-width="5" fill="none" opacity="0.6"/></g>')


def luis_calm(cx=540, cy=900, s=1.0):
    """Luis ya despejado: sin sudor, boca abierta hablando."""
    return luis(cx, cy, s, mood="talk", box=False)


def poli_facade(sign=True, door_lit=True):
    """Fachada del polideportivo al atardecer (hora 90), con la puerta de cristal y un cartel."""
    return ('<rect width="1080" height="1920" fill="url(#moonsky)"/>'
            '<rect x="-20" y="620" width="1120" height="900" fill="#141a2c" stroke="#0b0f1c" stroke-width="10"/>'
            '<path d="M -20 620 Q 540 430 1100 620" fill="#1a2238" stroke="#0b0f1c" stroke-width="10"/>'
            + ('<rect x="290" y="690" width="500" height="100" fill="#c9a24a"/>'
               '<text x="540" y="760" font-family="DejaVu Sans" font-weight="bold" font-size="50" fill="#2a1f16" text-anchor="middle">POLIDEPORTIVO</text>' if sign else "")
            + '<rect x="400" y="980" width="280" height="540" fill="#2a2a20"/>'
            + ('<rect x="400" y="980" width="280" height="540" fill="#fff3d1" opacity="0.16"/>' if door_lit else "")
            + '<path d="M 540 980 L 540 1520" stroke="#0b0f1c" stroke-width="8"/>'
            '<rect y="1500" width="1080" height="420" fill="#0d0f16"/><rect y="1500" width="1080" height="14" fill="#2a2e3a"/>')


def queue_poli():
    """La cola de familias sale del polideportivo y llega a la calle."""
    ppl = ""
    pts = [(470 - k * 40, 1520 + k * 24) for k in range(4)] + [(330 + k * 70, 1640 + k * 20) for k in range(10)]
    for k, (x, y) in enumerate(pts):
        s = min(1.2, 0.55 + k * 0.05)
        ppl += (f'<g transform="translate({x} {y}) scale({s:.2f})"><circle cx="0" cy="-230" r="34" fill="#2a3150" stroke="#5a6690" stroke-width="4"/>'
                f'<path d="M -50 0 L -45 -180 C -40 -200, 40 -200, 45 -180 L 50 0 Z" fill="#2a3150" stroke="#5a6690" stroke-width="4"/>'
                + (f'<circle cx="38" cy="-150" r="8" fill="#fff"/><circle cx="38" cy="-150" r="44" fill="url(#glow)" opacity="0.6"/>' if k % 3 == 1 else "")
                + '</g>')
    return poli_facade() + ppl


def hand_megaphone(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M 0 -40 L 220 -120 L 220 120 L 0 40 Z" fill="#e8ecf2" stroke="#666" stroke-width="6"/>'
            '<rect x="-50" y="-36" width="60" height="72" rx="10" fill="#e10600"/>'
            '<rect x="-30" y="30" width="30" height="80" rx="8" fill="#333"/>'
            + "".join(f'<path d="M {250 + i*45} -110 Q {290 + i*45} 0 {250 + i*45} 110" stroke="#ff9500" stroke-width="10" fill="none" opacity="{0.9 - i*0.25:.2f}"/>'
                      for i in range(3)) + '</g>')


def dni_card(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<rect x="-150" y="-95" width="300" height="190" rx="18" fill="#cfe0f2" stroke="#7fa6cc" stroke-width="6"/>'
            '<rect x="-130" y="-60" width="90" height="120" rx="8" fill="#8fa3b8"/>'
            '<circle cx="-85" cy="-25" r="24" fill="#5a6d82"/><path d="M -125 55 C -120 15, -50 15, -45 55 Z" fill="#5a6d82"/>'
            '<text x="50" y="-40" font-family="DejaVu Sans" font-weight="bold" font-size="40" fill="#1d3f6b" text-anchor="middle">DNI</text>'
            + "".join(f'<rect x="-20" y="{yy}" width="{w}" height="12" rx="6" fill="#7fa6cc"/>' for yy, w in ((0, 150), (30, 120), (60, 140)))
            + '</g>')


def clipboard(x, y, s=1.0, highlight=True):
    """Lista del polideportivo: nombres en filas y, junto a uno, «Trasladado. 3:00» a boli."""
    rows = "".join(f'<rect x="-230" y="{-200 + i*90}" width="{w}" height="22" rx="10" fill="#9aa1ab"/>'
                   for i, w in enumerate((300, 260, 320, 240, 280, 300)))
    mark = ('<rect x="-250" y="20" width="500" height="70" fill="#ffd400" opacity="0.35"/>'
            '<text x="230" y="70" font-family="DejaVu Sans" font-style="italic" font-weight="bold" font-size="40" fill="#1f3a8a" text-anchor="end" transform="rotate(-4 230 60)">Trasladado. 3:00</text>') if highlight else ""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<rect x="-300" y="-380" width="600" height="760" rx="24" fill="#6b4a2a"/>'
            '<rect x="-270" y="-330" width="540" height="690" fill="#f4f1e8"/>'
            '<rect x="-90" y="-410" width="180" height="70" rx="14" fill="#9aa1ab" stroke="#5a606d" stroke-width="6"/>'
            + rows + mark + '</g>')


def back_blows_icon(x, y, s=1.0):
    """Golpes en la espalda: Hugo inclinado hacia delante y una mano abierta que golpea entre los omóplatos."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<g transform="rotate(60) scale(0.75) translate(-540 -1150)">' + hugo(540, 900, 1.0, mood="choke") + '</g>'
            '<g transform="translate(-60 -190) rotate(-30)">'
            '<path d="M 0 -20 L 0 -260" stroke="#2c3550" stroke-width="80" stroke-linecap="round"/>'
            '<ellipse cx="0" cy="0" rx="75" ry="55" fill="url(#skin)"/>'
            + "".join(f'<rect x="{-60 + i*30}" y="20" width="24" height="70" rx="12" fill="url(#skin)"/>' for i in range(4)) + '</g>'
            + "".join(f'<path d="M {dx} {dy} l {ex} {ey}" stroke="#ffd400" stroke-width="12" stroke-linecap="round"/>'
                      for dx, dy, ex, ey in ((-170, -110, -50, 10), (60, -150, 50, -20), (-20, -40, 20, 50))) + '</g>')


def no_voice(x, y, s=1.0):
    """Onda de voz tachada: no sale el sonido."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            + "".join(f'<path d="M {i*50} -60 Q {i*50 + 40} 0 {i*50} 60" stroke="#9fd4ff" stroke-width="12" fill="none" opacity="{0.9 - i*0.2:.2f}"/>' for i in range(4))
            + '<circle cx="80" cy="0" r="120" fill="none" stroke="#e10600" stroke-width="16"/>'
            '<path d="M -5 85 L 165 -85" stroke="#e10600" stroke-width="16"/></g>')


RED = lambda op: f'<rect width="1080" height="1920" fill="#e10600" opacity="{op}"/>'
DARK = lambda c: f'<rect width="1080" height="1920" fill="{c}"/>'

scenes = {
    # apertura B: zumo y caramelos; Luis vuelve
    "01_zumo": svg(STAIRS_LUIS + BEAM_ON(540, 1000) + luis(540, 880, 0.85, mood="worry", box=False) + sweat(540, 780, 0.85) +
                   '<path d="M 1080 1350 C 900 1300, 820 1280, 760 1250" stroke="#2c3550" stroke-width="80" fill="none" stroke-linecap="round"/>' +
                   sugar_aid(720, 1150, 0.8)),
    "02_quince_min": svg(STAIRS_LUIS + BEAM_ON(540, 1000) + wall_clock(0, 15, 820, 520, 160) +
                         luis(420, 1000, 0.8, mood="worry", box=False) + candy(760, 1620, 1.1) + candy(880, 1660, 1.0, "#f2c200")),
    "03_que_hago": svg(DARK("#0c1020") + BEAM_ON(540, 900) +
                       '<g transform="translate(540 1050) scale(1.6) translate(-540 -900)">' + luis_calm() + '</g>'),
    "04_ha_vuelto": svg(STAIRS_LUIS + BEAM_ON(540, 900) + luis(380, 1000, 0.8, mood="talk", box=False) +
                        mujer_luis(760, 980, 0.8, point=False)),
    # vas al polideportivo, con Hugo
    "05_salis": svg(poli_facade(door_lit=False) + '<rect width="1080" height="1920" fill="#000" opacity="0.25"/>' +
                    phone_hand(40, 1700, rot=-12) + BEAM_ON(600, 1200) +
                    '<g transform="translate(840 1580) scale(0.6) translate(-540 -900)">' + hugo(540, 900, 1.0, mood="ok") + '</g>'),
    "06_hugo_caramelos": svg(wallpaper("#14182a", "#10142a") + BEAM_ON(540, 1000) + hugo(540, 950, 1.1, mood="ok") +
                             candy(430, 1420, 0.9) + candy(560, 1470, 0.8, "#f2c200") +
                             '<rect x="360" y="1440" width="180" height="110" rx="20" fill="#d1ab27" stroke="#a8861c" stroke-width="6"/>'),
    "07_cola_calle": svg(queue_poli()),
    "08_megafono": svg(poli_facade() + voluntario(380, 1040, 0.85, mood="shout") + hand_megaphone(560, 1020, 1.0) +
                       dni_card(820, 1700, 0.9)),
    "09_hora90": svg(poli_facade() + '<rect width="1080" height="1920" fill="#000" opacity="0.35"/>' + wall_clock(6, 0, 540, 900, 300)),
    # Hugo se atraganta
    "10_hugo_rie": svg(queue_poli() + '<rect width="1080" height="1920" fill="#000" opacity="0.4"/>' + BEAM_ON(540, 1000) +
                       hugo(540, 1000, 1.15, mood="laugh") + candy(330, 1410, 0.8)),
    "11_se_calla": svg(DARK("#0c1020") + BEAM_ON(540, 900) +
                       '<g transform="translate(540 1150) scale(1.8) translate(-540 -900)">' + hugo(540, 900, 1.0, mood="choke") + '</g>'),
    "12_manos_cuello": svg(DARK("#120810") + BEAM_ON(540, 900) + hugo(540, 900, 1.25, mood="choke", hands_neck=True) + RED(0.1)),
    "13_no_voz": svg(DARK("#0c1020") + '<g transform="translate(400 1100) scale(1.5) translate(-540 -900)">' +
                     hugo(540, 900, 1.0, mood="choke", hands_neck=True) + '</g>' + no_voice(790, 620, 1.0)),
    "14_morado": svg(DARK("#140818") + '<g transform="translate(540 1300) scale(2.4) translate(-540 -900)">' +
                     hugo(540, 900, 1.0, mood="choke", hands_neck=True) + '</g>' +
                     '<ellipse cx="540" cy="1300" rx="300" ry="320" fill="#6a3fa0" opacity="0.25"/>' + RED(0.12)),
    "15_senora": svg(queue_poli() + '<rect width="1080" height="1920" fill="#000" opacity="0.35"/>' +
                     senora_cola(720, 1000, 0.9, mood="shout") +
                     '<g transform="translate(260 1380) scale(0.55) translate(-540 -900)">' + hugo(540, 900, 1.0, mood="choke", hands_neck=True) + '</g>'),
    "16_dale_agua": svg(DARK("#14100c") + BEAM_ON(540, 900) + senora_cola(500, 1050, 1.3, mood="shout")),
    # decisión
    "17_decision": svg('<rect width="540" height="1920" fill="#0e1424"/><rect x="540" width="540" height="1920" fill="#14100c"/>' +
                       '<g transform="translate(270 900) scale(1.5)">' +
                       '<rect x="-50" y="-150" width="100" height="290" rx="22" fill="#bfe6ff" fill-opacity="0.75" stroke="#7fb3d9" stroke-width="6"/>'
                       '<rect x="-25" y="-195" width="50" height="50" rx="8" fill="#1f6fbf"/><rect x="-50" y="-40" width="100" height="60" fill="#1f6fbf" opacity="0.8"/></g>' +
                       back_blows_icon(750, 1000, 0.95) + '<rect x="532" y="0" width="16" height="1280" fill="#e10600"/>'),
    # suspenso: la lista
    "18_lista": svg(GYM + LANTERN + voluntario(540, 980, 1.0, mood="serious") + clipboard(760, 1380, 0.55, highlight=False) + RED(0.08)),
    "19_lista_cerca": svg(DARK("#0c0f1c") + BEAM_ON(540, 900) + clipboard(540, 1050, 1.25, highlight=True)),
    "20_nadie": svg(GYM + '<rect width="1080" height="1920" fill="#000" opacity="0.4"/>' +
                    '<rect x="330" y="1180" width="420" height="90" rx="14" fill="#4a5a3a"/>'
                    '<rect x="345" y="1270" width="14" height="110" fill="#222"/><rect x="720" y="1270" width="14" height="110" fill="#222"/>'
                    '<rect x="360" y="1150" width="140" height="50" rx="20" fill="#d9d4c4"/>' + RED(0.1)),
    "21_final": svg(poli_facade(door_lit=False) + '<rect width="1080" height="1920" fill="#000" opacity="0.45"/>' + RED(0.1)),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
