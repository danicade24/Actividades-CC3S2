import random
from src import game_logic

def test_select_word(mocker):
    # Simulamos la apertura de un archivo que contiene "perro", "gato", "elefante"
    mocker.patch("builtins.open", mocker.mock_open(read_data="perro\ngato\nelefante"))
    palabra = game_logic.select_word()  # No pasar 'filename'
    assert palabra in ["perro", "gato", "elefante"]

def test_file_not_found(mocker):
    # Simulamos que el archivo no existe, lanzando un FileNotFoundError
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    palabra = game_logic.select_word()  # No pasar 'filename'
    assert palabra is None
