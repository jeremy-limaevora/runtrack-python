height=int(input("indiquer la hauteur du rectangle : "))
width=int(input("indiquer la largeur du rectangle : "))
for i in range(height):
    if i==0 or i==height-1:
        print('|'+ '-' *(width-2) + '|')

    else:
        print('|'+ '-' *(width-2) + '|')