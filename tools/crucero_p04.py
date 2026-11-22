"""Capas y plan de montaje de la Parte 04 del crucero (vidIQ compose). Guion v2 «hilo conductor»."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render
from crucero_p03 import weight, _inner, _blur, _movil, _encoger

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p04"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p04/"
VOZ = 71.31; COLA = 2.5
VOZ_URL = "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/3648fb93-180b-45f7-af13-833e577369ae.mp3"
IMG = {
 "foto": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/3b75261f-1807-43f7-870e-62228452c7bf.jpeg",
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "comedor": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/89ba9c1f-6c89-42bc-b73b-4d544cc7cb41.jpeg",
 "aerea": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/13a55cbe-ad2c-48f9-a935-e566a67a7a83.jpeg",
}
PROPIAS = ("ficha", "tachada")
AUTORES = ["Kuiyibo Campos", "Mizuno K", "Artem Podrez", "Zenia Diamond", "cottonbro studio", "Alex Green",
           "Ramazan Toygun", "Yaroslav Shuraev", "Tima Miroshnichenko", "Airam Dato-on", "Mikhail Nilov", "Ali Alcántara",
           "Yaroslav Shuraev"]
VID = {
 "servidores": "https://videos.pexels.com/video-files/28709421/12457750_1080_1920_30fps.mp4",
 "ventana": "https://videos.pexels.com/video-files/13801255/13801255-hd_1080_1920_24fps.mp4",
 "espalda": "https://videos.pexels.com/video-files/7599305/7599305-hd_1080_2048_25fps.mp4",
 "corredor": "https://videos.pexels.com/video-files/37572085/15921474_1080_1920_30fps.mp4",
 "puerta5008": "https://videos.pexels.com/video-files/6466565/6466565-hd_1080_2048_25fps.mp4",
 "baile": "https://videos.pexels.com/video-files/6624531/6624531-hd_1080_1920_24fps.mp4",
 "cubierta": "https://videos.pexels.com/video-files/35596349/15085071_1080_1920_30fps.mp4",
 "pastillero": "https://videos.pexels.com/video-files/8088659/8088659-hd_1080_2048_24fps.mp4",
 "blister": "https://videos.pexels.com/video-files/5406014/5406014-hd_1080_1920_25fps.mp4",
 "salon": "https://videos.pexels.com/video-files/37410282/15844398_1080_1620_30fps.mp4",
 "libreta": "https://videos.pexels.com/video-files/8873342/8873342-hd_1080_1920_25fps.mp4",
 "escalera": "https://videos.pexels.com/video-files/6279825/6279825-hd_1080_1920_24fps.mp4",
 "pasillo": "https://videos.pexels.com/video-files/7251759/7251759-hd_1080_1920_25fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
# Sin chips de fecha/hora/lugar (norma del 20-nov): lo dice la narración.
SHOTS = [
 ("foto", "Lo que sabemos: alguien hizo fotos que nadie pudo hacer.", "Alguien hizo fotos que *nadie* pudo hacer.", "historia:noa.viaja|8|13-OCT · 23:51", KB(1.0, .5, .5, 1.1, .5, .52), "cut"),
 ("servidores", "Y el inspector Rey fue directo a una sala que decía no conocer.", "Rey fue *directo* a una sala que decía no conocer.", "", None, "fade"),
 ("servidores2", "17 de octubre, mediodía. Sala de servidores.", "17 de octubre, mediodía. Sala de *servidores*.", "", None, "dip_to_black"),
 ("ventana", "Le pregunté a Rey cómo la conocía.", "Le pregunté a Rey cómo la *conocía*.", "", None, "cut"),
 ("espalda", "\"Todos los barcos son iguales\", dijo. No le creí.", "«Todos los barcos son *iguales*». No le *creí*.", "", None, "cut"),
 ("maestro", "Pero había algo más urgente: si las fotos eran falsas, ¿dónde estaba de verdad la gente?", "Si las fotos eran falsas, ¿dónde estaba *la* *gente*?", "", KB(1.4, .65, .5, 1.6, .7, .5), "fade"),
 ("corredor", "Comparé las historias con los camarotes.", "Comparé las historias con los *camarotes*.", "", None, "fade"),
 ("puerta5008", "Camarote cinco cero cero ocho.", "Camarote *5008*.", "", None, "cut"),
 ("ficha", "Rosa Méndez, sesenta y siete años, viuda.", "Rosa Méndez, *67* años, viuda.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("baile", "En su cuenta, once días de fiesta: baila en el salón,", "Once días de fiesta: *baila* en el salón…", "historia:rosa.mendez|5|10-OCT", None, "fade"),
 ("cubierta", "canta en cubierta.", "…*canta* en cubierta.", "historia:rosa.mendez|8|13-OCT", None, "cut"),
 ("pastillero", "En su mesilla, un pastillero y tres blísteres del corazón.", "Un pastillero y tres blísteres del *corazón*.", "", None, "fade"),
 ("blister", "Los conté. Desde el seis de octubre no faltaba ni una pastilla.", "Desde el 6 de octubre, *ni* *una* menos.", "nota", None, "cut"),
 ("comedor", "Una paciente del corazón no deja su tratamiento once días para irse a bailar.", "Nadie deja su tratamiento *once* *días* para irse a bailar.", "", KB(1.0, .5, .5, 1.12, .45, .5), "fade"),
 ("salon", "Rosa no estaba en ese salón.", "Rosa *no* *estaba* en ese salón.", "sello:NO ESTABA AHÍ", None, "fade"),
 ("tachada", "Las historias ponían a la gente donde no estaba.", "Ponían a la gente donde *no* *estaba*.", "", KB(1.0, .5, .45, 1.06, .5, .45), "cut"),
 ("libreta", "Pista número cuatro. Catorce y diez.", "Pista número *cuatro*.", "sello:PISTA 4", None, "fade"),
 ("escalera", "Entonces lo oí. Tres golpes. Debajo de mis pies.", "*Tres* *golpes*. Debajo de mis pies.", "sello:TOC · TOC · TOC", None, "cut"),
 ("pasillo", "La cubierta de abajo estaba precintada. Y vacía.", "Precintada. Y *vacía*.", "sello:PRECINTADA", None, "fade"),
 ("aerea", "¿Quién golpeaba desde abajo?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]


def _tachada():
    """Historia de Rosa con la figura tachada en rojo."""
    S = C.SANS
    body = (f'<rect x="262" y="470" width="556" height="1080" rx="40" fill="#1b2a30"/>'
            f'<text x="300" y="545" {S} font-size="30" fill="#fff">rosa.mendez</text>'
            f'<text x="300" y="585" {S} font-size="24" fill="#ccc">DÍA 5 · 10-OCT · salón</text>'
            f'<circle cx="540" cy="860" r="70" fill="#9fb3b8"/>'
            f'<path d="M420,1260 Q430,980 540,960 Q650,980 660,1260 Z" fill="#9fb3b8"/>'
            f'<line x1="360" y1="760" x2="720" y2="1300" stroke="{C.RED}" stroke-width="26" stroke-linecap="round"/>'
            f'<line x1="720" y1="760" x2="360" y2="1300" stroke="{C.RED}" stroke-width="26" stroke-linecap="round"/>')
    return C._svg(_movil(body))


def capas():
    bgm = _blur(ROOT / "crucero/maestro/barco_maestro.jpg", OUT / "_bg_maestro.png")
    bgc = _blur(ROOT / "crucero/p01/img/comedor.jpg", OUT / "_bg_comedor.png", -0.3)
    V.componer(bgc, [_encoger(render(_tachada(), OUT / "_tach.png"))], OUT / "tachada.png")
    ficha = render(C.ficha("Rosa Méndez", "Pasajera · camarote 5008",
                           ["EDAD: 67", "ESTADO: viuda", "TRATAMIENTO: corazón"]), OUT / "_ficha.png")
    V.componer(bgm, [ficha], OUT / "ficha.png")
    V.capa(V.vineta(), OUT / "L_vineta.png")
    V.capa(V.portada(4, "Sus pastillas *seguían* ahí"), OUT / "L_portada.png")
    for i, (src, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Quién golpeaba desde *abajo*?", "PARTE 05 EL MARTES")
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
                    body += _inner(C.nota_forense(["Rosa Méndez · 5008", "pastillero: lleno desde 6-OCT", "blísteres: 0 tomas"]))
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
        if src == "servidores2":
            sc["startFromSeconds"] = 12
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
