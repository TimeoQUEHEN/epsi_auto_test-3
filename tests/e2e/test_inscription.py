import pytest

@pytest.mark.e2e
def test_inscription_via_formulaire_affiche_confirmation(session_connectee):
    # Arrange
    dashboard = session_connectee
    catalogue = dashboard.ouvrir_catalogue()

    # Act
    inscription = catalogue.s_inscrire("python-avance")
    inscription.s_inscrire_au_cours("Jean Dupont", "Envie de progresser en Python")

    # Assert
    message = inscription.message_confirmation()
    assert "confirm" in message.lower() or "enregistr" in message.lower(), (
        f"Message de confirmation inattendu apres inscription : '{message}'"
    )

@pytest.mark.e2e
@pytest.mark.parametrize(
    "cours_id, titre",
    [
        ("python-avance", "Python avance"),
        ("selenium-nuls", "Selenium pour les nuls"),
    ],
)
def test_inscription_via_formulaire_affiche_confirmation_loop(session_connectee, cours_id, titre):
    dashboard = session_connectee
    catalogue = dashboard.ouvrir_catalogue()

    inscription = catalogue.s_inscrire(cours_id)
    inscription.s_inscrire_au_cours("Jean Dupont", "Envie de progresser")

    message = inscription.message_confirmation()
    assert "confirm" in message.lower() or "enregistr" in message.lower(), (
        f"Message de confirmation inattendu pour '{titre}' : '{message}'"
    )