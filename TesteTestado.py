

from playwright.sync_api import sync_playwright

import time




with sync_playwright() as playwright:

    # Inicializar o navegador

    browser = playwright.chromium.launch(headless=False)




    # Criar um contexto

    context = browser.new_context()




    # Criar uma nova página

    page = context.new_page()


    # Abrir o Google




    for i in range(100000000):

        # Abrir o Google

        page.goto('https://www.google.com')

       

        # Criar uma nova página para a próxima iteração

        page = context.new_page()




    time.sleep(10)


