import time
import traceback
from core.browser import create_driver
from core.config import config

from tests.homepage_test import run as homepage_test
from tests.search_positive_test import run as search_test

from core.logger import logger


class TestRunner:

    def __init__(self):

        self.driver = None

        self.tests = [
            ("Homepage Test", homepage_test),
            ("Search Test", search_test)
        ]
        self.results = []

    def setup(self):

        self.driver = create_driver(
            config["browser"]["headless"]
        )

        self.driver.get(
            config["website"]["url"]
        )

    def execute(self):

        for test_name, test in self.tests:

            logger.info(f"===== {test_name} =====")

            try:

                test(self.driver)

                logger.info(f"✅ {test_name} PASSED")
                self.results.append({
                    "name": test_name,
                    "status": "PASSED",
                    "error": None
                })

            except Exception as e:

                logger.error(f"❌ {test_name} FAILED")
                traceback.print_exc()
                self.results.append({
                    "name": test_name,
                    "status": "FAILED",
                    "error": str(e)
                })

    def teardown(self):

        if self.driver:
            self.driver.quit()

    def run(self):

        logger.info("===== TestPilot Started =====")
        start = time.time()

        self.setup()

        try:

            self.execute()

        finally:

            self.teardown()
        

        end = time.time()

        logger.info("===== TestPilot Finished =====")
        logger.info(f"Execution Time : {end-start:.2f} sec")
        logger.info("========== Summary ==========")
        for result in self.results:

            if result["error"]:
                logger.info(
                    f"{result['name']:<25} {result['status']} ({result['error']})"
                )
            else:
                logger.info(
                    f"{result['name']:<25} {result['status']}"
                )