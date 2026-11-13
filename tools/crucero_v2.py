"""Sistema visual v2 del crucero: la imagen manda, la marca acompaña.

Capas (todas PNG 1080x1920 con transparencia, para superponer en vidIQ compose sobre imagen/vídeo 9:16):
  viñeta()                 → oscurece bordes (siempre)
  barra()                  → marca mínima arriba: DIAGNÓSTICO OCULTO · EXP. PERSÉFONE
  sub(texto)               → subtítulo grande en el tercio inferior; *palabra* = acento rojo
  chip(lineas)             → dato de expediente (hora, coordenadas)
  sello(texto)             → sello rojo
  portada(parte, gancho)   → primer fotograma
  cierre(pregunta, sig)    → último plano
`python3 tools/crucero_v2.py muestra` compone una muestra sobre fondos provisionales.
"""
import sys, pathlib, html, re, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import W, H, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEAL, ICE, RED = "#0b2a30", "#eef6f7", "#d0142c"
COND = 'font-family="DejaVu Sans Condensed" font-weight="bold"'
MONO = 'font-family="DejaVu Sans Mono" font-weight="bold"'
SERIF = 'font-family="DejaVu Serif Condensed" font-weight="bold"'
SHADOW = 'stroke="#000" stroke-opacity="0.55" stroke-width="10" paint-order="stroke"'


def svg(body, defs=""):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><defs>{defs}</defs>{body}</svg>'


def _wrap(t, n):
    out, cur = [], ""
    for w in t.split():
        plain = lambda s: s.replace("*", "")
        if cur and len(plain(cur)) + 1 + len(plain(w)) > n:
            out.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    return out + ([cur] if cur else [])


def _spans(line, base, accent=RED):
    parts = re.split(r"(\*[^*]+\*)", line)
    return "".join(f'<tspan fill="{accent}">{html.escape(p[1:-1])}</tspan>' if p.startswith("*") else html.escape(p)
                    for p in parts if p)


GRAD = ('<linearGradient id="top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0.78"/>'
        '<stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>'
        '<linearGradient id="bot" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0.88"/>'
        '<stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>'
        '<radialGradient id="vig" cx="0.5" cy="0.5" r="0.75"><stop offset="0.55" stop-color="#000" stop-opacity="0"/>'
        f'<stop offset="1" stop-color="{TEAL}" stop-opacity="0.85"/></radialGradient>')


def vineta():
    return f'<rect width="{W}" height="{H}" fill="url(#vig)"/>'


def barra():
    return (f'<rect width="{W}" height="230" fill="url(#top)"/>'
            f'<text x="56" y="92" {COND} font-size="27" letter-spacing="5" fill="{ICE}" fill-opacity="0.85">DIAGNÓSTICO OCULTO</text>'
            f'<text x="1024" y="92" {MONO} font-size="24" fill="{ICE}" fill-opacity="0.7" text-anchor="end">EXP. PERSÉFONE</text>'
            f'<rect x="56" y="108" width="64" height="5" fill="{RED}"/>')


def sub(texto, y=1500):
    lines = _wrap(texto, 19)
    y0 = y - 40 * (len(lines) - 1)
    out = f'<rect y="{H - 760}" width="{W}" height="760" fill="url(#bot)"/>'
    out += "".join(f'<text x="540" y="{y0 + 92 * i}" {COND} font-size="82" fill="{ICE}" text-anchor="middle" {SHADOW}>'
                   f'{_spans(l, ICE)}</text>' for i, l in enumerate(lines))
    return out


def chip(lineas, y=200):
    h = 26 + 52 * len(lineas)
    out = f'<rect x="56" y="{y}" width="{max(len(l) for l in lineas) * 23 + 70}" height="{h}" fill="{TEAL}" fill-opacity="0.82"/>'
    out += f'<rect x="56" y="{y}" width="8" height="{h}" fill="{RED}"/>'
    out += "".join(f'<text x="86" y="{y + 56 + 52 * i}" {MONO} font-size="36" fill="{ICE}">{html.escape(l)}</text>'
                   for i, l in enumerate(lineas))
    return out


def sello(texto, x=540, y=900, rot=-7, size=58):
    w = 40 + size * 0.66 * len(texto)
    return (f'<g transform="rotate({rot} {x} {y})" opacity="0.92"><rect x="{x - w / 2}" y="{y - size * 1.05}" width="{w}" '
            f'height="{size * 1.55}" fill="none" stroke="{RED}" stroke-width="7" rx="8"/>'
            f'<text x="{x}" y="{y + size * 0.1}" {COND} font-size="{size}" letter-spacing="3" fill="{RED}" text-anchor="middle">'
            f'{html.escape(texto)}</text></g>')


def portada(parte, gancho):
    lines = _wrap(gancho.upper(), 15)
    out = f'<rect width="{W}" height="620" fill="url(#top)"/><rect y="{H - 820}" width="{W}" height="820" fill="url(#bot)"/>'
    out += (f'<text x="540" y="96" {COND} font-size="30" letter-spacing="9" fill="{ICE}" fill-opacity="0.9" text-anchor="middle">DIAGNÓSTICO OCULTO</text>'
            f'<text x="540" y="214" {SERIF} font-size="94" fill="{ICE}" text-anchor="middle" {SHADOW}>EL CRUCERO QUE</text>'
            f'<text x="540" y="318" {SERIF} font-size="94" fill="{ICE}" text-anchor="middle" {SHADOW}>REGRESÓ VACÍO</text>')
    out += sello("EXPEDIENTE PERSÉFONE", 540, 410, -3, 36)
    out += (f'<text x="540" y="{1390 - 92 * (len(lines) - 1)}" {COND} font-size="200" fill="{ICE}" text-anchor="middle" '
            f'letter-spacing="2" {SHADOW}>PARTE {parte:02d}</text>')
    y0 = 1560 - 46 * (len(lines) - 1)
    out += "".join(f'<text x="540" y="{y0 + 96 * i}" {COND} font-size="84" fill="{ICE}" text-anchor="middle" {SHADOW}>'
                   f'{_spans(l, ICE)}</text>' for i, l in enumerate(lines))
    out += f'<text x="540" y="1860" {COND} font-size="28" letter-spacing="6" fill="{ICE}" fill-opacity="0.75" text-anchor="middle">FICCIÓN</text>'
    return out


def cierre(pregunta, siguiente):
    lines = _wrap(pregunta.upper(), 15)
    out = f'<rect width="{W}" height="{H}" fill="#000" fill-opacity="0.35"/><rect y="{H - 1100}" width="{W}" height="1100" fill="url(#bot)"/>'
    out += barra()
    y0 = 1180 - 50 * (len(lines) - 1)
    out += "".join(f'<text x="540" y="{y0 + 100 * i}" {COND} font-size="92" fill="{ICE}" text-anchor="middle" {SHADOW}>'
                   f'{_spans(l, ICE)}</text>' for i, l in enumerate(lines))
    out += f'<text x="540" y="{y0 + 100 * len(lines) + 30}" {COND} font-size="40" fill="{ICE}" fill-opacity="0.8" text-anchor="middle">Te leo en comentarios</text>'
    pw = 140 + 30 * len(siguiente)
    out += (f'<rect x="{540 - pw / 2}" y="1560" width="{pw}" height="120" fill="{RED}"/>'
            f'<text x="540" y="1640" {COND} font-size="56" fill="#fff" text-anchor="middle">{html.escape(siguiente)}</text>')
    return out


def capa(body, out):
    return render(svg(body, GRAD), out)


def fondo(src, out, crop=None, modo="feather", ancho=1400, cy=0.46):
    """Fondo provisional 9:16 (en producción las imágenes ya vienen en 9:16 y no hace falta).
    'fill' recorta y escala; 'feather' pone la imagen grande, a sangre en los lados y fundida arriba/abajo
    con su propia versión desenfocada, para que no se vea como un recuadro."""
    c = f"crop={crop[2]}:{crop[3]}:{crop[0]}:{crop[1]}," if crop else ""
    if modo == "fill":
        vf = f"{c}scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H}"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", vf, "-frames:v", "1", "-update", "1", str(out)], check=True)
        return out
    fc = (f"[0]{c}split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=45:2,eq=brightness=-0.10[bg];"
          f"[b]scale={ancho}:-2:flags=lanczos,crop={W}:ih,format=rgba,"
          f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='255*clip(min(Y/(0.22*H),(H-Y)/(0.22*H)),0,1)'[fg];"
          f"[bg][fg]overlay=0:{H}*{cy}-h/2")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-filter_complex", fc, "-frames:v", "1", "-update", "1", str(out)], check=True)
    return out


def componer(bg, capas, out):
    args = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(bg)]
    for c in capas:
        args += ["-i", str(c)]
    fc = "".join(f"[{'v' + str(i) if i else '0'}][{i + 1}]overlay[v{i + 1}];" for i in range(len(capas)))[:-1].rsplit("[", 1)[0]
    subprocess.run(args + ["-filter_complex", fc, "-frames:v", "1", "-update", "1", str(out)], check=True)
    return out


def muestra(boceto, outdir):
    outdir = pathlib.Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    t = lambda n: outdir / n
    vig = capa(vineta(), t("L_vineta.png"))
    frames = [
        ("01_portada", (0, 285, 511, 235), dict(ancho=2050, cy=0.5), [capa(portada(1, "La comida aún estaba *caliente*"), t("L1.png"))]),
        ("02_radio", (0, 880, 511, 221), dict(ancho=2100, cy=0.45), [vig, capa(barra() + chip(["06:52 · RADIO", "PESQUERO «SANTA BÁRBARA»"]) +
                                                         sub("«La comida aún está *caliente*»"), t("L2.png"))]),
        ("03_deriva", (0, 1102, 511, 434), dict(ancho=1700), [vig, capa(barra() + chip(["17-OCT · 06:30", "29°14'N 21°40'W"], y=1110) +
                                                           sub("Llevaba *once* *días* desaparecido."), t("L3.png"))]),
        ("04_elena", (530, 190, 494, 420), dict(ancho=1500, cy=0.42), [vig, capa(barra() + sub("Me llamo Elena Varela. Soy *médica* *forense*."), t("L4.png"))]),
        ("05_comedor", (0, 694, 511, 407), dict(ancho=1700, cy=0.44), [vig, capa(barra() + sub("Fríos. Pero *frescos*. No tenían once días."), t("L5.png"))]),
        ("06_movil", (540, 694, 484, 407), dict(ancho=1600, cy=0.44), [vig, capa(barra() + sub("«Tu historia se ha *publicado*»"), t("L6.png"))]),
        ("07_cierre", (0, 1270, 511, 266), dict(ancho=2000, cy=0.36), [capa(cierre("¿Quién *publicó* esa historia?", "PARTE 02 EN EL PERFIL"), t("L7.png"))]),
    ]
    res = []
    for name, crop, kw, capas in frames:
        bg = fondo(boceto, t(f"bg_{name}.png"), crop, **kw)
        res.append(componer(bg, capas, t(f"{name}.png")))
    return res


if __name__ == "__main__" and sys.argv[1:2] == ["muestra"]:
    for f in muestra(sys.argv[2], sys.argv[3]):
        print(f)
