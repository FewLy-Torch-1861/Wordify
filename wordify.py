#!/usr/bin/env python3

import argparse
import base64
import hashlib
import os
import shutil

WELCOME_MESSAGE = "Wordify"

ENCRYPTION_TYPES = {
    1: "Caesar Cipher",
    2: "Reverse",
}

ENCODE_TYPES = {1: "Base64", 2: "Base32", 3: "Base16", 4: "Hex (Not Done)"}

DECODE_TYPES = {
    1: "Base64",
    2: "Base32",
    3: "Base16",
    4: "Hex (Not Done)",
}

HASH_TYPES = {
    1: "SHA1 (Not Done)",
    2: "SHA256",
    3: "SHA512 (Not Done)",
    4: "MD5 (Not Done)",
}


def banner():
    os.system("clear")
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")
    print(
        "Just a text encode/encryption/hash tool for Arch-based Linux written in Python.\n"
    )
    print("1 - Supported encryption types:")
    for k, v in ENCRYPTION_TYPES.items():
        print(f"  {k} - {v}")

    print("\n2 - Supported encode types:")
    for k, v in ENCODE_TYPES.items():
        print(f"  {k} - {v}")

    print("\n3 - Supported decode types:")
    for k, v in DECODE_TYPES.items():
        print(f"  {k} - {v}")

    print("\n4 - Supported hash types:")
    for k, v in HASH_TYPES.items():
        print(f"  {k} - {v}")
    print("\nq - Exit\n")


def list_supported():
    print("Supported encryption types:")
    for k, v in ENCRYPTION_TYPES.items():
        print(f" {k} - {v}")

    print("\nSupported encode types:")
    for k, v in ENCODE_TYPES.items():
        print(f" {k} - {v}")

    print("\nSupported decode types:")
    for k, v in DECODE_TYPES.items():
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
    try:
        if enc_type == 1:
            return caesar_cipher(text, caesar_shift or 3)

        elif enc_type == 2:
            return text[::-1]

        else:
            raise ValueError("Unsupported encryption type")

    except Exception as e:
        return f"\nEncryption error: {e}"


def encode(encode_type, text):
    try:
        encoded_bytes = text.encode("UTF-8")
        if encode_type == 1:
            return base64.b64encode(encoded_bytes).decode()

        elif encode_type == 2:
            return base64.b32encode(encoded_bytes).decode()

        elif encode_type == 3:
            return base64.b16encode(encoded_bytes).decode()

        elif encode_type == 4:
            return "Not done!"

        else:
            raise ValueError("Unsupported encoding type")

    except Exception as e:
        return f"\nEncoding error: {e}"


def decode(decode_type, text):
    try:
        encoded_bytes = text.encode("UTF-8")
        if decode_type == 1:
            return base64.b64decode(encoded_bytes).decode()

        elif decode_type == 2:
            return base64.b32decode(encoded_bytes).decode()

        elif decode_type == 3:
            return base64.b16decode(encoded_bytes).decode()

        elif decode_type == 4:
            return "Not done!"

        else:
            raise ValueError("Unsupported decoding type")

    except Exception as e:
        return f"\nDecoding error: {e}"


def hash_(hash_type, text):
    try:
        if hash_type == 1:
            return "Not done!"

        elif hash_type == 2:
            return hashlib.sha256(text.encode("UTF-8")).hexdigest()

        elif hash_type == 3:
            return "Not done!"

        elif hash_type == 4:
            return "Not done!"

        else:
            raise ValueError("Unsupported hash type")

    except Exception as e:
        return f"\nHashing error: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="Wordify - simple encode/encryption/hash tool"
    )
    parser.add_argument("-l", "--list", action="store_true", help="List supported")
    parser.add_argument("-e", "--encrypt", type=int, help="Encryption type (1-2)")
    parser.add_argument("-E", "--encode", type=int, help="Encoding type (1-4)")
    parser.add_argument("-d", "--decode", type=int, help="Decoding type (1-4)")
    parser.add_argument("-H", "--hash", type=int, help="Hash type (1-4)")
    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        help="Caesar cipher shift (for encryption type 1 only)",
    )
    parser.add_argument("text", nargs="?", help="Text to use")

    args = parser.parse_args()

    try:
        if args.list:
            list_supported()
            return

        if args.encrypt and args.text:
            print(encrypt(args.encrypt, args.text, args.shift))
            return

        if args.encode and args.text:
            print(encode(args.encode, args.text))
            return

        if args.decode and args.text:
            print(decode(args.decode, args.text))
            return

        if args.hash and args.text:
            print(hash_(args.hash, args.text))
            return

        parser.print_help()

    except Exception as e:
        print(f"\nMain error: {e}")


if __name__ == "__main__":
    main()
