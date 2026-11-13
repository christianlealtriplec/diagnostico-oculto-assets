"""Capas y plan de montaje de la Parte 01 del crucero (vidIQ compose)."""
import sys, pathlib, json, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p01"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p01/"
VOZ = 53.55; COLA = 2.5
IMG = {
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "aerea": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/13a55cbe-ad2c-48f9-a935-e566a67a7a83.jpeg",
 "popa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/5afabeb8-e91c-42a9-8a13-f2620868b45e.jpeg",
 "comedor": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/89ba9c1f-6c89-42bc-b73b-4d544cc7cb41.jpeg",
 "platos": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/8258aafb-ab1d-446d-bf6b-1be01764f429.jpeg",
}
VID = {
 "pesquero": "https://videos.pexels.com/video-files/16347802/16347802-hd_1080_1920_60fps.mp4",
 "oceano": "https://videos.pexels.com/video-files/8820114/8820114-hd_1080_1920_25fps.mp4",
 "pasillo": "https://videos.pexels.com/video-files/10577869/10577869-hd_2160_3840_30fps.mp4",
 "pasillo2": "https://videos.pexels.com/video-files/6010698/6010698-hd_1080_1920_25fps.mp4",
 "ropa": "https://videos.pexels.com/video-files/9146503/9146503-hd_1080_1920_30fps.mp4",
 "movil": "https://videos.pexels.com/video-files/7822022/7822022-hd_1080_1920_30fps.mp4",
 "hermana": "https://videos.pexels.com/video-files/14993817/14993817-hd_720_1280_60fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
# (fuente, tipo, texto hablado, subtítulo en pantalla, extra, kenburns, transición)
SHOTS = [
 ("maestro", "image", "\"La comida aún está caliente\".", "«La comida aún está *caliente*»", "", KB(1.0, .5, .55, 1.1, .55, .55), "cut"),
 ("platos", "image", "Eso dijo por radio", "Eso dijo por *radio*", "chip:06:52 · RADIO|PESQUERO «SANTA BÁRBARA»", KB(1.0, .5, .6, 1.12, .5, .62), "fade"),
 ("pesquero", "video", "el patrón de un pesquero portugués", "el patrón de un pesquero *portugués*", "", None, "fade"),
 ("oceano", "video", "a las seis y cincuenta y dos de la mañana.", "a las *6:52* de la mañana.", "", None, "fade"),
 ("aerea", "image", "Acababa de subir a un crucero que llevaba once días desaparecido:", "Un crucero desaparecido hace *once días*", "chip:17-OCT · 06:30|29°14'N 21°40'W;sello:11 DÍAS SIN RASTRO", KB(1.0, .5, .5, 1.15, .5, .45), "fade"),
 ("maestro", "image", "el Perséfone.", "el *Perséfone*.", "", KB(1.4, .62, .55, 1.2, .55, .55), "fade"),
 ("ficha", "image", "Me llamo Elena Varela. Soy médica forense.", "Me llamo Elena Varela. Soy *médica* *forense*.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("pasillo", "video", "A las once subí a bordo con la Guardia Civil.", "A las once subí a bordo con la *Guardia* *Civil*.", "chip:17-OCT · 11:00", None, "fade"),
 ("pasillo2", "video", "No había nadie.", "No había *nadie*.", "", None, "cut"),
 ("comedor", "image", "Quinientas noventa personas, y ni una.", "*590* personas. Y ni una.", "chip:A BORDO: 590|ENCONTRADAS: 0", KB(1.0, .5, .6, 1.1, .5, .55), "fade"),
 ("ropa", "video", "Luces encendidas. Maletas en los camarotes.", "Luces encendidas. *Maletas* en los camarotes.", "", None, "fade"),
 ("comedor", "image", "En el comedor, cuatrocientos platos servidos.", "*400* platos servidos.", "", KB(1.35, .62, .72, 1.6, .55, .78), "fade"),
 ("platos", "image", "Ya fríos. Pero frescos: ni moho, ni olor.", "Ya fríos. Pero *frescos*: ni moho, ni olor.", "nota", KB(1.25, .45, .7, 1.45, .45, .72), "fade"),
 ("aerea", "image", "Esa comida no tenía once días. La habían servido esa misma madrugada.", "No tenía once días. La sirvieron *esa* *madrugada*.", "", KB(1.3, .5, .5, 1.5, .5, .5), "fade"),
 ("pasillo2", "video", "Pasillo siete. Camarote siete uno uno cuatro.", "Pasillo 7. Camarote *7114*.", "chip:PASILLO 7 · CAMAROTE 7114", None, "dip_to_black"),
 ("movil", "video", "Sobre la cama, un móvil vibró.", "Sobre la cama, un móvil *vibró*.", "", None, "cut"),
 ("pantalla", "image", "\"Tu historia se ha publicado\".", "«Tu historia se ha *publicado*»", "", KB(1.0, .5, .45, 1.08, .5, .45), "cut"),
 ("hermana", "video", "La cuenta era de una pasajera desaparecida. Era mi hermana.", "Era de una pasajera desaparecida. Era *mi* *hermana*.", "", None, "fade"),
 ("popa", "image", "¿Quién publicó esa historia?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]


def weight(t):
    return len(t) + 6 * sum(t.count(p) for p in ".;:!?") + 3 * t.count(",")


def _datauri(path):
    import base64, io
    small = OUT / "_elena_small.jpg"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(path), "-vf", "scale=500:-2", "-q:v", "3", "-frames:v", "1", "-update", "1", str(small)], check=True)
    return "data:image/jpeg;base64," + base64.b64encode(small.read_bytes()).decode()


def capas():
    # escenas propias: ficha de Elena y pantalla del móvil, sobre el barco maestro desenfocado
    bgm = OUT / "_bg_maestro.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(ROOT / "crucero/maestro/barco_maestro.jpg"), "-vf",
                    f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.28:saturation=0.6",
                    "-frames:v", "1", "-update", "1", str(bgm)], check=True)
    ficha = render(C.ficha("Dra. Elena Varela", "Médica forense · Instituto de Medicina Legal de Las Palmas",
                           ["ABORDA: 17-OCT 11:00", "PARENTESCO: hermana de", "una pasajera (7114)"],
                           foto=_datauri(ROOT / "crucero/maestro/elena.jpg")), OUT / "_ficha.png")
    V.componer(bgm, [ficha], OUT / "ficha.png")
    blur_c = OUT / "_bg_comedor.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(OUT / "img/comedor.jpg"), "-vf",
                    f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2,eq=brightness=-0.3",
                    "-frames:v", "1", "-update", "1", str(blur_c)], check=True)
    tel = C.notificacion("noa.viaja", "Tu historia se ha publicado", "ahora").replace("06:31", "11:42")
    V.componer(blur_c, [render(tel, OUT / "_tel.png")], OUT / "pantalla.png")
    # capas por plano
    V.capa(V.vineta(), OUT / "L_vineta.png")
    V.capa(V.portada(1, "La comida aún estaba *caliente*"), OUT / "L_portada.png")
    for i, (src, tipo, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Quién *publicó* esa historia?", "PARTE 02 EN EL PERFIL")
        else:
            body = V.barra() + (V.sub(sub) if sub else "")
            for e in filter(None, extra.split(";")):
                if e.startswith("chip:"):
                    body += V.chip(e[5:].split("|"), y=200)
                elif e.startswith("sello:"):
                    body += V.sello(e[6:], 540, 820, -6, 60)
                elif e == "nota":
                    body += C.nota_forense(["Comedor Atlántico · 11:00", "400 platos · fríos", "sin moho, sin olor", "→ servidos < 12 h"]).split(">", 1)[1].rsplit("</svg>", 1)[0]
        V.capa(body, OUT / f"L{i:02d}.png")


def plan():
    total = sum(weight(s[2]) for s in SHOTS)
    durs = [VOZ * weight(s[2]) / total for s in SHOTS]
    durs[-1] += COLA
    scenes, overlays, t = [], [], 0.0
    overlays.append({"kind": "image", "src": RAW + "L_vineta.png", "start": 0, "duration": round(sum(durs), 2), "position": {"x": 0, "y": 0, "width": 1, "height": 1}})
    for i, ((src, tipo, habla, sub, extra, kb, tr), d) in enumerate(zip(SHOTS, durs)):
        url = RAW + f"{src}.png" if src in ("ficha", "pantalla") else (IMG.get(src) or VID[src])
        sc = {"source": url, "type": "image" if src in ("ficha", "pantalla") or src in IMG else "video", "duration": round(d, 2)}
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
            "voiceover": {"audioUrl": "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/e686eaa6-1cf8-4680-9208-1c50ff13a327.mp3", "volume": 1.1},
            "music": {"audioUrl": "https://ai-music-tracks.s3.us-east-1.amazonaws.com/4065b5e6-8066-45ac-a648-6f0f86e15b82/74581a90-9381-4108-9197-4193bd755598.wav", "volume": 0.7, "duckTo": 0.25, "fadeMs": 400}}


if __name__ == "__main__":
    capas()
    p = plan()
    (OUT / "compose.json").write_text(json.dumps(p, ensure_ascii=False, indent=1))
    print(len(p["scenes"]), "escenas ·", len(p["overlays"]), "capas ·", round(sum(s["duration"] for s in p["scenes"]), 2), "s")
