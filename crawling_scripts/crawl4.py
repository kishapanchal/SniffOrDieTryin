import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "testphp.vulnweb.com"

response = request(target_url)
print(response.content)  # this will print HTML code directly