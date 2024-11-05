class Warehouse:

    """Classe Warehouse per la creazione di un piccolo gestionale"""

    def __init__(self):
        self.inventory = {}
        self.dizionario_vendite = {}

    def add_product(self):

        """"Metodo per aggiungiungere nuovi prodotti al magazzino"""

        product_name = self.inserimento_controllo_nome()
        quantity = self.inserimento_controllo_quantita()
        self.check_product(product_name,quantity)
        self.check_lunghezza_dizionario(product_name,quantity)

    def inserimento_controllo_nome(self):

        """Metodo per controllare che il nome insierito non contenga caratteri numerici"""

        while True:
            try:
                product_name = input("Inserisci il nome del prodotto: ")
                for i in product_name:
                    if i.isdigit():
                        raise ValueError("Il nome del prodotto non può contenere numeri.")
                return product_name
            except ValueError as Errore:
                print(Errore)

    def inserimento_controllo_quantita(self):

        """Metodo per controllare che la quantitá inserita sia un numero positivo"""

        while True:
            try:
                quantity = input('Inserisci la quantità: ')
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError('La quantità del prodotto deve essere un numero intero positivo, Riprova:')
                else:
                    return quantity
            except ValueError as errore:
                print('Errore:', errore)
        
    def check_product(self, product_name, quantity):

        """Metodo per controllare la presenza del prodotto nell'inventario e aggiungere quantitá"""

        if  product_name in self.inventory:
            if 'quantity' in self.inventory[product_name]:
                self.inventory[product_name]['quantity'] += quantity
        else:
            self.inventory[product_name]={'quantity': quantity}    

    def check_lunghezza_dizionario(self, product_name,quantity):

        """Metodo per il controllo della lunghezza della lista e aggiunta di prezzo vendita e prezzo acquisto"""

        if len(self.inventory[product_name])<3:
            while True:
                try:
                    buy_price = float(input('Inserisci il prezzo di acquisto: '))
                    sell_price = float(input('Inserisci il prezzo di vendita: '))
                    if buy_price < 0 or sell_price < 0:
                        raise ValueError('Il prezzo non può essere negativo.')
                    if sell_price <= buy_price:
                        raise ValueError('Il prezzo di vendita deve essere maggiore del prezzo di acquisto.')
                    self.inventory[product_name]['buy_price'] = buy_price
                    self.inventory[product_name]['sell_price'] = sell_price
                    break
                except ValueError as errore:
                    print('Errore:', errore)
                    print('Assicurati di inserire solo valori numerici per i prezzi.')
            return print(f'AGGIUNTO: {quantity}  X  {product_name}')
        else:
            return print(f'AGGIUNTO: {quantity}  X  {product_name}')
    

    def sell_product(self):

        """Metodo per aggiungere le vendite"""

        product_name = self.inserimento_controllo_nome_vendite()
        quantity = self.inserimento_controllo_quantita_vendite(product_name)
        self.sell_go_on(product_name, quantity)


    def inserimento_controllo_nome_vendite(self):

        """Metodo per il contollo del nome inserito e gestione degli errori"""

        while True:
            try:
                product_name = input("Inserisci il nome del prodotto: ")
                if product_name.isdigit():
                    raise ValueError("Il nome del prodotto non può essere un numero.")
                if product_name not in self.inventory:
                    raise NameError('Il nome del prodotto non è presente in magazzino.')
                return product_name
            except ValueError as Errore:
                print(Errore)
            except NameError as Errore1:
                print(Errore1)

    def inserimento_controllo_quantita_vendite(self, product_name):

        """Metodo per il controllo della validitá della quantitá inserita"""

        while True:
            try:
                quantity = int(input('Inserisci la quantità: '))
                if quantity <= 0:
                    raise ValueError('La quantità deve essere maggiore di zero.')
                elif quantity > self.inventory[product_name]['quantity']:
                    raise ValueError('La quantità deve essere inferiore o uguale a quella presente in magazzino.')
                else:
                    return quantity
            except ValueError as errore:
                print('Errore:', errore)
    
    def sell_go_on(self, product_name, quantity):

        """Metodo per consentire l'aggiunta di diversi prodotti in fase di vendita e aggiornamento dei dizionari"""

        comando = input('Aggiungere un altro prodotto? (si/no)')
        if comando == 'si':
            self.dizionario_vendite[product_name] = {'quantity': quantity, 'sell_price': self.inventory[product_name]['sell_price'], 'buy_price': self.inventory[product_name]['buy_price']}
            self.inventory[product_name]['quantity'] -= quantity
            self.sell_product()
        
        elif comando == 'no':
            self.dizionario_vendite[product_name] = {'quantity': quantity, 'sell_price': self.inventory[product_name]['sell_price'], 'buy_price': self.inventory[product_name]['buy_price']}
            self.inventory[product_name]['quantity'] -= quantity
            print('VENDITA REGISTRATA')
            list_tot = []
            for product_name, values in self.dizionario_vendite.items():
                totale = (values['quantity'] * values['sell_price']) 
                list_tot.append(totale)
                print(f"- {values['quantity']} X {product_name}: € {values['sell_price']}")
                
            print(f"TOTALE : {sum(list_tot):.2f} €")
    
    def profit_calculate(self):

        """Metodo per il calcolo del profitto"""

        lordo_totale = 0
        netto_totale = 0

        for product , values in self.dizionario_vendite.items():
            lordo = values['quantity'] * values['sell_price']
            netto = lordo - (values['quantity'] * values ['buy_price'])
            lordo_totale += lordo
            netto_totale += netto
        return print(f'Profitto: Lordo = {lordo_totale:.2f}  Netto = {netto_totale:.2f}  ' )
        

    def stampa(self):

        """Metodo per stampare la situzione del magazzino"""
        
        print(f"{'PRODOTTO':<20} {'QUANTITA':<10} {'PREZZO'}")
        no_quantities = []
        for product, values in self.inventory.items():
            if values['quantity']== 0:
                no_quantities.append(product)

        for product, values in self.inventory.items():
            print(f"{product:<20} {values['quantity']:<10} {values['sell_price']}")