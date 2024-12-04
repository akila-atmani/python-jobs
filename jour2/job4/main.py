N = int(input("Entrez un entier N de 1 à N : "))
for i in range(1,N+1,1):
    print(f"Table de multiplication de {i}:")

    for r in range(1, 11,1):
        print(f"{i} x {r} = {i * r}")