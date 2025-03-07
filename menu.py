from rich import print
import os
from password_util import get_password, check_have_i_been_pwned, check_password_local, calc_local_score

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def print_menu() -> str:
    clear()
    print("[green]=========================================[green]")
    print("[green]        PASSWORD-STRENGTH CHECKER        [green]")
    print("[green]=========================================[green]")
    print("[green]       [1] Check password strength (local)       [green]")
    print("[green]       [2] Check password leak (online)           [green]")
    print("[green]       [3] Rule of Thumbs                [green]")
    print("[green]       [4] Exit                          [green]")
    print("[green]=========================================[green]")
    print("[green]       Enter your choice (1-4):          [green]")
    return input()

def handle_user_input(user_input: str):
    input_as_int: int | None = None
    try:
        input_as_int = int(user_input)
    except ValueError:
        raise ValueError("Invalid input. Input was not a number. Please enter a number between 1-4.")
        return
    if not input_as_int or input_as_int < 1 or input_as_int > 4:
        raise ValueError("Invalid input. Please enter a number between 1-4.")
        return

    match input_as_int:
        case 1:
            password: str = check_password_local_menu()
            if not password:
                return
            else:
                check_result_local: dict[str, bool] = check_password_local(password)
                print_local_result(check_result_local)
        case 2:
            password: str = have_i_been_pwned_menu()
            if not password:
                return
            else:
                check_result: tuple[bool, int] = check_have_i_been_pwned(password)
                if check_result[0]:
                    print_message(f"Your password has been leaked {check_result[1]} times", "ERROR", "red")
                    print_message("This does not mean that your user/password combination has been leaked. But the password will be in wordlists.\n\nYou can look at https://haveibeenpwned.com/ if your account has been leaked.", "INFORMATION", "yellow")
                else:
                    print_message("Your password has not been leaked", "SUCCESS", "green")
        case 3:
            print_rule_of_thumbs()
        case 4:
            print("[green]Exiting...[green]")
            exit(0)

def print_message(message: str, header, color)-> None:
    clear()
    print(f"[{color}]================={header}==================[{color}]\n")
    print(f"[{color}]{message}[{color}]\n")
    print("[green]Press return Key to continue...[green]")
    input()

def print_rule_of_thumbs():
    clear()
    print("[green]=========================================[green]")
    print("[green]        RULE OF THUMBS                  [green]")
    print("[green]=========================================[green]")
    print("[green]       [1] Use a unique password for every account[green]")
    print("[green]       [2] Enable Two-Factor Authentication (2FA)[green]")
    print("[green]       [3] Use a passphrase (e.g., three random words)[green]")
    print("[green]       [4] Use a password generator[green]")
    print("[green]       [5] Use a password manager[green]")
    print("[green]       [6] Consider passwordless logins (e.g., passkeys)[green]")
    print("[green]=========================================[green]")
    print("[green]       Press return key to go back          [green]")
    input()

def have_i_been_pwned_menu() -> str:
    clear()
    print("[green]=========================================[green]")
    print("[green]        Check for Password Leak          [green]")
    print("[green]=========================================[green]")
    print("[green]             Information:                [green]")
    print("[green] Your password will be hashed and the    [green]")
    print("[green] first 5 characters will be sent to      [green]")
    print("[green] the haveibeenpwned. So the clear        [green]")
    print("[green] password will never be sent.            [green]")
    print("[green]=========================================[green]")
    print("[green]       Enter your password:              [green]")
    print("[green]    (or return for previous menu)         [green]")
    password: str = get_password()
    if not password:
        return ""
    return password

def check_password_local_menu() -> str:
    clear()
    print("[green]=========================================[green]")
    print("[green]        Check Password Strength          [green]")
    print("[green]=========================================[green]")
    print("[green]             Information:                [green]")
    print("[green] Your password will be checked against  [green]")
    print("[green] the local password rules.               [green]")
    print("[yellow] 12 characters, upper- and lowercase,\n number and special charackter[yellow]")
    print("[green]=========================================[green]")
    print("[green]       Enter your password:              [green]")
    print("[green]    (or return for previous menu)         [green]")
    password: str = get_password()
    if not password:
        return ""
    return password

def print_local_result(check_result: dict[str,bool])->None:
    clear()
    score_info: tuple[int, int, int] = calc_local_score(check_result)
    score, total, percentage = score_info
    print("[green]=========================================[green]")
    print("[green]        Password Strength Result         [green]")
    print("[green]=========================================[green]")
    if not check_result["length"]:
        print("[red]Password must be at least 12 characters[red]")
        print(f"[red]Score: {score}/{total} => {percentage}% [red]")
    elif(percentage == 100):
        print(f"[green]Score: {score}/{total} => {percentage}% [green]")
    elif(percentage >= 80):
        print(f"[yellow]Score: {score}/{total} => {percentage}% [yellow]")
    else:
        print(f"[red]Score: {score}/{total} => {percentage}% [red]")
    print("[green]=========================================[green]")
    print("[green]       Detailed Result                   [green]")
    print("[green]=========================================[green]")
    if check_result["length"]:
        print("[green]Length: OK [green]")
    else:
        print("[red]Length: FAILED [red]")
    if check_result["upper"]:
        print("[green]Upper case: OK [green]")
    else:
        print("[red]Upper case: FAILED [red]")
    if check_result["lower"]:
        print("[green]Lower case: OK [green]")
    else:
        print("[red]Lower case: FAILED [red]")
    if check_result["digit"]:
        print("[green]Digit: OK [green]")
    else:
        print("[red]Digit: FAILED [red]")
    if check_result["special"]:
        print("[green]Special char: OK [green]")
    else:
        print("[red]Special char: FAILED [red]")
    if(percentage >= 80):
        print("[yellow]==========================================[yellow]")
        print("[yellow] You should also check for password leaks  [yellow]")
        print("[yellow]==========================================[yellow]")
    else:
        print("[green]=========================================[green]")
    print("[green]Press return Key to continue...[green]")
    input()
