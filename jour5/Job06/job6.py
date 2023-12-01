def phare(nb_marche, cm):
    resultat = 0
    m = cm / 100

    for i in range(nb_marche):
        resultat += m * 2 * 5 * 7

    print("Pour", nb_marche, "marches de", cm, "cm, le gardien parcourt", resultat, "m par semaine.")

phare(5, 10)
