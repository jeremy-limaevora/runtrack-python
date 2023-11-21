inventaire= {"nom":"carte", "prix":35, "nb":250}
print(f"{inventaire["nom"]}, {inventaire["prix"]}€, en stock : {inventaire["nb"]}")
choix=int(input("Vous en voulez combien ? : "))
inventaire["nb"] = inventaire["nb"] - choix
inventaire["prix"] = inventaire["prix"] + ((inventaire["prix"] // 250) * 35)
print(f"{inventaire["nom"]}, {inventaire["prix"]}€, en stock : {inventaire["nb"]}")
