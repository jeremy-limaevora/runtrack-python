ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre) + decalage) % 26
            resultat += ALPHABET[indice]
        else:
            resultat += lettre
    return resultat

print(cesar('Bonjour tous le monde ', 2))
