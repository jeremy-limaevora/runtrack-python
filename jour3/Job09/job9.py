def classement_etudiant(n1, n2, n3):
    moyenne_etudiant = (n1 + n2 + n3) // 3
    
    if 15 <= moyenne_etudiant <= 20:
        return "Très bon élève"
    elif 11 <= moyenne_etudiant <= 14:
        return "Bon élève"
    elif 8 <= moyenne_etudiant <= 10:
        return "Élève moyen"
    else:
        return "Élève devant faire des efforts"


print(classement_etudiant( 16, 17, 18))
print(classement_etudiant(11, 13, 14))
print(classement_etudiant(8,9,10))
print(classement_etudiant(3,5,7))
