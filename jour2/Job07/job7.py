chaine = "abcdefghijklmnopqrstuvwxyz" * 10
nb_ligne = 10
indice = 0

for i in range(1, nb_ligne + 1):
    caractères = chaine[   indice: indice + i *2 - 1]
    print(caractères .center(nb_ligne * 2))
 
    indice += i * 2 -1