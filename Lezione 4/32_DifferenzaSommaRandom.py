import random
numero1 = random.randint(0, 10)
numero2 = random.randint(0, 10)
prodotto = numero1 * numero2
if prodotto > 20:
    risultato = numero1 - numero2
else:
    risultato = numero1 + numero2  
print("I numeri generati sono:", numero1, numero2)
print("Il risultato è:", risultato)