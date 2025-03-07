from rich import print
import os
from password_util import get_password, check_have_i_been_pwned

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def print_menu() -> str:
    clear()
    print("[green]=========================================[green]")
    print("[green]        PASSWORD-STRENGTH CHECKER        [green]")
    print("[green]=========================================[green]")
    print("[green]       [1] Check password strength       [green]")
    print("[green]       [2] Check password leak           [green]")
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
            print("[green]Checking password strength...[green]")
        case 2:
            password = have_i_been_pwned_menu()
            if not password:
                return
            else:
                check_result = check_have_i_been_pwned(password)
        case 3:
            print_rule_of_thumbs()
        case 4:
            print("[green]Exiting...[green]")
            exit(0)

def print_error_message(message: str)-> None:
    clear()
    print("[red]=================ERROR==================[red]\n")
    print(f"[red]{message}[red]\n")
    print("[red]Press any Key to continue...[red]")
    input()

def print_rule_of_thumbs():
    clear()
    print("[green]=========================================[green]")
    print("[green]        RULE OF THUMBS                  [green]")
    print("[green]=========================================[green]")
    print("[green]       [1] Use a password manager        [green]")
    print("[green]       [2] Use a passphrase              [green]")
    print("[green]       [3] Use 2FA                       [green]")
    print("[green]       [5] Use a different password for every account[green]")
    print("[green]       [6] Use a password generator      [green]")
    print("[green]       [7] Use a password strength checker[green]")
    print("[green]       [8] Use a password leak checker   [green]")
    print("[green]       [9] Use a password policy         [green]")
    print("[green]       [10] Use a passwordless login (PASSKEY)[green]")
    print("[green]=========================================[green]")
    print("[green]       Press any key to go back          [green]")
    input()

def have_i_been_pwned_menu() -> str:
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
    print("[green]    (or Enter for previous menu)         [green]")
    password = get_password()
    if not password:
        return ""
    return password
