import requests  # library to request over http

url = "testphp.vulnweb.com"  # safe pentesting site

try:
    get_response = requests.get("http://" + url)  # get request
    print(get_response)  # print http response code to test
except requests.exceptions.ConnectionError:
    print("Connection failed")