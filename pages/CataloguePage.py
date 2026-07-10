from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class CataloguePage(BasePage):

    def __init__(self, driver, base_url="http://localhost:8000"):
        super().__init__(driver, base_url)
        self.COURS_TITRES = (By.CLASS_NAME, "cours-titre")

    def ouvrir(self):
        self.ouvir_url("/catalogue")
        return self

    def cours_est_present(self, titre: str) -> bool:
        self.wait.until(lambda d: len(d.find_elements(*self.COURS_TITRES)) > 0)
        titres = [el.text for el in self.driver.find_elements(*self.COURS_TITRES)]
        return titre in titres

    def s_inscrire(self, cours_id: str):
        from pages.InscriptionPage import InscriptionPage
        self.driver.find_element(
            By.CSS_SELECTOR, f"a[href*='/cours/{cours_id}/inscription']"
        ).click()
        return InscriptionPage(self.driver, self.base_url)