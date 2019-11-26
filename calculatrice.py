def symboleI():
    return 1

def symboleV():
    return 5

def symboleX():
    return 10

def symboleL():
    return 50

def symboleC():
    return 100

def symboleD():
    return 500

def symboleM():
    return 1000

def conversion(chaine):
    somme = 0
    if len(chaine) == 1 :
        if chaine[0] == 'M':
            somme += symboleM()
        elif chaine[0] == 'D':
            somme += 500
        elif chaine[0] == 'C':
            somme += 100
        elif chaine[0] == 'L':
            somme += 50
        elif chaine[0] == 'X':
            somme += 10
        elif chaine[0] == 'V':
            somme += 5
        elif chaine[0] == 'I':
            somme += 1
    else:
        for i in range(0, len(chaine)):
            if chaine[i] == 'M':
                somme += symboleM()
            elif chaine[i] == 'D':
                somme += symboleD()
            elif chaine[i] == 'C':
                somme += symboleC()
    return somme