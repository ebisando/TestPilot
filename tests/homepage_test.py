import os

def run(driver):

    print("\n========== Homepage Test ==========")

    print("Current URL:")
    print(driver.current_url)

    print("Page Title:")
    print(driver.title)

    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot("screenshots/homepage.png")

    print("✅ Homepage screenshot saved.")