from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    TIMEOUT = 10

    def __init__(self, driver, base_url="http://localhost:8000"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def ouvir_url(self, url):
        self.driver.get(f"{self.base_url}/{url.lstrip('/')}")

    def saisir_texte(self, locator: tuple, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def lire_texte(self, locator: tuple) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def cliquer(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def check_exist(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_element(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))