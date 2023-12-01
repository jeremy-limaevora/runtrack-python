def arrondie(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            difference = note % 5
            if difference >= 3:
                note_arrondie = note + (5 - difference)
                notes_arrondies.append(note_arrondie)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

notes_eleve = [83, 72, 55, 38, 91]
notes1 = arrondie(notes_eleve)
print(notes1)
