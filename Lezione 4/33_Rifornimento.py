prezzo_litro = 1.76
litri = float(input("Inserisci il numero di litri di benzina: "))
totale = litri * prezzo_litro
if totale > 60:
    totale = totale * 0.95
print("Il totale da pagare è:", totale)