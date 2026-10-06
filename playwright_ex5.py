from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=300)
context = browser.new_context()
page = context.new_page()
page.goto("https://login.salesforce.com/")

page.locator("#username").fill("123@gmail.com")
page.locator("#Login").click()
page.locator("#password").fill("1234")
checkbox = page.locator("#rememberUn")
checkbox.click()
print(checkbox.is_checked())
if page.locator("#rememberUn").is_checked():
    page.locator("#Login").click()
print(page.locator("#error").inner_text())







input("end")