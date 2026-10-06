from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=300)
context = browser.new_context()
page = context.new_page()
page.goto("https://prd.canvusapps.com/signup")

page.locator("#user_name").fill("Tomer Darmon")
page.locator("#user_email").fill("123@gmail.com")
page.locator("#user_password").fill("1234")
page.locator("#user_password_confirmation").fill("1234")
page.locator("#company_name").fill("Arkia")
page.locator(".btn-primary").click()
error_msg = page.locator(".alert-block").inner_text()
print(error_msg)

input("end")