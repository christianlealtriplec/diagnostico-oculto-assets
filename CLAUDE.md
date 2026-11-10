# Diagnóstico Oculto · Manual de producción diaria

Canal de historias interactivas de supervivencia con educación sanitaria. El responsable (sanitario) supervisa de forma puntual; Claude produce y publica **una parte al día a las 18:00 (Europe/Madrid)**, con 3 historias de Instagram (10:00 resultado · 17:47 estreno · 18:03 votación) en YouTube Shorts, Instagram Reels y TikTok.

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
- Especificación del montaje: `tools/parts/t1_p1.py` es el ejemplo (SHOTS con el texto hablado EXACTO troceado en frases cortas; ~2–3 s por plano). Usa el tipo `alarma` (temblor + destello rojo) en 2–3 planos por capítulo, en los golpes de la historia (aparece el problema, empeora, la complicación).
- Constructor: `python3 tools/build_part.py t1 N <segundos_de_voz>` → `t1/pN/t1_pN_sin_audio.mp4`.
- Voz: `vidiq_voiceover_generate` con voz `nPczCjzI2devNBz1zQrb` (Brian). Música: `recursos.musica_url` de estado.json.
- Alojamiento: el repo es público; las URL `https://raw.githubusercontent.com/christianlealtriplec/diagnostico-oculto-assets/main/...` sirven para vidIQ.

## Proceso diario (sesión programada, 09:13)
1. Clonar/actualizar el repo, leer `estado.json` y el guion de la parte siguiente (N = ultima_parte_programada + 1).
   **Guardia:** si la parte `ultima_parte_programada` se publica HOY o más tarde (aún no hay votos), NO produzcas nada: termina con un aviso de una línea («Hoy se publica el Capítulo X a las 18:00; mañana produzco el siguiente»).
2. **Votos de la parte N-1:** localizar su vídeo de YouTube en el canal `UClqKHj0j-QY2ZPPOrJChHAw` (`vidiq_user_videos` o `vidiq_channel_videos`), leer comentarios (`vidiq_video_comments`) y contar A/B (cuenta una opinión por autor; acepta «A», «la A», «opción A», etc.). Si es posible, sumar los de Instagram. Si hay menos de 10 votos en total, gana la opción **correcta** (la más didáctica). Guardar votos y rama en estado.json.
   **2b. Historia IG de resultado (10:00):** en cuanto tengas los votos, `python3 tools/stories.py resultado t1 N <ganadora> "<título del capítulo N>" <una escena PNG de la parte N-1>` (solo ganadora, título y «HOY A LAS 18H»; NUNCA el número de votos) → `t1/pN/story_resultado.mp4` (vídeo de 10 s con música); commit + push y programar en Metricool HOY a las 10:00 Europe/Madrid: providers solo instagram, `instagramData {type: STORY, isAiGenerated: true}`, media = URL raw del MP4, SIN texto. Si ya pasaron las 10:00, prográmala 10 minutos después de ahora.
3. **Guion hablado de la parte N** = apertura de la rama ganadora (narra la acción, NUNCA «Ganó la A/B») + historia + ESCALADA (solo si la decisión anterior fue la incorrecta, justo antes de «Decides tú») + decisión + SUSPENSO (≤ 1.000 caracteres; si se pasa, recortar SOLO frases narrativas, nunca la lección). Actualizar `salud` en estado.json según la tabla «Marcador de salud» del guion.
4. Generar la voz y anotar su duración real.
5. Dibujar las escenas nuevas de la parte, escribir `tools/parts/t1_pN.py` (gancho = HOOK_UI del guion; reloj = «HORA XX / 72»; `SALUD = estado.json["salud"]` (marcador de corazones fijo arriba a la izquierda); el SUSPENSO va en un plano `alarma` después del texto de la decisión, y el plano final es tipo `decision` con DECISION_UI y texto vacío (""), que dura solo la cola de 2,5 s; una tarjeta roja CARD_UI con la lección de la parte ANTERIOR justo después de la apertura) y construir el vídeo con la duración de la voz. El constructor pone en el primer fotograma (portada) la etiqueta amarilla «T1 · CAPÍTULO N» bajo el gancho; comprobarla en la revisión.
6. Revisar 4–6 fotogramas extraídos con ffmpeg: textos legibles, sin solapes, escenas que encajan con la frase. Corregir si hace falta.
7. Commit + push → `vidiq_video_upload` con la URL raw → `vidiq_compose` (1 escena = el vídeo; voiceover = la voz, volumen 1.1; music = musica_url, volume 0.6, duckTo 0.22, fadeMs 400) → esperar con `vidiq_job_poll`.
8. Programar en Metricool (`createScheduledPost`, blogId 7976298) para HOY a las 18:00 Europe/Madrid en youtube (type short, category EDUCATION, madeForKids false, isAiGeneratedContent true), instagram (REEL, isAiGenerated true) y tiktok (isAigc true). Título: `72 horas sin luz | T1 · Capítulo N: <título> 🔦 #shorts` (TikTok igual sin `#shorts`). Texto: primera línea `📺 T1 · Capítulo N: <título>` + gancho + pregunta A/B + «Comenta A o B» + aviso médico + hashtags `#72horassinluz #apagon #primerosauxilios #supervivencia #salud #diagnosticooculto`. Añadir siempre `firstCommentText` con el comentario de votación: «🗳️ VOTA AQUÍ 👇\nA) …\nB) …\nResponde con A o B. Mañana, el Capítulo N+1 según lo que gane.» (el epílogo no lleva votación). **8b. Historias IG de estreno y votación:** `python3 tools/stories.py estreno t1 N "<título>" "<HOOK_UI>" <escena PNG de la parte N>` → `t1/pN/story_estreno.mp4`, programar HOY a las 17:47; y `python3 tools/stories.py voto t1 N "<título>" "<opción A>" "<opción B>" <otra escena PNG de la parte N>` → `t1/pN/story_voto.mp4`, programar HOY a las 18:03. Ambas igual que la 2b (STORY, solo instagram, media = URL raw del MP4, sin texto). El epílogo no lleva historia de votación. Las historias NO son críticas: si fallan, sigue con el capítulo y menciónalo en el aviso. No responder comentarios automáticamente: vidIQ exige aprobación del texto exacto de cada respuesta.
9. Actualizar estado.json (parte, uuid de Metricool del reel y de las 3 historias, URL del vídeo, votos) → commit + push.
10. Avisar al responsable (mensaje corto): parte programada, enlace al vídeo, rama ganadora y votos, créditos restantes. Recordarle que puede cancelarla en Metricool antes de las 18:00.

## Lunes: informe semanal
Además del proceso diario, añadir al aviso una tabla con vistas, retención, comentarios/votos, seguidores ganados por red (Metricool analytics) y 1–2 recomendaciones.

## Fin de temporada y siguiente temporada
- El día que se programa la Parte 6, además: escribir el BORRADOR de la temporada siguiente en `temporadas/tN_guiones_BORRADOR.md` (mismo formato: 6 partes + epílogo, segunda persona, dilemas A/B reales, una lección sanitaria por parte, ≤1.000 caracteres por guion, contenido médico conservador y verificable), apoyándose en lo que mejor haya funcionado según las métricas. Enviar al responsable el enlace y la lista de puntos médicos a revisar.
- Un borrador NO se produce nunca. Solo cuando el responsable dé su OK médico se renombra a `tN_guiones.md`, se actualiza `estado.json` (temporada, parte 0) y la producción diaria continúa.
- Tras publicar el epílogo, si no hay temporada aprobada, NO producir: recordar al responsable que el borrador espera su OK.
