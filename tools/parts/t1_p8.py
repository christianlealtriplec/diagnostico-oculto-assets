"""Parte 08 · Vuelve a irse (arco «Sin fecha de fin»; sin votación previa: el epílogo no tenía decisión)."""
CLOCK = "HORA 73 · SIN FECHA DE FIN"
HOOK_UI = "SE VA OTRA VEZ.|Y HUGO NO SE|DESPIERTA BIEN."
DECISION_UI = "DECIDES TÚ|A) LE DEJAS DORMIR|B) VIGILAR Y DESPERTARLE|COMENTA A o B"
CARD_UI = {2: "SI ALGUIEN NO|RESPIRA: PIDE AYUDA|Y COMPRIME FUERTE|Y RÁPIDO"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ BAÑERA LLENA", "+ RADIO DE RAMÓN", "- POCO GAS", "- SIN LUZ OTRA VEZ"]
SHOTS = [
    ("01_parpadea", 1.0, 1.12, .5, .3, "La luz parpadea.", "hook"),
    ("02_una_dos", 1.0, 1.12, .5, .4, "Una vez. Dos.", "alarma"),
    ("03_se_va", 1.0, 1.1, .5, .3, "Y se va.", "sub"),
    ("04_hugo_grita", 1.0, 1.15, .55, .55, "Hugo grita en la escalera.", "sub"),
    ("05_bajas_linterna", 1.0, 1.12, .5, .6, "Bajas con la linterna: está sentado en el rellano, con la mano en la frente.", "sub"),
    ("06_hugo_rellano", 1.0, 1.15, .52, .45, "Me he caído.", "dialogo:HUGO"),
    ("07_chichon", 1.0, 1.2, .55, .42, "Un chichón enorme.", "alarma"),
    ("08_ramon_dial", 1.0, 1.12, .5, .45, "Arriba, Don Ramón gira el dial de su radio:", "sub"),
    ("08_ramon_dial", 1.25, 1.4, .6, .5, "Fallo en cascada. Sin fecha de reparación.", "dialogo:RADIO"),
    ("09_ambulancia", 1.0, 1.12, .5, .75, "Tu madre se ha ido en la ambulancia con la abuela.", "sub"),
    ("10_mandas_tu", 1.0, 1.12, .5, .55, "Ahora mandas tú.", "sub"),
    ("11_estatica", 1.0, 1.15, .5, .5, "Y entre la estática, una voz que conoces:", "sub"),
    ("12_voz_tio", 1.0, 1.12, .5, .4, "Soy yo… estoy en el polideportivo… no vengáis.", "dialogo:RADIO"),
    ("13_recuerdo_tio", 1.0, 1.15, .5, .45, "Es tu tío. El que se fue la primera noche y no volvió.", "sub"),
    ("14_hugo_bosteza", 1.0, 1.12, .5, .45, "Hugo bosteza:", "sub"),
    ("14_hugo_bosteza", 1.2, 1.35, .5, .42, "Tengo mucho sueño.", "dialogo:HUGO"),
    ("15_cunado_dormir", 1.0, 1.12, .5, .45, "Tu cuñado:", "sub"),
    ("15_cunado_dormir", 1.2, 1.35, .5, .42, "Déjale dormir, que descanse.", "dialogo:CUÑADO"),
    ("07_chichon", 1.25, 1.45, .55, .42, "Pero se ha dado un golpe en la cabeza.", "alarma"),
    ("16_decision", 1.0, 1.08, .4, .45, "Decides tú. A: le dejas dormir tranquilo.", "sub"),
    ("16_decision", 1.0, 1.08, .6, .45, "B: le vigilas toda la noche y le despiertas cada pocas horas para ver cómo responde. Comenta A o B.", "sub"),
    ("17_no_vengais", 1.0, 1.15, .5, .5, "Y la radio repite: «no vengáis». Tres veces.", "alarma"),
    ("18_final", 1.0, 1.06, .5, .5, "", "decision"),
]
