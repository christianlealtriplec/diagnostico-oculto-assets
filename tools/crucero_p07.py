"""Capas y plan de montaje de la Parte 07 del crucero (vidIQ compose). Guion v2 «hilo conductor»."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render
from crucero_p03 import weight, _inner, _blur
from crucero_p02 import _datauri as _datauri_raw

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p07"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p07/"
VOZ = 63.24; COLA = 2.5
VOZ_URL = "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/48a417d1-ec87-40d2-b2cb-77f6ffcd4bc2.mp3"
IMG = {
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "comedor": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/89ba9c1f-6c89-42bc-b73b-4d544cc7cb41.jpeg",
 "lucia": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/fd3a7999-5d56-41dd-bb22-69dca8c3d8ff.jpeg",
}
PROPIAS = ("ficha", "reales", "girado", "lista", "ferrer")
AUTORES = ["Artem Podrez", "SHEMÁ", "Nicola Narracci", "Tima Miroshnichenko", "RDNE Stock project", "HÜSEYİN AVCI"]
VID = {
 "espejo": "https://videos.pexels.com/video-files/4604026/4604026-hd_1080_1920_27fps.mp4",
 "muelle": "https://videos.pexels.com/video-files/39661168/16907265_1080_1920_50fps.mp4",
 "fibra": "https://videos.pexels.com/video-files/40277493/17202148_1080_1920_30fps.mp4",
 "tableta": "https://videos.pexels.com/video-files/4962002/4962002-hd_1080_1920_25fps.mp4",
 "grifo": "https://videos.pexels.com/video-files/5614823/5614823-hd_1080_1920_25fps.mp4",
 "contrato": "https://videos.pexels.com/video-files/7841594/7841594-hd_1080_1920_30fps.mp4",
 "tuberias": "https://videos.pexels.com/video-files/36928186/15643830_1080_1920_30fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
# Sin chips de fecha/hora/lugar (norma del 20-nov): lo dice la narración.
SHOTS = [
 ("espejo", "Lo que sabemos: Memoria estaba apagada.", "Memoria estaba *apagada*.", "vaho", None, "cut"),
 ("muelle", "Y aun así publicó una foto mía en el muelle, esa misma mañana. Me dejó helada.", "Y aun así publicó una foto *mía* en el muelle.", "marco", None, "dip_to_black"),
 ("fibra", "Bellini rastreó el envío: había entrado en Memoria desde la red del propio barco.", "Entró desde la *red* del propio barco.", "", None, "fade"),
 ("maestro", "Un barco vacío y precintado.", "Un barco vacío y *precintado*.", "sello:PRECINTADO", KB(1.0, .5, .5, 1.1, .5, .45), "dip_to_black"),
 ("tableta", "Para saber qué era real, Bellini separó las historias que la IA no había tocado.", "Separó las historias que la IA *no* había tocado.", "", None, "fade"),
 ("reales", "Las fotos de verdad. Quedaron muy pocas.", "Las fotos de *verdad*. Quedaron muy pocas.", "sello:REALES: 3", KB(1.0, .5, .45, 1.06, .5, .45), "cut"),
 ("ficha", "Una era de Lucía Ferrer, dieciséis años, pasajera.", "*Lucía* *Ferrer*, dieciséis años, pasajera.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("grifo", "Seis de octubre, de madrugada. Un selfi en el baño de su camarote.", "De madrugada. Un *selfi* en el baño de su camarote.", "", None, "fade"),
 ("lucia", "Sudadera roja, auriculares. Normal.", "Sudadera *roja*, auriculares. Normal.", "historia_lucia", KB(1.15, .5, .4, 1.25, .5, .42), "cut"),
 ("espejo2", "Hasta que miré el espejo empañado. Había letras en el vaho. Del revés.", "Había letras en el *vaho*. Del revés.", "vaho", None, "dip_to_black"),
 ("girado", "Giré la imagen. \"No bebáis el agua\".", "«No bebáis el *agua*»", "", KB(1.0, .5, .45, 1.1, .5, .45), "cut"),
 ("lista", "Busqué a su familia en la lista.", "Busqué a su *familia* en la lista.", "", KB(1.0, .5, .45, 1.06, .5, .5), "fade"),
 ("ferrer", "Lucía viajaba con su padre, Andrés Ferrer.", "Viajaba con su padre, *Andrés* *Ferrer*.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("contrato", "Su empresa aparecía en el contrato de reforma del barco.", "Su empresa reformó el *barco*.", "nota", None, "fade"),
 ("tuberias", "Le pedí a Rey que buscara qué había instalado. El sistema de agua potable.", "Había instalado el sistema de *agua* *potable*.", "sello:AGUA POTABLE", None, "cut"),
 ("comedor", "¿Por qué el padre de Lucía?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]

MANO = 'font-family="DejaVu Sans" font-weight="bold" font-style="oblique"'
FOG = ('<filter id="fz" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="40"/></filter>'
       '<filter id="fl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>')


def _letras(girado, y0=700, op=0.75):
    """Letras trazadas con el dedo en el vaho: del revés (espejo) o ya giradas."""
    t = "" if girado else ' transform="translate(1080 0) scale(-1 1)"'
    b = f'<g{t} filter="url(#fl)">'
    for k, l in enumerate(("NO BEBÁIS", "EL AGUA")):
        b += (f'<text x="540" y="{y0 + 190 * k}" {MANO} font-size="150" fill="#0d1416" fill-opacity="{op}" '
              f'text-anchor="middle" letter-spacing="6">{l}</text>')
    return b + '</g>'


def _vaho(girado=False):
    b = (f'<rect width="{W}" height="{H}" fill="#cfd8da" fill-opacity="0.38"/>'
         f'<ellipse cx="540" cy="820" rx="520" ry="560" fill="#e6eeef" fill-opacity="0.35" filter="url(#fz)"/>')
    return b + _letras(girado)


def _girado():
    """Imagen girada: espejo empañado con el mensaje legible."""
    body = (f'<rect width="{W}" height="{H}" fill="#2b3538"/>'
            f'<rect x="90" y="300" width="900" height="1180" rx="20" fill="#aebbbd"/>'
            f'<ellipse cx="540" cy="860" rx="420" ry="520" fill="#d9e2e3" filter="url(#fz)"/>'
            f'<rect x="90" y="300" width="900" height="1180" rx="20" fill="none" stroke="#596569" stroke-width="16"/>')
    body += _letras(True, y0=820, op=0.85)
    body += f'<line x1="200" y1="1180" x2="880" y2="1180" stroke="{V.RED}" stroke-width="12"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><defs>{FOG}</defs>{body}</svg>'


def _reales():
    S = C.SANS
    reales = {6, 13, 17}
    body = f'<rect width="{W}" height="{H}" fill="#071216"/>'
    body += f'<text x="540" y="490" {S} font-size="40" fill="{C.MUTE}" text-anchor="middle">HISTORIAS DEL PERSÉFONE · FILTRO: SIN IA</text>'
    for i in range(20):
        x, y = 230 + (i % 4) * 160, 530 + (i // 4) * 160
        real = i in reales
        body += (f'<rect x="{x}" y="{y}" width="140" height="140" rx="12" fill="{"#f4f8f8" if real else "#2c3639"}" '
                 f'stroke="{"#fff" if real else "#3d4a4e"}" stroke-width="{6 if real else 2}"/>')
        if not real:
            body += f'<text x="{x + 70}" y="{y + 82}" {S} font-size="30" fill="#55656a" text-anchor="middle">IA</text>'
        else:
            body += f'<text x="{x + 70}" y="{y + 80}" {S} font-size="26" fill="#1e8a4c" text-anchor="middle">REAL</text>'
    return C._svg(body)


def _lista():
    S, M = C.SANS, C.MONO
    filas = [("FARIÑA, Tomás", "6208"), ("FERNÁNDEZ, Ana", "6210"), ("FERRER, Andrés", "6214"), ("FERRER, Lucía", "6214"),
             ("FIGUERAS, Pau", "6217"), ("FLORES, Marta", "6221"), ("FUENTES, Iker", "6225")]
    body = f'<rect x="110" y="420" width="860" height="900" fill="#f2f2ee" stroke="#000" stroke-width="4"/>'
    body += f'<rect x="110" y="420" width="860" height="90" fill="{C.TEAL}"/>'
    body += f'<text x="540" y="480" {S} font-size="36" fill="{C.ICE}" text-anchor="middle">LISTA DE PASAJEROS · PERSÉFONE</text>'
    body += f'<text x="150" y="570" {M} font-size="28" fill="#666">PASAJERO</text><text x="930" y="570" {M} font-size="28" fill="#666" text-anchor="end">CAMAROTE</text>'
    for k, (n, c) in enumerate(filas):
        y = 650 + 90 * k
        if "FERRER" in n:
            body += f'<rect x="130" y="{y - 58}" width="820" height="80" fill="{C.RED}" fill-opacity="0.18" stroke="{C.RED}" stroke-width="4"/>'
        body += (f'<text x="150" y="{y}" {M} font-size="40" fill="#111">{C.esc(n)}</text>'
                 f'<text x="930" y="{y}" {M} font-size="40" fill="#111" text-anchor="end">{c}</text>')
    return C._svg(body)


def _marco_muelle():
    h = _inner(C.historia("noa.viaja", 11, "18-OCT", total=12, actual=12))
    return h.replace("DÍA 11 · 18-OCT", "18-OCT · 10:58")


def _marco_lucia():
    h = _inner(C.historia("lucia.ferrer", 1, "06-OCT", total=1, actual=1))
    return h.replace("DÍA 1 · 06-OCT", "06-OCT · 00:31")


def _datauri(path, name):
    return _datauri_raw(path, name)


def capas():
    import crucero_p02
    crucero_p02.OUT = OUT
    bgm = _blur(ROOT / "crucero/maestro/barco_maestro.jpg", OUT / "_bg_maestro.png")
    ficha = render(C.ficha("Lucía Ferrer", "Pasajera · camarote 6214",
                           ["EDAD: 16", "VIAJA CON: su padre", "FOTO: real (sin IA)"],
                           foto=_datauri(ROOT / "crucero/maestro/lucia.jpg", "lucia")), OUT / "_ficha.png")
    V.componer(bgm, [ficha], OUT / "ficha.png")
    fer = render(C.ficha("Andrés Ferrer", "Pasajero · camarote 6214 · padre de Lucía",
                         ["EDAD: 47", "EMPRESA: Ferrer Hidráulica", "SITUACIÓN: desaparecido"]), OUT / "_ferrer.png")
    V.componer(bgm, [fer], OUT / "ferrer.png")
    render(_reales(), OUT / "reales.png")
    render(_girado(), OUT / "girado.png")
    render(_lista(), OUT / "lista.png")
    V.capa(V.vineta(), OUT / "L_vineta.png")
    vaho = lambda: _vaho(False)
    render(V.svg(vaho() + V.portada(7, "Míralo en el *espejo*"), V.GRAD + FOG), OUT / "L_portada.png")
    for i, (src, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Por qué el *padre* de Lucía?", "PARTE 08 EL LUNES")
        else:
            body = ""
            if extra == "vaho":
                body += vaho()
            body += (V.sub(sub) if sub else "")
            if extra not in ("marco", "historia_lucia"):
                body = V.barra() + body
            for e in filter(None, extra.split(";")):
                if e.startswith("sello:"):
                    t = e[6:]
                    sy = 400 if src in PROPIAS else 820
                    body += V.sello(t, 540, sy, -6, 60 if len(t) < 14 else 50)
                elif e == "marco":
                    body += _marco_muelle()
                elif e == "historia_lucia":
                    body += _marco_lucia()
                elif e == "nota":
                    body += _inner(C.nota_forense(["Ferrer Hidráulica", "reforma del barco · 2024"]))
        render(V.svg(body, V.GRAD + FOG), OUT / f"L{i:02d}.png")


def plan():
    total = sum(weight(s[1]) for s in SHOTS)
    durs = [VOZ * weight(s[1]) / total for s in SHOTS]
    durs[-1] += COLA
    full = {"x": 0, "y": 0, "width": 1, "height": 1}
    scenes, overlays, t = [], [], 0.0
    overlays.append({"kind": "image", "src": RAW + "L_vineta.png", "start": 0, "duration": round(sum(durs), 2), "position": full})
    for i, ((src, habla, sub, extra, kb, tr), d) in enumerate(zip(SHOTS, durs)):
        key = src[:-1] if src.endswith("2") else src
        url = RAW + f"{src}.png" if src in PROPIAS else (IMG.get(key) or VID[key])
        sc = {"source": url, "type": "image" if src in PROPIAS or key in IMG else "video", "duration": round(d, 2)}
        if src == "espejo2":
            sc["startFromSeconds"] = 8
        if sc["type"] == "image" and kb:
            sc["kenBurns"] = kb
        if i and tr != "cut":
            sc["transitionIn"] = {"kind": tr, "duration": 0.3 if tr == "fade" else 0.4}
        scenes.append(sc)
        if i == 0:
            p = min(d, 2.2)
            overlays.append({"kind": "image", "src": RAW + "L_portada.png", "start": 0, "duration": round(p, 2), "position": full})
            if d > p + 0.05:
                overlays.append({"kind": "image", "src": RAW + "L00.png", "start": round(p, 2), "duration": round(d - p, 2), "position": full})
        else:
            overlays.append({"kind": "image", "src": RAW + f"L{i:02d}.png", "start": round(t, 2), "duration": round(d, 2), "position": full})
        t += d
    return {"format": "vertical", "scenes": scenes, "overlays": overlays,
            "voiceover": {"audioUrl": VOZ_URL, "volume": 1.1},
            "music": {"audioUrl": "https://ai-music-tracks.s3.us-east-1.amazonaws.com/4065b5e6-8066-45ac-a648-6f0f86e15b82/74581a90-9381-4108-9197-4193bd755598.wav", "volume": 0.7, "duckTo": 0.25, "fadeMs": 400},
            "captions": {"style": "none"}}


if __name__ == "__main__":
    capas()
    p = plan()
    (OUT / "compose.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    print(len(p["scenes"]), "escenas ·", len(p["overlays"]), "capas ·", round(sum(s["duration"] for s in p["scenes"]), 2), "s")
    for s, (src, *_ ) in zip(p["scenes"], SHOTS):
        print(f'{src:16s} {s["duration"]}')
