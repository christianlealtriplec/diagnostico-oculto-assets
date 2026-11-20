"""Capas y plan de montaje de la Parte 03 del crucero (vidIQ compose)."""
import sys, pathlib, json, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p03"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p03/"
VOZ = 71.97; COLA = 2.5
VOZ_URL = "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/1f31a55d-6ea7-4345-9d61-0b34a7702fe7.mp3"
IMG = {
 "foto": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/3b75261f-1807-43f7-870e-62228452c7bf.jpeg",
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "popa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/5afabeb8-e91c-42a9-8a13-f2620868b45e.jpeg",
 "noa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/98a941fa-c2b9-46f8-894e-70212240d71d.jpeg",
}
PROPIAS = ("cuadricula", "ficha", "plano")
AUTORES = ["Artem Podrez", "정규송 Nui MALAMA", "Bradley Murray", "K", "Larkkid Dung", "MART PRODUCTION",
           "Ali Alcántara", "cottonbro studio", "Yaroslav Shuraev", "Kuiyibo Campos"]
VID = {
 "movil": "https://videos.pexels.com/video-files/6279146/6279146-hd_1080_1920_30fps.mp4",
 "olas": "https://videos.pexels.com/video-files/35072027/14856546_1080_1920_30fps.mp4",
 "oceano": "https://videos.pexels.com/video-files/9153497/9153497-hd_720_1280_30fps.mp4",
 "piscina": "https://videos.pexels.com/video-files/33661313/14302051_1080_1920_24fps.mp4",
 "cielo": "https://videos.pexels.com/video-files/33129399/14120166_1080_1920_30fps.mp4",
 "pasillo": "https://videos.pexels.com/video-files/7251759/7251759-hd_1080_1920_25fps.mp4",
 "manos": "https://videos.pexels.com/video-files/15689201/15689201-hd_1080_1920_24fps.mp4",
 "espalda": "https://videos.pexels.com/video-files/7599305/7599305-hd_1080_2048_25fps.mp4",
 "puerta": "https://videos.pexels.com/video-files/6279825/6279825-hd_1080_1920_24fps.mp4",
 "servidores": "https://videos.pexels.com/video-files/28709421/12457750_1080_1920_30fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
HIST13 = "historia:8|13-OCT · 23:51"
# (fuente, texto hablado, subtítulo, extra, kenburns, transición)
SHOTS = [
 ("foto", "Esta foto se hizo desde el agua. De noche. En mitad del océano.", "Esta foto se hizo desde el *agua*. De noche.", HIST13, KB(1.0, .5, .5, 1.1, .5, .52), "cut"),
 ("movil", "Es la historia que se publicó a las once y cuarenta y dos, mientras yo buscaba a mi hermana.", "Se publicó a las *11:42*, mientras buscaba a mi hermana.", "chip:17-OCT · 11:42|CAMAROTE 7114", None, "fade"),
 ("foto", "El Perséfone, con todas las luces encendidas, visto a ras de las olas.", "Todas las luces encendidas. A ras de las *olas*.", HIST13, KB(1.35, .5, .56, 1.7, .5, .58), "fade"),
 ("olas", "Fecha: trece de octubre.", "Fecha: *13* de octubre.", "chip:13-OCT · 23:51", None, "cut"),
 ("oceano", "Para hacerla, alguien tenía que estar en el agua, de noche, a cientos de millas de la costa.", "Alguien tenía que estar *en* *el* *agua*.", "sello:380 MILLAS DE LA COSTA", None, "fade"),
 ("piscina", "Volví atrás. Día nueve: Noa en la piscina, vista desde arriba.", "Día 9: Noa en la piscina, vista desde *arriba*.", "historia:9|14-OCT", None, "dip_to_black"),
 ("cielo", "Encima de esa piscina no hay nada. Ni un balcón. Ni una cámara.", "*Nada*. Ni un balcón. Ni una cámara.", "nota", None, "fade"),
 ("noa", "Día siete: el pañuelo que nunca se puso.", "Día 7: el pañuelo que *nunca* se puso.", "historia:7|12-OCT", KB(1.0, .45, .4, 1.12, .5, .5), "fade"),
 ("cuadricula", "No era una historia rara. Eran muchas.", "No era una historia rara. Eran *muchas*.", "sello:IMPOSIBLES", KB(1.0, .5, .45, 1.06, .5, .45), "cut"),
 ("pasillo", "Alguien estaba haciendo fotos que nadie pudo hacer.", "Fotos que *nadie* pudo hacer.", "", None, "fade"),
 ("ficha", "Subí a buscar al inspector Tomás Rey, de la Guardia Civil.", "El inspector *Tomás* *Rey*, Guardia Civil.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("manos", "Le enseñé el móvil.", "Le enseñé el *móvil*.", "", None, "cut"),
 ("espalda", "\"Si se publican desde el barco, salen de sus servidores\", dijo.", "«Si se publican desde el barco, salen de sus *servidores*»", "", None, "fade"),
 ("puerta", "Y echó a andar. Cubierta dos. Una puerta sin rótulo.", "Cubierta 2. Una puerta *sin* *rótulo*.", "chip:CUBIERTA 2", None, "fade"),
 ("servidores", "La sala de servidores.", "La sala de *servidores*.", "", None, "cut"),
 ("plano", "No miró el plano ni una vez.", "No miró el plano *ni* *una* *vez*.", "sello:NO LO MIRÓ", KB(1.0, .5, .45, 1.08, .5, .45), "fade"),
 ("maestro", "Decía que nunca había estado en este barco.", "Decía que *nunca* había estado en este barco.", "", KB(1.5, .3, .55, 1.7, .25, .55), "fade"),
 ("popa", "¿Cómo sabía Rey dónde estaban los servidores?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]


def weight(t):
    return len(t) + 6 * sum(t.count(p) for p in ".;:!?") + 3 * t.count(",")


def _inner(svg):
    return svg.split(">", 1)[1].rsplit("</svg>", 1)[0]


def _blur(src, out, b=-0.28):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf",
                    f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness={b}:saturation=0.6",
                    "-frames:v", "1", "-update", "1", str(out)], check=True)
    return out


def _movil(contenido):
    return (f'<rect x="230" y="420" width="620" height="1180" rx="70" fill="#050708" stroke="#3a4648" stroke-width="10"/>'
            f'<rect x="262" y="470" width="556" height="1080" rx="40" fill="#0f1416"/>' + contenido)


def _cuadricula():
    S = C.SANS
    marcadas = {7, 8, 9}
    body = f'<text x="300" y="545" {S} font-size="24" fill="{C.MUTE}">11:42</text><text x="780" y="545" {S} font-size="22" fill="{C.RED}" text-anchor="end">SIN SERVICIO</text>'
    body += f'<text x="300" y="610" {S} font-size="34" fill="{C.ICE}">noa.viaja</text><text x="300" y="648" {S} font-size="24" fill="{C.MUTE}">Tus historias · 11</text>'
    for i in range(11):
        d = i + 1
        x, y = 300 + (i % 3) * 165, 680 + (i // 3) * 160
        roja = d in marcadas
        body += (f'<rect x="{x}" y="{y}" width="150" height="150" rx="14" fill="{C.TEAL}" stroke="{C.RED if roja else C.ICE}" '
                 f'stroke-opacity="{1 if roja else 0.35}" stroke-width="{8 if roja else 2}"/>'
                 f'<text x="{x + 75}" y="{y + 62}" {S} font-size="30" fill="{C.ICE}" text-anchor="middle">DÍA {d}</text>'
                 f'<text x="{x + 75}" y="{y + 96}" {S} font-size="20" fill="{C.MUTE}" text-anchor="middle">{d + 5}-OCT</text>'
                 f'<text x="{x + 75}" y="{y + 132}" {S} font-size="{15 if roja else 18}" fill="{C.RED if roja else "#7fd18b"}" text-anchor="middle">{"¿Desde dónde?" if roja else "Publicada"}</text>')
    return C._svg(_movil(body))


def _plano():
    """Plano de evacuación genérico de una cubierta (sin nombres reales)."""
    S = C.SANS
    g = "#1e8a4c"
    body = f'<rect x="110" y="560" width="860" height="700" fill="#f2f2ee" stroke="#000" stroke-width="4"/>'
    body += f'<rect x="110" y="560" width="860" height="80" fill="{g}"/>'
    body += f'<text x="540" y="614" {S} font-size="36" fill="#fff" text-anchor="middle">PLANO DE EVACUACIÓN · CUBIERTA 2</text>'
    # casco
    body += '<path d="M170,760 L800,760 Q930,900 800,1040 L170,1040 Z" fill="none" stroke="#333" stroke-width="6"/>'
    body += '<line x1="170" y1="900" x2="840" y2="900" stroke="#888" stroke-width="3" stroke-dasharray="14 10"/>'
    for x in range(230, 780, 110):
        body += f'<rect x="{x}" y="780" width="90" height="100" fill="#dfe3e3" stroke="#555" stroke-width="2"/>'
        body += f'<rect x="{x}" y="920" width="90" height="100" fill="#dfe3e3" stroke="#555" stroke-width="2"/>'
    body += '<rect x="560" y="920" width="90" height="100" fill="#c9cfd0" stroke="#333" stroke-width="3"/>'
    for x0 in (210, 520):
        body += f'<path d="M{x0},900 l60,0 m-18,-14 l18,14 l-18,14" stroke="{g}" stroke-width="7" fill="none"/>'
    body += f'<circle cx="300" cy="900" r="16" fill="{C.RED}"/>'
    body += f'<text x="170" y="1110" {S} font-size="28" fill="#222">● USTED ESTÁ AQUÍ</text>'
    body += f'<text x="170" y="1160" {S} font-size="28" fill="{g}">→ PUNTO DE REUNIÓN</text>'
    return C._svg(body)


def _encoger(png):
    """Reduce la pantalla del móvil al 78 % y la sube para dejar libre el subtítulo."""
    out = png.with_name(png.stem + "_s.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(png), "-filter_complex",
                    f"color=c=black@0:s={W}x{H},format=rgba[bg];[0]scale=iw*0.78:-1[m];[bg][m]overlay=(W-w)/2:(H-h)/2-140:format=auto",
                    "-frames:v", "1", "-update", "1", str(out)], check=True)
    return out


def capas():
    bgm = _blur(ROOT / "crucero/maestro/barco_maestro.jpg", OUT / "_bg_maestro.png")
    bgc = _blur(ROOT / "crucero/p01/img/comedor.jpg", OUT / "_bg_comedor.png", -0.3)
    V.componer(bgc, [_encoger(render(_cuadricula(), OUT / "_cuad.png"))], OUT / "cuadricula.png")
    ficha = render(C.ficha("Tomás Rey", "Inspector · Servicio Marítimo, Guardia Civil",
                           ["EDAD: 55", "CUERPO: Guardia Civil", "SERVICIO MARÍTIMO"]), OUT / "_ficha.png")
    V.componer(bgm, [ficha], OUT / "ficha.png")
    V.componer(bgm, [render(_plano(), OUT / "_plano.png")], OUT / "plano.png")
    V.capa(V.vineta(), OUT / "L_vineta.png")
    V.capa(V.portada(3, "Una foto *imposible*"), OUT / "L_portada.png")
    for i, (src, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Cómo sabía *Rey* dónde estaban?", "PARTE 04 EL DOMINGO")
        else:
            body = (V.sub(sub) if sub else "")
            if "historia:" not in extra:
                body = V.barra() + body
            for e in filter(None, extra.split(";")):
                if e.startswith("chip:"):
                    body += V.chip(e[5:].split("|"), y=200)
                elif e.startswith("sello:"):
                    t = e[6:]
                    body += V.sello(t, 540, 400 if src in PROPIAS else 820, -6, 60 if len(t) < 14 else 48)
                elif e.startswith("historia:"):
                    d, f = e[9:].split("|")
                    body += _inner(C.historia("noa.viaja", int(d), f))
                elif e == "nota":
                    body += _inner(C.nota_forense(["Día 9 · 14-OCT · piscina", "ángulo: ~12 m sobre el agua", "sin soporte posible"]))
        V.capa(body, OUT / f"L{i:02d}.png")


def plan():
    total = sum(weight(s[1]) for s in SHOTS)
    durs = [VOZ * weight(s[1]) / total for s in SHOTS]
    durs[-1] += COLA
    full = {"x": 0, "y": 0, "width": 1, "height": 1}
    scenes, overlays, t = [], [], 0.0
    overlays.append({"kind": "image", "src": RAW + "L_vineta.png", "start": 0, "duration": round(sum(durs), 2), "position": full})
    for i, ((src, habla, sub, extra, kb, tr), d) in enumerate(zip(SHOTS, durs)):
        url = RAW + f"{src}.png" if src in PROPIAS else (IMG.get(src) or VID[src])
        sc = {"source": url, "type": "image" if src in PROPIAS or src in IMG else "video", "duration": round(d, 2)}
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
            "music": {"audioUrl": "https://ai-music-tracks.s3.us-east-1.amazonaws.com/4065b5e6-8066-45ac-a648-6f0f86e15b82/74581a90-9381-4108-9197-4193bd755598.wav", "volume": 0.7, "duckTo": 0.25, "fadeMs": 400}}


if __name__ == "__main__":
    capas()
    p = plan()
    (OUT / "compose.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    print(len(p["scenes"]), "escenas ·", len(p["overlays"]), "capas ·", round(sum(s["duration"] for s in p["scenes"]), 2), "s")
    for s, (src, *_ ) in zip(p["scenes"], SHOTS):
        print(f'{src:12s} {s["duration"]}')
