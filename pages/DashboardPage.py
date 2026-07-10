from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

    def __init__(self, driver, base_url="http://localhost:8000"):
        super().__init__(driver, base_url)
        self.DECO_BTN = (By.ID, "logout")
        self.TITRE = (By.CLASS_NAME, "dashboard-title")
        self.CATALOGUE_LINK = (By.LINK_TEXT, "Catalogue")

    def est_affiche(self) -> bool:
        return self.check_exist(self.TITRE)

    def ouvrir_catalogue(self):
        from pages.CataloguePage import CataloguePage
        self.ouvir_url("/dashboard")
        self.cliquer(self.CATALOGUE_LINK)
        return CataloguePage(self.driver, self.base_url)

    def se_deconnecter(self):
        from pages.LoginPage import LoginPage
        self.ouvir_url("/dashboard")
        self.cliquer(self.DECO_BTN)
        return LoginPage(self.driver, self.base_url)