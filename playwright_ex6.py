from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=300)
context = browser.new_context()
page = context.new_page()
page.goto("https://playwright.dev/python/")
title = page.locator(".hero__title").inner_text()
print(title)
if "playwright" in title:
    print("yes")
else:
    print("no")

page.goto("https://www.google.com")
title_google = page.title()
if "google" in title_google:
    print("yes")
else:
    print("no")
page.go_back()


input("end")