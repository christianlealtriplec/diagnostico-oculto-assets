"""Historias de Instagram para cada capítulo: vídeo MP4 de 10 s con música (+ PNG). 0 créditos.

Uso:
  python3 tools/stories.py estreno t1 N "<título>" "<gancho, líneas con |>" <escena.png>
      -> t1/pN/story_estreno.mp4    (17:47: «estreno a las 18h»)
  python3 tools/stories.py voto t1 N "<título>" "<opción A>" "<opción B>" <escena.png>
      -> t1/pN/story_voto.mp4       (se publica a las 18:03 el día del capítulo N)
  python3 tools/stories.py resultado t1 N <ganadora A|B> "<título del capítulo N>" <escena.png>
      -> t1/pN/story_resultado.mp4  (se publica a las 10:00; ganadora del capítulo N-1, título del N y «HOY A LAS 18H»; sin número de votos)
La escena de fondo es cualquier PNG 1080x1920 ya dibujado (se oscurece).
"""
import sys, pathlib, subprocess, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import W, H, PAL, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
TMP = pathlib.Path("/tmp/do_build"); TMP.mkdir(parents=True, exist_ok=True)
F = 'font-family="DejaVu Sans" font-weight="bold" text-anchor="middle"'


def wrap(t, n):
    lines, cur = [], ""
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + [cur] if cur else lines


def txt(lines, y, size, fill, gap=None, stroke=True):
    gap = gap or int(size * 1.25)
    st = 'stroke="#000" stroke-width="9" paint-order="stroke"' if stroke else ""
    return "".join(f'<text x="540" y="{y + gap * i}" {F} font-size="{size}" fill="{fill}" {st}>{html.escape(l)}</text>'
                   for i, l in enumerate(lines)), y + gap * len(lines)


def box(y, h, fill="#000", op=0.85):
    return f'<rect x="60" y="{y}" width="960" height="{h}" rx="18" fill="{fill}" fill-opacity="{op}"/>'


MUSIC = ROOT / "recursos" / "story_tension.m4a"
SECS = 10


def compose(scene, overlay_body, out):
    """Genera out (.png, fotograma final) y out.with_suffix('.mp4'): 10 s con zoom lento,
    destello inicial, texto que aparece y música de tensión."""
    out.parent.mkdir(parents=True, exist_ok=True)
    ov = render(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{overlay_body}</svg>', TMP / f"ov_{out.stem}.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(scene), "-i", str(ov), "-filter_complex",
                    f"[0]scale={W}:{H},eq=brightness=-0.07[b];[b][1]overlay", "-frames:v", "1", "-update", "1", str(out)], check=True)
    n = SECS * 30
    vf = (f"[0:v]scale=2160:3840,eq=brightness=-0.07,zoompan=z='1+0.10*on/{n}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d={n}:s={W}x{H}:fps=30,"
          f"fade=in:st=0:d=0.35:color=white[bg];"
          f"[1:v]format=rgba,fade=in:st=0.3:d=0.45:alpha=1[ui];[bg][ui]overlay=0:0,fade=out:st={SECS - 0.4}:d=0.4,format=yuv420p[v];"
          f"[2:a]atrim=0:{SECS},afade=t=out:st={SECS - 1.2}:d=1.2[a]")
    mp4 = out.with_suffix(".mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(scene), "-loop", "1", "-i", str(ov), "-i", str(MUSIC),
                    "-filter_complex", vf, "-map", "[v]", "-map", "[a]", "-frames:v", str(n), "-t", str(SECS),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", str(mp4)], check=True)
    return mp4


def estreno(season, n, title, hook, scene):
    s = season.upper()
    body = box(150, 140, PAL["red"], 0.95)
    body += f'<text x="540" y="245" {F} font-size="66" fill="#fff">⚠ ESTRENO A LAS 18H</text>'
    t, y = txt([f"PARTE {n:02d}"], 420, 64, "#ffd400"); body += t
    t, y = txt(wrap(title.upper(), 18), y + 20, 84, "#fff"); body += t
    hl = [l for part in hook.split("|") for l in wrap(part, 24)]
    y = max(y + 80, 1050)
    body += box(y, 70 + 70 * len(hl))
    t, _ = txt(hl, y + 85, 54, "#fff", 70, False); body += t
    body += f'<text x="540" y="1760" {F} font-size="54" fill="#ffd400" stroke="#000" stroke-width="9" paint-order="stroke">🔔 NO TE LO PIERDAS</text>'
    return compose(scene, body, ROOT / season / f"p{n}" / "story_estreno.png")


def voto(season, n, title, a, b, scene):
    s = season.upper()
    body = box(150, 130, PAL["red"], 0.95)
    body += f'<text x="540" y="238" {F} font-size="60" fill="#fff">🔦 NUEVA PARTE</text>'
    t, y = txt([f"PARTE {n:02d}"], 380, 64, "#ffd400")
    body += t
    t, y = txt(wrap(title.upper(), 20), y + 20, 70, "#fff")
    body += t
    y = max(y + 60, 1000)
    la, lb = wrap(f"A) {a}", 26), wrap(f"B) {b}", 26)
    h = 150 + 62 * (len(la) + len(lb))
    body += box(y, h)
    body += f'<text x="540" y="{y + 85}" {F} font-size="58" fill="#ffd400">¿QUÉ HARÍAS TÚ?</text>'
    t, y2 = txt(la, y + 160, 48, "#3fd27a", 62, False); body += t
    t, _ = txt(lb, y2, 48, "#ff6b61", 62, False); body += t
    body += f'<text x="540" y="1760" {F} font-size="54" fill="#fff" stroke="#000" stroke-width="9" paint-order="stroke">VOTA A o B EN EL REEL 👆</text>'
    out = ROOT / season / f"p{n}" / "story_voto.png"
    return compose(scene, body, out)


def resultado(season, n, win, title, scene):
    s = season.upper()
    body = box(150, 130, "#000", 0.85)
    body += f'<text x="540" y="238" {F} font-size="56" fill="#ffd400">RESULTADO · PARTE {n - 1:02d}</text>'
    t, y = txt([f"GANÓ LA {win}"], 520, 130, "#fff"); body += t
    ll = wrap(title.upper(), 18)
    h = 200 + 80 * len(ll)
    y = 1180
    body += box(y, h, PAL["red"], 0.95)
    body += f'<text x="540" y="{y + 80}" {F} font-size="50" fill="#ffd400">{s} · CAPÍTULO {n}</text>'
    t, _ = txt(ll, y + 170, 68, "#fff", 80, False); body += t
    body += f'<text x="540" y="1760" {F} font-size="64" fill="#fff" stroke="#000" stroke-width="9" paint-order="stroke">HOY A LAS 18H</text>'
    out = ROOT / season / f"p{n}" / "story_resultado.png"
    return compose(scene, body, out)


if __name__ == "__main__":
    k, season, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
    if k == "estreno":
        print(estreno(season, n, sys.argv[4], sys.argv[5], pathlib.Path(sys.argv[6])))
    elif k == "voto":
        print(voto(season, n, *sys.argv[4:7], pathlib.Path(sys.argv[7])))
    else:
        print(resultado(season, n, sys.argv[4], sys.argv[5], pathlib.Path(sys.argv[6])))
