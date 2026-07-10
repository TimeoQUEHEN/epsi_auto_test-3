import os
import uuid
import pytest
from faker import Faker
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

from app.inscription import supprimer_compte
from pages.LoginPage import LoginPage

load_dotenv()

@pytest.fixture(scope="session")
def payment_api():
    return os.getenv("PAYMENT_API_URL", "http://localhost:9000/pay")

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:8000").rstrip("/")


@pytest.fixture
def driver():
    headless = True #os.getenv("HEADLESS", "true").lower() != "false"
    options = Options()
    if headless:
        options.add_argument("--headless=new")

    navigateur = webdriver.Chrome(options=options)
    yield navigateur
    navigateur.quit()


@pytest.fixture
def session_connectee(driver, base_url, compte_connu):
    login_page = LoginPage(driver, base_url)
    return login_page.login(compte_connu["email"], compte_connu["password"])

@pytest.fixture
def compte_connu():
    """Reproduit exactement le compte genere au demarrage de l'app (meme seed, meme ordre d'appel)."""
    Faker.seed(0)
    f = Faker("fr_FR")

    compte = {
        "nom": f.name(),
        "email": f.email(),
        "password": f.password(),
    }

    yield compte

    supprimer_compte(compte["email"])

@pytest.fixture
def fake():
    Faker.seed(42)          # seed fixe -> runs reproductibles
    return Faker("fr_FR")   # locale française


@pytest.fixture(scope="function")
def compte_utilisateur(fake):
    """Genere un apprenant unique, et le supprime apres le test (teardown)."""
    unique_suffix = uuid.uuid4().hex[:8]
    email_local, domaine = fake.email().split("@")

    apprenant = {
        "nom": fake.name(),
        "email": f"{email_local}+{unique_suffix}@{domaine}",
        "password": fake.password(length=12),
    }

    yield apprenant

    supprimer_compte(apprenant["email"])
