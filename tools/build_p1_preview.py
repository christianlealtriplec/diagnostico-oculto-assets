"""Monta la Parte 1 (vista previa sin voz) con fundidos suaves entre planos."""
import sys, pathlib, subprocess, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import W, H, ui, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
SC = ROOT / "t1" / "p1"
TMP = pathlib.Path("/tmp/claude-0/-home-claude/25afd332-29ca-5f42-b4e4-629cf7d8f299/scratchpad/p1build")
TMP.mkdir(parents=True, exist_ok=True)
CPS = 12.3   # caracteres por segundo de la voz
XF = 0.35    # duración del fundido
CLOCK = "HORA 00 / 72"

# (escena, zoom inicial, zoom final, foco x, foco y, texto, tipo)
SHOTS = [
    ("05_abuela_cara", 1.0, 1.10, .40, .45, "TU ABUELA RESPIRA CON|UNA MÁQUINA. Y SE APAGÓ.", "hook"),
    ("09_salon", 1.0, 1.08, .5, .6, "Son las nueve de la noche.", "sub"),
    ("09_salon", 1.35, 1.5, .25, .35, "Se va la luz.", "sub"),
    ("01_apagon", 1.0, 1.08, .5, .4, "No en tu casa: en toda España.", "sub"),
    ("02_sin_servicio", 1.0, 1.12, .5, .4, "El móvil, sin cobertura.", "sub"),
    ("10_calle", 1.0, 1.1, .5, .6, "La calle, a oscuras.", "sub"),
    ("01_apagon", 1.3, 1.45, .7, .3, "Y entonces lo oyes: el silencio.", "sub"),
    ("11_puerta_3b", 1.0, 1.1, .5, .3, "En el tercero,", "sub"),
    ("06_maquina_off", 1.0, 1.08, .5, .45, "la máquina de oxígeno de tu abuela Carmen", "sub"),
    ("06_maquina_off", 1.45, 1.6, .45, .3, "ha dejado de sonar.", "sub"),
    ("03_escalera", 1.0, 1.15, .5, .55, "Subes con la linterna del móvil.", "sub"),
    ("04_abuela_plano", 1.0, 1.08, .45, .5, "Está sentada en la cama,", "sub"),
    ("05_abuela_cara", 1.15, 1.3, .38, .5, "respirando rápido,", "sub"),
    ("05_abuela_cara", 1.7, 1.9, .33, .58, "los labios empiezan a ponerse grises.", "sub"),
    ("04_abuela_plano", 1.25, 1.35, .6, .5, "Sus pulmones necesitan ese oxígeno.", "sub"),
    ("12_enchufe", 1.0, 1.12, .5, .45, "Y la máquina va enchufada a la pared.", "sub"),
    ("13_armario", 1.0, 1.08, .5, .5, "Buscas, piensas… y en el armario", "sub"),
    ("07_botella", 1.0, 1.08, .5, .5, "ves una botella metálica alta,", "sub"),
    ("07_botella", 1.5, 1.7, .45, .24, "con una ruedecita.", "sub"),
    ("08_tio_grita", 1.0, 1.08, .5, .45, "Pero tu tío te grita desde la puerta:", "sub"),
    ("08_tio_grita", 1.3, 1.45, .5, .4, "«¡Ni la toques, eso es peligroso!", "sub"),
    ("14_hueco_escalera", 1.0, 1.2, .5, .5, "Bajémosla a la calle, ahí hay más aire».", "sub"),
    ("14_hueco_escalera", 1.3, 1.6, .5, .5, "Tres pisos. A oscuras.", "sub"),
    ("05_abuela_cara", 1.3, 1.42, .45, .45, "Con una mujer de ochenta años que no puede respirar.", "sub"),
    ("13_armario", 1.2, 1.3, .55, .65, "OXÍGENO EN CASA:|TEN SIEMPRE UNA|BOTELLA DE RESERVA", "card"),
    ("15_decision", 1.0, 1.04, .5, .5, "DECIDES TÚ|A) ABRO LA BOTELLA|B) LA BAJAMOS A LA CALLE|COMENTA A o B", "decision"),
]


def ui_png(i, text, kind):
    t = html.escape(text, quote=False)
    if kind == "hook":
        body = ui(clock=CLOCK, hook=t) + ('<text x="540" y="1830" font-family="DejaVu Sans" font-size="30" fill="#fff" '
                                         'stroke="#000" stroke-width="6" paint-order="stroke" text-anchor="middle">Ficción con fines educativos</text>')
    elif kind == "card":
        body = ui(clock=CLOCK, card=t)
    elif kind == "decision":
        l = t.split("|")
        body = ui(clock=CLOCK) + '<rect x="60" y="1220" width="960" height="430" rx="16" fill="#000" fill-opacity="0.85"/>'
        cols = ["#ffd400", "#3fd27a", "#ff3b30", "#fff"]
        body += "".join(f'<text x="540" y="{1310+95*k}" font-family="DejaVu Sans" font-weight="bold" font-size="{60 if k == 0 else 52}" '
                        f'fill="{cols[k]}" text-anchor="middle">{x}</text>' for k, x in enumerate(l))
    else:
        body = ui(clock=CLOCK, sub=t)
    return render(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{body}</svg>', TMP / f"ui_{i:02d}.png")


def dur(text, kind):
    if kind == "hook":
        return 3.2
    if kind in ("card", "decision"):
        return 4.0
    return max(1.9, len(text) / CPS + 0.25)


def ease(z0, z1, n):
    # zoom con aceleración suave (ease-in-out)
    return f"{z0}+({z1}-{z0})*(0.5-0.5*cos(PI*on/{n}))"


def build():
    clips, durs = [], []
    for i, (sc, z0, z1, fx, fy, text, kind) in enumerate(SHOTS):
        d = dur(text.replace("|", " "), kind) + XF
        n = int(d * 30)
        u = ui_png(i, text, kind)
        out = TMP / f"shot_{i:02d}.mp4"
        vf = (f"[0:v]scale=2160:3840,zoompan=z='{ease(z0, z1, n)}':x='(iw-iw/zoom)*{fx}':y='(ih-ih/zoom)*{fy}':d={n}:s={W}x{H}:fps=30[bg];"
              f"[1:v]format=rgba,fade=in:st={XF}:d=0.15:alpha=1,fade=out:st={d - XF - 0.05:.2f}:d=0.05:alpha=1[ui];[bg][ui]overlay=0:0,format=yuv420p")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(SC / f"{sc}.png"), "-loop", "1", "-i", str(u),
                        "-filter_complex", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(out)], check=True)
        clips.append(out); durs.append(n / 30)
    # cadena de fundidos
    inputs, fc, prev, off = [], [], "[0:v]", 0.0
    for c in clips:
        inputs += ["-i", str(c)]
    for k in range(1, len(clips)):
        off += durs[k - 1] - XF
        lab = f"[v{k}]"
        fc.append(f"{prev}[{k}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}{lab}")
        prev = lab
    final = ROOT / "t1" / "p1" / "p1_preview_sin_voz.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(fc), "-map", prev,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(final)], check=True)
    return final


if __name__ == "__main__":
    f = build()
    print(f, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                            capture_output=True, text=True).stdout.strip())
