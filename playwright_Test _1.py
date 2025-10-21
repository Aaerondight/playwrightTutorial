import re
from playwright.sync_api import Playwright, sync_playwright, expect


def log_in(page) -> None:
    #Set timeout to 5 seconds
    #page.set_default_timeout(5000)

    expect(page.get_by_test_id("handle-button").locator("span")).to_contain_text("Log In")
    expect(page.locator('xpath=//span[contains(@class, "LcZX5c")]')).to_be_visible()
    print(expect(page.get_by_text("123-456-7890", exact=True)).to_be_visible())
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
    expect(page.get_by_role("text", name="About playwright-practice")).to_be_visible()
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

def get_all_links(page, context) -> None:
    all_links = page.get_by_role("link").all()

    for link in all_links:
        href = link.get_attribute("href")
        if "mailto:" not in href and "tel:" not in href:

            with context.expect_page() as new_page:
                link.click(button="middle")
            new_tab = new_page.value
            new_tab.wait_for_load_state("load")

            new_tab.wait_for_load_state("load")
            response = new_tab.request.get(new_tab.url)

            print(f"{new_tab.url}: Status {response.status}")
            new_tab.close()


def log_in2(page) -> None:
    #Set timeout to 5 seconds
    #page.set_default_timeout(5000)

    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("itsamemario@mairo.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("qwertyui")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    #page.wait_for_selector(".dVkVf7")
    page.wait_for_selector("[aria-label='itsamemario account']")
    #page.wait_for_load_state("networkidle")
    expect(page.get_by_text("Log In", exact=True)).not_to_be_visible()
    print("Test case 1.1 passed!")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    #get_all_links(page, context)
    log_in2(page)

    context.close()
    browser.close()
