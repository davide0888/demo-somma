"""Somma di due numeri con gestione delle eccezioni.

L'utente puo' uscire dal programma soltanto premendo il tasto 'q'.
Tutti gli altri errori vengono gestiti per evitare la chiusura improvvisa.
"""


def chiedi_numero(prompt: str):
    """Chiede un numero all'utente e gestisce l'uscita con 'q'."""
    while True:
        try:
            valore = input(prompt)
            if valore.lower() == 'q':
                return 'q'
            return float(valore)
        except ValueError:
            print("Valore non valido. Riprovare o premere 'q' per uscire.")
        except Exception as err:
            # Gestione generica di eventuali errori imprevisti
            print(f"Errore: {err}. Riprovare o premere 'q' per uscire.")


def main():
    print("Calcolatore di somma. Premi 'q' in qualsiasi momento per uscire.")
    while True:
        try:
            numero1 = chiedi_numero("Inserisci il primo numero: ")
            if numero1 == 'q':
                break
            numero2 = chiedi_numero("Inserisci il secondo numero: ")
            if numero2 == 'q':
                break
            somma = numero1 + numero2
            print("La somma è:", somma)
        except KeyboardInterrupt:
            # L'utente ha premuto Ctrl+C: avviso e continua
            print("\nInterruzione tramite tastiera. Premere 'q' per uscire.")
        except EOFError:
            # L'utente ha premuto Ctrl+D: avviso e continua
            print("\nFine dell'input rilevata. Premere 'q' per uscire.")
        except Exception as err:
            # Gestione di eventuali errori non previsti
            print(f"Errore inaspettato: {err}. Riprovare.")
    print("Uscita dal programma.")


if __name__ == "__main__":
    main()
