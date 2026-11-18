"""Capas y plan de montaje de la Parte 02 del crucero (vidIQ compose)."""
import sys, pathlib, json, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p02"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p02/"
VOZ = 63.71; COLA = 2.5
VOZ_URL = "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/969ab1bf-7d79-48e0-9d14-02eaa1261d19.mp3"
IMG = {
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "aerea": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/13a55cbe-ad2c-48f9-a935-e566a67a7a83.jpeg",
 "popa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/5afabeb8-e91c-42a9-8a13-f2620868b45e.jpeg",
 "platos": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/8258aafb-ab1d-446d-bf6b-1be01764f429.jpeg",
 "noa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/98a941fa-c2b9-46f8-894e-70212240d71d.jpeg",
}
PROPIAS = ("historias", "ficha", "chat", "sinservicio")
VID = {  # Pexels: hello aesthe, RDNE Stock project, Aleks Magnusson, Angkel Lee, Doğu Tuncer, Sururi Ballıdağ, Ahmed, Pavel Danilyuk, Timur Weber
 "cama": "https://videos.pexels.com/video-files/15404180/15404180-hd_1080_1920_30fps.mp4",
 "scroll": "https://videos.pexels.com/video-files/10374888/10374888-hd_720_1280_24fps.mp4",
 "atardecer": "https://videos.pexels.com/video-files/17352384/17352384-hd_1080_1920_60fps.mp4",
 "piscina": "https://videos.pexels.com/video-files/28195522/12324262_360_640_30fps.mp4",
 "brindis": "https://videos.pexels.com/video-files/14549646/14549646-hd_720_1280_25fps.mp4",
 "gente": "https://videos.pexels.com/video-files/27403612/12136004_360_640_30fps.mp4",
 "horizonte": "https://videos.pexels.com/video-files/13663887/13663887-hd_720_1280_60fps.mp4",
 "maleta": "https://videos.pexels.com/video-files/4407779/4407779-hd_720_1280_30fps.mp4",
 "panuelo": "https://videos.pexels.com/video-files/9142477/9142477-hd_1080_1920_30fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
# (fuente, tipo, texto hablado, subtítulo, extra, kenburns, transición)
SHOTS = [
 ("maestro", "image", "Mi hermana publicó todos los días.", "Mi hermana publicó *todos* los días.", "", KB(1.0, .5, .55, 1.1, .55, .55), "cut"),
 ("popa", "image", "Desde un barco que no existía.", "Desde un barco que *no* *existía*.", "chip:6-OCT · 00:12|LOCALIZADOR APAGADO", KB(1.0, .5, .5, 1.12, .5, .45), "fade"),
 ("historias", "image", "Once días sin señal. Once historias.", "Once días *sin* *señal*. Once historias.", "sello:11 HISTORIAS", KB(1.0, .5, .45, 1.06, .5, .45), "fade"),
 ("cama", "video", "Me senté en su cama, en el siete uno uno cuatro,", "Me senté en su cama, en el *7114*,", "chip:17-OCT · 11:42|CAMAROTE 7114", None, "dip_to_black"),
 ("scroll", "video", "y las vi una a una.", "y las vi *una* *a* *una*.", "", None, "cut"),
 ("atardecer", "video", "Día uno: un atardecer en cubierta.", "Día 1: un atardecer en *cubierta*.", "historia:1|6-OCT", None, "cut"),
 ("piscina", "video", "Día dos: la piscina.", "Día 2: la *piscina*.", "historia:2|7-OCT", None, "cut"),
 ("brindis", "video", "Día tres: un brindis en el comedor.", "Día 3: un *brindis* en el comedor.", "historia:3|8-OCT", None, "cut"),
 ("ficha", "image", "Noa tiene veintinueve años y vive de contar sus viajes.", "Noa tiene *29* años y vive de contar sus *viajes*.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("chat", "image", "Antes de zarpar me escribió: \"Ven conmigo\". No fui.", "Me escribió: «Ven conmigo». *No* *fui*.", "", KB(1.0, .5, .45, 1.08, .5, .42), "fade"),
 ("gente", "video", "En sus historias todo era normal. Demasiado normal.", "Todo era normal. *Demasiado* normal.", "", None, "fade"),
 ("aerea", "image", "Un barco desaparecido, y nadie parecía preocupado.", "Un barco desaparecido. Y nadie *preocupado*.", "", KB(1.25, .5, .5, 1.45, .45, .5), "fade"),
 ("horizonte", "video", "Nadie buscaba cobertura. Nadie miraba el horizonte.", "Nadie buscaba *cobertura*. Nadie miraba el horizonte.", "", None, "fade"),
 ("sinservicio", "image", "¿Cómo publicaba sin señal?", "¿Cómo publicaba *sin* *señal*?", "sello:SIN SEÑAL", KB(1.0, .5, .45, 1.1, .5, .45), "cut"),
 ("noa", "image", "Día siete. Noa sonríe en la popa. El viento le mueve un pañuelo verde.", "Día 7. El viento le mueve un pañuelo *verde*.", "historia:7|12-OCT", KB(1.0, .45, .4, 1.12, .5, .5), "dip_to_black"),
 ("maleta", "video", "Me levanté. Abrí su maleta.", "Me levanté. Abrí su *maleta*.", "", None, "fade"),
 ("panuelo", "video", "Ahí estaba. El mismo pañuelo verde. Doblado. Con la etiqueta puesta.", "El mismo pañuelo verde. Con la *etiqueta* puesta.", "nota", None, "fade"),
 ("noa", "image", "Nunca se lo había puesto.", "*Nunca* se lo había puesto.", "historia:7|12-OCT", KB(1.6, .68, .62, 1.9, .7, .64), "cut"),
 ("platos", "image", "Entonces, ¿quién es la mujer de esa historia?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]


def weight(t):
    return len(t) + 6 * sum(t.count(p) for p in ".;:!?") + 3 * t.count(",")


def _datauri(path):
    import base64, io
    small = OUT / "_elena_small.jpg"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(path), "-vf", "scale=500:-2", "-q:v", "3", "-frames:v", "1", "-update", "1", str(small)], check=True)
    return "data:image/jpeg;base64," + base64.b64encode(small.read_bytes()).decode()



def _inner(svg):
    return svg.split(">", 1)[1].rsplit("</svg>", 1)[0]


def _blur(src, out, b=-0.28):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf",
                    f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness={b}:saturation=0.6",
                    "-frames:v", "1", "-update", "1", str(out)], check=True)
    return out


def _datauri(path, name):
    import base64
    small = OUT / f"_{name}_small.jpg"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(path), "-vf", "crop=iw:iw*1.27:0:ih*0.12,scale=500:-2", "-q:v", "3", "-frames:v", "1", "-update", "1", str(small)], check=True)
    return "data:image/jpeg;base64," + base64.b64encode(small.read_bytes()).decode()


def _movil(contenido):
    return (f'<rect x="230" y="420" width="620" height="1180" rx="70" fill="#050708" stroke="#3a4648" stroke-width="10"/>'
            f'<rect x="262" y="470" width="556" height="1080" rx="40" fill="#0f1416"/>' + contenido)


def _historias11():
    S = C.SANS
    body = f'<text x="300" y="545" {S} font-size="24" fill="{C.MUTE}">11:42</text><text x="780" y="545" {S} font-size="22" fill="{C.RED}" text-anchor="end">SIN SERVICIO</text>'
    body += f'<text x="300" y="610" {S} font-size="34" fill="{C.ICE}">noa.viaja</text><text x="300" y="648" {S} font-size="24" fill="{C.MUTE}">Tus historias · 11</text>'
    for i in range(11):
        x, y = 300 + (i % 3) * 165, 680 + (i // 3) * 160
        body += (f'<rect x="{x}" y="{y}" width="150" height="150" rx="14" fill="{C.TEAL}" stroke="{C.ICE}" stroke-opacity="0.35" stroke-width="2"/>'
                 f'<text x="{x + 75}" y="{y + 62}" {S} font-size="30" fill="{C.ICE}" text-anchor="middle">DÍA {i + 1}</text>'
                 f'<text x="{x + 75}" y="{y + 96}" {S} font-size="20" fill="{C.MUTE}" text-anchor="middle">{i + 6}-OCT</text>'
                 f'<text x="{x + 75}" y="{y + 132}" {S} font-size="18" fill="#7fd18b" text-anchor="middle">Publicada</text>')
    return C._svg(_movil(body))


def _sinservicio():
    S = C.SANS
    body = (f'<text x="300" y="545" {S} font-size="24" fill="{C.MUTE}">12-OCT</text>'
            f'<text x="780" y="545" {S} font-size="24" fill="{C.RED}" text-anchor="end">SIN SERVICIO</text>'
            f'<g transform="translate(540 760)" fill="none" stroke="{C.MUTE}" stroke-width="10" stroke-linecap="round">'
            f'<rect x="-75" y="20" width="22" height="40" fill="{C.MUTE}" stroke="none"/><rect x="-35" y="-5" width="22" height="65" fill="{C.MUTE}" stroke="none" opacity="0.4"/>'
            f'<rect x="5" y="-30" width="22" height="90" fill="{C.MUTE}" stroke="none" opacity="0.4"/><rect x="45" y="-55" width="22" height="115" fill="{C.MUTE}" stroke="none" opacity="0.4"/>'
            f'<line x1="-90" y1="-70" x2="90" y2="80" stroke="{C.RED}"/></g>'
            f'<text x="540" y="900" {S} font-size="34" fill="{C.ICE}" text-anchor="middle">Sin conexión</text>'
            f'<rect x="290" y="980" width="500" height="160" rx="28" fill="{C.ICE}" fill-opacity="0.94"/>'
            f'<circle cx="345" cy="1035" r="30" fill="{C.TEAL}"/><text x="345" y="1046" {S} font-size="28" fill="{C.ICE}" text-anchor="middle">N</text>'
            f'<text x="390" y="1030" {S} font-size="26" fill="#111">noa.viaja</text><text x="770" y="1030" {S} font-size="22" fill="#555" text-anchor="end">ahora</text>'
            f'<text x="390" y="1075" {S} font-size="28" fill="#222">Tu historia se ha</text><text x="390" y="1113" {S} font-size="28" fill="#222">publicado · DÍA 7</text>')
    return C._svg(_movil(body))


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
    V.componer(bgm, [_encoger(render(_historias11(), OUT / "_hist.png"))], OUT / "historias.png")
    ficha = render(C.ficha("Noa", "Pasajera · camarote 7114 · creadora de contenido de viajes",
                           ["EDAD: 29", "PARENTESCO: hermana de", "la Dra. Varela"],
                           foto=_datauri(ROOT / "crucero/maestro/noa.jpg", "noa")), OUT / "_ficha.png")
    V.componer(bgm, [ficha], OUT / "ficha.png")
    V.componer(bgc, [_encoger(render(C.chat("Noa", "30 de septiembre", "Ven conmigo"), OUT / "_chat.png"))], OUT / "chat.png")
    V.componer(bgm, [_encoger(render(_sinservicio(), OUT / "_sin.png"))], OUT / "sinservicio.png")
    V.capa(V.vineta(), OUT / "L_vineta.png")
    V.capa(V.portada(2, "Publicó *todos* los días"), OUT / "L_portada.png")
    for i, (src, tipo, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Quién es la *mujer* de esa historia?", "PARTE 03 EL VIERNES")
        else:
            body = (V.sub(sub) if sub else "")
            if "historia:" not in extra:
                body = V.barra() + body
            for e in filter(None, extra.split(";")):
                if e.startswith("chip:"):
                    body += V.chip(e[5:].split("|"), y=200)
                elif e.startswith("sello:"):
                    body += V.sello(e[6:], 540, 320 if src in PROPIAS else 820, -6, 60)
                elif e.startswith("historia:"):
                    d, f = e[9:].split("|")
                    body += _inner(C.historia("noa.viaja", int(d), f))
                elif e == "nota":
                    body += _inner(C.nota_forense(["Maleta · camarote 7114", "pañuelo verde", "etiqueta intacta", "→ sin uso"]))
        V.capa(body, OUT / f"L{i:02d}.png")


def plan():
    total = sum(weight(s[2]) for s in SHOTS)
    durs = [VOZ * weight(s[2]) / total for s in SHOTS]
    durs[-1] += COLA
    scenes, overlays, t = [], [], 0.0
    overlays.append({"kind": "image", "src": RAW + "L_vineta.png", "start": 0, "duration": round(sum(durs), 2), "position": {"x": 0, "y": 0, "width": 1, "height": 1}})
    for i, ((src, tipo, habla, sub, extra, kb, tr), d) in enumerate(zip(SHOTS, durs)):
        url = RAW + f"{src}.png" if src in PROPIAS else (IMG.get(src) or VID[src])
        sc = {"source": url, "type": "image" if src in PROPIAS or src in IMG else "video", "duration": round(d, 2)}
        if sc["type"] == "image" and kb:
            sc["kenBurns"] = kb
        if i and tr != "cut":
            sc["transitionIn"] = {"kind": tr, "duration": 0.3 if tr == "fade" else 0.4}
        scenes.append(sc)
        if i == 0:
            overlays.append({"kind": "image", "src": RAW + "L_portada.png", "start": 0, "duration": round(min(d, 2.2), 2), "position": {"x": 0, "y": 0, "width": 1, "height": 1}})
            st, dd = min(d, 2.2), max(d - 2.2, 0.01)
        else:
            st, dd = t, d
            st, dd = (t if i else 0), d
        if not (i == 0 and d <= 2.2):
            overlays.append({"kind": "image", "src": RAW + f"L{i:02d}.png", "start": round(st if i else 2.2, 2), "duration": round(dd, 2), "position": {"x": 0, "y": 0, "width": 1, "height": 1}})
        t += d
    return {"format": "vertical", "scenes": scenes, "overlays": overlays,
            "voiceover": {"audioUrl": VOZ_URL, "volume": 1.1},
            "music": {"audioUrl": "https://ai-music-tracks.s3.us-east-1.amazonaws.com/4065b5e6-8066-45ac-a648-6f0f86e15b82/74581a90-9381-4108-9197-4193bd755598.wav", "volume": 0.7, "duckTo": 0.25, "fadeMs": 400}}


if __name__ == "__main__":
    capas()
    p = plan()
    (OUT / "compose.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    print(len(p["scenes"]), "escenas ·", len(p["overlays"]), "capas ·", round(sum(s["duration"] for s in p["scenes"]), 2), "s")
