import requests

def check_website(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return True
        else:
            return False
    except:
        return False

print(check_website('https://easysmarthub.ru'))
print(check_website('https://easysmarthub.ru/contact'))
print(check_website('https://easysmarthub.ru/1'))
print(check_website('https://easysmarthub.ru/mega'))
