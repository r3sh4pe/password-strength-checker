# Password Strength Checker

## Overview
The Password Strength Checker is a Python-based application designed to help users evaluate the strength of their passwords. It provides various functionalities such as checking password strength locally, verifying against common password wordlists, and checking for password leaks using the Have I Been Pwned API.

## Features
- **Local Password Strength Check**: Evaluates the password based on length, uppercase, lowercase, digits, and special characters.
- **Wordlist Check**: Verifies if the password is present in user defined password wordlists. More wordlists can be added to the `password_lists` directory.
- **Password Leak Check**: Uses the Have I Been Pwned API to check if the password has been leaked.
- **Rules of Thumb**: Provides best practices for creating strong passwords.

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/r3sh4pe/password-strength-checker.git
    cd password-strength-checker
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Run the application**:
    ```sh
    python password_checker.py
    ```

2. **Follow the on-screen menu**:
    - **Check password strength (local)**: Evaluates the password based on predefined rules.
    - **Check against local wordlists**: Checks if the password is present in user defined wordlists. (`password_lists` directory)
    - **Check password leak (online)**: Uses the Have I Been Pwned API to check for password leaks.
    - **Rule of Thumbs**: Displays best practices for creating strong passwords.
    - **Exit**: Exits the application.
