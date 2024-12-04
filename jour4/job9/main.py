def moyenne (N1,N2,N3):
  return (N1+N2+N3)/3


N1 = float(input("Entrez la première note :") )
N2= float(input("Entrez le deuxieme note:"))
N3 = float(input("Entrez le troisiéme note:"))
moyenne_etudiant = moyenne(N1,N2,N3)

if 15<moyenne_etudiant<20:
  print("La moyenne de l'eleve est:", moyenne_etudiant,"Très bon élève") 
elif 11<moyenne_etudiant<14:
  print("La moyenne de l'eleve est:", moyenne_etudiant,"Bon élève")
elif 8<moyenne_etudiant<10:
  print("La moyenne de l'eleve est:", moyenne_etudiant,"Élève moyen")
elif 0<moyenne_etudiant<7:
  print("La moyenne de l'eleve est:", moyenne_etudiant,"Élève devant faire des efforts")
  




