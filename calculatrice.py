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
            return symboleM()
        elif chaine[0] == 'D':
            return symboleD()
        elif chaine[0] == 'C':
            return symboleC()
        elif chaine[0] == 'L':
            return symboleL()
        elif chaine[0] == 'X':
            return symboleX()
        elif chaine[0] == 'V':
            return symboleV()
        elif chaine[0] == 'I':
            return symboleI()
    else:
        if len(chaine) == 2 and chaine[0] < chaine[1]:
            return conversion(chaine[1]) - conversion(chaine[0])
        for i in range(0, len(chaine)):
            if chaine[i] == 'M':
                somme += symboleM()
            elif chaine[i] == 'D':
                somme += symboleD()
            elif chaine[i] == 'C':
                somme += symboleC()
            elif chaine[i] == 'L':
                somme += 50
            elif chaine[i] == 'X':
                somme += 10
            elif chaine[i] == 'V':
                somme += 5
            elif chaine[i] == 'I':
                somme += 1
    return somme