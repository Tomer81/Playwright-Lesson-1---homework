from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=300)
context = browser.new_context()
page = context.new_page()
page.goto("https://www.ebay.com/sch/ebayadvsearch")

page.locator("#_nkw").fill("tent")
page.locator("#_ex_kw").fill("black")

page.locator("[value='LH_BIN']").click()
page.locator(".adv-form__actions .btn--primary").click()
page.go_back()



input("end")
