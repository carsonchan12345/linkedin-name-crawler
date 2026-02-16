from playwright.sync_api import sync_playwright
import time
import csv
import sys

# CSS selector for the "Load more" button on LinkedIn
LOAD_MORE_BUTTON_SELECTOR = 'button.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--full.artdeco-button--secondary.ember-view.scaffold-finite-scroll__load-button'

# global playwright objects
page = None
browser = None
playwright = None

# a function to navigate to linkedin login page and wait for manual login
def login():
    page.goto("https://www.linkedin.com/uas/login")
    time.sleep(15)
    # Wait for feed to confirm login success
    try:
        page.wait_for_url("**/feed/**", timeout=10000)
    except:
        pass  # Already logged in or still on login page

# navigate to linkedin company page, /people/ is the url of linkedin company employee page, 
# scroll to bottom, find and click "Load more" button until no more people can be loaded

def scroll_down(company_name): # add a parameter to pass in the company name
    page.goto("https://www.linkedin.com/company/" + company_name + "/people/", wait_until="domcontentloaded")
    # Wait longer for LinkedIn to load and verify we're on the correct page
    time.sleep(10)
    
    # Check if we got redirected
    current_url = page.url
    if "/feed/" in current_url or "/people/" not in current_url:
        print(f"Warning: Redirected to {current_url}. Trying again...")
        time.sleep(5)
        page.goto("https://www.linkedin.com/company/" + company_name + "/people/", wait_until="networkidle")
        time.sleep(10)
    # Keep clicking "Load more" button until it's no longer available
    while True:
        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
        # Try to find the "Load more" button
        load_more_button = page.query_selector(LOAD_MORE_BUTTON_SELECTOR)
        
        if load_more_button:
            # Button found, click it
            try:
                load_more_button.click()
                time.sleep(2.5)  # Wait for content to load
            except Exception:
                # Button might not be clickable anymore
                break
        else:
            # No more "Load more" button, exit loop
            break
    
    # Target div class that contains "ember-view lt-line-clamp lt-line-clamp--single-line"
    # This will grab elements like "John Parker"
    elements = page.query_selector_all('div.ember-view.lt-line-clamp.lt-line-clamp--single-line')
    return elements

# end playwright browser
def end():
    browser.close()
    playwright.stop()

# main function
if __name__ == "__main__":
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    login()
    test=scroll_down(sys.argv[1])
    fileout=open(sys.argv[1]+"_employee.csv","w")
    for res in test:
        #check if textContent is not empty
        text_content = res.text_content()
        if text_content and text_content.strip() != "" and text_content.strip() != "LinkedIn Member":
            try:
            # strip string res of space and then split by space write all to employee.csv
                fileout.write(",".join(text_content.strip().split(" ")))
                fileout.write("\n")
            except:
                pass
    time.sleep(2)
    end()





