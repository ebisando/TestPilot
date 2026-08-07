from core.browser import create_driver
from core.utils import load_config
from tests.homepage_test import run as homepage_test
from tests.search_test import run as search_test

config = load_config()

url = config["website"]["url"]
headless = config["browser"]["headless"]

driver = create_driver(headless)

print("Opening:", url)

driver.get(url)

homepage_test(driver)
search_test(driver)

input("Press Enter to close browser...")

driver.quit()