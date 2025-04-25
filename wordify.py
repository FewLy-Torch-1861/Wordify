#!/usr/bin/env python3

import os
import shutil
import argparse
import base64
import sys

WELCOME_MESSAGE = "Wordify"

ENCRYPTION_TYPES = {
    1: "Caesar Cipher",
    2: "Reverse",
    3: "Base64",
    4: "Base32",
    5: "Base16",
}


def banner():
    os.system("clear")
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")
    print(
        "Just a simple word encryption tool for Arch-based Linux written in Python.\n\n"
        "Supported encryption types:"
    )
    for k, v in ENCRYPTION_TYPES.items():
        print(f" {k} - {v}")
    print(f" q - Exit\n")


def list_encryption_types():
    print("Supported encryption types:")
    for k, v in ENCRYPTION_TYPES.items():
        print(f" {k} - {v}")


def check_dependency(cmd, pkg_name):
    if not shutil.which(cmd):
        print(f"{cmd} is not installed. Installing {pkg_name}...")
        os.system(f"sudo pacman -S {pkg_name} --noconfirm --needed")
        os.system("clear")


def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def encrypt(text, enc_type, caesar_shift=None):
    if enc_type == 1:
        return caesar_cipher(text, caesar_shift or 3)
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
    parser = argparse.ArgumentParser(description="Wordify - simple encryption tool")
    parser.add_argument("-t", "--type", type=int, help="Encryption type (1-5)")
    parser.add_argument(
        "-s", "--shift", type=int, help="Caesar cipher shift (for type 1 only)"
    )
    parser.add_argument(
        "-l", "--list", action="store_true", help="List encryption types"
    )
    parser.add_argument("text", nargs="?", help="Text to encrypt")

    args = parser.parse_args()

    if args.list:
        list_encryption_types()
        return

    if args.type and args.text:
        try:
            result = encrypt(args.text, args.type, args.shift)
            print(result)
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    # Interactive mode
    try:
        check_dependency("wl-copy", "wl-clipboard")
        check_dependency("figlet", "figlet")

        banner()

        enc_type = input("Enter encryption type (1-5, q): ")
        if enc_type == "q":
            exit()

        enc_type = int(enc_type)
        plain_text = input("Enter text to encrypt: ")
        caesar_shift = None

        if enc_type == 1:
            try:
                caesar_shift = int(input("Enter shift amount (number): "))
            except ValueError:
                print("Invalid number. Using default shift = 3")
                caesar_shift = 3

        encrypted_text = encrypt(plain_text, enc_type, caesar_shift)

        os.system(f'wl-copy <<< "{encrypted_text}"')
        print("\nEncrypted text copied to clipboard:", encrypted_text)
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
