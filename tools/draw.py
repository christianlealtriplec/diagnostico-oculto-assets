"""Biblioteca de dibujo de Diagnóstico Oculto · 72 horas sin luz.

Personajes y escenarios reutilizables en SVG (1080x1920). Cada escena es una
función que devuelve el SVG completo; render() lo pasa a PNG con rsvg-convert.
"""
import subprocess, pathlib

W, H = 1080, 1920
PAL = dict(night0="#070b17", night1="#141b31", moon="#3d5d92", moon2="#1b2946",
           skin="#e7c09c", skin_d="#b98a66", skin_l="#f6dcc2", hair="#eef0f5",
           red="#e10600", red_d="#8f1414", grey="#5a606d", grey_d="#41454f",
           tube="#bfe6ff", lamp="#fff3d1")

DEFS = f"""
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{PAL['night0']}"/><stop offset="1" stop-color="{PAL['night1']}"/></linearGradient>
 <linearGradient id="moonsky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{PAL['moon']}"/><stop offset="1" stop-color="{PAL['moon2']}"/></linearGradient>
 <radialGradient id="beam" cx="0.1" cy="1" r="1">
  <stop offset="0" stop-color="{PAL['lamp']}" stop-opacity="0.6"/>
  <stop offset="0.55" stop-color="{PAL['lamp']}" stop-opacity="0.16"/>
  <stop offset="1" stop-color="{PAL['lamp']}" stop-opacity="0"/></radialGradient>
 <radialGradient id="skin" cx="0.38" cy="0.35" r="0.85">
  <stop offset="0" stop-color="{PAL['skin_l']}"/><stop offset="0.6" stop-color="{PAL['skin']}"/>
  <stop offset="1" stop-color="{PAL['skin_d']}"/></radialGradient>
 <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <radialGradient id="vig" cx="0.5" cy="0.5" r="0.75">
  <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.75"/></radialGradient>
 <filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
 <filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
</defs>"""


def svg(body, ui=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'{DEFS}<rect width="{W}" height="{H}" fill="url(#bg)"/>{body}'
            f'<rect width="{W}" height="{H}" fill="url(#vig)"/>{ui}</svg>')


def render(svg_text, out_png):
    out = pathlib.Path(out_png)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".svg")
    tmp.write_text(svg_text, encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), str(tmp), "-o", str(out)], check=True)
    tmp.unlink()
    return out

# ---------- piezas ----------

def window(x=690, y=330, w=300, h=470, lit_windows=()):
    city = (f'<polygon points="{x+10},{y+h} {x+10},{y+h-100} {x+50},{y+h-100} {x+50},{y+h-150} {x+100},{y+h-150} '
            f'{x+100},{y+h-80} {x+140},{y+h-80} {x+140},{y+h}" fill="#0c1324"/>'
            f'<polygon points="{x+160},{y+h} {x+160},{y+h-110} {x+210},{y+h-110} {x+210},{y+h-190} {x+260},{y+h-190} {x+260},{y+h}" fill="#0c1324"/>')
    lit = "".join(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{PAL["lamp"]}"/>'
                  f'<circle cx="{cx}" cy="{cy}" r="22" fill="url(#glow)" opacity="0.5"/>' for cx, cy in lit_windows)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#moonsky)"/>'
            f'<circle cx="{x+w-60}" cy="{y+70}" r="26" fill="#d6e4ff"/>'
            f'<circle cx="{x+w-60}" cy="{y+70}" r="70" fill="url(#glow)" opacity="0.35"/>{city}{lit}'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#04060d" stroke-width="18"/>'
            f'<line x1="{x+w/2}" y1="{y}" x2="{x+w/2}" y2="{y+h}" stroke="#04060d" stroke-width="12"/>'
            f'<line x1="{x}" y1="{y+h/2}" x2="{x+w}" y2="{y+h/2}" stroke="#04060d" stroke-width="12"/>'
            f'<polygon points="{x},{y+h} {x+w},{y+h} {x+w+120},{y+h+460} {x-140},{y+h+460}" fill="{PAL["moon"]}" opacity="0.13"/>')


def beam(x0=140, y0=1640, x1=620, y1=640, x2=1040, y2=980):
    return f'<polygon points="{x0},{y0} {x0-40},{y0-120} {x1},{y1} {x2},{y2}" fill="url(#beam)"/>'


def phone_hand(x=60, y=1560, rot=-18, screen=False):
    scr = (f'<rect x="{x+38}" y="{y+22}" width="104" height="200" rx="12" fill="#7aa7ff" opacity="0.85"/>'
           f'<text x="{x+90}" y="{y+130}" font-family="DejaVu Sans" font-weight="bold" font-size="17" fill="#fff" text-anchor="middle">Sin servicio</text>') if screen else ""
    return (f'<g transform="rotate({rot} {x+90} {y+125})">'
            f'<path d="M {x-20} {y+360} L {x} {y+130} C {x+10} {y+80}, {x+80} {y+60}, {x+130} {y+90} L {x+170} {y+360} Z" fill="{PAL["skin_d"]}"/>'
            f'<rect x="{x+25}" y="{y}" width="130" height="245" rx="22" fill="#0e0e10" stroke="#2a2a30" stroke-width="4"/>{scr}'
            f'<circle cx="{x+55}" cy="{y+28}" r="10" fill="#fff"/><circle cx="{x+55}" cy="{y+28}" r="40" fill="url(#glow)" opacity="0.9"/>'
            f'<ellipse cx="{x+160}" cy="{y+90}" rx="32" ry="19" fill="{PAL["skin"]}"/>'
            f'<ellipse cx="{x+166}" cy="{y+140}" rx="32" ry="19" fill="{PAL["skin_d"]}"/></g>')


def abuela(cx=362, cy=850, s=1.0, mood="ahogo", cannula=True, lips="#8a8f9c"):
    """Abuela Carmen: 80 años, pelo blanco corto, rebeca gris, gafas nasales."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate({-362} {-850})"'
    mouth = ('<ellipse cx="365" cy="932" rx="24" ry="18" fill="#2a1d1a" stroke="{l}" stroke-width="7"/>' if mood == "ahogo"
             else '<path d="M 342 930 Q 365 948 388 930" stroke="{l}" stroke-width="7" fill="none" stroke-linecap="round"/>').format(l=lips)
    eyes = ('<path d="M 316 838 Q 333 848 352 838" stroke="#3b2d26" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '<path d="M 378 838 Q 396 848 414 838" stroke="#3b2d26" stroke-width="6" fill="none" stroke-linecap="round"/>') if mood == "ahogo" else (
            '<ellipse cx="334" cy="840" rx="9" ry="10" fill="#3b2d26"/><ellipse cx="396" cy="840" rx="9" ry="10" fill="#3b2d26"/>'
            '<circle cx="337" cy="837" r="3" fill="#fff"/><circle cx="399" cy="837" r="3" fill="#fff"/>')
    can = ('<path d="M 298 906 C 330 896, 346 893, 362 896 C 378 893, 396 896, 428 906" fill="none" stroke="{t}" stroke-width="7"/>'
           '<circle cx="353" cy="893" r="6" fill="#e3f6ff"/><circle cx="373" cy="893" r="6" fill="#e3f6ff"/>'
           '<path d="M 298 906 C 266 900, 258 868, 266 846" fill="none" stroke="{t}" stroke-width="6"/>'
           '<path d="M 428 906 C 460 900, 466 868, 460 846" fill="none" stroke="{t}" stroke-width="6"/>').format(t=PAL["tube"]) if cannula else ""
    return (f'<g {t}>'
            f'<path d="M 200 1250 C 205 1070, 280 1000, 362 992 C 450 1000, 522 1070, 530 1250 Z" fill="{PAL["grey"]}"/>'
            f'<path d="M 362 996 L 340 1250 L 385 1250 Z" fill="{PAL["grey_d"]}"/>'
            f'<path d="M 230 1100 C 260 1060, 300 1050, 330 1060" stroke="{PAL["grey_d"]}" stroke-width="10" fill="none"/>'
            f'<ellipse cx="395" cy="1110" rx="50" ry="35" fill="url(#skin)"/>'
            f'<rect x="334" y="905" width="58" height="85" fill="{PAL["skin_d"]}"/>'
            f'<ellipse cx="362" cy="850" rx="106" ry="126" fill="url(#skin)"/>'
            f'<ellipse cx="300" cy="900" rx="26" ry="14" fill="#d98c7a" opacity="0.35"/>'
            f'<ellipse cx="425" cy="900" rx="26" ry="14" fill="#d98c7a" opacity="0.35"/>'
            f'<path d="M 300 880 Q 310 905 330 912" stroke="{PAL["skin_d"]}" stroke-width="4" fill="none" opacity="0.7"/>'
            f'<path d="M 424 880 Q 414 905 396 912" stroke="{PAL["skin_d"]}" stroke-width="4" fill="none" opacity="0.7"/>'
            f'<path d="M 258 845 C 236 742, 300 686, 365 686 C 444 686, 494 742, 472 845 C 462 794, 432 762, 402 772 C 372 742, 320 747, 300 782 C 284 792, 268 818, 258 845 Z" fill="{PAL["hair"]}"/>'
            f'<path d="M 300 712 C 330 700, 380 698, 420 712" stroke="#cfd3dd" stroke-width="5" fill="none"/>'
            f'<circle cx="266" cy="862" r="23" fill="#dfe2ea"/><circle cx="460" cy="857" r="23" fill="#dfe2ea"/>'
            f'<path d="M 310 812 Q 330 796 354 807" stroke="#7d6b5f" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M 376 807 Q 398 794 420 809" stroke="#7d6b5f" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'{eyes}<path d="M 362 850 Q 351 881 369 889" stroke="{PAL["skin_d"]}" stroke-width="5" fill="none"/>'
            f'{can}{mouth}</g>')


def bed(x=90, y=760):
    return (f'<rect x="{x+30}" y="{y}" width="620" height="260" rx="30" fill="#2a2018"/>'
            f'<rect x="{x+50}" y="{y+20}" width="580" height="220" rx="22" fill="none" stroke="#3a2d22" stroke-width="6"/>'
            f'<rect x="{x}" y="{y+250}" width="700" height="140" rx="20" fill="#d9d4cc"/>'
            f'<ellipse cx="{x+240}" cy="{y+220}" rx="215" ry="92" fill="#ece8e1"/>')


def blanket(x=90, y=1150):
    return (f'<path d="M {x} {y} C {x+110} {y-40}, {x+510} {y-40}, {x+700} {y} L {x+700} {y+180} L {x} {y+180} Z" fill="{PAL["red_d"]}"/>'
            f'<path d="M {x} {y} C {x+110} {y-40}, {x+510} {y-40}, {x+700} {y}" stroke="#c42a2a" stroke-width="10" fill="none"/>'
            f'<path d="M {x+180} {y+40} C {x+260} {y+80}, {x+300} {y+120}, {x+320} {y+180}" stroke="#6e0f0f" stroke-width="8" fill="none"/>'
            f'<rect x="{x}" y="{y+180}" width="700" height="60" fill="#3a2a20"/>')


def concentrator(x=800, y=1080, s=1.0, off=True):
    disp = "OFF" if off else "2 L/min"
    col = "#4b5263" if off else "#5cff9a"
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect width="190" height="300" rx="28" fill="#c9ccd2"/><rect x="0" y="230" width="190" height="70" rx="20" fill="#b3b7bf"/>'
            f'<rect x="30" y="40" width="130" height="70" rx="10" fill="#1b2030"/>'
            f'<text x="95" y="86" font-family="DejaVu Sans Mono" font-weight="bold" font-size="26" fill="{col}" text-anchor="middle">{disp}</text>'
            f'<circle cx="50" cy="150" r="12" fill="#3a3f4a"/><circle cx="90" cy="150" r="12" fill="#3a3f4a"/>'
            f'<rect x="30" y="200" width="130" height="14" rx="7" fill="#9ea3ab"/>'
            f'<path d="M 140 300 C 150 340, 200 330, 230 360" stroke="#1a1a1a" stroke-width="8" fill="none"/></g>')


def tube(d):
    return f'<path d="{d}" fill="none" stroke="{PAL["tube"]}" stroke-width="7" opacity="0.9"/>'


def tio(cx=540, cy=900, s=1.0):
    """Tío: 50 años, calvo con barba, polo azul, gritando y señalando."""
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    return (f'<g {t}>'
            f'<path d="M 360 1500 C 360 1180, 430 1070, 540 1060 C 650 1070, 720 1180, 720 1500 Z" fill="#2f4f86"/>'
            f'<path d="M 690 1150 C 800 1080, 880 980, 930 880" stroke="#2f4f86" stroke-width="80" fill="none" stroke-linecap="round"/>'
            f'<circle cx="935" cy="870" r="42" fill="url(#skin)"/><path d="M 950 860 L 1010 800" stroke="{PAL["skin"]}" stroke-width="24" stroke-linecap="round"/>'
            f'<rect x="505" y="960" width="70" height="110" fill="{PAL["skin_d"]}"/>'
            f'<ellipse cx="540" cy="880" rx="120" ry="140" fill="url(#skin)"/>'
            f'<path d="M 425 900 C 430 1010, 480 1040, 540 1045 C 600 1040, 650 1010, 655 900 C 630 960, 600 975, 540 975 C 480 975, 450 960, 425 900 Z" fill="#4a3a33"/>'
            f'<ellipse cx="540" cy="955" rx="40" ry="34" fill="#260f0c"/><rect x="515" y="928" width="50" height="10" fill="#f2f2f2"/>'
            f'<path d="M 465 815 L 520 835" stroke="#3a2c25" stroke-width="12" stroke-linecap="round"/>'
            f'<path d="M 615 815 L 560 835" stroke="#3a2c25" stroke-width="12" stroke-linecap="round"/>'
            f'<ellipse cx="497" cy="855" rx="13" ry="15" fill="#fff"/><ellipse cx="583" cy="855" rx="13" ry="15" fill="#fff"/>'
            f'<circle cx="497" cy="857" r="7" fill="#222"/><circle cx="583" cy="857" r="7" fill="#222"/>'
            f'<ellipse cx="420" cy="885" rx="18" ry="30" fill="{PAL["skin_d"]}"/><ellipse cx="660" cy="885" rx="18" ry="30" fill="{PAL["skin_d"]}"/>'
            f'<path d="M 440 790 C 470 760, 610 760, 640 790" stroke="#f0d9c4" stroke-width="6" fill="none" opacity="0.6"/></g>')


def door(x=300, y=420, w=480, h=1180):
    return (f'<rect x="{x-30}" y="{y-30}" width="{w+60}" height="{h+30}" fill="#1b1612"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#0f1220"/>'
            f'<rect x="{x-30}" y="{y-30}" width="{w+60}" height="{h+30}" fill="none" stroke="#3a2d22" stroke-width="10"/>')


def oxygen_bottle(x=430, y=520, s=1.0, hand=True, open_=False):
    dial = "#3fd27a" if open_ else "#c9ccd2"
    h = (f'<path d="M 760 760 C 700 700, 640 690, 600 700 L 560 710 C 540 715, 535 740, 555 745 L 610 740" fill="{PAL["skin"]}" stroke="{PAL["skin_d"]}" stroke-width="4"/>'
         f'<path d="M 1080 900 C 950 860, 850 790, 760 760 L 820 840 C 900 880, 1000 930, 1080 960 Z" fill="#33363f"/>') if hand else ""
    return (f'<g transform="translate({x} {y}) scale({s}) translate(-430 -520)">'
            f'<rect x="300" y="600" width="260" height="1000" rx="110" fill="#2f6b4f"/>'
            f'<rect x="300" y="600" width="260" height="1000" rx="110" fill="url(#beam)" opacity="0.5"/>'
            f'<path d="M 330 680 C 330 640, 360 620, 380 620" stroke="#5fa784" stroke-width="16" fill="none"/>'
            f'<rect x="390" y="470" width="80" height="140" fill="#9aa0a8"/><rect x="370" y="440" width="120" height="50" rx="10" fill="#b8bdc4"/>'
            f'<circle cx="530" cy="465" r="48" fill="#e8e8e8" stroke="#555" stroke-width="6"/>'
            f'<path d="M 530 465 L 555 435" stroke="{PAL["red"]}" stroke-width="6"/>'
            f'<circle cx="430" cy="410" r="44" fill="{dial}" stroke="#555" stroke-width="6"/>'
            f'<rect x="330" y="900" width="200" height="120" rx="8" fill="#f2f2f2"/>'
            f'<text x="430" y="955" font-family="DejaVu Sans" font-weight="bold" font-size="40" fill="#2f6b4f" text-anchor="middle">O₂</text>'
            f'<text x="430" y="995" font-family="DejaVu Sans" font-size="22" fill="#333" text-anchor="middle">MEDICINAL</text>'
            f'{h}</g>')


def stairs():
    steps = "".join(f'<polygon points="{80+i*10},{1900-i*120} {1000-i*10},{1900-i*120} {980-i*10},{1840-i*120} {100+i*10},{1840-i*120}" fill="{c}"/>'
                    for i, c in enumerate(["#1d2235", "#181c2d", "#151927", "#121521", "#0f121c", "#0d0f18", "#0b0d14", "#090b11", "#08090e", "#06070b", "#05060a", "#040508", "#030406"]))
    rail = '<path d="M 120 1700 L 380 300" stroke="#3a1414" stroke-width="22"/><path d="M 960 1700 L 700 300" stroke="#3a1414" stroke-width="22"/>'
    fig = ('<path d="M 470 1150 C 470 1060, 520 1020, 560 1020 C 600 1020, 650 1060, 650 1150 L 640 1320 L 480 1320 Z" fill="#1e2c4f"/>'
           '<circle cx="560" cy="960" r="62" fill="#1a1a22"/><path d="M 500 1320 L 470 1460" stroke="#16203a" stroke-width="44" stroke-linecap="round"/>'
           '<path d="M 620 1320 L 660 1420" stroke="#16203a" stroke-width="44" stroke-linecap="round"/>')
    return steps + rail + fig + '<polygon points="140,1880 100,1760 470,700 820,760" fill="url(#beam)"/>'


def city_night():
    blds = ""
    import random
    rnd = random.Random(7)
    x = -20
    while x < W:
        bw = rnd.randint(110, 200); bh = rnd.randint(500, 1100)
        blds += f'<rect x="{x}" y="{1500-bh}" width="{bw}" height="{bh+500}" fill="#0b1122" stroke="#070b16" stroke-width="4"/>'
        for wy in range(1500 - bh + 40, 1480, 70):
            for wx in range(x + 18, x + bw - 30, 50):
                blds += f'<rect x="{wx}" y="{wy}" width="22" height="34" fill="#0f172c"/>'
        x += bw + 6
    lights = "".join(f'<circle cx="{a}" cy="{b}" r="6" fill="{PAL["lamp"]}"/><circle cx="{a}" cy="{b}" r="26" fill="url(#glow)" opacity="0.5"/>'
                     for a, b in [(160, 980), (520, 760), (840, 1120), (330, 1260)])
    return (f'<rect width="{W}" height="900" fill="url(#moonsky)"/>'
            f'<circle cx="820" cy="300" r="46" fill="#dbe7ff"/><circle cx="820" cy="300" r="140" fill="url(#glow)" opacity="0.3"/>{blds}{lights}')


def silhouette_window_person():
    return ('<path d="M 0 1920 L 0 1250 C 60 1150, 180 1120, 260 1140 C 330 1100, 360 1010, 330 930 C 300 850, 210 830, 150 870 C 90 910, 80 1000, 110 1060 C 60 1080, 20 1130, 0 1160 Z" fill="#05070d"/>'
            '<rect x="240" y="1180" width="110" height="200" rx="16" fill="#0e0e10" transform="rotate(-12 295 1280)"/>'
            '<rect x="252" y="1196" width="86" height="168" rx="10" fill="#7aa7ff" opacity="0.85" transform="rotate(-12 295 1280)"/>'
            '<ellipse cx="250" cy="1040" rx="80" ry="120" fill="#7aa7ff" opacity="0.22" filter="url(#blur6)"/>')

# ---------- UI ----------

def ui(clock=None, hook=None, sub=None, card=None):
    out = ""
    if clock:
        out += (f'<rect x="350" y="105" width="380" height="72" rx="12" fill="#000" fill-opacity="0.78"/>'
                f'<text x="540" y="155" font-family="DejaVu Sans Mono" font-weight="bold" font-size="38" fill="#ff3b30" text-anchor="middle">{clock}</text>')
    if hook:
        lines = hook.split("|")
        hh = 70 + 72 * len(lines)
        out += f'<rect x="60" y="215" width="960" height="{hh}" rx="14" fill="{PAL["red"]}" fill-opacity="0.95"/>'
        out += "".join(f'<text x="540" y="{295+72*i}" font-family="DejaVu Sans" font-weight="bold" font-size="54" fill="#fff" text-anchor="middle">{l}</text>' for i, l in enumerate(lines))
    if card:
        lines = card.split("|")
        hh = 60 + 66 * len(lines)
        out += f'<rect x="60" y="1340" width="960" height="{hh}" rx="14" fill="{PAL["red"]}" fill-opacity="0.95"/>'
        out += "".join(f'<text x="540" y="{1410+66*i}" font-family="DejaVu Sans" font-weight="bold" font-size="48" fill="#fff" text-anchor="middle">{l}</text>' for i, l in enumerate(lines))
    if sub:
        lines, cur = [], ""
        for w in sub.split():
            if cur and len(cur) + 1 + len(w) > 24:
                lines.append(cur); cur = w
            else:
                cur = f"{cur} {w}".strip()
        lines.append(cur)
        y0 = 1530 - 34 * (len(lines) - 1)
        out += "".join(f'<text x="540" y="{y0+68*i}" font-family="DejaVu Sans" font-weight="bold" font-size="56" fill="#fff" '
                       f'stroke="#000" stroke-width="10" paint-order="stroke" text-anchor="middle">{l}</text>' for i, l in enumerate(lines))
    return out


# ---------- familia (Capítulo 4 en adelante) ----------

def _woman(cx, cy, s, body, hair_back, hair_front, mood, extra="", glasses=False, earrings=None):
    t = f'transform="translate({cx} {cy}) scale({s}) translate(-540 -900)"'
    if mood == "shout":
        brows = ('<path d="M 470 805 L 520 822" stroke="#3a2c25" stroke-width="10" stroke-linecap="round"/>'
                 '<path d="M 610 805 L 560 822" stroke="#3a2c25" stroke-width="10" stroke-linecap="round"/>')
        mouth = '<ellipse cx="540" cy="958" rx="34" ry="28" fill="#2a1410"/><rect x="516" y="934" width="48" height="9" fill="#f2f2f2"/>'
    elif mood == "worry":
        brows = ('<path d="M 470 818 L 520 802" stroke="#3a2c25" stroke-width="9" stroke-linecap="round"/>'
                 '<path d="M 610 818 L 560 802" stroke="#3a2c25" stroke-width="9" stroke-linecap="round"/>')
        mouth = '<path d="M 508 962 Q 540 945 572 962" stroke="#8a3a32" stroke-width="8" fill="none" stroke-linecap="round"/>'
    else:
        brows = ('<path d="M 470 808 Q 495 798 520 808" stroke="#3a2c25" stroke-width="9" fill="none"/>'
                 '<path d="M 560 808 Q 585 798 610 808" stroke="#3a2c25" stroke-width="9" fill="none"/>')
        mouth = '<path d="M 510 955 Q 540 975 570 955" stroke="#8a3a32" stroke-width="8" fill="none" stroke-linecap="round"/>'
    gl = ('<rect x="465" y="832" width="66" height="52" rx="14" fill="#cfe3ff" fill-opacity="0.2" stroke="#4a2a5a" stroke-width="6"/>'
          '<rect x="549" y="832" width="66" height="52" rx="14" fill="#cfe3ff" fill-opacity="0.2" stroke="#4a2a5a" stroke-width="6"/>'
          '<line x1="531" y1="856" x2="549" y2="856" stroke="#4a2a5a" stroke-width="6"/>') if glasses else ""
    ear = (f'<circle cx="422" cy="935" r="12" fill="{earrings}"/><circle cx="658" cy="935" r="12" fill="{earrings}"/>') if earrings else ""
    return (f'<g {t}>{hair_back}'
            f'<path d="M 360 1560 C 360 1190, 440 1080, 540 1070 C 640 1080, 720 1190, 720 1560 Z" fill="{body}"/>'
            f'<rect x="510" y="965" width="60" height="110" fill="{PAL["skin_d"]}"/>'
            '<ellipse cx="540" cy="880" rx="108" ry="130" fill="url(#skin)"/>'
            '<ellipse cx="434" cy="895" rx="15" ry="26" fill="#b98a66"/><ellipse cx="646" cy="895" rx="15" ry="26" fill="#b98a66"/>'
            f'{ear}{hair_front}{brows}'
            '<ellipse cx="498" cy="858" rx="11" ry="13" fill="#2b211c"/><ellipse cx="582" cy="858" rx="11" ry="13" fill="#2b211c"/>'
            '<circle cx="501" cy="854" r="3.5" fill="#fff"/><circle cx="585" cy="854" r="3.5" fill="#fff"/>'
            f'{gl}<path d="M 540 868 Q 530 902 548 908" stroke="#b98a66" stroke-width="5" fill="none"/>'
            '<ellipse cx="478" cy="920" rx="20" ry="11" fill="#e08f80" opacity="0.35"/><ellipse cx="602" cy="920" rx="20" ry="11" fill="#e08f80" opacity="0.35"/>'
            f'{mouth}{extra}</g>')


def madre(cx=540, cy=900, s=1.0, mood="worry", hold=None):
    """Tu madre: 55 años, melena castaña con moño, gafas moradas, rebeca verde botella.
    hold: None | "hielo" (cuenco con hielo)."""
    back = '<ellipse cx="540" cy="700" rx="70" ry="60" fill="#5a3a22"/>'
    front = ('<path d="M 430 870 C 410 760, 470 735, 540 735 C 615 735, 672 760, 650 870 C 640 810, 600 790, 540 792 C 480 790, 440 810, 430 870 Z" fill="#6b4428"/>'
             '<path d="M 470 770 C 510 750, 570 750, 610 770" stroke="#8a5a36" stroke-width="6" fill="none"/>')
    body = "#1f5a46"
    extra = ('<path d="M 490 1072 L 540 1130 L 590 1072" fill="none" stroke="#e8e2d6" stroke-width="12"/>'
             + "".join(f'<circle cx="540" cy="{y}" r="8" fill="#e8e2d6"/>' for y in (1180, 1250, 1320, 1390)))
    if hold == "hielo":
        extra += ('<path d="M 390 1150 C 380 1250, 420 1300, 470 1300" stroke="#1f5a46" stroke-width="66" fill="none" stroke-linecap="round"/>'
                  '<path d="M 690 1150 C 700 1250, 660 1300, 610 1300" stroke="#1f5a46" stroke-width="66" fill="none" stroke-linecap="round"/>'
                  '<path d="M 400 1250 L 680 1250 C 670 1360, 620 1390, 540 1390 C 460 1390, 410 1360, 400 1250 Z" fill="#4a6fa5"/>'
                  + "".join(f'<rect x="{x}" y="{y}" width="56" height="56" rx="10" fill="#d8f2ff" opacity="0.92" transform="rotate({r} {x+28} {y+28})"/>'
                            for x, y, r in [(430, 1205, -12), (490, 1190, 8), (550, 1200, -5), (608, 1210, 15)]) +
                  '<ellipse cx="460" cy="1300" rx="34" ry="24" fill="url(#skin)"/><ellipse cx="620" cy="1300" rx="34" ry="24" fill="url(#skin)"/>')
    return _woman(cx, cy, s, body, back, front, mood, extra, glasses=True)


def tia(cx=540, cy=900, s=1.0, mood="shout", hold=None):
    """Tu tía: 50 años, pelo rizado pelirrojo, jersey morado, pendientes de aro dorados.
    hold: None | "pasta" (tubo de pasta de dientes)."""
    curls = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#b5471f"/>' for x, y, r in
                    [(420, 800, 46), (440, 730, 50), (500, 690, 52), (580, 690, 52), (640, 730, 50), (660, 800, 46),
                     (415, 880, 40), (665, 880, 40), (420, 950, 34), (660, 950, 34)])
    front = ('<path d="M 440 830 C 450 760, 500 740, 540 745 C 590 740, 635 760, 645 830 C 620 790, 580 780, 540 790 C 500 780, 460 790, 440 830 Z" fill="#c95427"/>')
    body = "#5b2d7a"
    extra = '<path d="M 470 1080 C 500 1110, 580 1110, 610 1080" stroke="#7a45a0" stroke-width="16" fill="none"/>'
    if hold == "pasta":
        extra += ('<path d="M 690 1150 C 790 1090, 830 1000, 840 930" stroke="#5b2d7a" stroke-width="70" fill="none" stroke-linecap="round"/>'
                  '<g transform="rotate(-25 860 860)">'
                  '<path d="M 820 700 L 900 700 L 920 960 L 800 960 Z" fill="#f4f6f8" stroke="#c7ccd3" stroke-width="5"/>'
                  '<rect x="820" y="760" width="80" height="60" fill="#2d7fd1"/><rect x="842" y="660" width="36" height="44" rx="6" fill="#e10600"/>'
                  '</g><ellipse cx="850" cy="910" rx="44" ry="34" fill="url(#skin)"/>')
    return _woman(cx, cy, s, body, curls, front, mood, extra, earrings="#e0b52a")
