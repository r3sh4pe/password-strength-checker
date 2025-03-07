import hashlib
import os
from getpass import getpass

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


def check_password_local(password: str) -> dict[str, bool]:
    result: dict[str, bool] = {
        "length": False,
        "upper": False,
        "lower": False,
        "digit": False,
        "special": False
    }
    if len(password) >= 12:
        result["length"] = True
    for char in password:
        if char.isupper():
            result["upper"] = True
        if char.islower():
            result["lower"] = True
        if char.isdigit():
            result["digit"] = True
        if not char.isalnum():
            result["special"] = True
    return result


def check_against_wordlists(password: str) -> bool:
    wordlist_dir = './password_lists/'
    for wordlist_file in os.listdir(wordlist_dir):
        with open(os.path.join(wordlist_dir, wordlist_file), 'r') as file:
            if password in file.read().splitlines():
                return True
    return False


def calc_local_score(check_result: dict[str, bool]) -> tuple[int, int, int]:
    score: int = 0
    for value in check_result.values():
        if value:
            score += 1
    return score, len(check_result), int(score / len(check_result) * 100)

def check_sha_wordlist(hash_start: str) -> list[str]:
    result: list[str] = []
    hash_start_upper = hash_start.upper()
    wordlist_dir = './password_lists/'
    for wordlist_file in os.listdir(wordlist_dir):
        if not wordlist_file.endswith('.sha1'):
            continue
        with open(os.path.join(wordlist_dir, wordlist_file), 'r') as file:
            for line in file.read().splitlines():
                if line.startswith(hash_start_upper):
                    result.append(line[5:])
    return result