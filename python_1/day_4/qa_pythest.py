import pytest
from test_def import name_upper 


def test_test_def():
    assert name_upper('Evgeny') == 'EVGENY'


def calc(a,b):
    return a + b


def uppers(word):
    return word.upper()


def test_upper():
    assert uppers('word') == 'WORD'


def test_calc():
    assert calc(2, 2) == 4


def test_isupper():
    word = uppers('word')
    assert word.isupper()

    
def test_failed_upper():
    assert 'foo'.upper() == 'FOo'
