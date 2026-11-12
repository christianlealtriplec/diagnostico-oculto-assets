"""Capítulo 4 · La vela (rama A ganadora en el Capítulo 3: generador fuera)."""
CLOCK = "HORA 41 / 72"
HOOK_UI = "HUGO GRITA. SE HA|QUEMADO CON UNA VELA."
DECISION_UI = "DECIDES TÚ|A) HIELO DIRECTAMENTE|B) AGUA DEL GRIFO|COMENTA A o B"
CARD_UI = {6: "GENERADOR SIEMPRE|FUERA Y LEJOS DE|VENTANAS. ABRIR NO|BASTA: MONÓXIDO"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ VELAS", "+ PILAS", "- POCA AGUA"]
SHOTS = [
    ("11_mano_quemada", 1.0, 1.10, .55, .45, "Apagas el generador.", "hook"),
    ("01_cunado_carga", 1.0, 1.10, .5, .45, "¡Ayúdame!", "dialogo:TÚ"),
    ("01_cunado_carga", 1.3, 1.45, .55, .6, "le gritas a tu cuñado.", "sub"),
    ("02_patio", 1.0, 1.10, .6, .8, "Lo sacáis al patio, lejos de las ventanas, y abrís todo.", "sub"),
    ("03_hugo_mejor", 1.0, 1.10, .5, .4, "Una hora después, Hugo levanta la cabeza:", "sub"),
    ("03_hugo_mejor", 1.3, 1.45, .5, .35, "Ya no me duele.", "dialogo:HUGO"),
    ("02_patio", 1.4, 1.55, .8, .85, "Era monóxido de carbono.", "card"),
    ("04_radio", 1.0, 1.10, .45, .55, "Hora cuarenta y uno. La radio crepita:", "sub"),
    ("04_radio", 1.3, 1.45, .45, .55, "Protección Civil: el apagón sigue. Generadores, nunca dentro de casa.", "dialogo:RADIO"),
    ("05_luis_bolsa", 1.0, 1.10, .5, .45, "Luis sube con una bolsa:", "sub"),
    ("05_luis_bolsa", 1.3, 1.45, .5, .55, "Por lo de la insulina. Velas y pilas.", "dialogo:LUIS"),
    ("06_velas_luz", 1.0, 1.12, .5, .55, "Por fin, luz.", "sub"),
    ("07_techo_hugo", 1.0, 1.10, .45, .2, "Esa noche, un golpe en el techo. Otro.", "alarma"),
    ("07_techo_hugo", 1.35, 1.5, .5, .75, "¿Quién vive arriba?", "dialogo:HUGO"),
    ("08_madre", 1.0, 1.10, .5, .4, "Don Ramón. Hace días que no le veo.", "dialogo:MADRE"),
    ("09_puerta_4a", 1.0, 1.12, .5, .3, "Llamáis. Nadie abre.", "sub"),
    ("10_vela_caida", 1.0, 1.12, .5, .65, "Y entonces, el grito: Hugo ha tirado una vela.", "alarma"),
    ("11_mano_quemada", 1.3, 1.5, .5, .42, "Cera hirviendo en la mano. Piel roja, una ampolla.", "sub"),
    ("12_toalla_cortina", 1.0, 1.10, .5, .6, "La cortina humea: la apagas con una toalla mojada.", "sub"),
    ("13_madre_hielo", 1.0, 1.10, .5, .45, "¡Hielo, rápido!", "dialogo:MADRE"),
    ("14_tia_pasta", 1.0, 1.10, .5, .4, "¡Pasta de dientes, que alivia!", "dialogo:TÍA"),
    ("15_grifo", 1.0, 1.15, .5, .4, "El grifo aún gotea.", "sub"),
    ("16_decision", 1.2, 1.3, .25, .6, "Decides tú. A: hielo directamente.", "sub"),
    ("16_decision", 1.2, 1.3, .75, .6, "B: agua del grifo y no parar. Comenta A o B.", "sub"),
    ("17_arriba", 1.0, 1.15, .5, .3, "Y arriba, alguien arrastra algo pesado.", "alarma"),
    ("15_grifo", 1.0, 1.05, .5, .5, "", "decision"),
]
