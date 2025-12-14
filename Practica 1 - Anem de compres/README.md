# Practica 1, Anem de compres!
---
## Enunciat de la practica:
Fes un parell de programes interactius en Python que demani:

    el DNI del client.
    el preu de l'article que ha comprat.
    el tant per cent de descompte.
    el tant per cent d'IVA.

Amb aquestes dades ha de calcular:

    el NIF (DNI).
    el preu total.

Per calcular el preu final cal seguir els següents passos:

    preu amb descompte: amb el preu inicial, calcular el descompte i restar-lo al preu inicial.
    preu final: amb el preu amb descompte, calcular l'IVA i sumar-lo al preu amb descompte.

#### Exemple:
Si s'introdueixen les següents dades...

    12345678
    1000
    10
    21
    
El resultat ha de ser:

    12345678
    1110.0

Si s'introdueixen les següents dades...

    56785678
    800
    36
    21

El resultat ha de ser:

    56785678
    680.0

---

Has de fer un programa que calculi de forma automatitzada el NIF de cada un dels DNI que se li donin a través de la consola.
Les dades que ha de demanar l'ordinador són:

    un número de DNI.
    Ha de  calcular i mostrar el NIF (DNI + lletra).

 
#### Exemple:

    Dona'm el DNI: 12345678
        El NIF és 12345678Z
    Dona'm el DNI: 87654321
        El NIF és 87654321X
    Dona'm el DNI: 44444444
        El NIF és 44444444A 

---
# Que pots veure en aquest apartat:
Trobarem els dos exercicis demanats;

* El primer es el compres.py, aquest podem veure que demana certes dades per finalment retornarte el preu final de la teva compra despres de pasar per un descompte i el IVA.

* En el segon, el NIF.py veurem que a mes del preu ens dira la lletra del nostre DNI a partir dels seus numeros introduits al principi.
---
# Com executar el codi:
1. Amb la ajuda del VSCode podem executar el codi amb la seva terminal.
2. Si tenim en la terminal el interpret de python instalat el podem executar amb "python nomDelScript.py".
