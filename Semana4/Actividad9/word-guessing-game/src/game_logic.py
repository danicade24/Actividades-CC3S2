import random

def select_word():
    """
    Selección de una palabra al azar del archivo words.txt.
    """
    arr = []
    try:
        with open("words.txt") as file:
            for line in file:
                arr.append(line.strip())
            return arr[random.randint(0, len(arr) - 1)]
    except FileNotFoundError:
        print("El archivo 'words.txt' no fue encontrado.")
    
        
def guess_letter(word, letter, secret_word):
    """
    Recibe una letra del jugador y verifica si está en la palabra secreta.
    Actualiza el progreso del jugador.
    Controla los intentos restantes.
    """
    var = 0
    for char in word:
        if letter == char:
            var += 1
    
    if var != 0:
        print(f"¡Correcto! La letra '{letter}' está en la palabra")
        replace(word, secret_word, letter)
    else:
        print(f"La letra '{letter}' no está en la palabra")
        
            
def give_hint(word, secret_word):
    """
        Ofrece al jugador una pista revelando una letra aleatoria 
        de la palabra secreta.
        Limita el número de pistas disponibles.
    """
    hints = []
    for char in word:
        hints.append(char)
    
    while True:
        hint = random.choice(hints)
        if hint not in secret_word:
            break
    
    print(f"\nPista: La letra '{hint}' está en la palabra.")
    replace(word, secret_word, hint)
    
def replace(word,secret_word, letter):
    for index, char in enumerate(word):
            if char == letter:
                secret_word[index] = letter
            else:
                pass
    print(f"Palabra: ", end="")
    print(" ".join(secret_word)) 
    print()