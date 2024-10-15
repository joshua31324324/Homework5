'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works'''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2,4) == 8

def test_division():
    '''Test that division function works'''                