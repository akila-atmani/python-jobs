l = [1,2,3,4,5]
print(l)
#l[0],l[-1]=l[-1],l[0] solution plus rapide de google mais moin lisible 
int1 = l[0]
int2 = l[-1]
l[0] = int2
l[-1] = int1
print(l)