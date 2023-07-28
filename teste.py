from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000)
    page.fill('//*[@id="APjFqb"]','preço passagem Passaro Marrom')
    page.click("input[name='btnK']")
    page.wait_for_timeout(5000)
    print(page.title())
    browser.close()