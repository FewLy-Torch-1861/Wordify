#! /bin/bash

# CONFIGS
WELCOME_MESSAGE='Wordify'

banner() {
    figlet -f slant $WELCOME_MESSAGE
}

if which figlet >/dev/null 2>&1; then
    banner
else
    echo -e 'Figlet is not install\nInstalling Figlet...'
    sleep 0.5
    sudo pacman -S figlet --noconfirm --needed
    clear
    banner
fi

