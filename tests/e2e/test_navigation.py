import pytest

@pytest.mark.e2e
def test_catalogue_contient_un_cours_attendu(session_connectee):
    # Arrange
    dashboard = session_connectee

    # Act
    catalogue = dashboard.ouvrir_catalogue()

    # Assert
    assert catalogue.cours_est_present("Python avance"), (
        "Le cours 'Python avance' est absent du catalogue"
    )