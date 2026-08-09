from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:

    BOOK_TITLES = (By.CSS_SELECTOR, 'a[data-key="bib-title"]')
    NO_RESULTS_MESSAGE = (
        By.TAG_NAME,
        "h4"
    )
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_results(self):
        return self.driver.find_elements(*self.BOOK_TITLES)

    def get_no_results_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.NO_RESULTS_MESSAGE)
    ).text