import pytest

@pytest.fixture
def t_setup():
    print("zaczynamy")
    return [1,2,3,4]

@pytest.mark.dupa4
def test_funkcja_aplikacji_1(t_setup):   
    assert t_setup[0]==1

@pytest.mark.dupa3
@pytest.mark.parametrize("in1, in2, expected", [('ala','ola', 'alaola'),(' ',' ','  ')])
def test_funkcja_aplikacji_2(t_setup, in1, in2, expected):
    assert t_setup[1] == 2
    assert in1+in2 == expected

@pytest.mark.dupa1                      
def test_funkcja_a0():   
    assert 1==1

@pytest.mark.dupa2                      
def test_funkcja_a1():   
    assert 1==2