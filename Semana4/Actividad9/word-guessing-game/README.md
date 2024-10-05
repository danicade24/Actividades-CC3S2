## Juego de Adivinanza

## Descripción
Este juego consiste en adivinar una palabra secreta letra por letra. A medida que el jugador va adivinando, el juego muestra el progreso, revelando las letras correctas adivinadas y manteniendo ocultas las que faltan por descubrir.

## Funcionalidades futuras

- **Selección aleatoria de palabras:** Las palabras a adivinar se seleccionarán aleatoriamente de una lista.
- **Sistema de pistas limitado:** El jugador podrá pedir pistas, pero estas estarán limitadas.
- **Control de intentos fallidos:** Se tendrá un número limitado de intentos fallidos antes de que el jugador pierda la partida.
- **Niveles de dificultad:** Permitirá que el jugador seleccione un nivel de dificultad para el juego.
- **Tabla de puntuaciones:** Un sistema para registrar y mostrar las puntuaciones de los jugadores.

## Instrucciones para ejecutar el juego

1. Debe de clonar el repositorio donde se enuentra el juego
    ```bash
    git clone https://github.com/danicade24/Actividades-CC3S2.git
    ```
2. Diríjase al directorio donde se encuentra el juego

    ```bash
    cd Actividades-CC3S2/Semana4/Actividad9/word-guesing-game
    ```

3. Ejecute el comando
    ```bash
    python3 src/main.py
    ```
4. Para ejecutar la prueba automatizada de BDD que valida la funcionalidad del mensaje de bienvenida, utiliza el siguiente comando:
    ```bash
    behave
    ```
    Antes de ejecutar verifique si tiene `behave`instalado, si no lo tiene puede instalarlo con:

    ```bash
    pip install behave
    ```


    Después de ejecutarlo debería obtener una salida como esta:

    ```gherkin
    Característica: Inicio del juego de adivinanza # features/iniciar_juego.feature:3

    Escenario: Ver mensaje de bienvenida al iniciar el juego                                # features/iniciar_juego.feature:5
        Dado que el juego esta configurado                                                    # features/steps/game_steps.py:8 0.000s
        Cuando ejecuto el archivo principal                                                   # features/steps/game_steps.py:13 0.026s
        Entonces el juego muestra el mensaje "Bienvenido al Juego de Adivinanza de Palabras!" # features/steps/game_steps.py:21 0.000s
        Y el juego muestra el mensaje "La configuración inicial del juego se ha completado."  # features/steps/game_steps.py:21 0.000s

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    4 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.026s
    ```

### Nota: En este momento el juego se encuentra en la fase inicial de desarrollo, si se ejecuta lanzará como salida:
```bash
Bienvenido al Juego de Adivinanza de Palabras!

La configuración inicial del juego se ha completado.
```
