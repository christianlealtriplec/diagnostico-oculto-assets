"""Parte 12 · El polideportivo (rama B ganadora en la 11: 2 votos B en IG, 0 en YT; <10 → la correcta, B)."""
CLOCK = "HORA 90 · SIN FECHA DE FIN"
HOOK_UI = "HUGO SE ATRAGANTA.|Y NO PUEDE TOSER."
DECISION_UI = "DECIDES TÚ|A) AGUA PARA QUE BAJE|B) GOLPES Y COMPRESIONES|COMENTA A o B"
CARD_UI = {4: "HIPOGLUCEMIA: SI ESTÁ|CONSCIENTE, AZÚCAR RÁPIDO.|SI NO, NADA POR BOCA"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ GARRAFAS LLENAS", "+ DNI", "- CARAMELOS", "- CASI SIN COMIDA"]
SHOTS = [
    ("01_zumo", 1.0, 1.12, .6, .55, "Le das un vaso de zumo y dos caramelos.", "hook"),
    ("02_quince_min", 1.0, 1.12, .5, .5, "Quince minutos después, Luis te mira:", "sub"),
    ("03_que_hago", 1.0, 1.15, .5, .45, "¿Qué hago en la escalera?", "dialogo:LUIS"),
    ("04_ha_vuelto", 1.0, 1.1, .5, .5, "Ha vuelto.", "sub"),
    ("05_salis", 1.0, 1.15, .5, .6, "Con lo que ha dicho Don Ramón, no hay nada que pensar: vas al polideportivo.", "sub"),
    ("06_hugo_caramelos", 1.0, 1.15, .45, .7, "Hugo no se separa de ti y se guarda los caramelos que sobraron.", "sub"),
    ("07_cola_calle", 1.0, 1.15, .5, .75, "La cola llega a la calle.", "sub"),
    ("08_megafono", 1.0, 1.12, .4, .5, "Megáfono:", "sub"),
    ("08_megafono", 1.12, 1.25, .45, .5, "Solo familiares, con DNI.", "dialogo:MEGÁFONO"),
    ("09_hora90", 1.0, 1.12, .5, .45, "Hora noventa.", "sub"),
    ("10_hugo_rie", 1.0, 1.15, .5, .5, "Hugo se mete un caramelo en la boca, se ríe y,", "sub"),
    ("11_se_calla", 1.0, 1.15, .5, .5, "de golpe, se calla.", "sub"),
    ("12_manos_cuello", 1.0, 1.2, .5, .5, "Se lleva las manos al cuello.", "alarma"),
    ("13_no_voz", 1.0, 1.12, .45, .5, "No tose. No le sale la voz.", "sub"),
    ("14_morado", 1.0, 1.2, .5, .6, "Se está poniendo morado.", "alarma"),
    ("15_senora", 1.0, 1.12, .6, .5, "Una señora:", "sub"),
    ("16_dale_agua", 1.0, 1.15, .5, .45, "¡Dale agua, que baje!", "dialogo:SEÑORA"),
    ("17_decision", 1.0, 1.08, .3, .5, "Decides tú. A: le das agua para que baje.", "sub"),
    ("17_decision", 1.0, 1.08, .7, .5, "B: cinco golpes fuertes en la espalda y, si no sale, cinco compresiones en la tripa. Comenta A o B.", "sub"),
    ("18_lista", 1.0, 1.2, .5, .5, "Dentro, un voluntario lee la lista.", "alarma"),
    ("19_lista_cerca", 1.0, 1.15, .5, .5, "Junto al nombre de tu tío, a boli:", "sub"),
    ("19_lista_cerca", 1.15, 1.3, .55, .55, "Trasladado. Tres de la mañana.", "dialogo:VOLUNTARIO"),
    ("20_nadie", 1.0, 1.12, .5, .6, "Nadie sabe adónde.", "sub"),
    ("21_final", 1.0, 1.06, .5, .5, "", "decision"),
]
