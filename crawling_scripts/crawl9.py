#/usr/bin/env python
# Extracts Links: It fetches a webpage and extracts all the URLs (links) found in the href attributes of anchor (<a>) tags.
#
# Content-Type Check: Before processing, it checks if the page is HTML (text/html). If it’s not HTML (e.g., images or other files), it skips the page.
#
# Decoding HTML: The content is decoded into text using UTF-8, with any decoding errors ignored.
#
# Recursive Crawling: It recursively follows the links found on each page, ensuring it only follows links within the target URL (e.g., http://192.168.100.133/mutillidae/).
# due to recursive call it is covering all the links which are there on main page and sub pages . it is like finding SITEMAP
#
# Avoiding Duplicates: It tracks the URLs already visited and avoids visiting them again.
import requests
import re
import urllib.parse

target_url = "http://testphp.vulnweb.com/"
target_links = []

def extract_links_from(url):
    try:
        response = requests.get(url)
        if 'text/html' in response.headers['Content-Type']:
            response_text = response.content.decode('utf-8', errors='ignore')
            return re.findall('(?:href=")(.*?)"', response_text)
        else:
            return []
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return []

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)