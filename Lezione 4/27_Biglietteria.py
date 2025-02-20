prezzo = float(input("inserisci il prezzo del biglietto: ")) 
numero = int(input("inserisci il numero di biglietti acquistati: "))
omaggio = numero // 20
biglietti_pagati = numero - omaggio
totale = biglietti_pagati * prezzo
print("il totale da pagare è:", totale)