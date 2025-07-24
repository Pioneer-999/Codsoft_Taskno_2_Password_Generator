# Codsoft_Taskno_2_Password_Generator

# Password Generator - Python

## Project Overview

This project is a *Password Generator* written in *Python* as part of *CodSoft Internship* Task 2. It helps users generate strong and secure passwords by specifying the desired password length and ensuring the use of random characters for better security.

---

## Features

- Accepts user input for desired password length
- Generates strong, random passwords
- Includes uppercase, lowercase, digits, and symbols
- Uses built-in `random` and `string` libraries
- Prevents weak passwords with too-short lengths
- Outputs the password in a user-friendly format

---

## How It Works

1. The program prompts the user to input the desired password length.
2. It uses Python’s `random` and `string` libraries to build a secure password.
3. At least one character from each category (uppercase, lowercase, digit, symbol) is guaranteed.
4. Remaining characters are randomly chosen and shuffled.
5. The password is printed for the user to copy.

---

## Requirements

- Python 3.x
- No external libraries required

---

## Files Included

- `PasswordGenerator.py` – The main Python script
- `README.md` – Documentation file (this file)

---
Run the script:

```bash
python password_generator.py
