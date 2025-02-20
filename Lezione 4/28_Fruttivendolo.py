prezzo_pesca = float(input("inserisci il prezzo di una pesca: "))
quantità = int(input("inserisci il numero di pesche acquistate: "))
totale = prezzo_pesca * quantità
if totale > 10:
    totale = totale * 0.80
print("il totale da pagare è:", totale)