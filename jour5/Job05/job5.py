alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alph(lettre):
    return alph.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in alph:
            indice = (position_alphabet(lettre) + decalage) % 26
            resultat += alph[indice]
        else:
            resultat += lettre
    return resultat

print(cesar('Bonjour tous le monde ', 2))
