"""Monta la Parte 1 (vista previa sin voz): escenas con zoom + textos + cortes."""
import sys, pathlib, subprocess, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from draw import W, H, ui, render

ROOT = pathlib.Path(__file__).resolve().parent.parent
SC = ROOT / "t1" / "p1"
TMP = pathlib.Path("/tmp/claude-0/-home-claude/25afd332-29ca-5f42-b4e4-629cf7d8f299/scratchpad/p1build")
TMP.mkdir(parents=True, exist_ok=True)
CPS = 12.3  # caracteres por segundo de la voz (medido con Sarah)
CLOCK = "HORA 00 / 72"

# (escena, zoom inicial, zoom final, foco x, foco y, texto, tipo)
SHOTS = [
    ("05_abuela_cara", 1.0, 1.12, .40, .45, "TU ABUELA RESPIRA CON|UNA MÁQUINA. Y SE APAGÓ.", "hook"),
    ("01_apagon", 1.0, 1.08, .5, .4, "Son las nueve de la noche.", "sub"),
    ("01_apagon", 1.15, 1.25, .7, .3, "Se va la luz.", "sub"),
    ("01_apagon", 1.0, 1.1, .3, .6, "No en tu casa: en toda España.", "sub"),
    ("02_sin_servicio", 1.0, 1.15, .5, .4, "El móvil, sin cobertura.", "sub"),
    ("01_apagon", 1.3, 1.4, .5, .7, "La calle, a oscuras.", "sub"),
    ("06_maquina_off", 1.0, 1.05, .5, .45, "Y entonces lo oyes: el silencio.", "sub"),
    ("06_maquina_off", 1.3, 1.45, .45, .32, "La máquina de oxígeno de tu abuela", "sub"),
    ("06_maquina_off", 1.6, 1.7, .45, .3, "ha dejado de sonar.", "sub"),
    ("03_escalera", 1.0, 1.15, .5, .55, "Subes con la linterna del móvil.", "sub"),
    ("04_abuela_plano", 1.0, 1.08, .45, .5, "Está sentada en la cama,", "sub"),
    ("05_abuela_cara", 1.1, 1.25, .38, .5, "respirando rápido.", "sub"),
    ("05_abuela_cara", 1.6, 1.8, .33, .58, "Los labios, grises.", "sub"),
    ("04_abuela_plano", 1.2, 1.3, .55, .5, "Sus pulmones necesitan ese oxígeno.", "sub"),
    ("06_maquina_off", 1.0, 1.1, .5, .5, "Y la máquina va enchufada a la pared.", "sub"),
    ("07_botella", 1.0, 1.08, .5, .5, "En el armario, una botella metálica", "sub"),
    ("07_botella", 1.5, 1.7, .45, .24, "con una ruedecita.", "sub"),
    ("08_tio_grita", 1.0, 1.1, .5, .45, "«¡Ni la toques, es peligroso!»", "sub"),
    ("08_tio_grita", 1.3, 1.45, .5, .4, "«¡Bajémosla a la calle!»", "sub"),
    ("03_escalera", 1.2, 1.35, .5, .5, "Tres pisos. A oscuras.", "sub"),
    ("05_abuela_cara", 1.3, 1.45, .4, .5, "80 años. Sin poder respirar.", "sub"),
    ("07_botella", 1.1, 1.2, .5, .5, "OXÍGENO EN CASA:|TEN SIEMPRE UNA|BOTELLA DE RESERVA", "card"),
    ("04_abuela_plano", 1.0, 1.06, .5, .5, "A) ABRO LA BOTELLA|B) LA BAJAMOS A LA CALLE|COMENTA A o B", "decision"),
]


def ui_png(i, text, kind):
    t = html.escape(text, quote=False)
    extra = ""
    if kind == "hook":
        body = ui(clock=CLOCK, hook=t) + ('<text x="540" y="1830" font-family="DejaVu Sans" font-size="30" fill="#fff" '
                                         'stroke="#000" stroke-width="6" paint-order="stroke" text-anchor="middle">Ficción con fines educativos</text>')
    elif kind == "card":
        body = ui(clock=CLOCK, card=t)
    elif kind == "decision":
        lines = t.split("|")
        body = ui(clock=CLOCK) + '<rect x="60" y="1180" width="960" height="330" rx="16" fill="#000" fill-opacity="0.85"/>'
        body += "".join(f'<text x="540" y="{1270+95*k}" font-family="DejaVu Sans" font-weight="bold" font-size="{54 if k < 2 else 50}" '
                        f'fill="{"#fff" if k < 2 else "#ff3b30"}" text-anchor="middle">{l}</text>' for k, l in enumerate(lines))
    else:
        body = ui(clock=CLOCK, sub=t)
    svgt = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{body}</svg>'
    return render(svgt, TMP / f"ui_{i:02d}.png")


def dur(text, kind):
    if kind == "hook":
        return 3.0
    if kind in ("card", "decision"):
        return 4.0
    return max(1.8, len(text) / CPS + 0.3)


def build():
    parts = []
    for i, (sc, z0, z1, fx, fy, text, kind) in enumerate(SHOTS):
        d = dur(text.replace("|", " "), kind)
        n = int(d * 30)
        u = ui_png(i, text, kind)
        out = TMP / f"shot_{i:02d}.mp4"
        zexpr = f"{z0}+({z1}-{z0})*on/{n}"
        vf = (f"[0:v]scale=2160:3840,zoompan=z='{zexpr}':x='(iw-iw/zoom)*{fx}':y='(ih-ih/zoom)*{fy}':d={n}:s={W}x{H}:fps=30[bg];"
              f"[bg][1:v]overlay=0:0,format=yuv420p")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(SC / f"{sc}.png"), "-i", str(u),
                        "-filter_complex", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(out)], check=True)
        parts.append(out)
    lst = TMP / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    final = ROOT / "t1" / "p1" / "p1_preview_sin_voz.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", "-movflags", "+faststart", str(final)], check=True)
    return final


if __name__ == "__main__":
    f = build()
    print(f, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                            capture_output=True, text=True).stdout.strip())
