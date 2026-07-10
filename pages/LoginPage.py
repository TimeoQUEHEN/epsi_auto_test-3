from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver, base_url="http://localhost:8000"):
        super().__init__(driver, base_url)
        self.EMAIL_INPUT = (By.ID, "email")
        self.PASSWD_INPUT = (By.ID, "password")
        self.SUBMIT_BTN = (By.ID, "submit")
        self.ERROR_MSG = (By.ID, "erreur")

    def open(self):
        self.ouvir_url("/login")
        return self

    def login(self, user, passwd):
        self.ouvir_url("/login")
        self.saisir_texte(self.EMAIL_INPUT, user)
        self.saisir_texte(self.PASSWD_INPUT, passwd)
        self.cliquer(self.SUBMIT_BTN)
        return DashboardPage(self.driver, self.base_url)

    def message_erreur(self) -> str:
        return self.lire_texte(self.ERROR_MSG)