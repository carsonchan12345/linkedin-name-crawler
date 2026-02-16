# Linkedin Name Crawler
A prototype script to crawl all employee name of a company and save to csv.

Tested on python 3.8 and playwright 1.41.0

# FOR EDUCATIONAL PURPOSE ONLY!!!

## Prerequisite
You need a linkedin account with a lot of connections. (識人好過識字)

## Installation
```
pip install -r requirement.txt
playwright install chromium
```

## Usage

You need to manually enter you linkedin credential as it may trigger captura if you automate the login progress. 

The company name is hxxps://www.linkedin.com/company/**company_name**/

```
python linkedin_crawler.py company_name
```
