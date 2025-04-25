#!/usr/bin/env python3


import os
import shutil
import time
import base64

WELCOME_MESSAGE = "Wordify"


def banner():
    os.system("clear")
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")
    print(
        "Just a simple word encryption tool for Arch-based Linux written in Python.\n\n"
        "Supported encryption types:\n"
        " 1 - Caesar Cipher\n"
        " 2 - Reverse\n"
        " 3 - Base64\n"
        " 4 - Base32\n"
        " 5 - Base16\n"
        " q - Exit\n"
    )


def check_dependency(cmd, pkg_name):
    if not shutil.which(cmd):
        print(f"{cmd} is not installed. Installing {pkg_name}...")
        time.sleep(0.5)
        os.system(f"sudo pacman -S {pkg_name} --noconfirm --needed")
        os.system("clear")


# Dependency checks
check_dependency("wl-copy", "wl-clipboard")
check_dependency("figlet", "figlet")

banner()


def caesar_cipher(text):
    try:
        shift = int(input("Enter shift amount (number): "))
    except ValueError:
        print("Invalid number. Using default shift = 3")
        shift = 3

    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def encrypt(text, enc_type):
    if enc_type == 1:
        return caesar_cipher(text)
    elif enc_type == 2:
        return text[::-1]
    elif enc_type == 3:
        return base64.b64encode(text.encode()).decode()
    elif enc_type == 4:
        return base64.b32encode(text.encode()).decode()
    elif enc_type == 5:
        return base64.b16encode(text.encode()).decode()
    else:
        return "Invalid encryption type."


def main():
    try:
        enc_type = input("Enter encryption type (1-5, q): ")
        if enc_type == "q":
            exit()
        enc_type = int(enc_type)
        plain_text = input("Enter text to encrypt: ")
        encrypted_text = encrypt(plain_text, enc_type)

        os.system(f'wl-copy <<< "{encrypted_text}"')
        print("\nEncrypted text copied to clipboard:", encrypted_text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
