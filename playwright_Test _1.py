import re
from playwright.sync_api import Playwright, sync_playwright, expect


def log_in(page) -> None:
    page.wait_for_load_state("networkidle")
    expect(page.get_by_test_id("handle-button").locator("span")).to_contain_text("Log In")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("itsamemario@mairo.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("qwertyui")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    
    # Assertion 1
    page.wait_for_load_state("networkidle")
    expect(page.get_by_test_id("handle-button").locator("span")).not_to_contain_text("Log In")
    print("Test case 1.1 passed!")
    
    # Assertion 2
    page.get_by_test_id("handle-button").click()
    expect(page.get_by_test_id("custom-menu").get_by_role("list")).to_contain_text("My Orders")
    print("Test case 1.2 passed!")

    print("Test scenario 1: User login completed successfully")
    page.screenshot(path="playwrightTutorial/log_in.png")

def change_name(page) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click()
    page.get_by_role("menuitem", name="My Account").click()
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").fill("Mario")
    page.get_by_role("textbox", name="Last name").click()
    page.get_by_role("textbox", name="Last name").fill("Luigi")
    page.get_by_role("button", name="Update Info").click()

    # Assertion 1
    expect(page.get_by_role("alert")).to_contain_text("Info updated.")
    print("Test case 2.1 passed!")
    page.screenshot(path="playwrightTutorial/change_name.png")
    print("Test scenario 2: User name change completed successfully")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    try:
        log_in(page)
    except Exception as e:
        print(f"Test case 1.0 failed: {e}")
    try:
        change_name(page)
    except Exception as e:
        print(f"Test case 2.0 failed: {e}")
    finally:
        context.close()
        browser.close()
