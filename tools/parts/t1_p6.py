"""Capítulo 6 · La abuela no responde (rama B ganadora en el Capítulo 5: a la basura, latas; <10 votos)."""
CLOCK = "HORA 70 / 72"
HOOK_UI = "TU ABUELA NO RESPONDE."
DECISION_UI = "DECIDES TÚ|A) TODOS A BUSCAR AYUDA|B) AYUDA Y COMPRIMIR YA|COMENTA A o B"
CARD_UI = {5: "EL OLOR NO DICE SI|ESTÁ MALO. CARNE,|LECHE, HUEVO SIN FRÍO|HORAS: A LA BASURA"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ BAÑERA LLENA", "+ NOTA 4.º A", "- POCO GAS", "- SIN COBERTURA"]
SHOTS = [
    ("01_basura", 1.0, 1.10, .5, .55, "Tiras el pollo, la tortilla y la leche.", "hook"),
    ("02_cunado_loco", 1.0, 1.10, .5, .45, "Tu cuñado:", "sub"),
    ("02_cunado_loco", 1.3, 1.45, .5, .4, "¡Estás loco!", "dialogo:CUÑADO"),
    ("03_garbanzos", 1.0, 1.10, .5, .6, "Cenáis garbanzos de lata y pan duro.", "sub"),
    ("03_garbanzos", 1.3, 1.45, .4, .45, "Nadie se pone malo.", "sub"),
    ("01_basura", 1.25, 1.4, .5, .65, "A veces lo valiente es tirar comida.", "card"),
    ("04_radio_hora70", 1.0, 1.10, .5, .55, "Hora setenta. La radio:", "sub"),
    ("04_radio_hora70", 1.3, 1.5, .5, .58, "No se descarta que el apagón se alargue varios días.", "dialogo:RADIO"),
    ("05_cunado_baja", 1.0, 1.12, .5, .5, "Tu cuñado baja del cuarto:", "sub"),
    ("05_cunado_baja", 1.3, 1.45, .5, .38, "Don Ramón no abre, pero la radio sigue sonando.", "dialogo:CUÑADO"),
    ("06_golpe", 1.0, 1.15, .5, .6, "Un golpe en la habitación.", "sub"),
    ("07_abuela_suelo", 1.0, 1.15, .5, .78, "Tu abuela, en el suelo.", "alarma"),
    ("08_sacudir", 1.0, 1.10, .5, .55, "¡Abuela!", "dialogo:TÚ"),
    ("08_sacudir", 1.15, 1.3, .45, .6, "La sacudes de los hombros. Nada.", "sub"),
    ("09_pecho", 1.0, 1.10, .5, .5, "Miras su pecho: no respira con normalidad, solo boquea de vez en cuando.", "sub"),
    ("09_pecho", 1.3, 1.5, .5, .52, "Eso no es respirar.", "alarma"),
    ("10_sin_cobertura", 1.0, 1.15, .45, .4, "El móvil, sin cobertura.", "sub"),
    ("11_cunado_llaves", 1.0, 1.10, .5, .5, "Tu cuñado coge las llaves:", "sub"),
    ("11_cunado_llaves", 1.25, 1.4, .55, .5, "¡Bajo a por una ambulancia!", "dialogo:CUÑADO"),
    ("12_hugo_puerta", 1.0, 1.12, .5, .55, "Hugo llora en la puerta.", "sub"),
    ("13_minutos", 1.0, 1.15, .5, .47, "Cada minuto sin sangre en el cerebro cuenta.", "sub"),
    ("14_decision", 1.2, 1.3, .25, .6, "Decides tú, y esta decisión cierra la temporada. A: todos a buscar ayuda.", "sub"),
    ("14_decision", 1.2, 1.3, .75, .6, "B: uno sale a pedir ayuda y tú empiezas a comprimir ya. Comenta A o B.", "sub"),
    ("15_radio_calla", 1.0, 1.15, .5, .3, "Y arriba, la radio se calla.", "alarma"),
    ("07_abuela_suelo", 1.0, 1.05, .5, .5, "", "decision"),
]
