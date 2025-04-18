import os
import shutil
import time

WELCOME_MESSAGE = "Wordify"


def banner():
    os.system(f"figlet -f slant {WELCOME_MESSAGE}")


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


def encrypt(text, type):
    if type == "caesar_cipher":
        result = caesar_cipher(text)
        return result


print("""
All supported encryption type
 - caesar_cipher (Caesar Cipher)
""")
encryption_type = input("Enter encryption type: ")
plain_text = input("Enter text to encrypt: ")
encrypted = encrypt(plain_text, encryption_type)

print("Encrypted text:", encrypted)
