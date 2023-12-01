alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alph(lettre):
    return alph.find(lettre)

def jc(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in alph:
            indice = (position_alph(lettre) + decalage) % 26
            resultat += alph[indice]
        else:
            resultat += lettre
    return resultat

print(jc('Bonjour tous le monde ', 2))
