
def funkcja_aplikacji(people):
    return [item['imie']+' '+item['nazwisko']+': '+item['tytul'] for item in people]


import pytest

@pytest.fixture
def sample_data():
    return [
        {
            'imie':'dupa',
            'nazwisko':'zbita',
            'tytul':'pierdziel' 
        },
        {
            'imie':'ola',
            'nazwisko':'zprzedszkola',
            'tytul':'szesciolatka'
        },
        ]

@pytest.mark.dupa1
def test_funkcja_aplikacji_1(sample_data):   
    assert funkcja_aplikacji(sample_data) == ["dupa zbita: pierdziel",
                                         "ola zprzedszkola: szesciolatka",], "test failed"
@pytest.mark.dupa2
def test_funkcja_aplikacji_2(sample_data):   
    assert funkcja_aplikacji(sample_data) == ["dupa zbita: pierdziel",
                                         "ola zprzedszkola: szesciolatka",], "test failed"
@pytest.mark.dupa1                      
def test_funkcja_a(sample_data):   
    assert funkcja_aplikacji(sample_data) == ["dupa zbita: pierdziel",
                                         "ola zprzedszkola: szesciolatka",], "test failed"

if __name__=='__main__':
    print('ok')