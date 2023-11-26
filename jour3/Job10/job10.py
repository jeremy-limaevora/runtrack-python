def pair_impair(nb):
    if isinstance(nb, int) and nb > 0:
        if nb % 2 == 0:
            print("pair")
        else:
            print("impair")
    else:
        print("aucun des deux")

pair_impair(2)
pair_impair(8)
pair_impair(3)
pair_impair(5)
pair_impair(-4)
