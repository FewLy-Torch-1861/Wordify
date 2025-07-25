#!/usr/bin/env python3

import argparse
import base64
import hashlib

ENCRYPTION_TYPES = {1: "Caesar Cipher", 2: "Reverse"}
ENCODE_TYPES = {1: "Base64", 2: "Base32", 3: "Base16", 4: "Hex"}
DECODE_TYPES = {1: "Base64", 2: "Base32", 3: "Base16", 4: "Hex"}
HASH_TYPES = {1: "SHA1", 2: "SHA256", 3: "SHA512", 4: "MD5"}


def save_to_file(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        print(f"\nFile save error: {e}")


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
            return encoded_bytes.hex()

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
            return bytes.fromhex(text).decode()

        else:
            raise ValueError("Unsupported decoding type")

    except Exception as e:
        return f"\nDecoding error: {e}"


def hash_(hash_type, text):
    try:
        encoded_bytes = text.encode("UTF-8")
        if hash_type == 1:
            return hashlib.sha1(encoded_bytes).hexdigest()

        elif hash_type == 2:
            return hashlib.sha256(encoded_bytes).hexdigest()

        elif hash_type == 3:
            return hashlib.sha512(encoded_bytes).hexdigest()

        elif hash_type == 4:
            return hashlib.md5(encoded_bytes).hexdigest()

        else:
            raise ValueError("Unsupported hash type")

    except Exception as e:
        return f"\nHashing error: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="Wordify - simple encode/encryption/hash tool"
    )
    parser.add_argument("-l", "--list", action="store_true", help="List supported")
    parser.add_argument(
        "-o", "--output", type=str, help="Output file to save the result"
    )
    parser.add_argument("-E", "--encrypt", type=int, help="Encryption type (1-2)")
    parser.add_argument("-e", "--encode", type=int, help="Encoding type (1-4)")
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

    def final(result):
        try:
            print(result)
            if args.output:
                save_to_file(args.output, result)

        except Exception as e:
            return f"\nFinal error: {e}"

    try:
        if args.list:
            list_supported()
            return

        if args.encrypt and args.text:
            result = encrypt(args.encrypt, args.text, args.shift)
            final(result)
            return

        if args.encode and args.text:
            result = encode(args.encode, args.text)
            final(result)
            return

        if args.decode and args.text:
            result = decode(args.decode, args.text)
            final(result)
            return

        if args.hash and args.text:
            result = hash_(args.hash, args.text)
            final(result)
            return

        parser.print_help()

    except Exception as e:
        print(f"\nMain error: {e}")


if __name__ == "__main__":
    main()
