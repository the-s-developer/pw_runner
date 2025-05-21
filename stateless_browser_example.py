from patchright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        browser.close()

if __name__ == "__main__":
    main()
