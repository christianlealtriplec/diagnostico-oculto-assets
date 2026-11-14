# Diagnóstico Oculto · Manual de producción diaria

Canal de historias interactivas de supervivencia con educación sanitaria. El responsable (sanitario) supervisa de forma puntual; Claude produce y publica **una parte al día a las 18:00 (Europe/Madrid)** en YouTube Shorts, Instagram Reels y TikTok, **alternando dos series independientes** según `temporadas/calendario.json`: «72 horas sin luz» (apagón, ilustrada, votación A/B) y «El crucero que regresó vacío» (expediente realista, sin votación). Con el apagón van 3 historias de Instagram (10:00 resultado · 17:47 estreno · 18:03 votación). Plan aprobado el 13/11/2026: documento «Diagnóstico Oculto · Plan de la nueva fase». Las dos historias NO se cruzan nunca.

## Reglas que no se rompen
1. **Contenido médico:** usar SOLO los guiones aprobados de `temporadas/`. No inventar ni cambiar consejos médicos. Si una temporada no tiene guiones aprobados, NO producir: avisar al responsable.
2. **Publicar** solo partes de guiones aprobados, con el aviso «Ficción con fines educativos. No sustituye una consulta médica. Ante una urgencia, llama al 112.» y la etiqueta de IA activada en las 3 redes.
3. **Créditos vidIQ:** comprobar `vidiq_balance` al empezar. Si quedan < 150, no producir y avisar.
4. **Si algo falla** (voz, montaje, subida, programación): no publicar nada a medias. Avisar al responsable con qué falló.
5. **Nunca** regenerar voz o montaje de pago sin motivo; cada parte cuesta ~45 créditos (voz 28 + montaje ~17).
6. Mensajes al responsable: cortos, en tabla, sin relleno.

## Recursos
- Estado de la temporada: `temporadas/estado.json` (actualizar SIEMPRE al terminar y hacer commit + push).
- Guiones: `temporadas/t1_guiones.md`.
- Dibujo: `tools/draw.py` (personajes: `abuela()`, `tio()`, `phone_hand()`, `concentrator()`, `oxygen_bottle()`, escenarios en `tools/draw2.py`). Estilo: noche azul oscuro, haz de linterna cálido, acentos rojos, viñeta. Reutilizar personajes para que sean siempre iguales.
- Escenas por parte: `tools/t1_p1.py` es el ejemplo. Crear `tools/t1_pN.py` con ~12–15 escenas NUEVAS (cada imagen como máximo 2 veces en la parte) y renderizar a `t1/pN/`.
- Especificación del montaje: `tools/parts/t1_p1.py` es el ejemplo (SHOTS con el texto hablado EXACTO troceado en frases cortas; ~2–3 s por plano). Usa el tipo `alarma` (temblor + destello rojo) en 2–3 planos por capítulo, en los golpes de la historia (aparece el problema, empeora, la complicación). Cada frase de diálogo (entre comillas en el guion) va en su propio plano `dialogo:NOMBRE` (bocadillo con el nombre: CARMEN, HUGO, LUIS, CUÑADO, MADRE, TÍA, DON RAMÓN, TÚ, RADIO, MEGÁFONO) sobre una escena con ese personaje; la narración, en `sub`/`alarma`. Objetivo: que el capítulo se sienta vivido, no contado. Que los personajes HAGAN cosas (cargar, buscar, subir escaleras, tapar, abrir puertas) y que los escenarios cambien dentro del capítulo (salón, cocina, rellano, escalera, patio, calle, puerta del 4.º A…); evita repetir el mismo plano estático. Si aparece un personaje nuevo (p. ej. Don Ramón), créalo una vez como función en `tools/draw.py` y reutilízalo siempre.
- Constructor: `python3 tools/build_part.py t1 N <segundos_de_voz>` → `t1/pN/t1_pN_sin_audio.mp4`.
- Voz: `vidiq_voiceover_generate` con voz `nPczCjzI2devNBz1zQrb` (Brian). Música: `recursos.musica_url` de estado.json.
- Alojamiento: el repo es público; las URL `https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/...` sirven para vidIQ.

## Qué toca hoy
**⚠ METRICOOL SIN CUPO (14-nov-2026):** el plan gratis de Metricool solo publica 20 por mes (cuenta 1 por red) y quedan 5, reservados. Hasta nueva orden en este manual: NO uses `createScheduledPost` ni `updateScheduledPost` y NO hagas historias de IG. Produce la parte con normalidad hasta tener el vídeo final de vidIQ (pasos de voz, montaje y revisión), guarda su URL en estado.json (estado «montada, pendiente de publicar»), commit + push, y avisa al responsable con el enlace: la sesión principal la publicará por otra vía. No avances `ultima_parte_programada` hasta que esté programada.

Lee `temporadas/calendario.json` y busca la fecha de hoy. Si no hay entrada, no produzcas y avisa. Si la parte del calendario de hoy ya está programada (≤ `ultima_parte_programada` de su serie), no produzcas nada (solo el informe del lunes, si toca) y termina sin aviso. Si toca **crucero** y `estado.json → series.crucero.listo` no es `true`, NO produzcas: avisa al responsable («hoy tocaba el crucero, piloto pendiente de validar»); si es `true`, sigue la sección «Crucero» de abajo. Si toca **apagón**, sigue el proceso de abajo con N = la parte del calendario (debe ser ultima_parte_programada + 1; si no coincide, no produzcas y avisa). Numeración: PARTE 01, 02… nunca se reinicia; títulos `72 horas sin luz | Parte NN: <título> 🔦 #shorts` y `El crucero que regresó vacío | Parte NN: <título> 🚢 #shorts`.

## Proceso diario del apagón (sesión programada, 09:13)
1. Clonar/actualizar el repo, leer `estado.json` y el guion de la parte N del calendario.
   **Guardia:** si la parte `ultima_parte_programada` se publica HOY o más tarde (aún no hay votos), NO produzcas nada: termina con un aviso de una línea («Hoy se publica el Capítulo X a las 18:00; mañana produzco el siguiente»).
2. **Votos de la parte N-1:** localizar su vídeo de YouTube en el canal `UClqKHj0j-QY2ZPPOrJChHAw` (`vidiq_user_videos` o `vidiq_channel_videos`), leer comentarios (`vidiq_video_comments`) y contar A/B (cuenta una opinión por autor; acepta «A», «la A», «opción A», etc.). Si es posible, sumar los de Instagram. Si hay menos de 10 votos en total, gana la opción **correcta** (la más didáctica). Guardar votos y rama en estado.json.
   **2b. Historia IG de resultado (10:00):** en cuanto tengas los votos, `python3 tools/stories.py resultado t1 N <ganadora> "<título del capítulo N>" <una escena PNG de la parte N-1>` (solo ganadora, título y «HOY A LAS 18H»; NUNCA el número de votos) → `t1/pN/story_resultado.mp4` (vídeo de 10 s con música); commit + push y programar en Metricool HOY a las 10:00 Europe/Madrid: providers solo instagram, `instagramData {type: STORY, isAiGenerated: true}`, media = URL raw del MP4, SIN texto. Si ya pasaron las 10:00, prográmala 10 minutos después de ahora.
3. **Guion hablado de la parte N** = apertura de la rama ganadora (narra la acción, NUNCA «Ganó la A/B») + historia + ESCALADA (solo si la decisión anterior fue la incorrecta, justo antes de «Decides tú») + decisión + SUSPENSO (≤ 1.000 caracteres; si se pasa, recortar SOLO frases narrativas, nunca la lección). Actualizar `salud` en estado.json según la tabla «Marcador de salud» del guion.
4. Generar la voz y anotar su duración real.
5. Dibujar las escenas nuevas de la parte, escribir `tools/parts/t1_pN.py` (gancho = HOOK_UI del guion; reloj = «HORA XX / 72»; `SALUD = estado.json["salud"]` (marcador de corazones fijo arriba a la izquierda); `MOCHILA = estado.json["mochila"]` (recuadro arriba a la derecha, máx. 4 objetos; «+» ayuda, «-» perjudica), actualizado antes con la línea «Mochila:» del guion del capítulo; el SUSPENSO va en un plano `alarma` después del texto de la decisión, y el plano final es tipo `decision` con DECISION_UI y texto vacío (""), que dura solo la cola de 2,5 s; una tarjeta roja CARD_UI con la lección de la parte ANTERIOR justo después de la apertura) y construir el vídeo con la duración de la voz. El constructor pone en el primer fotograma (portada) la etiqueta amarilla «PARTE NN» bajo el gancho; comprobarla en la revisión.
6. Revisar 4–6 fotogramas extraídos con ffmpeg: textos legibles, sin solapes, escenas que encajan con la frase. Corregir si hace falta.
7. Commit + push → `vidiq_video_upload` con la URL raw → `vidiq_compose` (1 escena = el vídeo; voiceover = la voz, volumen 1.1; music = musica_url, volume 0.6, duckTo 0.22, fadeMs 400) → esperar con `vidiq_job_poll`.
8. Programar en Metricool (`createScheduledPost`, blogId 7976298) para HOY a las 18:00 Europe/Madrid en youtube (type short, category EDUCATION, madeForKids false, isAiGeneratedContent true), instagram (REEL, isAiGenerated true) y tiktok (isAigc true). Título: `72 horas sin luz | Parte NN: <título> 🔦 #shorts` (TikTok igual sin `#shorts`). Texto: primera línea `📺 72 horas sin luz · Parte NN: <título>` + gancho + pregunta A/B + «Comenta A o B» + aviso médico + hashtags `#72horassinluz #apagon #primerosauxilios #supervivencia #salud #diagnosticooculto`. Añadir siempre `firstCommentText` con el comentario de votación: «🗳️ VOTA AQUÍ 👇\nA) …\nB) …\nResponde con A o B. La Parte N+1, en dos días, según lo que gane.» (el epílogo no lleva votación). **8b. Historias IG de estreno y votación:** `python3 tools/stories.py estreno t1 N "<título>" "<HOOK_UI>" <escena PNG de la parte N>` → `t1/pN/story_estreno.mp4`, programar HOY a las 17:47; y `python3 tools/stories.py voto t1 N "<título>" "<opción A>" "<opción B>" <otra escena PNG de la parte N>` → `t1/pN/story_voto.mp4`, programar HOY a las 18:03. Ambas igual que la 2b (STORY, solo instagram, media = URL raw del MP4, sin texto). El epílogo no lleva historia de votación. Las historias NO son críticas: si fallan, sigue con el capítulo y menciónalo en el aviso. No responder comentarios automáticamente: vidIQ exige aprobación del texto exacto de cada respuesta.
9. Actualizar estado.json (parte, uuid de Metricool del reel y de las 3 historias, URL del vídeo, votos) → commit + push.
10. Avisar al responsable (mensaje corto): parte programada, enlace al vídeo, rama ganadora y votos, créditos restantes. Recordarle que puede cancelarla en Metricool antes de las 18:00.

## Lunes: informe semanal
Además del proceso diario, añadir al aviso una tabla con vistas, retención, comentarios/votos, seguidores ganados por red (Metricool analytics) y 1–2 recomendaciones.

## Crucero («El crucero que regresó vacío»)
Expediente realista, narra la Dra. Elena Varela. SIN votación, SIN marcador de salud ni mochila. Historias de IG: ninguna (solo el apagón las lleva).
Guiones: `temporadas/crucero_guiones.md`. Ejemplo completo y probado: `tools/crucero_p01.py` (Parte 01, publicada el 16-nov).

### Guardias (antes de gastar nada)
- N = parte del calendario = `series.crucero.ultima_parte_programada + 1`; si no, no produzcas y avisa.
- El encabezado de la Parte N en el guion debe estar aprobado: si dice «BORRADOR» o «pendiente de OK», o no existe, NO produzcas y avisa («el guion de la Parte N del crucero está pendiente de tu OK»).
- `vidiq_balance` ≥ 150.
- No revelar nada que el guion no diga; no cruzar nunca con el apagón.

### Proceso
1. Voz: `vidiq_voiceover_generate` con el guion EXACTO (sin las comillas «» exteriores) y la voz `series.crucero.voz_id` (Sarah). Anota URL y duración real.
2. Imágenes IA nuevas (solo las que marca «Recursos» del desglose): `vidiq_generate_thumbnail` purpose "image", 9:16, fotorrealista cinematográfico, sin texto ni logotipos; si sale el barco, pasa `barco_maestro.url` como referenceImages; si sale un personaje ya creado, su URL de `series.crucero.imagenes`. Guarda la URL en `series.crucero.imagenes.<nombre>` (se reutiliza toda la serie). Si una imagen IA sale con texto, deformaciones o no encaja con la frase, se repite UNA vez como máximo; si vuelve a fallar, usa vídeo de archivo y menciónalo en el aviso.
3. Archivo: `vidiq_find_broll` (vertical) por cada plano «archivo»; elige un clip 1080×1920 (o 2160×3840) que encaje con la frase y apunta el autor de Pexels.
4. Copia `tools/crucero_p01.py` → `tools/crucero_pNN.py` y ajusta: OUT/RAW (`crucero/pNN/`), VOZ (duración real), IMG/VID, SHOTS (texto hablado EXACTO troceado en frases de 1,5–2,5 s; subtítulo con `*palabra*` en rojo; capas `chip:`, `sello:`, `nota`, `cierre`), las escenas propias de `capas()` (fichas con `C.ficha`, móvil con `C.notificacion`/`C.chat`, historias de Noa con `C.historia` como capa sobre la imagen) y el texto de `V.portada(N, gancho)` y `V.cierre(pregunta, "PARTE N+1 EL <DÍA>")`. Cada imagen IA, como mucho 2 veces por parte. Ejecuta: `python3 tools/crucero_pNN.py` → capas PNG + `crucero/pNN/compose.json`.
5. Revisión local: superpone 4–6 capas sobre la imagen o un fondo oscuro (`V.componer`) y míralas: textos legibles, sin solapes, portada con «PARTE NN», cierre correcto, sin destripes. Corrige si hace falta.
6. Commit + push (las capas deben estar en GitHub antes del montaje) → `vidiq_compose` con el contenido de compose.json (voz 1.1; música `series.crucero.musica_url` 0.7, duckTo 0.25, fadeMs 400) → `vidiq_job_poll` hasta el final. Si falla, NO programes y avisa.
7. Metricool `createScheduledPost` (blogId 7976298) para la fecha del calendario a las 18:00 Europe/Madrid, youtube (short, category ENTERTAINMENT, madeForKids false, isAiGeneratedContent true, tags de la serie), instagram (REEL, showReelOnFeed, isAiGenerated true) y tiktok (PUBLIC_TO_EVERYONE, isAigc true), media = URL del vídeo final. Copia el formato del post de la Parte 01 (uuid -2537489549492335008):
   - Título: `El crucero que regresó vacío | Parte NN: <título> 🚢 #shorts` (TikTok sin `#shorts`).
   - Texto: `🚢 El crucero que regresó vacío · Parte NN: <título>` + 2 frases de gancho (sin destripar el final) + «¿Qué crees que pasó? Te leo en comentarios.» + «Ficción: barco, naviera y personajes inventados. Ficción con fines educativos. No sustituye una consulta médica. Ante una urgencia, llama al 112.» + «Imágenes de archivo: Pexels (<autores>).» + `#elcruceroqueregresovacio #misterio #crucero #expedientepersefone #historiasdemisterio #diagnosticooculto`.
   - `firstCommentText`: «🕵️ <pregunta del cierre>\nDeja tu teoría aquí 👇\nParte NN+1, el <día> a las 18:00.» (en la Parte 14: «Gracias por seguir el expediente.» sin anunciar otra parte).
8. estado.json → `series.crucero.partes.N` (título, video_final, duración, voz_url, metricool_uuid, post_id, créditos, estado) y `ultima_parte_programada = N`; línea en registro.log; commit + push.
9. Aviso al responsable (tabla): parte, fecha y hora, enlace al vídeo, imágenes nuevas, créditos gastados y restantes, y que puede cancelarlo en Metricool.

### Guiones del crucero
Se escriben en la sesión principal con 4 días de antelación y el responsable los aprueba (encabezado sin «BORRADOR»). La tarea programada no escribe ni cambia guiones.

## Continuidad y guiones nuevos
- Cada parte empieza en el segundo exacto en que acabó la anterior de su serie; cada problema nace del anterior; las pistas se recuperan.
- Los guiones completos se escriben con antelación en la sesión principal. La tarea programada NO escribe borradores de temporada ni inventa partes: si falta el guion de la parte del calendario, no produce y avisa.
- Contenido médico: solo el aprobado (lecciones del arco «Sin fecha de fin» aprobadas el 13/11/2026; datos forenses del crucero, ídem).
