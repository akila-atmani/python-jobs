a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a + b > c and a+c>b and b+c>a:
    print("c'est un triangle")
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print("c'est un rectangle")
elif a == b == c:
    print("c'est un equilatérale")
elif a == b or a == c or b == c:
    print("c'est un isocéle")
    
else:
    print("c'est pas un triangle")
