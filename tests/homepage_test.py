import os
from core.logger import logger

def run(driver):

    logger.info("Current URL: " + driver.current_url)

    logger.info("Page Title: " + driver.title)

    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot("screenshots/homepage.png")

    logger.info("✅ Homepage screenshot saved.")