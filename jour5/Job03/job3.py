hauteur = int(input("Rentrer la hauteur du triangle : "))
for i in range(hauteur):
    espaces = hauteur - i - 1
    underscores = 2 * i + 1
    print(" " * espaces + "/" + "_" * underscores + "\\")

