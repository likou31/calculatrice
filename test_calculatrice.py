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