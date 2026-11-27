"""Parte 13 · El tío (rama B ganadora en la 12: 2 votos B en IG, 0 en YT; <10 → la correcta, B)."""
CLOCK = "HORA 94 · SIN FECHA DE FIN"
HOOK_UI = "TU TÍO HA VUELTO.|SANGRANDO."
DECISION_UI = "DECIDES TÚ|A) TORNIQUETE CON CINTURÓN|B) PRESIÓN DIRECTA|COMENTA A o B"
CARD_UI = {5: "ATRAGANTADO SIN TOS:|5 GOLPES EN LA ESPALDA|+ 5 COMPRESIONES|EN LA TRIPA"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ TU TÍO", "+ GARRAFAS LLENAS", "- SECRETO", "- CASI SIN COMIDA"]
SHOTS = [
    ("01_inclinas", 1.0, 1.12, .5, .55, "Le inclinas hacia delante.", "hook"),
    ("02_golpes", 1.0, 1.15, .45, .6, "Un golpe entre los omóplatos. Dos. Tres.", "sub"),
    ("03_compresion", 1.0, 1.15, .5, .6, "Le abrazas por detrás, puño sobre la tripa, y aprietas hacia dentro y arriba.", "sub"),
    ("04_caramelo_sale", 1.0, 1.12, .6, .45, "El caramelo sale.", "sub"),
    ("05_hugo_llora", 1.0, 1.12, .5, .5, "Hugo llora. Llorar es respirar.", "sub"),
    ("06_poli_noche", 1.0, 1.1, .5, .6, "Nadie en el polideportivo sabe adónde llevan a la gente.", "sub"),
    ("07_vuelta_casa", 1.0, 1.12, .5, .7, "Volvéis a casa de noche, en silencio.", "sub"),
    ("08_portal_lejos", 1.0, 1.08, .5, .6, "Hora noventa y cuatro.", "sub"),
    ("09_portal_linterna", 1.0, 1.25, .4, .7, "En el portal, alguien sentado en el suelo, a oscuras.", "sub"),
    ("10_calvo_barba", 1.0, 1.15, .5, .55, "Calvo. Barba. Polo azul.", "sub"),
    ("11_tu_tio", 1.0, 1.2, .5, .55, "Tu tío.", "alarma"),
    ("12_primera_noche", 1.0, 1.1, .5, .5, "El que salió la primera noche a buscar ayuda para la abuela y no volvió.", "sub"),
    ("13_brazo", 1.0, 1.2, .5, .5, "Tiene el brazo envuelto en una camiseta empapada de sangre:", "alarma"),
    ("14_tio_habla", 1.0, 1.15, .5, .5, "Me tiré de la furgoneta… me corté con la valla.", "dialogo:TÍO"),
    ("15_gotea", 1.0, 1.2, .5, .65, "La sangre gotea en el escalón.", "sub"),
    ("16_cinturon", 1.0, 1.1, .5, .65, "Tu cuñado se quita el cinturón:", "sub"),
    ("16_cinturon", 1.12, 1.25, .5, .5, "¡Un torniquete, rápido!", "dialogo:CUÑADO"),
    ("17_decision", 1.0, 1.08, .3, .5, "Decides tú. A: torniquete con el cinturón.", "sub"),
    ("17_decision", 1.0, 1.08, .7, .5, "B: presión directa y firme sobre la herida, sin soltar. Comenta A o B.", "sub"),
    ("18_agarra", 1.0, 1.2, .5, .55, "Tu tío te agarra:", "alarma"),
    ("19_secreto", 1.0, 1.2, .5, .5, "Que nadie del polideportivo sepa que estoy aquí.", "dialogo:TÍO"),
    ("20_final", 1.0, 1.06, .5, .5, "", "decision"),
]
