import requests

from selenium.webdriver.common.by import By

from core.logger import logger


def run(driver):

    logger.info("========== Broken Link Test ==========")

    links = driver.find_elements(
        By.TAG_NAME,
        "a"
    )

    logger.info(f"Found {len(links)} links.")

    urls = []

    for link in links:

        url = link.get_attribute("href")

        if not url:
            continue

        if url.startswith("javascript:"):
            continue

        if url.startswith("mailto:"):
            continue

        if url.startswith("tel:"):
            continue

        urls.append(url)

    urls = list(dict.fromkeys(urls))

    logger.info(f"Checking {len(urls)} unique URLs...")

    broken_links = []

    for url in urls:

        try:
            if "tpl.ca" not in url:

                logger.info(
                    f"Skipping external URL: {url}"
                )

                continue
            response = requests.get(
                url,
                timeout=5
            )
            if response.status_code == 403:

                logger.info(
                    f"Access denied (403): {url}"
                )
            elif response.status_code == 404 or response.status_code >= 500:

                logger.warning(
                    f"Broken link: {url} ({response.status_code})"
                )

                broken_links.append(
                    (url, response.status_code)
                )

        except requests.RequestException as e:

            logger.error(
                f"Error checking {url}: {e}"
            )

            broken_links.append(
                (url, str(e))
            )
    logger.info(
        f"Broken links found: {len(broken_links)}"
    )

    assert len(broken_links) == 0, (
        f"{len(broken_links)} broken links found."
    )