from warehouse import Warehouse
from utilities import help_menu, leggi_dizionario_da_file, scrivi_dizionario_su_file
import json

def commands():
        
        """Piccola console di comando per la creazione dell'istanza e la gestione dei diversi metodi in base all'input utente"""
        
        inventory_file = 'inventory.json'
        magazzino = Warehouse()
        leggi_dizionario_da_file(magazzino, inventory_file)
        command = input('Inserisci un comando: ')
        while command != 'chiudi':
            if command == "aggiungi":
                magazzino.add_product()
            elif command == 'vendita':
                magazzino.sell_product()
            elif command == 'elenca':
                magazzino.stampa()
            elif command == "aiuto":
                help_menu()
            elif command == 'profitti':
                magazzino.profit_calculate()
            else:
                print('Comando non valido')
                help_menu()
            command = input('Inserisci un comando: ')
        scrivi_dizionario_su_file(magazzino, inventory_file)
        print('Bye Bye')
if __name__ == '__main__':
    commands()