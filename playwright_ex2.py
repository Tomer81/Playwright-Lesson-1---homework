from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=300)
context = browser.new_context()
page = context.new_page()
page.goto("https://login.salesforce.com/")

page.locator("#forgot_password_link").click()
new_page_title = page.title()
print(new_page_title)
if "Reset Your Password" not in new_page_title:
    print("wrong title")

page.locator("#un").fill("Tomer")
page.locator("#continue").click()
error_msg = page.locator("#username-error").inner_text()
print(error_msg)





input("end")