# Librerias:
import random

# Variables inicials        :
numeroAleatori = int(random.randrange(1, 10))
numeroUsuari = 0    
contador = 0        # Establim el contador

#Bucle:
while numeroUsuari != numeroAleatori:
    contador += 1       #Sumem un al contador per cada volta.
    numeroUsuari =int(input("Introdueix el numero: "))      #Demanem el numero al usuari

    if numeroUsuari > numeroAleatori:   #El numero es mes gran.
        print("[·] Nop, el numero que has posat no es el correcte, el numero que busques es mes petit. ")
    elif numeroUsuari < numeroAleatori: #El numero es mes petit.
        print("[·] Nop, el numero que has posat no es el correcte, el numero que busques es mes gran. ")
    
    if contador == 3:   #Si fem 3 intents perdem.
        print(f"\n\n[!] T'has quedat sense intents... El numero era el: {numeroAleatori}")
        exit()

#Encertem el numero:
print(f"\n[+]Enorabona! Has acertat el numero en {contador} intents!")
