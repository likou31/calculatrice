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