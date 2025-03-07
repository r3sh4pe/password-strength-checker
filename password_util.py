from getpass import getpass
import hashlib
import requests

def get_password() -> str:
    return getpass()

def check_have_i_been_pwned(password: str) -> tuple[bool, int]:
    sha1_password: str = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix: str = sha1_password[:5]
    suffix: str = sha1_password[5:]
    r: requests.Response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes: list[list[str]] = [line.split(":") for line in r.text.splitlines()]
    for h, count in hashes:
        if h == suffix:
            return (True, int(count))
    return (False, 0)

def check_password_local() -> str:
    return ""
