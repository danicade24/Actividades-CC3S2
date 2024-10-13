"""
Este módulo contiene los steps para las pruebas BDD del Juego de Adivinanza
"""

from behave import given, when, then
import subprocess

@given('que el juego esta configurado')
def step_configure_game(context):
    # No hay configuración necesaria aquí por el momento
    pass

@when('ejecuto el archivo principal')
def step_execute_game(context):
    # La función subprocess.run() se llama con los argumentos ["python", "file"]. 
    # Esto significa que el intérprete de Python será llamado para ejecutar el script file.py
    # capture_output=True permite obtener la salida del script en la variable result.stdout
    result = subprocess.run(['python', 'src/main.py'], stdin=None, capture_output=True, text=True)
    context.output = result.stdout  # Guardar la salida en el contexto

@then('el juego muestra el mensaje "{mensaje}"')
def step_check_message(context, mensaje):
    # Verificar si el mensaje esperado está en la salida capturada
    assert mensaje in context.output, f"Se esperaba que apareciera '{mensaje}' pero no apareció. Salida: {context.output}"
