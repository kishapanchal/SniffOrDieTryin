import ntpath
import requests
import re
import urllib.parse

target_url = "http://testphp.vulnweb.com/"

def extract_links_from(url):
    response = requests.get(url)
    response_text = response.content.decode('utf-8')
    return re.findall('(?:href=")(.*?)"', response_text)

href_links = extract_links_from(target_url)
for link in href_links:
    u = urllib.parse.urlparse(target_url)
    new_path = ntpath.join(u.path, link)
    s = urllib.parse.urlunparse((u.scheme, u.netloc, new_path, '', '', ''))
    print(s)
    print("------------------")
    if s.startswith(target_url):
        print(s)