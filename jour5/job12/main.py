l=[3,17,2,1,100,1,5,9,25]

for i in range(len(l)):
    for j in range(len(l)-1):
     if l[j] > l[j+1]:
        x = l[j] 
        y = l[j+1]
        l[j]=y
        l[j+1]= x

print(l)    