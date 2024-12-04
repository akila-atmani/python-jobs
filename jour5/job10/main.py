L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
ma_liste = []  # Liste vide pour stocker les éléments valides

# Remplir ma_liste avec les éléments compris entre 25 et 90
for i in L:
    if 25 <= i <= 90:
        ma_liste.append(i)
print(ma_liste)        

produit = 1
for i in range(0,len(ma_liste),1):
    produit = produit * ma_liste[i]
print(produit)
    
    