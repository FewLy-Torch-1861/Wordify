#!/usr/bin/env python3

import os
import shutil
import argparse
import base64
import hashlib

WELCOME_MESSAGE = "Wordify"

ENCRYPTION_TYPES = {
    1: "Caesar Cipher",
    2: "Reverse",
}

ENCODE_TYPES = {
    1: "Base64",
    2: "Base32",
    3: "Base16",
}

HASH_TYPES = {1: "SHA-256"}


def banner():
    os.system("clear")
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")
    print(
        "Just a text encode\\encryption\\hash tool for Arch-based Linux written in Python.\n"
    )
    print("1 - Supported encryption types:")
    for k, v in ENCRYPTION_TYPES.items():
        print(f"  {k} - {v}")
    print("\n2 - Supported encode types:")
    for k, v in ENCODE_TYPES.items():
        print(f"  {k} - {v}")
    print("\n3 - Supported hash types:")
    for k, v in HASH_TYPES.items():
        print(f"  {k} - {v}")
    print(f"\nq - Exit\n")


def list_supported():
    print("Supported encryption types:")
    for k, v in ENCRYPTION_TYPES.items():
        print(f" {k} - {v}")
    print("\nSupported encode types:")
    for k, v in ENCODE_TYPES.items():
        print(f" {k} - {v}")
    print("\nSupported hash types:")
    for k, v in HASH_TYPES.items():
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


def encrypt(enc_type, text, caesar_shift=None):
    if enc_type == 1:
        result = caesar_cipher(text, caesar_shift)
        return result
    elif enc_type == 2:
        result = text[::-1]
        return result


def encode(encode_type, text):
    if encode_type == 1:
        result = base64.b64encode(text.encode("UTF-8")).decode()
        return result
    elif encode_type == 2:
        result = base64.b32encode(text.encode("UTF-8")).decode()
        return result
    elif encode_type == 3:
        result = base64.b16encode(text.encode("UTF-8")).decode()
        return result


def hash_(hash_type, text):
    if hash_type == 1:
        result = hashlib.sha256(text.encode("UTF-8")).hexdigest()
        return result


def main():
    parser = argparse.ArgumentParser(
        description="Wordify - simple encode\\encryption\\hash tool"
    )
    parser.add_argument("-l", "--list", action="store_true", help="List supported")
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Interactive mode"
    )
    parser.add_argument("--encrypt", type=int, help="Encryption type (1-2)")
    parser.add_argument("--encode", type=int, help="Encoding type (1-3)")
    parser.add_argument("--hash", type=int, help="Hash type (1)")
    parser.add_argument(
        "-s", "--shift", type=int, help="Caesar cipher shift (for encryption type 1 only)"
    )
    parser.add_argument("text", nargs="?", help="Text to encrypt")

    args = parser.parse_args()

    if args.list:
        list_supported()
        return

    if args.encrypt and args.text:
        result = encrypt(int(args.encrypt), str(args.text), int(args.shift))
        print(result)
        return

    if args.encode and args.text:
        result = encode(int(args.encode), str(args.text))
        print(result)
        return

    if args.hash and args.text:
        result = hash_(int(args.hash), str(args.text))
        print(result)
        return

    if args.interactive:
        check_dependency("wl-copy", "wl-clipboard")
        check_dependency("figlet", "figlet")

        banner()

        mode = input("\nWhat do you want to do (1-3, q): ")

        if mode == "q":
            exit()

        mode = int(mode)

        if mode == 1:
            enc_type = int(input("Encryption type (1-2): "))
            plain_text = str(input("Text to encrypt: "))

            if enc_type == 1:
                shift = int(input("Shift (default 3): "))
                result = encrypt(enc_type, plain_text, shift)
                print(f"{result}")
            else:
                result = encrypt(enc_type, plain_text)
                print(f"{result}")
        elif mode == 2:
            encode_type = int(input("Encoding type (1-3): "))
            plain_text = str(input("Text to encode: "))
            result = encode(encode_type, plain_text)
            print(f"{result}")
        elif mode == 3:
            hash_type = int(input("Hash type (1): "))
            plain_text = str(input("Text to hash: "))
            result = hash_(hash_type, plain_text)
            print(f"{result}")
        return


if __name__ == "__main__":
    main()
