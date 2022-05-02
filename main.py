import requests
import uuid
from multiprocessing import Pool

def main(proxy):
    proxy = proxy.strip()

    email = str(uuid.uuid4()) + "@yandex.ru"
    password = str(uuid.uuid4())
    
    data = {"email": email, "password": password}
    proxies = {'https': f"http://{proxy}"}
    
    response = requests.post("https://account.my.games/signup_email/", data = data, proxies = proxies).json()
    
    if response["status"] == "ok":
        print(f"\nEmail: {email}\n"
            f"Password: {password}\n")
        with open("accounts.txt", "a+") as accounts:
            accounts.write(f"{email}:{password}\n")
            
    elif response["status"] == "fail":
        print(response["body"]["descr"])



if __name__ == '__main__':
    while True:
        with open("proxy.txt", "r") as file:
            all_proxy = file.readlines()
            with Pool(60) as p:
                p.map(main, all_proxy)
