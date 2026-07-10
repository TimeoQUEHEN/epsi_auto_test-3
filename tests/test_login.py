import pytest
from pages.LoginPage import LoginPage

@pytest.mark.e2e
def test_login_valide_arrive_sur_dashboard(driver, base_url, compte_connu):
    """Test isole, sans fixture session_connectee (cf. note 'En pratique' de l'exercice) :
    si celui-ci echoue, on sait que le login lui-meme est casse."""
    login_page = LoginPage(driver, base_url)

    dashboard = login_page.login(compte_connu["email"], compte_connu["password"])

    assert dashboard.est_affiche(), (
        "Le titre du tableau de bord n'est pas visible apres un login valide"
    )

@pytest.mark.e2e
def test_login_refuse_mauvais_mot_de_passe(driver, base_url, compte_connu):
    login_page = LoginPage(driver, base_url)

    login_page.login(compte_connu["email"], "MauvaisMdp!")
    message = login_page.message_erreur()

    assert message, "Aucun message d'erreur affiche pour un mauvais mot de passe"

@pytest.mark.e2e
def test_login_refuse_utilisateur_inconnu(driver, base_url, compte_utilisateur):
    login_page = LoginPage(driver, base_url)

    login_page.login(compte_utilisateur["email"], compte_utilisateur["password"])
    message = login_page.message_erreur()

    assert message, "Aucun message d'erreur affiche pour un utilisateur inconnu"

@pytest.mark.e2e
def test_login_refuse_champs_vides(driver, base_url):
    login_page = LoginPage(driver, base_url)

    login_page.login("", "")
    message = login_page.message_erreur()

    assert message, "Aucun message d'erreur affiche pour des champs vides"