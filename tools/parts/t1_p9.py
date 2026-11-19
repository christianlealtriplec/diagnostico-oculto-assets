"""Parte 09 · El agua (rama B ganadora en la 08: 3 votos B, 0 A; <10 → la correcta, B)."""
CLOCK = "HORA 76 · SIN FECHA DE FIN"
HOOK_UI = "YA NO SALE AGUA.|SOLO QUEDA|LA BAÑERA."
DECISION_UI = "DECIDES TÚ|A) LA BAÑERA TAL CUAL|B) HERVIR O LEJÍA|COMENTA A o B"
CARD_UI = {5: "GOLPE EN LA CABEZA:|VIGILAR 24 HORAS.|URGENCIAS SI VOMITA,|SE ADORMILA, SE|CONFUNDE O CONVULSIONA"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ BAÑERA LLENA", "+ HORNILLO", "+ LEJÍA", "- GAS PARA UNA VEZ"]
SHOTS = [
    ("01_vigilas", 1.0, 1.12, .4, .55, "Le vigilas toda la noche.", "hook"),
    ("02_despiertas", 1.0, 1.12, .5, .5, "Cada tres horas le despiertas:", "sub"),
    ("02_despiertas", 1.2, 1.35, .52, .42, "¿Cómo te llamas?", "dialogo:TÚ"),
    ("03_como_te_llamas", 1.0, 1.15, .5, .45, "Hugo…", "dialogo:HUGO"),
    ("04_responde_bien", 1.0, 1.12, .4, .55, "Responde bien, no vomita.", "sub"),
    ("05_manana", 1.0, 1.12, .45, .5, "Por la mañana, el chichón y nada más.", "sub"),
    ("06_hora76", 1.0, 1.15, .5, .45, "Hora setenta y seis.", "sub"),
    ("07_grifo_seco", 1.0, 1.18, .5, .35, "Del grifo no sale nada.", "alarma"),
    ("08_colegio", 1.0, 1.12, .4, .6, "Protección Civil reparte agua en el colegio,", "sub"),
    ("09_cola", 1.0, 1.15, .4, .7, "pero la cola da la vuelta a la manzana.", "sub"),
    ("10_vaso_banera", 1.0, 1.12, .45, .55, "Tu cuñado mete un vaso en la bañera:", "sub"),
    ("10_vaso_banera", 1.2, 1.35, .6, .45, "Agua es agua.", "dialogo:CUÑADO"),
    ("11_ramon_hornillo", 1.0, 1.12, .5, .6, "Don Ramón baja con un hornillo:", "sub"),
    ("11_ramon_hornillo", 1.2, 1.35, .5, .45, "Queda gas para una vez.", "dialogo:DON RAMÓN"),
    ("12_tia_lejia", 1.0, 1.15, .55, .55, "Tu tía encuentra en el armario una botella de lejía.", "sub"),
    ("13_hugo_sed", 1.0, 1.15, .5, .5, "Hugo tiene sed.", "sub"),
    ("14_tu_sed", 1.0, 1.15, .5, .5, "Tú también.", "sub"),
    ("15_decision", 1.0, 1.08, .3, .5, "Decides tú. A: bebéis el agua de la bañera tal cual.", "sub"),
    ("15_decision", 1.0, 1.08, .7, .5, "B: la hervís o la desinfectáis antes. Comenta A o B.", "sub"),
    ("16_llaman", 1.0, 1.15, .6, .5, "Esa noche, alguien llama a la puerta.", "alarma"),
    ("17_nadie", 1.0, 1.2, .5, .47, "Nadie espera a nadie.", "alarma"),
    ("18_final", 1.0, 1.06, .5, .5, "", "decision"),
]
