def quel_fruitsetlegumes (type,saison):
    if type == "fruits" and saison == "hivers":
     print("orange, mandarine et kiwi")
    elif type== "fruits" and saison== "été":
       print("Poire, fraise, cassis")
    elif type== "légumes" and saison== "hivers":
       print("carotte, topinambour, endive")
    elif type== "légumes" and saison== "été":
       print("artichaut, aubergine,navet")

quel_fruitsetlegumes("fruits","été") 
quel_fruitsetlegumes("légumes","hivers")