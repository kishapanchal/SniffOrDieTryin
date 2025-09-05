import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "testphp.vulnweb.com"
# NOTE: Make sure 'wordlist.txt' is in the same folder as this script
with open("wordlist.txt", "r") as wordlist_file:  
                                                  
    for line in wordlist_file:
        test_url = line + target_url
        print(test_url)