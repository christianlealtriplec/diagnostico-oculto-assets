"""Parte 1 final: imágenes y subtítulos sincronizados con la voz real (Brian, 63,48 s)."""
import sys, pathlib, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_p1_preview as B

VOICE_SECONDS = 63.48
TAIL = 2.5  # segundos finales con la decisión en pantalla y solo música

# (escena, z0, z1, fx, fy, texto hablado = subtítulo, tipo)
SHOTS = [
    ("05_abuela_cara", 1.0, 1.10, .40, .45, "Tu abuela respira con una máquina. Y se acaba de apagar.", "hook"),
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
    ("05_abuela_cara", 1.15, 1.3, .38, .5, "respirando rápido;", "sub"),
    ("05_abuela_cara", 1.7, 1.9, .33, .58, "los labios empiezan a ponerse grises.", "sub"),
    ("04_abuela_plano", 1.25, 1.35, .6, .5, "Sus pulmones necesitan ese oxígeno.", "sub"),
    ("12_enchufe", 1.0, 1.12, .5, .45, "Y la máquina va enchufada a la pared.", "sub"),
    ("13_armario", 1.0, 1.08, .5, .5, "Buscas, piensas... y en el armario", "sub"),
    ("07_botella", 1.0, 1.08, .5, .5, "ves una botella metálica alta,", "sub"),
    ("07_botella", 1.5, 1.7, .45, .24, "con una ruedecita.", "sub"),
    ("08_tio_grita", 1.0, 1.08, .5, .45, "Pero tu tío te grita desde la puerta:", "sub"),
    ("08_tio_grita", 1.3, 1.45, .5, .4, "«¡Ni la toques, eso es peligroso!", "sub"),
    ("14_hueco_escalera", 1.0, 1.2, .5, .5, "Bajémosla a la calle, ahí hay más aire».", "sub"),
    ("14_hueco_escalera", 1.3, 1.6, .5, .5, "Tres pisos. A oscuras.", "sub"),
    ("05_abuela_cara", 1.3, 1.42, .45, .45, "Con una mujer de ochenta años que no puede respirar.", "sub"),
    ("15_decision", 1.0, 1.05, .5, .5, "Decides tú. A: abres la botella. B: la bajáis a la calle. Comenta A o B.", "decision"),
]
DECISION_UI = "DECIDES TÚ|A) ABRO LA BOTELLA|B) LA BAJAMOS A LA CALLE|COMENTA A o B"
HOOK_UI = "TU ABUELA RESPIRA CON|UNA MÁQUINA. Y SE APAGÓ."


def weight(t):
    # caracteres + pausa extra por signo de puntuación
    return len(t) + 6 * sum(t.count(p) for p in ".;:!?") + 3 * t.count(",")


def plan():
    total = sum(weight(s[5]) for s in SHOTS)
    out = []
    for i, (sc, z0, z1, fx, fy, text, kind) in enumerate(SHOTS):
        d = VOICE_SECONDS * weight(text) / total
        if i == len(SHOTS) - 1:
            d += TAIL
        ui_text = HOOK_UI if kind == "hook" else DECISION_UI if kind == "decision" else text
        out.append((sc, z0, z1, fx, fy, ui_text, kind, d))
    return out


if __name__ == "__main__":
    B.SHOTS = [s[:7] for s in plan()]
    durs = [s[7] for s in plan()]
    B.dur = lambda text, kind, _it=iter(durs): next(_it)
    f = B.build()
    final = f.with_name("p1_final_sin_audio.mp4")
    f.rename(final)
    print(final, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(final)],
                                capture_output=True, text=True).stdout.strip())
