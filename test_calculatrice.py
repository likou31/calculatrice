from calculatrice import *

def test_symboleI():
    assert symboleI() == 1

def test_symboleV() :
    assert symboleV() == 5

def test_symboleX() :
    assert symboleX() == 10

def test_symboleL() :
    assert symboleL() == 50

def test_symboleC() :
    assert symboleC() == 100

def test_symboleD() :
    assert symboleD() == 500

def test_symboleM():
    assert symboleM() == 1000

def test_conversion():
    assert conversion("M") == 1000
    assert conversion("MM") == 2000
    assert conversion("MD") == 1500
    assert conversion("MDCC") == 1700
    assert conversion("IV") == 4
    assert conversion("MIV") == 1004
    assert conversion("MCMXLIV") == 1944

def test_conversion_un_element():
    assert conversion_un_element("M") == 1000

def test_addition_nombre_romain():
    assert addition_nombre_romain("III", "MCMXLIV") == 1947

def test_soustraction_nombre_romain():
    assert soustraction_nombre_romain("MCMXLIV", "III") == 1941

def test_multiplication_nombre_romain():
    assert multiplication_nombre_romain("III", "V") == 15

def test_division_nombre_romain():
    assert division_nombre_romain("II", "II") == 1
    assert division_nombre_romain("XV", "III") == 5

def test_calculatrice():
    assert calculatrice('+', "III", "IV") == 7
    assert calculatrice('-', "L", "X") == 40
    assert calculatrice('*', "V", "IV") == 20
    assert calculatrice('/', "XV", "V") == 3