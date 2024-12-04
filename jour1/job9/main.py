Nom = "parfum"
Prix_unitaire = 30
Quantité_en_stock = 10
print("Produit: ", Nom)
print("Prix: ", Prix_unitaire, "euro")
print("stock: ", Quantité_en_stock)

#print("saisir la quantité de parfum que vous souhaitez:")
nombre_parfum = int(input("saisir la quantité de parfum que vous souhaitez: "))

nouvelle_quantité = Quantité_en_stock - nombre_parfum
print("Nouvelle quantité:", nouvelle_quantité)

nouveau_prix = Prix_unitaire + (Prix_unitaire *(10/100) )

print ("nouveau prix:", nouveau_prix, "euro")