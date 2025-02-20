numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
if numero1 % numero2 == 0:
    print(numero1, "è multiplo di", numero2)
else:
    print(numero1, "non è multiplo di", numero2)