a = int(input("écrire un nombre entier supérieur à 0 :"))
for i in range (1, a+1):
    print(f"Table de multplication de {i}:")
    for b in range(1, 11):
        print(f"{i}x{b} = {i*b}")
        print() 
