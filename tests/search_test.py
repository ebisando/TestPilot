from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from core.utils import load_config
import os


def run(driver):

    config = load_config()
    keyword = config["test"]["search_keyword"]

    print("\n========== Search Test ==========")

    homepage = HomePage(driver)

    homepage.search(keyword)

    results_page = SearchResultsPage(driver)

    results = results_page.get_results()

    print(f"Found {len(results)} books.")

    assert len(results) > 0, "No books found!"

    assert any(
        keyword in result.text
        for result in results
    ), f"{keyword} not found!"

    print(results[0].text)

    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot(
        "screenshots/search_harry_potter.png"
    )

    print("✅ Search Test Passed")