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
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->", test_url)