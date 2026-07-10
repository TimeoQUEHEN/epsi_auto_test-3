import pytest

@pytest.mark.e2e
def test_deconnexion_retourne_a_lecran_login(session_connectee):
    # Arrange
    dashboard = session_connectee

    # Act
    login_page = dashboard.se_deconnecter()

    # Assert
    assert login_page.check_exist(login_page.SUBMIT_BTN), (
        "Le bouton de connexion n'est pas visible apres la deconnexion, "
        "retour a l'ecran de login incertain"
    )