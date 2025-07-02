# Chiedi due numeri all'utente con gestione dell'errore
def richiedi_numero(testo):
    """Richiede un numero all'utente e gestisce gli inserimenti non numerici."""
    while True:
        valore = input(testo)
        try:
            return float(valore)
        except ValueError:
            print("usa solo numeri pirla!")

numero1 = richiedi_numero("Inserisci il primo numero: ")
numero2 = richiedi_numero("Inserisci il secondo numero: ")

# Calcola la somma
somma = numero1 + numero2

# Stampa il risultato
print("La somma è:", somma)
