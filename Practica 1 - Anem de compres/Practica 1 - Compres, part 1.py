#VARIABLES

DNI=int(input("Introdueix el teu DNI: "))
Preu=float(input("Introdueix el preu del article comprat: "))
Descompte=float(input("Introdueix el descompte en percentatge: "))
IVA=float(input("Introdueix l'IVA en percentatge: "))

# Càlculem el preu

Preu_final=(Preu+(Preu*(IVA/100)))-(Preu*(Descompte/100))

# Mostrem per pantalla
print(f"El preu final serà: {Preu_final}")