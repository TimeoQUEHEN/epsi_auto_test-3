import pytest
import responses

from app.inscription import inscrire_cours_payant

@pytest.mark.e2e
@responses.activate
def test_paiment_ok(base_url, payment_api, compte_connu):
    responses.add(
        responses.POST,
        payment_api,
        json={"ok": True, "message": "Inscription confirmee"},
        status=200
    )
    resultat = inscrire_cours_payant(base_url, payment_api, compte_connu, "python-avance")

    assert resultat["ok"]
    assert len(responses.calls) == 1

@pytest.mark.e2e
@responses.activate
def test_paiment_bad(base_url, payment_api, compte_utilisateur):
    responses.add(
        responses.POST,
        payment_api,
        json={"ok": False, "message": "Paiement refuse, verifiez votre carte"},
        status=402
    )
    resultat = inscrire_cours_payant(base_url, payment_api, compte_utilisateur, "python-avance")

    assert not resultat["ok"]
    assert resultat["message"] == "Paiement refuse, verifiez votre carte"
    assert len(responses.calls) == 1