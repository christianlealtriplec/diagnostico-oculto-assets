"""Parte 11 · Luis (rama B ganadora en la 10: 1 voto B en IG, 0 en YT; <10 → la correcta, B)."""
CLOCK = "HORA 85 · SIN FECHA DE FIN"
HOOK_UI = "LUIS SUDA Y TIEMBLA.|SU MUJER QUIERE MÁS INSULINA."
DECISION_UI = "DECIDES TÚ|A) OTRA DOSIS DE INSULINA|B) AZÚCAR RÁPIDO YA|COMENTA A o B"
CARD_UI = {3: "HIPOTERMIA: A CUBIERTO,|FUERA LO MOJADO, MANTAS.|NI ALCOHOL NI FROTAR"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ GARRAFAS LLENAS", "+ HORNILLO", "+ LEJÍA", "- CASI SIN COMIDA"]
SHOTS = [
    ("01_colegio_dentro", 1.0, 1.12, .6, .55, "Lo metéis en el colegio.", "hook"),
    ("02_mantas", 1.0, 1.12, .5, .7, "Fuera la ropa mojada, dos mantas,", "sub"),
    ("03_caldo", 1.0, 1.15, .5, .55, "un caldo caliente con azúcar.", "sub"),
    ("04_tirita", 1.0, 1.12, .5, .5, "Media hora después vuelve a tiritar: su cuerpo vuelve a pelear.", "sub"),
    ("05_habla", 1.0, 1.12, .5, .5, "Entre mantas, el señor habla:", "sub"),
    ("05_habla", 1.12, 1.25, .5, .45, "En el polideportivo hay gente de todo el barrio.", "dialogo:SEÑOR"),
    ("06_furgonetas", 1.0, 1.15, .45, .7, "De noche llegan furgonetas y se llevan a algunos.", "dialogo:SEÑOR"),
    ("07_las_tres", 1.0, 1.15, .5, .5, "Al calvo se lo llevaron a las tres.", "dialogo:SEÑOR"),
    ("08_subes", 1.0, 1.15, .5, .65, "Subes las garrafas con la cabeza a mil.", "sub"),
    ("09_puerta_abierta", 1.0, 1.15, .4, .5, "En el segundo, la puerta de Luis está abierta.", "sub"),
    ("10_luis_escalera", 1.0, 1.2, .5, .5, "Está sentado en la escalera, sudando, temblando, con la mirada perdida:", "alarma"),
    ("11_que_dia", 1.0, 1.15, .5, .45, "¿Qué día es hoy?", "dialogo:LUIS"),
    ("12_pilar_pluma", 1.0, 1.15, .65, .55, "Su mujer, con la pluma de insulina en la mano:", "sub"),
    ("13_pilar_habla", 1.0, 1.12, .5, .45, "Se ha puesto su dosis, pero hoy casi no ha comido.", "dialogo:PILAR"),
    ("14_otra_dosis", 1.0, 1.15, .55, .45, "Le pongo otra, que con los nervios se le sube el azúcar.", "dialogo:PILAR"),
    ("15_hora85", 1.0, 1.12, .5, .45, "Hora ochenta y cinco.", "sub"),
    ("16_sintomas", 1.0, 1.2, .5, .4, "Sudor frío, temblor, confusión.", "alarma"),
    ("17_sin_comer", 1.0, 1.15, .5, .65, "Y casi sin comer.", "sub"),
    ("18_decision", 1.0, 1.08, .3, .5, "Decides tú. A: otra dosis de insulina.", "sub"),
    ("18_decision", 1.0, 1.08, .7, .5, "B: azúcar rápido ya, mientras pueda tragar. Comenta A o B.", "sub"),
    ("19_ramon_asoma", 1.0, 1.2, .7, .35, "Arriba, Don Ramón asoma con la radio:", "alarma"),
    ("20_ramon_habla", 1.1, 1.3, .5, .45, "Acaban de decir vuestro apellido. Desde el polideportivo.", "dialogo:DON RAMÓN"),
    ("21_final", 1.0, 1.06, .5, .5, "", "decision"),
]
