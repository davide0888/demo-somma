import os

while True:
    # Chiedi due numeri all'utente
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))

    # Calcola la somma
    somma = numero1 + numero2

    # Stampa il risultato
    print("La somma è:", somma)

    # Attendi input per ricominciare o uscire
    scelta = input("Premi un tasto per ricominciare oppure 'q' per uscire: ")
    if scelta.lower() == 'q':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
