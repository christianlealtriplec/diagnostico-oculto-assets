"""Historia de IG de lanzamiento del crucero: 13 s, 3 planos con zoom, destellos y música. 0 créditos.
Uso: python3 tools/story_crucero.py  → crucero/stories/lanzamiento.mp4 (+ fotogramas PNG de control)
"""
import sys, pathlib, subprocess, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crucero_v2 as V
from crucero_v2 import COND, SERIF, MONO, SHADOW, W, H

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "crucero" / "stories"; OUT.mkdir(parents=True, exist_ok=True)
TMP = pathlib.Path("/tmp/do_build/story_crucero"); TMP.mkdir(parents=True, exist_ok=True)
ICE, RED = "#eef6f7", "#d0142c"
MUSIC = ROOT / "recursos" / "story_misterio.m4a"
FPS = 30


def lanzamiento_capa():
    o = '<rect width="1080" height="1920" fill="#000" fill-opacity="0.25"/>'
    o += f'<rect width="{W}" height="860" fill="url(#top)"/><rect y="{H - 900}" width="{W}" height="900" fill="url(#bot)"/>'
    o += (f'<text x="540" y="250" {COND} font-size="30" letter-spacing="9" fill="{ICE}" fill-opacity="0.9" text-anchor="middle">DIAGNÓSTICO OCULTO PRESENTA</text>'
          f'<rect x="390" y="285" width="300" height="70" fill="{RED}"/>'
          f'<text x="540" y="335" {COND} font-size="40" letter-spacing="6" fill="#fff" text-anchor="middle">NUEVA SERIE</text>'
          f'<text x="540" y="480" {SERIF} font-size="104" fill="{ICE}" text-anchor="middle" {SHADOW}>EL CRUCERO QUE</text>'
          f'<text x="540" y="595" {SERIF} font-size="104" fill="{ICE}" text-anchor="middle" {SHADOW}>REGRESÓ <tspan fill="{RED}">VACÍO</tspan></text>')
    o += V.sello("EXPEDIENTE PERSÉFONE", 540, 700, -3, 38)
    o += (f'<text x="540" y="1180" {COND} font-size="64" fill="{ICE}" text-anchor="middle" {SHADOW}>590 personas desaparecen.</text>'
          f'<text x="540" y="1260" {COND} font-size="64" fill="{ICE}" text-anchor="middle" {SHADOW}>Tú tienes el expediente.</text>'
          f'<rect x="170" y="1330" width="740" height="150" fill="{RED}"/>'
          f'<text x="540" y="1434" {COND} font-size="88" letter-spacing="2" fill="#fff" text-anchor="middle">MAÑANA · 18:00</text>'
          f'<text x="540" y="1560" {COND} font-size="44" fill="{ICE}" text-anchor="middle" {SHADOW}>Activa las notificaciones</text>'
          f'<text x="540" y="1625" {COND} font-size="26" letter-spacing="6" fill="{ICE}" fill-opacity="0.7" text-anchor="middle">FICCIÓN</text>')
    return o


PLANOS = [  # (imagen, segundos, capa, zoom inicio→fin, centro y)
    (ROOT / "crucero/p01/img/platos.jpg", 3.4,
     V.barra() + V.chip(["17-OCT · 06:52", "AVISO POR RADIO"], 260) + V.sub("«La comida aún estaba *caliente*»", y=1400), (1.0, 1.14), 0.55),
    (ROOT / "crucero/p01/img/comedor.jpg", 3.4,
     V.barra() + V.sello("11 DÍAS DESAPARECIDO", 540, 760, -6, 60) + V.sub("*590* personas. Ni una a bordo.", y=1400), (1.12, 1.0), 0.5),
    (ROOT / "crucero/maestro/barco_maestro.jpg", 6.2, lanzamiento_capa(), (1.0, 1.10), 0.5),
]


def plano(i, img, secs, capa, z, cy):
    ov = V.capa(capa, TMP / f"c{i}.png")
    n = int(secs * FPS)
    z0, z1 = z
    vf = (f"[0:v]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},"
          f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*{cy}':d={n}:s={W}x{H}:fps={FPS},"
          f"eq=brightness=-0.04:saturation=0.9[bg];"
          f"[1:v]format=rgba,fade=in:st=0.15:d=0.35:alpha=1[ui];[bg][ui]overlay,format=yuv420p[v]")
    out = TMP / f"p{i}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(img), "-loop", "1", "-i", str(ov),
                    "-filter_complex", vf, "-map", "[v]", "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "20", str(out)], check=True)
    # fotograma de control (con la capa ya visible)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(secs - 0.5), "-i", str(out), "-frames:v", "1",
                    "-update", "1", str(OUT / f"lanzamiento_f{i}.png")], check=True)
    return out, secs


def main():
    clips = [plano(i, *p) for i, p in enumerate(PLANOS)]
    # transiciones: destello blanco y luego rojo
    T = 0.25
    inp, fc, last, off = [], "", "[0:v]", 0.0
    for c, _ in clips:
        inp += ["-i", str(c)]
    for k in range(1, len(clips)):
        off += clips[k - 1][1] - T
        tr = "fadewhite" if k == 1 else "fadeblack"
        fc += f"{last}[{k}:v]xfade=transition={tr}:duration={T}:offset={off:.2f}[x{k}];"
        last = f"[x{k}]"
    total = sum(s for _, s in clips) - T * (len(clips) - 1)
    fc += f"{last}fade=out:st={total - 0.4:.2f}:d=0.4[v];"
    fc += f"[{len(clips)}:a]atrim=0:{total:.2f},afade=t=in:d=0.3,afade=t=out:st={total - 1.2:.2f}:d=1.2[a]"
    mp4 = OUT / "lanzamiento.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inp, "-stream_loop", "-1", "-i", str(MUSIC), "-filter_complex", fc,
                    "-map", "[v]", "-map", "[a]", "-t", f"{total:.2f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(mp4)], check=True)
    print(mp4, round(total, 2), "s")


if __name__ == "__main__":
    main()
