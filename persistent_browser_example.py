from patchright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context("",headless=False)
        page = context.new_page()
        page.goto("https://example.com")
        print(page.title())
        context.close()

if __name__ == "__main__":
    main()
