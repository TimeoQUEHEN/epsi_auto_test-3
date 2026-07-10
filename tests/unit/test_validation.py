import pytest
from app.validation import email_valide

@pytest.mark.unit
def test_email_valide_valide():
    assert email_valide("test@gmail.com")

@pytest.mark.unit
def test_email_valide_faux():
    assert not email_valide("a@a")

@pytest.mark.unit
def test_email_valide_sans_arobase():
    assert not email_valide("a")

@pytest.mark.unit
def test_email_valide_mauvais_type():
    with pytest.raises(TypeError):
        email_valide(3)