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
    elif signe == '-':
        return soustraction_nombre_romain(nombre1, nombre2)
    elif signe == '*' :
        return multiplication_nombre_romain(nombre1, nombre2)
    elif signe == '/':
        return division_nombre_romain(nombre1, nombre2)

def conversion_un_element_francais_romain(nombre):
    if nombre == 1 :
        return 'I'
    if nombre == 5:
        return 'V'
    if nombre == 10 :
        return 'X'
    if nombre == 50 :
        return 'L'
    if nombre == 100 :
        return 'C'
    if nombre == 500 :
        return 'D'
    if nombre == 1000 :
        return 'M'

def conversion_chiffre_francais_romain(nombre):
    if nombre == 1 :
        return 'I'
    elif nombre == 2:
        return 'II'
    elif nombre == 3 :
        return 'III'
    elif nombre == 4:
        return 'IV'
    elif nombre == 5 :
        return 'V'
    elif nombre == 6:
        return 'VI'
    elif nombre == 7 :
        return 'VII'
    elif nombre == 8:
        return 'VIII'
    elif nombre == 9 :
        return 'IX'

def conversion_dizaine_francais_romain(nombre):
    if nombre == 10 :
        return 'X'
    elif nombre == 20 :
        return 'XX'
    elif nombre == 30 :
        return 'XXX'
    elif nombre == 40 :
        return 'XL'
    elif nombre == 50 :
        return 'L'
    elif nombre == 60 :
        return 'LX'
    elif nombre == 70 :
        return 'LXX'
    elif nombre == 80 :
        return 'LXXX'
    elif nombre == 90 :
        return 'XC'

def conversion_centaine_francais_romain(nombre):
    if nombre == 100 :
        return 'C'
    elif nombre == 200 :
        return 'CC'
    elif nombre == 300 :
        return 'CCC'
    elif nombre == 400 :
        return 'CD'
    elif nombre == 500 :
        return 'D'
    elif nombre == 600 :
        return 'DC'
    elif nombre == 700 :
        return 'DCC'
    elif nombre == 800 :
        return 'DCCC'
    elif nombre == 900 :
        return 'CM'

def conversion_francais_romain(nombre):
    resultat = ''
    nb = 0
    i = 1
    while nombre != 0 :
        nb = nombre % 10
        resultat = str(conversion_un_nombre(nb, i)) + resultat
        i *= 10
        nombre //= 10
    return resultat

def conversion_un_nombre(nombre, i):
    if nombre == 0 :
        return ''
    if nombre * i < 10 :
        return conversion_chiffre_francais_romain(nombre * i)
    elif nombre * i < 100 :
        return conversion_dizaine_francais_romain(nombre * i)
    elif nombre * i < 1000 :
        return conversion_centaine_francais_romain(nombre * i)
    else :
        return conversion_un_element_francais_romain(nombre * i)