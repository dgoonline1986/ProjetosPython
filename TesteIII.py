
#request

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request=p.request.new_context()
    response=request.get("https://www.google.com")
    
    
    print(response.status)
    #print(response.status_test)

