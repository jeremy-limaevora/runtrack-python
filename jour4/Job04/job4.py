def modifier_liste():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    index = fruits.index("orange")
    fruits[index] = "Mangue"
    return fruits

print(modifier_liste())
