
# Demanarem els primer numero:
numero1=float(input("Posa el primer numero: "))

# Demanarem l'operacio que vol fer:
operador=input("Posa l'operacio que vols fer (+, -, *, /, %): ")

#Demanem el segón numero:
numero2=float(input("Posa el segon numero: "))

# Decidim la operació a fer:

while operador != "+" and operador != "-" and operador != "*" and operador != "/" and operador != "%":
    print("\n[!] ERROR! Operador incorrecte!") #ERROR en el operador, tornem a demanarlo.
    print("[·] Torna a indicar el operador: ")
    operador=input("\nPosa l'operacio que vols fer (+, -, *, /, %): ")

#Triem y fem el calcul corresponent:
    if operador == "+":     #SUMA
        operacio=numero1+numero2
    elif operador == "-":   #RESTA
        operacio=numero1-numero2
    elif operador == "*":   #MULTIPLICACIÓ
        operacio=numero1*numero2
    elif operador == "/":   #DIVISIÓ
        operacio=numero1/numero2
    elif operador == "%":   #MÒDUL
        operacio=numero1%numero2

# RESULTAT FINAL:
print(f"El numero final es: {operacio}")

