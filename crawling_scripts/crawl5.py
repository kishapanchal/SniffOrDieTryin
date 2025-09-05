import requests
import re

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "testphp.vulnweb.com"

response = request(target_url)
response_text = response.content.decode('utf-8')
href_links = re.findall('(?:href=")(.*?)"', response_text)
print(href_links)