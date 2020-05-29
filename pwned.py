import requests
import hashlib
import re


def pwned(password):
    hashpass = hashlib.sha1(password).hexdigest()
    hash_prefix = hashpass[:5].upper()
    hash_suffix = hashpass[5:].upper()

    response = requests.get("https://api.pwnedpasswords.com/range/"+hash_prefix)

    string = response.content.decode("UTF-8")

    out = re.search(hash_suffix+r":[0-9]+", string)
    if(out):
        out = out.group()
        b = re.search("[0-9]+", out)
        a, b = out.split(":")
        return "your password has been pwned "+b+" times"
    else:
        return "Congratulations your password has not pwned"


if __name__ == "__main__":
    password = str.encode(input("Enter Your password: "))

    print(pwned(password))
