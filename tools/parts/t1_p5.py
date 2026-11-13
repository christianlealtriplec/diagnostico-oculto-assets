"""Capítulo 5 · La nevera (rama B ganadora en el Capítulo 4: agua del grifo)."""
CLOCK = "HORA 60 / 72"
HOOK_UI = "NO QUEDA COMIDA. SOLO|LO QUE HABÍA EN LA NEVERA."
DECISION_UI = "DECIDES TÚ|A) SI HUELE BIEN, SE COME|B) A LA BASURA; LATAS|COMENTA A o B"
CARD_UI = {5: "AGUA DEL GRIFO, NO|HELADA, 20 MINUTOS.|NI HIELO NI PASTA|DE DIENTES"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ BAÑERA LLENA", "+ NOTA 4.º A", "- POCO GAS"]
SHOTS = [
    ("13_comida", 1.0, 1.10, .5, .55, "Pones su mano bajo el grifo.", "hook"),
    ("02_hugo_frio", 1.0, 1.10, .45, .4, "¡Está fría!", "dialogo:HUGO"),
    ("03_aguanta", 1.0, 1.10, .45, .4, "Aguanta, campeón.", "dialogo:TÚ"),
    ("01_grifo_mano", 1.0, 1.15, .5, .5, "Veinte minutos sin parar.", "sub"),
    ("05_pano", 1.0, 1.10, .5, .45, "Luego, un paño limpio, sin pinchar la ampolla.", "sub"),
    ("05_pano", 1.3, 1.45, .55, .45, "No crece.", "card"),
    ("06_megafono", 1.0, 1.10, .5, .7, "Hora sesenta. Un coche con megáfono:", "sub"),
    ("06_megafono", 1.35, 1.5, .5, .7, "Agua cortada en todo el barrio. Racionad la que tengáis.", "dialogo:MEGÁFONO"),
    ("07_madre_banera", 1.0, 1.10, .4, .45, "Tu madre:", "sub"),
    ("07_madre_banera", 1.3, 1.45, .3, .4, "¡La bañera!", "dialogo:MADRE"),
    ("08_banera_llena", 1.0, 1.12, .5, .6, "La llenáis: agua para fregar y la cisterna.", "sub"),
    ("09_nota", 1.0, 1.10, .5, .5, "Bajo la puerta, una nota:", "sub"),
    ("09_nota", 1.3, 1.5, .5, .55, "Tengo radio. 4.º A.", "dialogo:DON RAMÓN"),
    ("10_puerta_4a", 1.0, 1.12, .5, .4, "Don Ramón. Pero no abre.", "sub"),
    ("11_hambre", 1.0, 1.10, .45, .45, "Y tenéis hambre.", "sub"),
    ("12_nevera_abre", 1.0, 1.10, .45, .55, "Tu cuñado abre la nevera:", "sub"),
    ("13_comida", 1.25, 1.4, .5, .55, "pollo, embutido, tortilla, leche.", "sub"),
    ("14_cunado_huele", 1.0, 1.10, .5, .45, "Huele bien. Si huele bien, está bien.", "dialogo:CUÑADO"),
    ("15_camping_gas", 1.0, 1.10, .55, .65, "Ya lo calienta en el camping gas,", "sub"),
    ("15_camping_gas", 1.3, 1.5, .3, .7, "y el cartucho está casi vacío.", "alarma"),
    ("16_nevera_cerrada", 1.0, 1.10, .5, .5, "Una nevera cerrada guarda el frío unas horas, no dos días.", "sub"),
    ("17_latas", 1.0, 1.15, .5, .65, "Pero solo quedan dos latas.", "alarma"),
    ("18_decision", 1.2, 1.3, .25, .6, "Decides tú. A: si huele bien, se come.", "sub"),
    ("18_decision", 1.2, 1.3, .75, .6, "B: tiráis lo perecedero y os apañáis con las latas. Comenta A o B.", "sub"),
    ("19_radio_arriba", 1.0, 1.15, .5, .3, "Esa noche, la radio de arriba suena. Una voz dice el nombre de tu calle.", "alarma"),
    ("16_nevera_cerrada", 1.0, 1.05, .5, .5, "", "decision"),
]
