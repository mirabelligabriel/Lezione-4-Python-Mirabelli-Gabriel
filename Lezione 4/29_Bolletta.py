quota_fissa = 20  
prezzo_primi_500 = 0.575  
prezzo_oltre_500 = 0.783  
consumo = float(input("Inserisci il consumo di gas in metri cubi: "))
if consumo <= 500:
    totale = quota_fissa + (consumo * prezzo_primi_500)
else:
    consumo_oltre_500 = consumo - 500
    totale = quota_fissa + (500 * prezzo_primi_500) + (consumo_oltre_500 * prezzo_oltre_500)
print("Il totale della bolletta è:", totale, "€")