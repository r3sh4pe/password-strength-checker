from getpass import getpass
import hashlib
import requests

def get_password() -> str:
    return getpass()

def check_have_i_been_pwned(password: str) -> (bool, int):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    r = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes = [line.split(":") for line in r.text.splitlines()]
    for h, count in hashes:
        if h == suffix:
            return (True, int(count))
    return (False, 0)
