import os
import shutil
import time
import base64

WELCOME_MESSAGE = "Wordify"


def banner():
    os.system("clear")
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")
    print(
        "Just a simple word encryption program for arch based linux writed in python.\n\nAll supported encryption type\n 1 - caesar_cipher\n 2 - reverse\n 3 - base64\n 4 - base32\n 5 - base16\n"
    )


# Check wl-copy
if not shutil.which("wl-copy"):
    print("wl-copy is not installed\nInstalling wl-copy...")
    time.sleep(0.5)
    os.system("sudo pacman -S wl-clipboard --noconfirm --needed")
    os.system("clear")

# Check figlet
if shutil.which("figlet"):
    banner()
else:
    print("Figlet is not installed\nInstalling Figlet...")
    time.sleep(0.5)
    os.system("sudo pacman -S figlet --noconfirm --needed")
    os.system("clear")
    banner()


def caesar_cipher(text):
    shift = int(input("Enter shift amount (number): "))
    result = ""
    for char in text:
        if char.isalpha():
            # Check case
            base = ord("A") if char.isupper() else ord("a")
            # Shift character
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Not encrypt non character
    return result


def encrypt(text, type):
    if type == 1:
        return caesar_cipher(text)
    elif type == 2:
        return text[::-1]
    elif type == 3:
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    elif type == 4:
        return base64.b32encode(text.encode("utf-8")).decode("utf-8")
    elif type == 5:
        return base64.b16encode(text.encode("utf-8")).decode("utf-8")
    else:
        return "Nope"


encryption_type = int(input("Enter encryption type (Number): "))
plain_text = input("Enter text to encrypt: ")
encrypted_text = encrypt(plain_text, encryption_type)

os.system(f"wl-copy {encrypted_text}")

print("\nEncrypted text:", encrypted_text, "\n")
