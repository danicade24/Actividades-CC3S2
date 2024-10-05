from game_logic import *

def game():
    print("Bienvenido al Juego de Adivinanza de Palabras!\n")
    print("La configuración inicial del juego se ha completado.\n")
    word = select_word()
    if word:
        print(f"La palabra ha sido seleccionada. ¡Comienza a adivinar!\n")
    
    print(" ".join(word) + '\n')    #imprime la palabra secreta
    
    secret_word = ["_"] * len(word)
    
    print(f"Palabra: ", end="")
    print(" ".join(secret_word)) 
    print()
    
    var=True
    while var:
        chain =  ''.join(secret_word)   #convertimos secret_word a sting
        if chain == word:
            var=False
            break
        
        # Adivina una letra de la palabra
        letter = input("Adivina una letra: ")
        guess_letter(word, letter, secret_word)
        
        chain =  ''.join(secret_word)   #convertimos secret_word a sting
        if chain == word:
            var=False
            break
        
        # Dar pista al jugador
        res = input(f"\n¿Necesita una pista(s/n)?: ")
        if res.lower() == 's':
            give_hint(word, secret_word)
    
if __name__ == "__main__":
    game()