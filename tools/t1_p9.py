"""Escenas de la Parte 09 · El agua (rama B ganadora en la 08: le vigilas y le despiertas cada pocas horas)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import *
from draw2 import wallpaper, floor_tiles, street, hallway_door
from draw3 import wall_clock
from draw4 import hugo, cunado
from draw5 import tap
from draw6 import bathtub, camping_stove

OUT = pathlib.Path(__file__).resolve().parent.parent / "t1" / "p9"

DARK_ROOM = wallpaper("#121626", "#0f1322") + floor_tiles(1500, "#17130f", "#120f0c")
KITCHEN = wallpaper("#151a24", "#11161f") + floor_tiles(1600, "#1d1914", "#17130f") + \
    ''.join(f'<rect x="{x}" y="380" width="200" height="260" rx="8" fill="#2a2f3a" stroke="#1a1e26" stroke-width="6"/>' for x in (60, 300, 780))
BATHROOM = ('<rect width="1080" height="1920" fill="#141a22"/>' +
            ''.join(f'<rect x="{x}" y="{y}" width="118" height="118" fill="#1b2430" stroke="#121820" stroke-width="4"/>'
                    for x in range(0, 1080, 120) for y in range(0, 1300, 120)) +
            floor_tiles(1300, "#1f1b17", "#191612"))
BEAM_ON = lambda x, y: f'<polygon points="0,1920 0,1600 {x-250},{y-300} {x+300},{y-250} 1080,1500 1080,1920" fill="url(#beam)" opacity="0.8"/>'
MORNING = ('<rect width="1080" height="1920" fill="#2b3550"/>'
           '<rect x="620" y="260" width="360" height="560" fill="#c9d8ef"/><rect x="620" y="260" width="360" height="560" fill="none" stroke="#3a3f55" stroke-width="20"/>'
           '<line x1="800" y1="260" x2="800" y2="820" stroke="#3a3f55" stroke-width="14"/>'
           '<polygon points="620,260 980,260 1080,1920 200,1920" fill="#fff6d8" opacity="0.10"/>')


def bump_hugo(cx, cy, s, mood="pain", hands_head=False):
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    return (hugo(cx, cy, s, mood=mood, hands_head=hands_head) +
            f'<g {t}><ellipse cx="575" cy="808" rx="38" ry="30" fill="#8a3a6a"/>'
            f'<ellipse cx="568" cy="800" rx="16" ry="10" fill="#c46a9a" opacity="0.7"/></g>')


def flashlight(x, y, rot=-30, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            '<rect x="-40" y="0" width="80" height="260" rx="20" fill="#2b2b30"/><rect x="-55" y="-60" width="110" height="80" rx="14" fill="#3a3a40"/>'
            '<ellipse cx="0" cy="-60" rx="55" ry="14" fill="#fff6d8"/>'
            '<ellipse cx="-10" cy="180" rx="70" ry="90" fill="url(#skin)"/></g>')


def hand_shoulder(x, y, s=1.0):
    """Tu mano (manga azul marino) entrando por la izquierda, sobre un hombro."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -700 220 C -420 160, -200 90, -40 40" stroke="#1c2a48" stroke-width="120" fill="none" stroke-linecap="round"/>'
            '<ellipse cx="10" cy="20" rx="90" ry="60" fill="url(#skin)"/>'
            + ''.join(f'<ellipse cx="{60+k*8}" cy="{-20+k*22}" rx="46" ry="18" fill="url(#skin)" transform="rotate(20 {60+k*8} {-20+k*22})"/>' for k in range(4)) +
            '</g>')


def bed_hugo(s=1.0, mood="sick"):
    return ('<g transform="translate(150 380)">' + bed(0, 760) + '</g>'
            + bump_hugo(400, 1090, 0.62, mood=mood) +
            '<g transform="translate(150 380)">' + blanket(0, 1150) + '</g>')


def glass(x, y, s=1.0, fill=0.0, dirty=False, tilt=0):
    lvl = int(220 * fill)
    col = "#9fb8a0" if dirty else "#9fd4ff"
    w = (f'<path d="M -78 {150-lvl} L 78 {150-lvl} L 70 150 L -70 150 Z" fill="{col}" opacity="0.7"/>' if fill else "")
    specks = ''.join(f'<circle cx="{-40+(k*29)%80}" cy="{150-lvl+20+(k*17)%(max(lvl-30,10))}" r="5" fill="#5a6a40" opacity="0.8"/>' for k in range(7)) if dirty and fill else ""
    return (f'<g transform="translate({x} {y}) rotate({tilt}) scale({s})">{w}{specks}'
            '<path d="M -90 -90 L 90 -90 L 72 160 L -72 160 Z" fill="#dfefff" fill-opacity="0.12" stroke="#e8f4ff" stroke-width="8"/>'
            '<path d="M -60 -70 L -48 130" stroke="#fff" stroke-width="8" opacity="0.4"/></g>')


def bleach(x, y, s=1.0, rot=0):
    """Botella de lejía blanca con tapón azul y etiqueta roja «LEJÍA»."""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            '<path d="M -110 -160 C -110 -240, -40 -260, -30 -320 L 30 -320 C 40 -260, 110 -240, 110 -160 L 110 260 C 110 290, 90 310, 60 310 L -60 310 C -90 310, -110 290, -110 260 Z" fill="#f2f4f6" stroke="#c8ced6" stroke-width="6"/>'
            '<rect x="-38" y="-380" width="76" height="66" rx="10" fill="#1f6fd1"/>'
            '<path d="M 60 -160 C 150 -150, 150 -20, 60 -10" stroke="#e6eaee" stroke-width="30" fill="none"/>'
            '<rect x="-95" y="-20" width="190" height="200" rx="14" fill="#e10600"/>'
            '<text x="0" y="70" font-family="DejaVu Sans" font-weight="bold" font-size="56" fill="#fff" text-anchor="middle">LEJÍA</text>'
            '<path d="M -50 115 l 30 -45 l 30 45 z" fill="#fff"/></g>')


def pot_boiling(x, y, s=1.0):
    bubbles = ''.join(f'<circle cx="{-150+k*50}" cy="{-210+(k%3)*8}" r="{10+(k%2)*6}" fill="#cfeaff"/>' for k in range(7))
    steam = ''.join(f'<path d="M {px} -260 C {px-30} -340, {px+30} -400, {px} -480" stroke="#e6edf5" stroke-width="16" fill="none" opacity="0.45"/>' for px in (-100, 0, 100))
    return (f'<g transform="translate({x} {y}) scale({s})">' + steam +
            '<path d="M -200 -230 L 200 -230 L 180 -20 C 175 10, 150 20, 120 20 L -120 20 C -150 20, -175 10, -180 -20 Z" fill="#8f969f"/>'
            '<ellipse cx="0" cy="-230" rx="200" ry="34" fill="#6fb6e8"/>' + bubbles +
            '<rect x="-270" y="-220" width="80" height="26" rx="12" fill="#3a3f48"/><rect x="190" y="-220" width="80" height="26" rx="12" fill="#3a3f48"/>'
            + ''.join(f'<path d="M {fx} 40 C {fx-18} 0, {fx+6} -20, {fx} -40 C {fx+18} -10, {fx+14} 20, {fx} 40 Z" fill="#4da3ff"/>' for fx in (-90, -30, 30, 90)) +
            '</g>')


def school():
    """Colegio a oscuras con furgoneta de Protección Civil y palés de garrafas."""
    return ('<rect width="1080" height="1100" fill="url(#moonsky)"/>'
            '<rect x="60" y="560" width="960" height="900" fill="#1a2030" stroke="#0e121c" stroke-width="10"/>'
            + ''.join(f'<rect x="{x}" y="{y}" width="110" height="140" fill="#0f1422"/>' for x in range(110, 980, 170) for y in (640, 860))
            + '<rect x="380" y="400" width="320" height="110" fill="#c9a24a"/>'
            '<text x="540" y="478" font-family="DejaVu Sans" font-weight="bold" font-size="56" fill="#2a1f16" text-anchor="middle">COLEGIO</text>'
            '<rect x="0" y="1460" width="1080" height="460" fill="#0d0f16"/>'
            # furgoneta Protección Civil
            '<g transform="translate(300 1560)"><rect x="-260" y="-300" width="440" height="270" rx="20" fill="#f2f4f6"/>'
            '<path d="M 180 -250 L 270 -250 L 310 -150 L 310 -30 L 180 -30 Z" fill="#e6e9ee"/><path d="M 190 -235 L 260 -235 L 295 -160 L 190 -160 Z" fill="#1a2a44"/>'
            '<rect x="-260" y="-150" width="570" height="34" fill="#ff8a00"/><rect x="-260" y="-116" width="570" height="20" fill="#1f4fbf"/>'
            '<path d="M -40 -270 L 30 -230 L -40 -190 L -110 -230 Z" fill="#ff8a00" stroke="#1f4fbf" stroke-width="8"/>'
            '<circle cx="-160" cy="-24" r="48" fill="#111"/><circle cx="220" cy="-24" r="48" fill="#111"/>'
            '<rect x="-40" y="-330" width="110" height="30" rx="8" fill="#ff8a00"/>'
            '<ellipse cx="15" cy="-320" rx="260" ry="90" fill="#ff8a00" opacity="0.3" filter="url(#blur6)"/></g>'
            # palé de garrafas
            '<g transform="translate(780 1600)"><rect x="-200" y="0" width="400" height="40" fill="#5a4026"/>'
            + ''.join(f'<rect x="{-190+i*95}" y="{-150-j*150}" width="85" height="145" rx="16" fill="#9fd4ff" opacity="0.75" stroke="#dfefff" stroke-width="4"/>'
                      f'<rect x="{-165+i*95}" y="{-175-j*150}" width="35" height="28" rx="6" fill="#1f6fd1"/>' for i in range(4) for j in range(2)) +
            '</g>')


def queue():
    """Cola larguísima de siluetas con linternas que dobla la esquina."""
    ppl = ""
    pts = [(1000 - k * 62, 1760 - k * 22) for k in range(14)] + [(150 - k * 4, 1450 - k * 75) for k in range(1, 9)]
    for k, (x, y) in reversed(list(enumerate(pts))):
        s = max(0.3, 1.05 - k * 0.04)
        ppl += (f'<g transform="translate({x} {y}) scale({s:.2f})"><circle cx="0" cy="-230" r="34" fill="#2a3150" stroke="#5a6690" stroke-width="4"/>'
                f'<path d="M -50 0 L -45 -180 C -40 -200, 40 -200, 45 -180 L 50 0 Z" fill="#2a3150" stroke="#5a6690" stroke-width="4"/>'
                + (f'<rect x="40" y="-90" width="44" height="80" rx="10" fill="#9fd4ff" opacity="0.8"/>' if k % 3 == 0 else "")
                + (f'<circle cx="38" cy="-150" r="8" fill="#fff"/><circle cx="38" cy="-150" r="44" fill="url(#glow)" opacity="0.6"/>' if k % 3 == 1 else "")
                + '</g>')
    return ('<rect width="1080" height="1000" fill="url(#moonsky)"/>'
            + ''.join(f'<rect x="{x}" y="{1300-h}" width="{w}" height="{h}" fill="#0c1222" stroke="#070b16" stroke-width="4"/>'
                      for x, w, h in [(260, 280, 950), (560, 540, 1100)])
            + '<rect y="1300" width="1080" height="620" fill="#0d0f16"/>'
            '<rect x="0" y="0" width="230" height="1300" fill="#0b0f1c"/>'
            '<rect x="700" y="1000" width="300" height="90" fill="#c9a24a"/>'
            '<text x="850" y="1062" font-family="DejaVu Sans" font-weight="bold" font-size="46" fill="#2a1f16" text-anchor="middle">COLEGIO</text>'
            + ppl)


def door_dark(knock=True):
    return (hallway_door(label="3ºB", knock=knock) + '<rect width="1080" height="1920" fill="#200404" opacity="0.45"/>')


def peephole():
    """Visto por la mirilla: rellano negro y una silueta borrosa."""
    return ('<rect width="1080" height="1920" fill="#000"/>'
            '<clipPath id="eye"><circle cx="540" cy="900" r="420"/></clipPath>'
            '<g clip-path="url(#eye)"><rect width="1080" height="1920" fill="#0a0d18"/>'
            '<ellipse cx="540" cy="900" rx="420" ry="420" fill="#1a2238"/>'
            '<g filter="url(#blur6)" transform="translate(540 1300) scale(1.4)"><circle cx="0" cy="-330" r="80" fill="#020308"/>'
            '<path d="M -150 120 L -130 -220 C -110 -260, 110 -260, 130 -220 L 150 120 Z" fill="#020308"/></g>'
            '<rect width="1080" height="1920" fill="#ff3b30" opacity="0.06"/></g>'
            '<circle cx="540" cy="900" r="420" fill="none" stroke="#111" stroke-width="40"/>'
            '<circle cx="540" cy="900" r="420" fill="url(#vig)"/>')


scenes = {
    # apertura B: le vigilas
    "01_vigilas": svg(DARK_ROOM + bed_hugo(mood="sick") + wall_clock(3, 0, 880, 840, 110) +
                      flashlight(900, 1560, rot=-35) + '<polygon points="900,1500 820,1480 300,1000 560,880" fill="url(#beam)" opacity="0.55"/>'),
    "02_despiertas": svg(DARK_ROOM + BEAM_ON(540, 950) + bump_hugo(560, 1050, 1.05, mood="sick") + hand_shoulder(470, 1350, 1.0)),
    "03_como_te_llamas": svg('<rect width="1080" height="1920" fill="#0e0a0c"/>' + BEAM_ON(540, 900) +
                             bump_hugo(540, 1150, 1.6, mood="pain")),
    "04_responde_bien": svg(DARK_ROOM + bed_hugo(mood="ok") + wall_clock(6, 0, 880, 840, 110) +
                            '<rect width="1080" height="1920" fill="#3fd27a" opacity="0.04"/>'),
    "05_manana": svg(MORNING + floor_tiles(1600, "#3a3128", "#332a22") + bump_hugo(470, 1120, 0.95, mood="ok")),
    # hora 76: no hay agua
    "06_hora76": svg(KITCHEN + wall_clock(4, 0, 540, 900, 260) + '<rect width="1080" height="1920" fill="#000" opacity="0.25"/>'),
    "07_grifo_seco": svg(KITCHEN + tap(540, 620, drip=False) + BEAM_ON(540, 800) +
                         '<g transform="translate(560 360)"><ellipse cx="0" cy="0" rx="70" ry="44" fill="url(#skin)"/>'
                         '<path d="M 60 -10 C 200 -60, 360 -80, 560 -120" stroke="#1c2a48" stroke-width="110" fill="none" stroke-linecap="round"/></g>'),
    "08_colegio": svg(school()),
    "09_cola": svg(queue()),
    # la bañera
    "10_vaso_banera": svg(BATHROOM + BEAM_ON(540, 1100) + cunado(700, 820, 0.75, mood="happy") +
                          bathtub(540, 1450, fill=0.75, running=False) + glass(350, 1050, 0.9, fill=0.6, dirty=True, tilt=-8)),
    "11_ramon_hornillo": svg(wallpaper("#10142a", "#0d1124") + floor_tiles(1500, "#1c1813", "#16120e") +
                             '<path d="M 80 1500 L 80 700 M 80 700 L 1000 700" stroke="#3a1414" stroke-width="22"/>' +
                             BEAM_ON(540, 950) + don_ramon(540, 860, 0.95, mood="shout", radio_hand=False) +
                             camping_stove(660, 1740, 0.7, low=True)),
    "12_tia_lejia": svg(KITCHEN + '<rect x="560" y="700" width="460" height="760" fill="#2a1f16" stroke="#17110c" stroke-width="14"/>'
                        '<rect x="585" y="725" width="410" height="710" fill="#0d0a08"/><line x1="585" y1="1080" x2="995" y2="1080" stroke="#3a2d22" stroke-width="12"/>'
                        + BEAM_ON(600, 900) + tia(380, 880, 0.8, mood="worry") + bleach(780, 1250, 0.75, rot=6)),
    "13_hugo_sed": svg(KITCHEN + BEAM_ON(540, 1000) + bump_hugo(540, 1000, 0.95, mood="sick") + glass(780, 1380, 1.0, fill=0.0)),
    "14_tu_sed": svg('<rect width="1080" height="1920" fill="#0b0d14"/>' + BEAM_ON(540, 900) +
                     '<g transform="translate(540 1100) rotate(-20)"><rect x="-90" y="-320" width="180" height="560" rx="40" fill="#cfe7ff" fill-opacity="0.15" stroke="#e8f4ff" stroke-width="10"/>'
                     '<rect x="-40" y="-380" width="80" height="70" rx="10" fill="#1f6fd1"/>'
                     '<path d="M -90 200 L 90 200 L 90 230 C 90 240, -90 240, -90 230 Z" fill="#9fd4ff" opacity="0.6"/></g>'
                     '<g transform="translate(560 1300)"><ellipse cx="0" cy="0" rx="120" ry="80" fill="url(#skin)"/>'
                     '<path d="M -60 60 C -200 200, -300 400, -360 700" stroke="#1c2a48" stroke-width="140" fill="none" stroke-linecap="round"/></g>'),
    # decisión: bañera tal cual / hervir o lejía
    "15_decision": svg('<rect width="540" height="1920" fill="#0a0c16"/><rect x="540" width="540" height="1920" fill="#14100c"/>'
                       '<g transform="translate(270 1200) scale(0.5) translate(-540 -1250)">' + bathtub(540, 1250, fill=0.75, running=False) + '</g>'
                       + glass(270, 820, 1.0, fill=0.6, dirty=True) +
                       pot_boiling(810, 820, 0.95) + camping_stove(810, 1180, 0.55, low=False) + bleach(960, 1290, 0.32) +
                       '<rect x="532" y="0" width="16" height="1920" fill="#e10600"/>'),
    # suspenso
    "16_llaman": svg(door_dark(knock=True)),
    "17_nadie": svg(peephole()),
    "18_final": svg(door_dark(knock=False) + '<rect width="1080" height="1920" fill="#000" opacity="0.35"/>'),
}

if __name__ == "__main__":
    for name, s in scenes.items():
        print(render(s, OUT / f"{name}.png"))
