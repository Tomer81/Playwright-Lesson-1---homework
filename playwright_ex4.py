from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=300)
context = browser.new_context()
page = context.new_page()
page.goto("https://www.wikipedia.org/")

#inner text
subtitle_page = page.locator(".jsl10n.localized-slogan").inner_text()
print(subtitle_page)

#get attribute
dropdown_language = page.locator("#searchLanguage")
dropdown_language.select_option("en")
print(dropdown_language.get_attribute("id"))

#is visible
page.locator("#searchInput").fill("corvette car")
print(page.locator("#searchInput").is_visible())

#is checked
page.locator("#js-link-box-en").click()
print(page.locator("#skin-client-pref-vector-feature-custom-font-size-value-1").is_checked())







input("end")