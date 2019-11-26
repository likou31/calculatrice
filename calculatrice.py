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
        for indice in range (0,len(chaine) - 1):
            if conversion(chaine[indice]) < conversion(chaine[indice + 1]):
                somme -= conversion(chaine[indice])
            else:
                somme += conversion(chaine[indice])
        somme += conversion(chaine[-1])
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

def soustraction_element(element, element_precedent):
    return element - element_precedent

def addition_nombre_romain(nombre1, nombre2):
    return conversion(nombre1) + conversion(nombre2)

def soustraction_nombre_romain(nombre1, nombre2):
    return conversion(nombre1) - conversion(nombre2)

def multiplication_nombre_romain(nombre1, nombre2):
    return conversion(nombre1) * conversion(nombre2)

def division_nombre_romain(nombre1, nombre2):
    return conversion(nombre1) / conversion(nombre2)

def calculatrice(signe, nombre1, nombre2):
    if signe == '+':
        return addition_nombre_romain(nombre1, nombre2)