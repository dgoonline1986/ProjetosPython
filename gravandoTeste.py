from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Pesquisa Google").click()
    page.get_by_role("link", name="SPTrans sptrans.com.br https://www.sptrans.com.br").click()
    page.get_by_role("textbox", name="Busca").click()
    page.get_by_role("textbox", name="Busca").fill("vale transporte")
    page.get_by_role("button", name="Buscar no site").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
