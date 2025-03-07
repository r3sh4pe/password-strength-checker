from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from password_util import check_have_i_been_pwned, check_password_local, check_against_wordlists, check_sha_wordlist

app = FastAPI(
    title="Password Strength Checker",
    description="Check the strength of your password",
    version="0.1"
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/unsecure/password/check/{password}")
async def check_password(password: str):
    local_result: dict[str, bool] = check_password_local(password)
    return local_result

@app.get("/unsecure/pwned/check/{password}")
async def check_pwned(password: str):
    pwned_result: tuple[bool, int] = check_have_i_been_pwned(password)
    result: dict[str, bool | int] = { "pwned": pwned_result[0], "count": pwned_result[1] }
    return result

@app.get("/unsecure/wordlist/check/{password}")
async def check_wordlist(password: str):
    wordlist_result: bool = check_against_wordlists(password)
    return { "pwned": wordlist_result }

@app.get("/secure/wordlist/check/{hash_start}")
async def check_hash(hash_start: str):
    hashes: list[str] = check_sha_wordlist(hash_start)
    return hashes