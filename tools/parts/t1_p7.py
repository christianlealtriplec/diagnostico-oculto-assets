"""Capítulo 7 · Epílogo (rama B ganadora en el Capítulo 6: uno pide ayuda y tú comprimes; 0 votos <10 → la correcta)."""
CLOCK = "HORA 72 / 72"
HOOK_UI = "¿SOBREVIVE CARMEN?"
DECISION_UI = "¿SE VA OTRA VEZ?|SÍGUENOS"
CARD_UI = {6: "NO RESPONDE Y NO|RESPIRA NORMAL: AYUDA|A GRITOS Y COMPRIME|FUERTE Y RÁPIDO"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ BAÑERA LLENA", "+ NOTA 4.º A", "- POCO GAS", "- SIN COBERTURA"]
SHOTS = [
    ("01_aporrea", 1.0, 1.12, .6, .5, "Tu cuñado sube al cuarto y aporrea la puerta.", "hook"),
    ("02_ramon_abre", 1.0, 1.12, .5, .45, "Don Ramón abre, con su radio:", "sub"),
    ("03_ramon_radio", 1.0, 1.15, .5, .4, "¡Emergencias, ¿me oyen?!", "dialogo:DON RAMÓN"),
    ("04_comprimes", 1.0, 1.15, .5, .7, "Tú, de rodillas, comprimes en el centro del pecho,", "sub"),
    ("05_ritmo", 1.05, 1.2, .5, .55, "fuerte y rápido, sin parar.", "alarma"),
    ("06_sanitarios", 1.0, 1.12, .5, .6, "Doce minutos después llegan los sanitarios.", "sub"),
    ("07_carmen_vive", 1.0, 1.12, .45, .5, "Carmen sobrevive gracias a esas compresiones.", "card"),
    ("08_hora72", 1.0, 1.1, .5, .5, "Hora setenta y dos.", "sub"),
    ("09_vuelve_luz", 1.0, 1.12, .5, .45, "Vuelve la luz.", "sub"),
    ("10_repaso", 1.0, 1.1, .5, .55, "Repasa lo que aprendiste:", "sub"),
    ("11_oxigeno", 1.0, 1.12, .45, .5, "oxígeno de reserva;", "sub"),
    ("12_insulina", 1.0, 1.12, .5, .45, "insulina fresca, nunca congelada;", "sub"),
    ("13_generador", 1.0, 1.12, .6, .7, "generador siempre fuera;", "sub"),
    ("14_quemadura", 1.0, 1.12, .5, .5, "quemaduras con agua del grifo veinte minutos;", "sub"),
    ("15_basura", 1.0, 1.12, .5, .6, "si dudas de la comida, a la basura;", "sub"),
    ("05_ritmo", 1.0, 1.1, .5, .6, "y si alguien no respira, comprime.", "sub"),
    ("16_parpadea", 1.0, 1.12, .5, .3, "Diez minutos después, la luz parpadea.", "alarma"),
    ("17_radio_aviso", 1.0, 1.1, .5, .55, "La radio:", "sub"),
    ("17_radio_aviso", 1.15, 1.3, .5, .55, "Atención: la red sigue inestable. No se descartan nuevos cortes.", "dialogo:RADIO"),
    ("18_guardalo", 1.0, 1.1, .5, .5, "Guárdalo y envíaselo a quien quieras.", "sub"),
    ("19_otra_vez", 1.0, 1.06, .5, .5, "", "decision"),
]
