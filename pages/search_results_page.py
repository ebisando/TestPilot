from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:

    BOOK_TITLES = (By.CSS_SELECTOR, 'a[data-key="bib-title"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_results(self):

        return self.wait.until(
            EC.presence_of_all_elements_located(
                self.BOOK_TITLES
            )
        )