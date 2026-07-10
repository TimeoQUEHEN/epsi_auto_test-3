import pytest

from app.tarification import prix_inscription

@pytest.mark.unit
def test_prix_inscription_unitaire():
    assert prix_inscription(1) == 40

@pytest.mark.unit
def test_prix_inscription_double():
    assert prix_inscription(2) == 80

@pytest.mark.unit
def test_prix_inscription_remise():
    assert prix_inscription(3) == 102

@pytest.mark.unit
def test_prix_inscription_exception():
    with pytest.raises(TypeError):
        prix_inscription("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")