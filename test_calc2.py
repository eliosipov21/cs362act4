import pytest
import calc


#palindrome tests
def test_one():
    res = calc.isPalindrome("Cucumeber")
    assert res == False

def test_two():
    res = calc.isPalindrome("aua")
    assert res == True

def test_three():
    res = calc.isPalindrome("121")
    assert res == True


#numwords tests
def test_4():
    res = calc.numWords("")
    assert res == 0

def test_5():
    res = calc.numWords("Hello")
    assert res == 1 

def test_6():
    res = calc.numWords("Hello world")
    assert res == 2 

def test_7():
    res = calc.numWords("Hello world .")
    assert res == 3 
