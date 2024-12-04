
chaine = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
n = 1
while index + n <= len(chaine):
    print(chaine[index:index+n])
    n += 2
