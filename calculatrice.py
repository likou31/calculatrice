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
        return conversion_un_element(chaine[0])
    else:
        if len(chaine) == 2 and chaine[0] < chaine[1]:
            return conversion(chaine[1]) - conversion(chaine[0])
        for i in chaine:
            somme += conversion(i)
    return somme

def conversion_un_element(element):
    if element == 'M':
        return symboleM()
    elif element == 'D':
        return symboleD()
    elif element == 'C':
        return symboleC()
    elif element == 'L':
        return symboleL()
    elif element == 'X':
        return symboleX()
    elif element == 'V':
        return symboleV()
    elif element == 'I':
        return symboleI()