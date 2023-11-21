montant = int(input("montant de l'investissement : "))
taux = int(input("taux du rendement : "))
montant = montant + 5000
taux = taux + 2
print("nouveau gain : ",(montant//100)*taux, "€")
montant = montant + ((montant//100)*10)
taux = taux - 1
print("nouveau gain:",(montant//100)*taux,"€")