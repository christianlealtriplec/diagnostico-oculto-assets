"""Parte 2 · La insulina (rama A ganadora en la Parte 1)."""
CLOCK = "HORA 03 / 72"
HOOK_UI = "TU VECINO NECESITA|INSULINA. Y LA NEVERA|NO ENFRÍA."
DECISION_UI = "DECIDES TÚ|A) AL CONGELADOR CON HIELO|B) A UN SITIO FRESCO|COMENTA A o B"
CARD_UI = {4: "OXÍGENO EN CASA:|TEN SIEMPRE UNA|BOTELLA DE RESERVA"}
SHOTS = [
    ("06_luis_puerta", 1.0, 1.10, .5, .45, "Ganó la A.", "hook"),
    ("01_botella_abierta", 1.0, 1.10, .5, .3, "Abriste la botella.", "sub"),
    ("02_abuela_recupera", 1.0, 1.12, .38, .45, "En dos minutos, los labios de Carmen", "sub"),
    ("02_abuela_recupera", 1.4, 1.6, .35, .55, "recuperan el color.", "sub"),
    ("03_abuela_cama_botella", 1.0, 1.08, .55, .5, "Esa botella de reserva existe para esto.", "card"),
    ("08_caja_insulina", 1.0, 1.1, .5, .45, "Tu vecino necesita insulina.", "sub"),
    ("09_nevera_off", 1.0, 1.1, .5, .55, "Y la nevera no enfría.", "sub"),
    ("04_reloj", 1.0, 1.15, .5, .4, "Hora tres.", "sub"),
    ("05_llaman", 1.0, 1.12, .7, .55, "Llaman a la puerta.", "sub"),
    ("06_luis_puerta", 1.25, 1.4, .5, .4, "Es Luis, el del segundo. Diabético.", "sub"),
    ("08_caja_insulina", 1.3, 1.45, .5, .45, "Tiene en la mano una caja de insulina:", "sub"),
    ("07_luis_cara", 1.0, 1.1, .5, .4, "«La nevera no enfría, ¿se me va a estropear?».", "sub"),
    ("10_mujer_congelador", 1.0, 1.08, .4, .45, "Detrás, su mujer: «Metámosla en el congelador", "sub"),
    ("11_hielo", 1.0, 1.12, .5, .55, "con todo el hielo que quede, que aguante fría».", "sub"),
    ("10_mujer_congelador", 1.3, 1.45, .75, .25, "Parece lógico. Más frío, más segura.", "sub"),
    ("14_movil_duda", 1.0, 1.1, .5, .4, "Pero tú has oído otra cosa:", "sub"),
    ("12_pluma", 1.0, 1.12, .5, .45, "que la insulina aguanta fuera de la nevera.", "sub"),
    ("12_pluma", 1.35, 1.55, .6, .4, "¿Cuánto? ¿De verdad?", "sub"),
    ("07_luis_cara", 1.3, 1.45, .5, .45, "Si te equivocas, Luis se queda sin su tratamiento", "sub"),
    ("09_nevera_off", 1.3, 1.45, .4, .6, "en mitad del apagón.", "sub"),
    ("11_hielo", 1.3, 1.45, .5, .55, "Decides tú. A: al congelador con hielo.", "sub"),
    ("13_sitio_fresco", 1.0, 1.12, .5, .55, "B: a un sitio fresco de la casa, lejos del calor.", "sub"),
    ("15_decision", 1.0, 1.05, .5, .5, "Comenta A o B.", "decision"),
]
