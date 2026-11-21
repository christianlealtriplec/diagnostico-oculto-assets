"""Parte 10 · La cola (v2 hilo conductor; rama B ganadora en la 09: 2 votos B en IG, 0 en YT; <10 → la correcta, B)."""
CLOCK = "HORA 80 · SIN FECHA DE FIN"
HOOK_UI = "SE CAE EN LA COLA.|Y YA NO TIEMBLA."
DECISION_UI = "DECIDES TÚ|A) UN TRAGO DE COÑAC|B) REFUGIO, SECO Y MANTAS|COMENTA A o B"
CARD_UI = {3: "AGUA DUDOSA: HERVIR|AL MENOS 1 MINUTO,|O 2 GOTAS DE LEJÍA APTA|POR LITRO Y ESPERAR 30 MIN"}
SALUD = {"CARMEN": 3, "HUGO": 3, "LUIS": 3}
MOCHILA = ["+ DOS GARRAFAS", "+ HORNILLO", "+ LEJÍA", "- SIN GAS"]
SHOTS = [
    ("01_hervir", 1.0, 1.12, .55, .6, "Hervís el agua en el hornillo de Don Ramón,", "hook"),
    ("02_borbotones", 1.0, 1.15, .5, .6, "un minuto a borbotones,", "sub"),
    ("03_tapada", 1.0, 1.12, .5, .65, "y la dejáis enfriar tapada.", "sub"),
    ("04_bebeis", 1.0, 1.12, .5, .5, "Nadie se pone malo.", "sub"),
    ("05_puerta", 1.0, 1.18, .5, .45, "Y entonces, la puerta. Tres golpes.", "alarma"),
    ("06_voluntario", 1.0, 1.12, .5, .5, "Es un voluntario de Protección Civil, con chaleco naranja:", "sub"),
    ("07_traed", 1.2, 1.32, .5, .45, "Mañana, agua en el colegio. Traed garrafas.", "dialogo:VOLUNTARIO"),
    ("08_se_va", 1.0, 1.12, .75, .5, "Antes de irse:", "sub"),
    ("09_pregunta", 1.0, 1.12, .5, .45, "¿Conocéis a un hombre calvo, con barba?", "dialogo:VOLUNTARIO"),
    ("09_pregunta", 1.15, 1.3, .5, .5, "Ha dado esta dirección en el polideportivo.", "dialogo:VOLUNTARIO"),
    ("10_tio", 1.0, 1.2, .5, .5, "Tu tío.", "alarma"),
    ("11_amanece", 1.0, 1.12, .5, .5, "Hora ochenta. Amanece.", "sub"),
    ("12_bajais", 1.0, 1.12, .5, .55, "Bajas a la cola con dos garrafas y tu cuñado.", "sub"),
    ("13_frio", 1.0, 1.15, .6, .7, "Hace un frío que muerde.", "sub"),
    ("14_senor", 1.0, 1.12, .5, .45, "Delante, un señor mayor en zapatillas, empapado.", "sub"),
    ("15_zapatillas", 1.0, 1.15, .5, .75, "Tiembla.", "sub"),
    ("16_senor_habla", 1.1, 1.25, .5, .5, "Vengo del polideportivo… estoy bien.", "dialogo:SEÑOR"),
    ("17_cae", 1.0, 1.2, .5, .8, "Y se cae al suelo.", "alarma"),
    ("18_voluntario_grita", 1.0, 1.12, .55, .45, "Un voluntario grita:", "sub"),
    ("18_voluntario_grita", 1.2, 1.35, .52, .4, "¡Una manta!", "dialogo:VOLUNTARIO"),
    ("19_petaca", 1.0, 1.15, .5, .55, "Tu cuñado saca una petaca:", "sub"),
    ("20_cunado", 1.1, 1.25, .5, .45, "Un trago de coñac, que esto calienta.", "dialogo:CUÑADO"),
    ("21_ya_no", 1.0, 1.15, .45, .8, "El señor ya no tiembla.", "sub"),
    ("22_mala_senal", 1.0, 1.15, .5, .55, "Y con este frío, eso no es buena señal.", "sub"),
    ("23_decision", 1.0, 1.08, .3, .5, "Decides tú. A: un trago de coñac para que entre en calor.", "sub"),
    ("23_decision", 1.0, 1.08, .7, .5, "B: a cubierto, fuera la ropa mojada, mantas y, si está despierto, algo caliente con azúcar. Comenta A o B.", "sub"),
    ("24_manga", 1.0, 1.18, .45, .55, "El señor te agarra la manga:", "alarma"),
    ("25_susurra", 1.1, 1.3, .5, .5, "Al calvo de la barba… se lo llevaron anoche.", "dialogo:SEÑOR"),
    ("26_final", 1.0, 1.06, .5, .45, "", "decision"),
]
