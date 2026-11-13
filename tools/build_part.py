"""Constructor genérico de partes.

Uso: python3 tools/build_part.py t1 2 <segundos_de_voz>
Lee tools/parts/t{T}_p{N}.py, que define:
  SHOTS = [(escena, z0, z1, fx, fy, texto_hablado, tipo), ...]   # tipo: hook | sub | dialogo:NOMBRE (bocadillo) | alarma (temblor + destello rojo) | card | decision
  HOOK_UI = "LÍNEA 1|LÍNEA 2"            # texto del gancho en pantalla
  DECISION_UI = "DECIDES TÚ|A) ...|B) ...|COMENTA A o B"   # o None si la parte no tiene decisión
  CLOCK = "HORA 03 / 72"
  CARD_UI = {índice_del_plano: "TEXTO|DE LA|TARJETA"}       # opcional, sustituye el subtítulo de ese plano
  SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}               # marcador de corazones, de estado.json["salud"]
  MOCHILA = ["+ VELAS", "+ PILAS", "- SIN AGUA"]            # objetos, de estado.json["mochila"]
Las escenas son PNG en t{T}/p{N}/ (o rutas relativas a t{T}/, p. ej. "p1/05_abuela_cara").
Genera t{T}/p{N}/t{T}_p{N}_sin_audio.mp4 sincronizado con la duración real de la voz.
"""
import sys, pathlib, importlib.util, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_p1_preview as B

TAIL = 2.5


def weight(t):
    return len(t) + 6 * sum(t.count(p) for p in ".;:!?") + 3 * t.count(",")


def main(season, part, voice_seconds):
    root = B.ROOT
    spec_path = root / "tools" / "parts" / f"{season}_p{part}.py"
    spec = importlib.util.spec_from_file_location("spec", spec_path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    shots = m.SHOTS
    cards = getattr(m, "CARD_UI", {})
    total = sum(weight(s[5]) for s in shots)
    plan, durs = [], []
    for i, (sc, z0, z1, fx, fy, text, kind) in enumerate(shots):
        d = voice_seconds * weight(text) / total + (TAIL if i == len(shots) - 1 else 0)
        ui_text = (m.HOOK_UI if kind == "hook" else
                   m.DECISION_UI if kind == "decision" else
                   cards.get(i, text))
        k = "card" if i in cards else kind
        plan.append((sc, z0, z1, fx, fy, ui_text, k)); durs.append(d)
    pdir = root / season / f"p{part}"
    pdir.mkdir(parents=True, exist_ok=True)
    # las escenas pueden venir de otras partes: B.SC apunta a la carpeta de la temporada
    B.SC = root / season
    B.SHOTS = [(s[0] if "/" in s[0] else f"p{part}/{s[0]}",) + s[1:] for s in plan]
    B.CLOCK = m.CLOCK
    B.SALUD = getattr(m, "SALUD", None)
    B.MOCHILA = getattr(m, "MOCHILA", None)
    B.LABEL = f"PARTE {part:02d}"
    B.FINAL = pdir / f"{season}_p{part}_sin_audio.mp4"
    it = iter(durs)
    B.dur = lambda text, kind: next(it)
    f = B.build()
    print(f, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                            capture_output=True, text=True).stdout.strip())


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]))
