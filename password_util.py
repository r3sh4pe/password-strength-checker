from getpass import getpass
import hashlib

def get_password() -> str:
    return getpass()

def check_have_i_been_pwned(password: str) -> bool:
    password = "P@ssw0rd"
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return False
