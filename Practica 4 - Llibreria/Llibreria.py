# Declarem variables
articles = []
preusArticles = []
article = None
preu = 1
comprobacio = True

### 

comprobacio2 = True
articleComprar = 1
articlesComprats = []
preuArticlesComprats = []


# Explicacio:
print("[+] Introdueix els artices que necesitis, per finalitzar introdueix $ com article o algun preu negatiu.")

# Bucle per afegir objectes:
while comprobacio == True:         
    article=input("Quin article vols afegir? ")     # Afegim articles a la llista.
    if article == "$":                              # Si es $ tanquem.
        comprobacio = False
        break
    preu=float(input("Quin preu vols afegir? "))    # Afegim el preu del article.
    if preu <= 0:                                   # Si el preu es 0 tanquem.
        comprobacio = False
        break
    articles.append(article)                        # Afegim articles al array
    preusArticles.append(preu)                      # Afegim preu al array 
    

# Mostrem la llista amb els seus preus:
print("\n\nLlista Completa:\n-----------------\n")

for i in range(len(articles)):
    print(f"[{i+1}] Article: {articles[i]} --> Preu: {preusArticles[i]}€")

# Comprar articles:
print("\n\nAra compra articles posant el seu numero, quan ja estiguis para de comparar posant un 0.\n") # Explicació
while comprobacio2 == True:      # Començem el bucle
    articleComprar=int(input("Quin article vols comprar? "))
    if articleComprar == 0:         # Si posem 0 sortim del bucle
        comprobacio2 = False
    
    if comprobacio2 == True:        # Mentres no sigui 0 afegim els articles a la llista de compra.
        articlesComprats.append(articles[articleComprar-1])
        preuArticlesComprats.append(preusArticles[articleComprar-1])
   

# Calculem el preu final i el mostrem:
preuFinal=sum(preuArticlesComprats)
print(f"\n\nEl preu total es: {preuFinal}€.")


