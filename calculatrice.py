def conversion(chaine):
    somme = 0
    for i in range (1,len(chaine)-1) :
        if chaine[i - 1] > chaine[i]:
            if chaine[i - 1] == 'M':
                somme += 1000
            elif chaine[i - 1] == 'D':
                somme += 500
            elif chaine[i - 1] == 'C':
                somme += 100
            elif chaine[i - 1] == 'L':
                somme += 50
            elif chaine[i - 1] == 'X':
                somme += 10
            elif chaine[i - 1] == 'V':
                somme += 5
            elif chaine[i - 1] == 'I':
                somme += 1
        else :
            pass
    return somme