# Linkedin Name Crawler
A small prototype that opens LinkedIn, goto company's "People" page and extracts all visible employee names into a CSV file. You can use the list of name to form different combination and identify the valid email address. (e.g. for OSINT, phishing, username list, etc)

It was an old project, but now updating it with some VIBE coding!

**Latest tested:** 2026-02-16  ✅

Tested on Python 3.8 and Playwright 1.41.0.

> **FOR EDUCATIONAL PURPOSE ONLY** — use responsibly and respect LinkedIn's terms of service. 

---

## Quick overview
- Launches a Chromium browser (visible window), prompts for manual login, visits `https://www.linkedin.com/company/<company_name>/people/`, scrolls and clicks **Load more**, then saves visible names to `<company_name>_employee.csv`.
- Designed for simple, manual scraping and debugging — not production use.

## Requirements
- Python 3.13
- Playwright (see `requirement.txt`)
- A LinkedIn account with sufficient visibility to view employee names

## Installation (Windows example)
1. (optional) Create & activate a virtual environment:
2. Install Python deps:
   - `pip install -r requirement.txt`
3. Install Playwright browsers:
   - `playwright install chromium`

## Usage
1. Run the crawler with the company URL slug (the part after `/company/`):

   `python linkedin_crawler.py company_name`

   Example: `python linkedin_crawler.py google` → output file `google_employee.csv`.

2. The script opens a visible Chromium window and waits (~15s) for you to log in manually. After login it will navigate to the company "People" page and begin scrolling. I tried auto login, but it will very likely trigger CAPTCHA, so I decided to give some window to login instead.

## Output format
- Output file: `<company_name>_employee.csv` (no header)
- Each scraped name is written as comma-separated tokens derived from splitting the displayed name on spaces.
  - Example lines: `John,Doe` or `Maria,Del,Rey` (multi-part names become extra columns)
- The script filters out entries like `LinkedIn Member`.

## Important notes & limitations 
- Manual login is required (the script waits so you can solve captchas).
- Name-splitting is naive (splits on spaces); post-process the CSV if you need structured First/Last fields.
- LinkedIn UI/HTML can change — selectors in `linkedin_crawler.py` may need updates (`LOAD_MORE_BUTTON_SELECTOR` and the name element selector).
- Use responsibly and only for permitted/ethical purposes.

## Troubleshooting
- Nothing is written to CSV: ensure you're logged in and can view the company "People" page in the opened browser.
- Captcha/2FA appears: complete it manually in the browser window, then re-run the script.
- To change wait timings, edit `time.sleep(...)` values in `linkedin_crawler.py`.
- To run headless (not recommended for this script), change `headless=False` to `headless=True` in the launch call.

## Where to change selectors
- `LOAD_MORE_BUTTON_SELECTOR` — button used to load more employees
- Name selector: `div.ember-view.lt-line-clamp.lt-line-clamp--single-line`

---
💡
