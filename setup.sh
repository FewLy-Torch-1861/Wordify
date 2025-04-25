#!/bin/bash

echo -e "Wordify Installer\n 1 - Install\n 2 - Uninstall\n 3 - Cancel"
read -p "Choose what to do: " option

case "$option" in
    1)
        echo "Installing..."
        if [[ -f "wordify.py" ]]; then
            sudo ln -sf "$(pwd)/wordify.py" /usr/local/bin/wordify
            sudo chmod +x "$(pwd)/wordify.py"

            if command -v python3 &> /dev/null; then
                echo "python3 is already installed, Great!"
            else
                echo -e "python3 is not install\n installing python3..."
                sudo pacman -S python3 --needed --noconfirm
            fi

            echo "Wordify installed at: $(which wordify)"
        else
            echo "wordify.py not found in current directory!"
        fi
        ;;
    2)
        if command -v wordify &> /dev/null; then
            echo "Uninstalling..."
            sudo rm -f "$(command -v wordify)"
            echo "Wordify has been deleted!"
        else
            echo "Wordify is not installed!"
        fi
        ;;
    3)
        exit 0
        ;;
    *)
        echo "Invalid option!"
        exit 1
        ;;
esac