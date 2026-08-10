from axe_selenium_python import Axe

from core.logger import logger


def run(driver):

    logger.info("========== Accessibility Test ==========")

    axe = Axe(driver)

    axe.inject()

    results = axe.run()

    violations = results["violations"]

    logger.info(f"Accessibility Violations: {len(violations)}")

    for violation in violations:

        logger.warning(
            f"""
        Rule     : {violation['id']}
        Impact   : {violation['impact']}
        Help     : {violation['help']}
        Affected : {len(violation['nodes'])}
        """
            )

    logger.info("✅ Accessibility Test Finished")