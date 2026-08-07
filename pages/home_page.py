from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    SEARCH_BOX = (By.CSS_SELECTOR, 'input[testid="main_search_input"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search(self, keyword):

        search_box = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_BOX)
        )

        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)