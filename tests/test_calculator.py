from calculator import add, div, mul, sub, expo, perc, rem
from decimal import Decimal

def test_add():
    assert add(1,1) == 2

def test_sub():
    assert sub(1,1) == 0

def test_mul():
    assert mul(1,1) == 1

def test_div():
    assert div(2,1) == 2

def test_div0():   
    try:
        div(1,0) 
    except ZeroDivisionError as e:
        print ("Zero Division Error")
        
def test_expo(): 
    assert expo(2,10) == 1024
    assert expo(3,10) == 59049

def test_perc(): 
    assert perc(2, 5) == 40
    assert perc(1, 3) == 33.33
    
def test_rem():
    assert rem(5, 3) == 2
   