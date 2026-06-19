from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    print(page.title())
    print("Google successfully launched!")
    page.wait_for_timeout(3000)
    browser.close()