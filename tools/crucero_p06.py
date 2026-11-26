"""Capas y plan de montaje de la Parte 06 del crucero (vidIQ compose). Guion v2 «hilo conductor»."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
import crucero as C
from draw import W, H, render
from crucero_p03 import weight, _inner, _blur, _movil, _encoger
from crucero_p04 import _tachada
from crucero_p02 import _sinservicio

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "p06"; OUT.mkdir(parents=True, exist_ok=True)
RAW = "https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/crucero/p06/"
VOZ = 65.65; COLA = 2.5
VOZ_URL = "https://assets.vidiq.com/voiceovers/4065b5e6-8066-45ac-a648-6f0f86e15b82/79fa4f8d-1635-4e0a-9e23-7720a0d78324.mp3"
IMG = {
 "maestro": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/95d097a9-3e21-4cb2-800c-d957b170c3b9.jpeg",
 "comedor": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/89ba9c1f-6c89-42bc-b73b-4d544cc7cb41.jpeg",
 "foto_imposible": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/3b75261f-1807-43f7-870e-62228452c7bf.jpeg",
 "noa": "https://ai-thumbnails.s3.amazonaws.com/editor/4065b5e6-8066-45ac-a648-6f0f86e15b82/98a941fa-c2b9-46f8-894e-70212240d71d.jpeg",
}
PROPIAS = ("tachada", "ficha", "memoria", "sinservicio", "apagados")
AUTORES = ["정규송 Nui MALAMA", "Armin Rimoldi", "Patt Garciia", "Nothing Ahead", "SHEMÁ", "Rahime Gül",
           "Mikhail Nilov", "Kuiyibo Campos", "RDNE Stock project", "Necip Duman"]
VID = {
 "olas": "https://videos.pexels.com/video-files/35072027/14856546_1080_1920_30fps.mp4",
 "galeria": "https://videos.pexels.com/video-files/5545115/5545115-hd_1080_1920_30fps.mp4",
 "puerto": "https://videos.pexels.com/video-files/36076441/15299929_1080_1920_30fps.mp4",
 "router": "https://videos.pexels.com/video-files/39918565/17032444_1080_1920_60fps.mp4",
 "cama": "https://videos.pexels.com/video-files/28048582/12290989_1080_1920_30fps.mp4",
 "cubierta": "https://videos.pexels.com/video-files/28945771/12525239_1080_1920_60fps.mp4",
 "tableta": "https://videos.pexels.com/video-files/6931255/6931255-hd_1080_1920_25fps.mp4",
 "datos": "https://videos.pexels.com/video-files/28709421/12457750_1080_1920_30fps.mp4",
 "vibra": "https://videos.pexels.com/video-files/7822022/7822022-hd_1080_1920_30fps.mp4",
 "muelle": "https://videos.pexels.com/video-files/39661168/16907265_1080_1920_50fps.mp4",
}
KB = lambda s0, x0, y0, s1, x1, y1: {"from": {"scale": s0, "x": x0, "y": y0}, "to": {"scale": s1, "x": x1, "y": y1}}
# Sin chips de fecha/hora/lugar (norma del 20-nov): lo dice la narración.
SHOTS = [
 ("olas", "Lo que sabemos: alguien cayó al mar y nadie pidió ayuda.", "Alguien cayó al mar y *nadie* pidió ayuda.", "", None, "cut"),
 ("tachada", "Y las historias del barco son mentira.", "Las historias del barco son *mentira*.", "", KB(1.0, .5, .45, 1.06, .5, .45), "fade"),
 ("galeria", "Pero ¿quién las escribía?", "¿*Quién* las escribía?", "", None, "cut"),
 ("puerto", "A la mañana siguiente, el Perséfone ya estaba amarrado en Las Palmas.", "A la mañana siguiente, amarrado en *Las* *Palmas*.", "", None, "dip_to_black"),
 ("router", "Junto a él, en una carpa, los servidores que se llevó Rey.", "En una carpa, los *servidores* que se llevó Rey.", "", None, "fade"),
 ("ficha", "Allí me esperaba Marco Bellini, el ingeniero que diseñó Memoria:", "*Marco* *Bellini*, el ingeniero que diseñó Memoria.", "", KB(1.0, .5, .45, 1.06, .5, .42), "dip_to_black"),
 ("memoria", "la IA de la naviera que escribía tus vacaciones por ti.", "La IA que escribía tus *vacaciones* por ti.", "", KB(1.0, .5, .45, 1.08, .5, .45), "fade"),
 ("comedor", "\"Usa las cámaras del barco y las fotos de cada pasajero.\"", "«Usa las *cámaras* del barco y las fotos de cada pasajero.»", "cctv", KB(1.0, .5, .5, 1.1, .5, .5), "cut"),
 ("cama", "\"Compone historias y las publica sola. Aunque estés durmiendo.\"", "«Las publica *sola*. Aunque estés durmiendo.»", "banner:noa.viaja|Tu historia se ha publicado", None, "fade"),
 ("foto_imposible", "¿Y las fotos imposibles?", "¿Y las fotos *imposibles*?", "pixeles", KB(1.0, .5, .45, 1.08, .5, .45), "dip_to_black"),
 ("foto_imposible2", "\"Cuando le falta una imagen, se la inventa.\"", "«Cuando le falta una imagen, se la *inventa*.»", "pixeles;sello:INVENTADA", KB(1.1, .5, .45, 1.2, .5, .42), "cut"),
 ("cubierta", "Por eso había fotos que nadie pudo hacer.", "Fotos que *nadie* pudo hacer.", "", None, "fade"),
 ("noa", "Las historias de mi hermana podían ser falsas. Todas.", "Las historias de mi hermana podían ser *falsas*. Todas.", "historia:7|12-OCT;sello:¿FALSAS?", KB(1.0, .45, .4, 1.12, .5, .5), "dip_to_black"),
 ("tableta", "¿Y cómo publicaba sin señal?", "¿Y cómo publicaba *sin* *señal*?", "", None, "cut"),
 ("sinservicio", "\"Sin conexión, no debería publicar nada.\"", "«Sin conexión, no debería publicar *nada*.»", "", KB(1.0, .5, .45, 1.08, .5, .45), "fade"),
 ("datos", "¿Se puede apagar?", "¿Se puede *apagar*?", "", None, "cut"),
 ("apagados", "\"Ya está apagada. Desconectamos los servidores ayer.\"", "«Ya está *apagada*. Desconectamos los servidores ayer.»", "sello:APAGADA", KB(1.0, .5, .45, 1.06, .5, .45), "dip_to_black"),
 ("vibra", "A las once, el móvil de Noa vibró en mi bolsillo. Nueva historia.", "A las once vibró el móvil de Noa. *Nueva* *historia*.", "banner:noa.viaja|Nueva historia", None, "cut"),
 ("muelle", "Era yo. En este muelle. Esa misma mañana.", "Era *yo*. En este muelle. Esa misma mañana.", "marco", None, "cut"),
 ("maestro", "¿Quién me hizo esa foto?", "", "cierre", KB(1.0, .5, .5, 1.12, .5, .45), "dip_to_black"),
]


def _memoria():
    """Logotipo genérico del sistema Memoria (marca inventada)."""
    S, M = C.SANS, C.MONO
    body = '<rect x="140" y="560" width="800" height="620" rx="30" fill="#0b1f24" fill-opacity="0.9" stroke="#e8f1f2" stroke-opacity="0.4" stroke-width="3"/>'
    body += f'<circle cx="540" cy="760" r="110" fill="none" stroke="{C.ICE}" stroke-width="10"/>'
    body += f'<circle cx="540" cy="760" r="62" fill="none" stroke="{C.RED}" stroke-width="10"/>'
    body += f'<circle cx="540" cy="760" r="18" fill="{C.ICE}"/>'
    body += f'<text x="540" y="985" {S} font-size="92" letter-spacing="14" fill="{C.ICE}" text-anchor="middle">MEMORIA</text>'
    body += f'<text x="540" y="1050" {M} font-size="32" fill="{C.MUTE}" text-anchor="middle">NAVIERA AURELIA</text>'
    body += f'<text x="540" y="1120" {S} font-size="30" fill="{C.MUTE}" text-anchor="middle">«Tus vacaciones, contadas por ti»</text>'
    return C._svg(body)


def _apagados():
    """Bastidores de servidores sin luces."""
    M = C.MONO
    body = f'<rect width="{W}" height="{H}" fill="#05080a"/>'
    for k, x in enumerate((150, 430, 710)):
        body += f'<rect x="{x}" y="420" width="220" height="1000" fill="#11181b" stroke="#2a3539" stroke-width="5"/>'
        for j in range(14):
            y = 450 + 68 * j
            body += f'<rect x="{x + 18}" y="{y}" width="184" height="52" fill="#182226" stroke="#26333a" stroke-width="2"/>'
            body += f'<circle cx="{x + 40}" cy="{y + 26}" r="7" fill="#2b3a3f"/><circle cx="{x + 62}" cy="{y + 26}" r="7" fill="#2b3a3f"/>'
    return C._svg(body)


def _banner(usuario, texto, y=300):
    S = C.SANS
    return (f'<rect x="120" y="{y}" width="840" height="170" rx="34" fill="{C.ICE}" fill-opacity="0.95"/>'
            f'<circle cx="200" cy="{y + 85}" r="44" fill="{C.TEAL}"/>'
            f'<text x="200" y="{y + 100}" {S} font-size="40" fill="{C.ICE}" text-anchor="middle">{C.esc(usuario[0].upper())}</text>'
            f'<text x="270" y="{y + 70}" {S} font-size="36" fill="#111">{C.esc(usuario)}</text>'
            f'<text x="920" y="{y + 70}" {S} font-size="28" fill="#555" text-anchor="end">ahora</text>'
            f'<text x="270" y="{y + 122}" {S} font-size="36" fill="#222">{C.esc(texto)}</text>')


def _cctv():
    M = C.MONO
    b = '<g fill="none" stroke="#fff" stroke-opacity="0.85" stroke-width="6">'
    for x, y, dx, dy in ((70, 270, 1, 1), (1010, 270, -1, 1), (70, 1130, 1, -1), (1010, 1130, -1, -1)):
        b += f'<path d="M{x},{y + 70 * dy} L{x},{y} L{x + 70 * dx},{y}"/>'
    b += '</g>'
    b += f'<circle cx="120" cy="330" r="16" fill="{C.RED}"/><text x="150" y="342" {M} font-size="36" fill="#fff">REC</text>'
    b += f'<text x="1000" y="342" {M} font-size="32" fill="#fff" text-anchor="end">CAM 07 · COMEDOR</text>'
    return b


def _pixeles():
    """Cuadrícula de píxeles en rojo: zona «inventada» de la foto."""
    b = ""
    for i in range(6):
        for j in range(5):
            x, y = 330 + 70 * i, 600 + 70 * j
            op = 0.55 if (i + j) % 2 == 0 else 0.25
            b += f'<rect x="{x}" y="{y}" width="64" height="64" fill="{C.RED}" fill-opacity="{op}" stroke="{C.RED}" stroke-width="2"/>'
    return b


def _marco_muelle():
    h = _inner(C.historia("noa.viaja", 11, "18-OCT", total=12, actual=12))
    return h.replace("DÍA 11 · 18-OCT", "18-OCT · 10:58")


def capas():
    bgm = _blur(ROOT / "crucero/maestro/barco_maestro.jpg", OUT / "_bg_maestro.png")
    bgc = _blur(ROOT / "crucero/p01/img/comedor.jpg", OUT / "_bg_comedor.png", -0.3)
    V.componer(bgc, [_encoger(render(_tachada(), OUT / "_tach.png"))], OUT / "tachada.png")
    ficha = render(C.ficha("Marco Bellini", "Ingeniero · diseñó Memoria, la IA de la naviera",
                           ["EDAD: 34", "CARGO: Ingeniero", "SISTEMA: Memoria"]), OUT / "_ficha.png")
    V.componer(bgm, [ficha], OUT / "ficha.png")
    V.componer(bgm, [render(_memoria(), OUT / "_memoria.png")], OUT / "memoria.png")
    V.componer(bgm, [_encoger(render(_sinservicio(), OUT / "_sin.png"))], OUT / "sinservicio.png")
    render(_apagados(), OUT / "apagados.png")
    V.capa(V.vineta(), OUT / "L_vineta.png")
    V.capa(V.portada(6, "Una IA escribía sus *vacaciones*"), OUT / "L_portada.png")
    for i, (src, habla, sub, extra, kb, tr) in enumerate(SHOTS):
        if extra == "cierre":
            body = V.cierre("¿Quién le hizo *esa foto*?", "PARTE 07 EL SÁBADO")
        else:
            body = (V.sub(sub) if sub else "")
            if "historia:" not in extra and "marco" not in extra:
                body = V.barra() + body
            for e in filter(None, extra.split(";")):
                if e.startswith("sello:"):
                    t = e[6:]
                    sy = 400 if src in PROPIAS else (1130 if ("pixeles" in extra or "historia:" in extra) else 820)
                    body += V.sello(t, 540, sy, -6, 60 if len(t) < 14 else 48)
                elif e.startswith("historia:"):
                    d, f = e[9:].split("|")
                    body += _inner(C.historia("noa.viaja", int(d), f))
                elif e.startswith("banner:"):
                    u, t = e[7:].split("|")
                    body += _banner(u, t)
                elif e == "cctv":
                    body += _cctv()
                elif e == "pixeles":
                    body += _pixeles()
                elif e == "marco":
                    body += _marco_muelle()
        V.capa(body, OUT / f"L{i:02d}.png")


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
