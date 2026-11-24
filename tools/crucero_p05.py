"""Capas y plan de montaje de la Parte 05 del crucero (vidIQ compose). Guion v2 «hilo conductor»."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render
from crucero_p03 import weight, _inner, _blur, _movil, _encoger
from crucero_p04 import _tachada

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p05"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p05/"
VOZ = 65.07; COLA = 2.5
VOZ_URL = "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/3c92ba30-fa25-43d1-9284-effa06e509ef.mp3"
IMG = {
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "comedor": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/89ba9c1f-6c89-42bc-b73b-4d544cc7cb41.jpeg",
 "popa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/5afabeb8-e91c-42a9-8a13-f2620868b45e.jpeg",
}
PROPIAS = ("tachada", "diario", "radio", "radio2")
AUTORES = ["Diego Castro Calderon", "Rafael Fernanz", "cottonbro studio", "Matthias Groeneveld", "Cemrecan Yurtman",
           "Sahil Sharma", "Artem Podrez", "Yusuf Çelik", "정규송 Nui MALAMA", "Los Muertos Crew", "Djimmer Koster"]
VID = {
 "maquinas": "https://videos.pexels.com/video-files/35069358/14855312_1080_1920_30fps.mp4",
 "linterna": "https://videos.pexels.com/video-files/18866694/18866694-hd_1080_1920_30fps.mp4",
 "precinto": "https://videos.pexels.com/video-files/10476428/10476428-hd_1080_2048_25fps.mp4",
 "corredor": "https://videos.pexels.com/video-files/15365457/15365457-hd_1080_1920_30fps.mp4",
 "salvavidas": "https://videos.pexels.com/video-files/34208169/14498612_1080_1920_25fps.mp4",
 "libro": "https://videos.pexels.com/video-files/11384843/11384843-hd_1080_1920_25fps.mp4",
 "papeles": "https://videos.pexels.com/video-files/7235113/7235113-hd_1080_1920_30fps.mp4",
 "consola": "https://videos.pexels.com/video-files/38868674/16523089_1080_1920_25fps.mp4",
 "olas": "https://videos.pexels.com/video-files/35072027/14856546_1080_1920_30fps.mp4",
 "movil": "https://videos.pexels.com/video-files/8810534/8810534-hd_1080_1920_24fps.mp4",
 "costa": "https://videos.pexels.com/video-files/30084348/12902923_1080_1920_30fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
# Sin chips de fecha/hora/lugar (norma del 20-nov): lo dice la narración.
SHOTS = [
 ("tachada", "Lo que sabemos: las historias del barco mienten.", "Las historias del barco *mienten*.", "", KB(1.0, .5, .45, 1.06, .5, .45), "cut"),
 ("comedor", "Rosa no estaba donde salía bailando.", "Rosa *no* *estaba* donde salía bailando.", "historia:rosa.mendez|5|10-OCT", KB(1.0, .5, .5, 1.1, .5, .5), "fade"),
 ("maquinas", "Y alguien golpeaba debajo de nosotros.", "Alguien *golpeaba* debajo de nosotros.", "sello:TOC · TOC · TOC", None, "cut"),
 ("linterna", "Bajamos hacia los golpes.", "Bajamos hacia los *golpes*.", "", None, "dip_to_black"),
 ("precinto", "Rey rompió el precinto de la cubierta tres.", "Rey rompió el *precinto* de la cubierta 3.", "", None, "cut"),
 ("corredor", "Los golpes pararon. No había nadie.", "Los golpes pararon. No había *nadie*.", "", None, "fade"),
 ("salvavidas", "Solo, junto a la barandilla, un soporte vacío. Faltaba un salvavidas.", "Un soporte vacío. Faltaba un *salvavidas*.", "sello:FALTA 1", None, "cut"),
 ("maestro", "Subimos al puente.", "Subimos al *puente*.", "", KB(1.3, .55, .4, 1.5, .55, .38), "dip_to_black"),
 ("libro", "El diario de navegación seguía en su sitio.", "El *diario* de navegación seguía en su sitio.", "", None, "fade"),
 ("diario", "Cinco de octubre, veintitrés cuarenta: último contacto por radio. Después, nada.", "5 de octubre, 23:40: *último* *contacto*. Después, nada.", "", KB(1.0, .5, .45, 1.06, .5, .42), "cut"),
 ("papeles", "Alguien había arrancado la página siguiente.", "Alguien había *arrancado* la página siguiente.", "nota", None, "fade"),
 ("consola", "En la consola de radio, un mensaje guardado.", "En la radio, un mensaje *guardado*.", "", None, "dip_to_black"),
 ("radio", "\"Hombre al agua\". Seis de octubre, dos y cinco de la madrugada.", "«Hombre al *agua*». 6 de octubre, 02:05.", "", KB(1.0, .5, .45, 1.08, .5, .45), "cut"),
 ("radio2", "Escrito. Nunca enviado.", "Escrito. *Nunca* *enviado*.", "sello:NUNCA ENVIADO", KB(1.08, .5, .45, 1.12, .5, .45), "cut"),
 ("olas", "Alguien cayó al mar, alguien lo vio, y alguien decidió no pedir ayuda.", "Alguien decidió *no* *pedir* *ayuda*.", "", None, "fade"),
 ("maestro2", "Esa noche remolcaron el Perséfone hacia Las Palmas.", "Esa noche lo remolcaron hacia *Las* *Palmas*.", "", KB(1.0, .5, .5, 1.15, .45, .5), "dip_to_black"),
 ("movil", "A las diez sonó mi teléfono. Era Madeira.", "Sonó mi teléfono. Era *Madeira*.", "", None, "cut"),
 ("costa", "El mar había devuelto un cuerpo. Llevaba el uniforme de la tripulación del Perséfone.", "Un *cuerpo*. Con el uniforme del *Perséfone*.", "", None, "fade"),
 ("popa", "¿Quién decidió no pedir ayuda?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]


def _diario():
    """Página del diario de navegación con la última anotación."""
    S, M = C.SANS, C.MONO
    body = f'<g transform="rotate(-2 540 800)"><rect x="140" y="440" width="800" height="740" fill="#efe6cc" stroke="#6b5a3a" stroke-width="4"/>'
    body += f'<text x="540" y="510" {S} font-size="34" fill="#3b2f1c" text-anchor="middle">DIARIO DE NAVEGACIÓN · PERSÉFONE</text>'
    body += '<line x1="170" y1="540" x2="910" y2="540" stroke="#6b5a3a" stroke-width="3"/>'
    filas = [("05-OCT 18:00", "Rumbo 245 · mar en calma"), ("05-OCT 21:15", "Sin novedad"), ("05-OCT 23:40", "Último contacto radio")]
    for i, (h, t) in enumerate(filas):
        y = 620 + 110 * i
        col = C.RED if i == 2 else "#1a2a6c"
        body += f'<text x="180" y="{y}" {M} font-size="32" fill="{col}">{h}</text>'
        body += f'<text x="460" y="{y}" font-family="DejaVu Serif" font-style="italic" font-size="31" fill="{col}">{t}</text>'
        body += f'<line x1="170" y1="{y + 30}" x2="910" y2="{y + 30}" stroke="#b9a77f" stroke-width="2"/>'
    body += f'<rect x="170" y="960" width="740" height="180" fill="none" stroke="{C.RED}" stroke-width="5" stroke-dasharray="18 12"/>'
    body += f'<text x="540" y="1065" {S} font-size="38" fill="{C.RED}" text-anchor="middle">DESPUÉS, NADA</text>'
    return C._svg(body + "</g>")


def _radio():
    """Pantalla de la consola de radio con el aviso guardado."""
    S, M = C.SANS, C.MONO
    g = "#39d98a"
    body = f'<rect x="120" y="560" width="840" height="640" rx="30" fill="#0a0f0d" stroke="#3a4648" stroke-width="12"/>'
    body += f'<text x="170" y="640" {M} font-size="30" fill="{g}">DSC · MENSAJES GUARDADOS (1)</text>'
    body += f'<line x1="160" y1="665" x2="920" y2="665" stroke="{g}" stroke-opacity="0.5" stroke-width="2"/>'
    body += f'<text x="540" y="790" {S} font-size="86" fill="{C.RED}" text-anchor="middle">MOB</text>'
    body += f'<text x="540" y="870" {S} font-size="52" fill="#fff" text-anchor="middle">HOMBRE AL AGUA</text>'
    body += f'<text x="540" y="960" {M} font-size="40" fill="{g}" text-anchor="middle">06-OCT · 02:05</text>'
    body += f'<rect x="300" y="1030" width="480" height="90" rx="10" fill="none" stroke="{C.RED}" stroke-width="5"/>'
    body += f'<text x="540" y="1090" {M} font-size="42" fill="{C.RED}" text-anchor="middle">NO ENVIADO</text>'
    return C._svg(body)


def capas():
    bgm = _blur(ROOT / "crucero/maestro/barco_maestro.jpg", OUT / "_bg_maestro.png")
    bgc = _blur(ROOT / "crucero/p01/img/comedor.jpg", OUT / "_bg_comedor.png", -0.3)
    V.componer(bgc, [_encoger(render(_tachada(), OUT / "_tach.png"))], OUT / "tachada.png")
    V.componer(bgm, [render(_diario(), OUT / "_diario.png")], OUT / "diario.png")
    rad = render(_radio(), OUT / "_radio.png")
    V.componer(bgm, [rad], OUT / "radio.png")
    V.componer(bgm, [rad], OUT / "radio2.png")
    V.capa(V.vineta(), OUT / "L_vineta.png")
    V.capa(V.portada(5, "Falta un *salvavidas*"), OUT / "L_portada.png")
    for i, (src, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Quién decidió no pedir *ayuda*?", "PARTE 06 EL JUEVES")
        else:
            body = (V.sub(sub) if sub else "")
            if "historia:" not in extra:
                body = V.barra() + body
            for e in filter(None, extra.split(";")):
                if e.startswith("sello:"):
                    t = e[6:]
                    body += V.sello(t, 540, 400 if src in PROPIAS else 820, -6, 60 if len(t) < 14 else 48)
                elif e.startswith("historia:"):
                    u, d, f = e[9:].split("|")
                    body += _inner(C.historia(u, int(d), f))
                elif e == "nota":
                    body += _inner(C.nota_forense(["diario de navegación", "falta 1 hoja", "corte irregular"]))
        V.capa(body, OUT / f"L{i:02d}.png")


def plan():
    total = sum(weight(s[1]) for s in SHOTS)
    durs = [VOZ * weight(s[1]) / total for s in SHOTS]
    durs[-1] += COLA
    full = {"x": 0, "y": 0, "width": 1, "height": 1}
    scenes, overlays, t = [], [], 0.0
    overlays.append({"kind": "image", "src": RAW + "L_vineta.png", "start": 0, "duration": round(sum(durs), 2), "position": full})
    for i, ((src, habla, sub, extra, kb, tr), d) in enumerate(zip(SHOTS, durs)):
        key = src.rstrip("2")
        url = RAW + f"{src}.png" if src in PROPIAS else (IMG.get(key) or VID[key])
        sc = {"source": url, "type": "image" if src in PROPIAS or key in IMG else "video", "duration": round(d, 2)}
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
