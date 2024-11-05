import json

def help_menu():

    """Menu di aiuto per l'utente"""

    print("I comandi disponibili sono i seguenti:")
    print("aggiungi: aggiungi un prodotto al magazzino")
    print("elenca: elenca i prodotti in magazzino")
    print("vendita: registra una vendita effettuata")
    print("profitti: mostra i profitti totali")
    print("aiuto: mostra i possibili comandi")
    print("chiudi: esci dal programma")

def leggi_dizionario_da_file(magazzino, inventory_file):

    """Funzione per l'apertura del file esterno e aggiornamento dell'inventario all'avvio del programma e gestione degli eventuali errori """

    try:
        with open(inventory_file, 'r') as file:
            content = file.read()  
            if content:
                magazzino.inventory = json.loads(content)  
            else:
                magazzino.inventory = {}
    except FileNotFoundError:
        magazzino.inventory = {}
    except json.JSONDecodeError:
        print(f"Errore: Il file {inventory_file} non contiene un JSON valido.")
        magazzino.inventory = {}

def scrivi_dizionario_su_file(magazzino, inventory_file):

    """Scrittura del contentuto dell'inventario alla chiusura del programma in un file esterno"""
    
    with open(inventory_file, 'w') as file:
        json.dump(magazzino.inventory, file, indent=4)