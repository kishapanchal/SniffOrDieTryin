import requests
import re

target_url = "http://testphp.vulnweb.com/"

def extract_links_from(url):
    response = requests.get(url)
    response_text = response.content.decode('utf-8')
    return re.findall('(?:href=")(.*?)"', response_text)

href_links = extract_links_from(target_url)
for link in href_links:
    print(link)