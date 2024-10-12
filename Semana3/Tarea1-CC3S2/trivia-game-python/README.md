## Tarea 1: Juego de trivia

### Descripción del juego

Es un juego de preguntas y respuestas donde los jugadores deben de responder preguntas con opción múltiples, es decir, cada pregunta tendrá una sola respuesta correcta.

### Reglas del juego

- El juego constará de 10 rondas con preguntas únicas
- Cada pregunta cuenta con 4 opciones de posibles respuestas numeradas. Solo una opción es la correcta.
- El jugador elige su respuesta ingresando el número correspondiente a la opción elegida.
- Cada respuesta correcta otorga un punto al jugador y las respuestas incorrectas no se penalizan.
- Al finalizar el juego, se mostrará la puntuación total del jugador junto con el número de respuestas correctas e incorrectas.

Primero construimos el contenedor de docker-compose con el comando:
```bash
docker compose up --build
```

Para acceder a nuestra base de datos ejecutamos
```bash
docker exec -it trivia-game-python-db-1 psql -U user -d trivia_db
```



