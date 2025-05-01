## Wordify
Just a text encode/encryption/hash tool for Linux written in Python.

## Table of contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)

## Features
### Encryption
- Caesar Cipher
- Reverse

### Encode/Decode
- Base64
- Base32
- Base16
- Hex

### Hash
- SHA1
- SHA256
- SHA512
- MD5

### Misc
- Export to file

## Installation

```sh
git clone https://github.com/FewLy-Torch-1861/Wordify.git
cd Wordify
./setup.sh
```

## Usage

```
usage: wordify [-h] [-l] [-o OUTPUT] [-e ENCRYPT] [-E ENCODE] [-d DECODE]
               [-H HASH] [-s SHIFT]
               [text]

Wordify - simple encode/encryption/hash tool

positional arguments:
  text                  Text to use

options:
  -h, --help            show this help message and exit
  -l, --list            List supported
  -o, --output OUTPUT   Output file to save the result
  -e, --encrypt ENCRYPT
                        Encryption type (1-2)
  -E, --encode ENCODE   Encoding type (1-4)
  -d, --decode DECODE   Decoding type (1-4)
  -H, --hash HASH       Hash type (1-4)
  -s, --shift SHIFT     Caesar cipher shift (for encryption type 1 only)
```

```
$ wordify -l

Supported encryption types:
 1 - Caesar Cipher
 2 - Reverse

Supported encode types:
 1 - Base64
 2 - Base32
 3 - Base16
 4 - Hex

Supported decode types:
 1 - Base64
 2 - Base32
 3 - Base16
 4 - Hex

Supported hash types:
 1 - SHA1
 2 - SHA256
 3 - SHA512
 4 - MD5
```

##

*created on archlinux using neovim btw.*
