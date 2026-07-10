import pytest
from app.validation import email_valide

@pytest.mark.unit
def test_email_valide_valide():
    assert email_valide("test@gmail.com") == True

@pytest.mark.unit
def test_email_valide_faux():
    assert email_valide("a@a") == False

@pytest.mark.unit
def test_email_valide_sans_arobase():
    assert email_valide("a") == False

@pytest.mark.unit
def test_email_valide_mauvais_type():
    with pytest.raises(TypeError):
        email_valide(3)