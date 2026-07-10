from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class InscriptionPage(BasePage):

    def __init__(self, driver, base_url="http://localhost:8000"):
        super().__init__(driver, base_url)
        self.NOM_INPUT = (By.ID, "nom")
        self.MOTIVATION_INPUT = (By.ID, "motivation")
        self.SUBMIT_BTN = (By.ID, "submit")
        self.SUCCESS_MSG = (By.ID, "flash")

    def ouvrir(self, cours_id: str):
        self.ouvir_url(f"/cours/{cours_id}/inscription")
        return self

    def s_inscrire_au_cours(self, nom: str, motivation: str = ""):
        self.saisir_texte(self.NOM_INPUT, nom)
        self.saisir_texte(self.MOTIVATION_INPUT, motivation)
        self.cliquer(self.SUBMIT_BTN)
        return self

    def message_confirmation(self) -> str:
        return self.lire_texte(self.SUCCESS_MSG)