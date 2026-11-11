"""Capítulo 3 · El generador (rama B ganadora en el Capítulo 2: sitio fresco)."""
CLOCK = "HORA 26 / 72"
HOOK_UI = "ALGUIEN HA METIDO UN|GENERADOR EN EL SALÓN"
DECISION_UI = "DECIDES TÚ|A) APAGARLO Y SACARLO|B) DEJARLO Y ABRIR|COMENTA A o B"
CARD_UI = {4: "LA INSULINA NO SE|CONGELA. AGUANTA|SEMANAS EN UN|SITIO FRESCO"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
SHOTS = [
    ("06_generador_salon", 1.0, 1.10, .5, .6, "Guardas la insulina en el armario del pasillo,", "hook"),
    ("01_armario_pasillo", 1.0, 1.10, .5, .5, "lejos de la ventana y del calor.", "sub"),
    ("01_armario_pasillo", 1.35, 1.5, .45, .52, "Fuera de la nevera aguanta semanas; congelada, no.", "sub"),
    ("02_luis_alivio", 1.0, 1.10, .5, .45, "Luis respira.", "sub"),
    ("02_luis_alivio", 1.25, 1.4, .5, .4, "Por fin algo sale bien.", "card"),
    ("03_reloj_26", 1.0, 1.15, .5, .43, "Hora veintiséis.", "sub"),
    ("04_frio", 1.0, 1.10, .5, .6, "Hace un frío que corta.", "sub"),
    ("05_cunado_garaje", 1.0, 1.10, .5, .5, "Tu cuñado sube del garaje con un generador de gasolina", "sub"),
    ("06_generador_salon", 1.3, 1.45, .5, .68, "y lo arranca en mitad del salón.", "alarma"),
    ("07_luz_estufa", 1.0, 1.10, .5, .5, "Luz. Estufa. Móviles cargando.", "sub"),
    ("08_cunado_orgulloso", 1.0, 1.12, .55, .45, "Todos aplauden. Tú no.", "sub"),
    ("09_hugo_cabeza", 1.0, 1.10, .5, .45, "Una hora después, Hugo se queja: le duele la cabeza.", "sub"),
    ("10_abuela_mareada", 1.0, 1.10, .45, .45, "Tu abuela, mareada.", "sub"),
    ("11_rendija", 1.0, 1.10, .55, .45, "Tu cuñado abre una rendija: «Es el frío, ya está».", "sub"),
    ("12_hugo_vomita", 1.0, 1.12, .5, .65, "Pero Hugo vomita.", "alarma"),
    ("11_rendija", 1.35, 1.5, .35, .5, "Y a ti también te late la cabeza.", "sub"),
    ("13_gas_invisible", 1.0, 1.12, .5, .5, "Hay un gas que no huele, no se ve y no avisa.", "sub"),
    ("04_frio", 1.3, 1.45, .5, .35, "Si lo apagas, volvéis al frío y a la oscuridad.", "sub"),
    ("14_decision", 1.2, 1.3, .25, .6, "Decides tú. A: lo apagas y lo sacas fuera, lejos de las ventanas.", "sub"),
    ("14_decision", 1.2, 1.3, .75, .6, "B: lo dejas y abres más las ventanas. Comenta A o B.", "sub"),
    ("15_vela", 1.0, 1.15, .55, .6, "Y mientras todos miran el generador, Hugo enciende una vela.", "alarma"),
    ("13_gas_invisible", 1.0, 1.05, .5, .5, "", "decision"),
]
