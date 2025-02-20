limite_velocita = float(input("Inserisci il limite di velocità: "))
velocita_tua = float(input("Inserisci la velocità a cui stavi andando: "))
superamento = velocita_tua - limite_velocita
if superamento <= 10:
    multa = 36
elif 10 < superamento <= 40:
    multa = 148
elif 40 < superamento <= 60:
    multa = 370
else:
    multa = 500
print("La multa da pagare è di", multa)