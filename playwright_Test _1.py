import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click()
    page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("qwertyui")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
    print("Test completed successfully")
