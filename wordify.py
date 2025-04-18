import os
import shutil
import time

WELCOME_MESSAGE = "Wordify"


def banner():
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")
    print(
        "Just a simple word encryption program for arch based linux writed in python.\n\nAll supported encryption type\n 1 - caesar_cipher\n 2 - reverse\n"
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
            # เช็คว่าเป็นตัวพิมพ์เล็กหรือใหญ่
            base = ord("A") if char.isupper() else ord("a")
            # เลื่อนตัวอักษร
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # ไม่ใช่ตัวอักษรก็ไม่ต้องเข้ารหัส
    return result


def reverse(text):
    result = text[::-1]
    return result


def encrypt(text, type):
    if type == 1:
        result = caesar_cipher(text)
        return result
    elif type == 2:
        result = reverse(text)
        return result


encryption_type = int(input("Enter encryption type (Number): "))
plain_text = input("Enter text to encrypt: ")
encrypted_text = encrypt(plain_text, encryption_type)

os.system(f"wl-copy {encrypted_text}")

print("\nEncrypted text:", encrypted_text)
