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


def encrypt(text, shift):
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


text = input("Enter text to encrypt: ")
shift_amount = int(input("Enter shift amount (number): "))
encrypted = encrypt(text, shift_amount)

print("Encrypted text:", encrypted)
