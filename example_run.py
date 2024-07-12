from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://naver.com")  # 캡처하고자 하는 URL 입력

    # Action
    page.screenshot(path="screenshot.png")
    page.locator("#test > input").click()
    page.get_by_text("test").click()

    browser.close()

with sync_playwright() as playwright:
    run(playwright)