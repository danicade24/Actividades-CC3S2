from game_logic import *

def game():
    print("\nBienvenido al Juego de Adivinanza de Palabras!\n")
    print("La configuración inicial del juego se ha completado.\n")
    word = select_word()
    if word:
        print(f"La palabra ha sido seleccionada. ¡Comienza a adivinar!\n")
    
    #print(" ".join(word) + '\n')    #imprime la palabra secreta
    
    secret_word = ["_"] * len(word)
    
    print(f"Palabra: ", end="")
    print(" ".join(secret_word)) 
    print()
    
    
    attempts = len(word) + 1
    number = 0
    
    while attempts > 0:
        chain =  ''.join(secret_word)   #convertimos secret_word a sting
        if chain == word:
            print(f"¡Felicidades! Has adivinado la palabra: '{word}'")
            break
        
        # Adivina una letra de la palabra
        letter = input("Adivina una letra: ")
        guess_letter(word, letter, secret_word, attempts)
        attempts -= 1
        
        chain =  ''.join(secret_word)   #convertimos secret_word a sting
        if chain == word:
            print(f"\n¡Felicidades! Has adivinado la palabra: '{word}'")
            break
        
        # Dar pista al jugador
        res = input(f"\n¿Necesita una pista(s/n)?: ")
        if res.lower() == 's':
            attempts -= 1
            give_hint(word, secret_word, number)
            number += 1
    
    if chain != word:
        print(f"\nLo siento, has pedido. La palabra era: '{word}'")
if __name__ == "__main__":
    game()