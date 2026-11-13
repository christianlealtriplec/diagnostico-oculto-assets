"""Gráficos del crucero («El crucero que regresó vacío»): portada, fichas de expediente,
datos, notificación de móvil y cierre. Todo 1080x1920, PNG con transparencia (para superponer
en vidIQ sobre el vídeo de archivo). 0 créditos.

Uso rápido:  python3 tools/crucero.py demo   → crucero/demo/*.png + previa compuesta
"""
import sys, pathlib, html, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import W, H, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEAL, ICE, RED, MUTE = "#0b1f24", "#e8f1f2", "#c8102e", "#9fb4b8"
SANS = 'font-family="DejaVu Sans" font-weight="bold"'
MONO = 'font-family="DejaVu Sans Mono" font-weight="bold"'
SERIF = 'font-family="DejaVu Serif" font-weight="bold"'


def _svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{body}</svg>'


def _wrap(t, n):
    out, cur = [], ""
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    return out + ([cur] if cur else [])


def esc(t):
    return html.escape(t, quote=False)


def marca():
    """Banda común del canal + nombre de la serie (arriba)."""
    return (f'<rect x="0" y="0" width="{W}" height="300" fill="{TEAL}" fill-opacity="0.82"/>'
            f'<text x="540" y="92" {SANS} font-size="30" letter-spacing="8" fill="{MUTE}" text-anchor="middle">DIAGNÓSTICO OCULTO</text>'
            f'<line x1="300" y1="118" x2="780" y2="118" stroke="{MUTE}" stroke-width="2"/>'
            f'<text x="540" y="190" {SERIF} font-size="62" fill="{ICE}" text-anchor="middle">EL CRUCERO QUE</text>'
            f'<text x="540" y="262" {SERIF} font-size="62" fill="{ICE}" text-anchor="middle">REGRESÓ VACÍO</text>')


def sello(x, y, texto, rot=-8, size=34):
    w = 26 + size * 0.62 * len(texto)
    return (f'<g transform="rotate({rot} {x} {y})"><rect x="{x - w / 2}" y="{y - size}" width="{w}" height="{size * 1.5}" '
            f'fill="none" stroke="{RED}" stroke-width="5" rx="6"/>'
            f'<text x="{x}" y="{y + 4}" {MONO} font-size="{size}" fill="{RED}" text-anchor="middle">{esc(texto)}</text></g>')


def portada(parte, gancho):
    """Primer fotograma: marca + PARTE grande + gancho de 2–6 palabras + sello. Abajo queda libre la imagen."""
    lines = _wrap(gancho.upper(), 16)
    body = marca() + sello(540, 400, "EXPEDIENTE PERSÉFONE", -4, 30)
    body += (f'<text x="540" y="560" {SANS} font-size="130" fill="{ICE}" text-anchor="middle" stroke="#000" '
             f'stroke-width="10" paint-order="stroke">PARTE {parte:02d}</text>')
    y0 = 1380 - 46 * (len(lines) - 1)
    body += f'<rect x="60" y="{y0 - 92}" width="960" height="{70 + 92 * len(lines)}" rx="10" fill="#000" fill-opacity="0.72"/>'
    body += "".join(f'<text x="540" y="{y0 + 92 * i}" {SANS} font-size="78" fill="{ICE}" text-anchor="middle">{esc(l)}</text>'
                    for i, l in enumerate(lines))
    body += f'<text x="540" y="1840" {SANS} font-size="28" fill="{MUTE}" text-anchor="middle">FICCIÓN</text>'
    return _svg(body)


def dato(lineas, y=330):
    """Etiqueta de datos (fecha, hora, coordenadas) estilo expediente."""
    h = 40 + 56 * len(lineas)
    body = f'<rect x="60" y="{y}" width="640" height="{h}" fill="{TEAL}" fill-opacity="0.85" stroke="{ICE}" stroke-opacity="0.4"/>'
    body += "".join(f'<text x="90" y="{y + 66 + 56 * i}" {MONO} font-size="40" fill="{ICE}">{esc(l)}</text>'
                    for i, l in enumerate(lineas))
    return _svg(body)


def ficha(nombre, rol, campos, foto=None):
    """Ficha de expediente de un personaje (foto fija o silueta)."""
    body = f'<rect x="90" y="520" width="900" height="760" fill="{ICE}" stroke="#000" stroke-width="3"/>'
    body += f'<rect x="90" y="520" width="900" height="70" fill="{TEAL}"/>'
    body += f'<text x="120" y="568" {MONO} font-size="32" fill="{ICE}">EXPEDIENTE PERSÉFONE · PERSONAL</text>'
    if foto:
        body += f'<image href="{foto}" x="130" y="630" width="330" height="420" preserveAspectRatio="xMidYMid slice"/>'
    else:
        body += (f'<rect x="130" y="630" width="330" height="420" fill="#c9d3d5"/>'
                 f'<circle cx="295" cy="790" r="85" fill="#7d8f93"/><path d="M160,1050 Q295,860 430,1050 Z" fill="#7d8f93"/>')
    body += f'<rect x="130" y="630" width="330" height="420" fill="none" stroke="#000" stroke-width="3"/>'
    body += f'<text x="500" y="680" {SANS} font-size="44" fill="#111">{esc(nombre)}</text>'
    body += "".join(f'<text x="500" y="{740 + 50 * i}" {SANS} font-size="30" fill="#333">{esc(l)}</text>'
                    for i, l in enumerate(_wrap(rol, 26)))
    body += "".join(f'<text x="130" y="{1110 + 52 * i}" {MONO} font-size="32" fill="#111">{esc(c)}</text>'
                    for i, c in enumerate(campos))
    body += sello(780, 1230, "CONFIDENCIAL", -10, 34)
    return _svg(body)


def notificacion(usuario, texto, hace="ahora"):
    """Pantalla de móvil con una notificación genérica (sin logotipos de redes reales)."""
    body = (f'<rect x="230" y="420" width="620" height="1180" rx="70" fill="#050708" stroke="#3a4648" stroke-width="10"/>'
            f'<rect x="262" y="470" width="556" height="1080" rx="40" fill="#0f1416"/>'
            f'<text x="540" y="640" {SANS} font-size="96" fill="{ICE}" text-anchor="middle">06:31</text>'
            f'<text x="540" y="690" {SANS} font-size="28" fill="{MUTE}" text-anchor="middle">viernes, 17 de octubre</text>'
            f'<rect x="290" y="780" width="500" height="190" rx="28" fill="{ICE}" fill-opacity="0.94"/>'
            f'<circle cx="345" cy="835" r="30" fill="{TEAL}"/>'
            f'<text x="345" y="846" {SANS} font-size="28" fill="{ICE}" text-anchor="middle">{esc(usuario[0].upper())}</text>'
            f'<text x="390" y="830" {SANS} font-size="26" fill="#111">{esc(usuario)}</text>'
            f'<text x="770" y="830" {SANS} font-size="22" fill="#555" text-anchor="end">{esc(hace)}</text>')
    body += "".join(f'<text x="390" y="{875 + 38 * i}" {SANS} font-size="28" fill="#222">{esc(l)}</text>'
                    for i, l in enumerate(_wrap(texto, 24)))
    return _svg(body)


def nota_forense(lineas):
    """Nota manuscrita del cuaderno de la forense."""
    body = f'<g transform="rotate(-3 540 960)"><rect x="170" y="700" width="740" height="{120 + 70 * len(lineas)}" fill="#f4ecd2"/>'
    body += "".join(f'<line x1="200" y1="{790 + 70 * i}" x2="880" y2="{790 + 70 * i}" stroke="#b9c7d6" stroke-width="2"/>'
                    for i in range(len(lineas)))
    body += "".join(f'<text x="210" y="{780 + 70 * i}" font-family="DejaVu Serif" font-style="italic" font-size="46" fill="#1a2a6c">{esc(l)}</text>'
                    for i, l in enumerate(lineas))
    return _svg(body + "</g>")


def cierre(pregunta, siguiente):
    lines = _wrap(pregunta.upper(), 18)
    body = f'<rect x="0" y="0" width="{W}" height="{H}" fill="{TEAL}" fill-opacity="0.78"/>' + marca()
    body += "".join(f'<text x="540" y="{820 + 96 * i}" {SANS} font-size="76" fill="{ICE}" text-anchor="middle">{esc(l)}</text>'
                    for i, l in enumerate(lines))
    body += f'<text x="540" y="{900 + 96 * len(lines)}" {SANS} font-size="40" fill="{MUTE}" text-anchor="middle">Te leo en comentarios</text>'
    pw = 120 + 27 * len(siguiente)
    body += f'<rect x="{540 - pw / 2}" y="1440" width="{pw}" height="110" rx="55" fill="{RED}"/>'
    body += f'<text x="540" y="1512" {SANS} font-size="46" fill="#fff" text-anchor="middle">{esc(siguiente)}</text>'
    return _svg(body)


def demo():
    out = ROOT / "crucero" / "demo"; out.mkdir(parents=True, exist_ok=True)
    items = {
        "portada_p01": portada(1, "La comida aún estaba caliente"),
        "dato_hallazgo": dato(["17-OCT · 06:30", "29°14'N · 21°40'W", "A LA DERIVA"]),
        "ficha_elena": ficha("Dra. Elena Varela", "Médica forense · Instituto de Medicina Legal de Las Palmas",
                             ["ABORDA: 17-OCT 11:00", "PARENTESCO: hermana de", "una pasajera (7114)"]),
        "nota_forense": nota_forense(["Comedor Atlántico", "400 platos servidos", "templados → < 2 h", "¿quién sirvió?"]),
        "notificacion": notificacion("noa.viaja", "Tu historia se ha publicado", "ahora"),
        "cierre_p01": cierre("¿Quién publicó esa historia?", "PARTE 02 en el perfil"),
    }
    for k, s in items.items():
        render(s, out / f"{k}.png")
    return out


if __name__ == "__main__" and sys.argv[1:] == ["demo"]:
    print(demo())
