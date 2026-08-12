import time

from core.logger import logger


def run(driver):

    # logger.info("========== Performance Test ==========")
    navigation = driver.execute_script("""
        return performance.getEntriesByType('navigation')[0];
        """)
    # print(navigation)

    logger.info(
        f"Total Load Time : {navigation['duration']/1000:.2f} sec"
    )

    logger.info(
            f"DOM Ready : {navigation['domContentLoadedEventEnd']/1000:.2f} sec"
        )

    logger.info(
            f"Response End : {navigation['responseEnd']/1000:.2f} sec"
        )

    logger.info(
            f"HTTP Status : {navigation['responseStatus']}"
        )
    assert navigation["responseStatus"] == 200


    duration = navigation["duration"]

    if duration < 1000:
        logger.info("Performance Grade : A")

    elif duration < 2000:
        logger.info("Performance Grade : B")

    elif duration < 3000:
        logger.info("Performance Grade : C")

    else:
        logger.warning(
            f"Page load is slow: {navigation['duration']:.0f} ms"
        )

    logger.info("✅ Performance Test Passed")