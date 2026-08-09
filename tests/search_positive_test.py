from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from core.config import config
from selenium.common.exceptions import TimeoutException
import os


def run(driver):

    keyword = config["test"]["search_keyword"]

    homepage = HomePage(driver)

    homepage.search(keyword)

    results_page = SearchResultsPage(driver)
    results = results_page.get_results()
    if results:
        print(f"Found {len(results)} books.")
    else:
        message = results_page.get_no_results_message()
        print(message)
        assert "Nothing found for" in message
        assert keyword in message
        print("✅ Proper error message displayed.")
        return

    results = results_page.get_results()

    print(f"Found {len(results)} books.")
    print("----------------")

    for result in results:

        print(result.text)

    print("----------------")
    assert len(results) > 0, "No books found!"

    assert any(
        keyword.lower() in result.text.lower()
        for result in results
    ), f"{keyword} not found!"

    print(results[0].text)

    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot(
        "screenshots/search_harry_potter.png"
    )

    print("✅ Search Test Passed")