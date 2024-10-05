# language: es

Característica: Inicio del juego de adivinanza

  Escenario: Ver mensaje de bienvenida al iniciar el juego
    Dado que el juego esta configurado
    Cuando ejecuto el archivo principal
    Entonces el juego muestra el mensaje "Bienvenido al Juego de Adivinanza de Palabras!"
    Y el juego muestra el mensaje "La configuración inicial del juego se ha completado."
