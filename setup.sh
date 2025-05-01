#!/bin/env bash

script_name="Wordify"
binary_name="wordify"

echo -e "${script_name} Installer\n 1 - Install\n 2 - Uninstall\n 3 - Cancel"
read -p "Choose what to do: " option

case "$option" in
  1)
    echo "Installing ${script_name}..."

    if [[ -f "${binary_name}.py" ]]; then
      sudo ln -sf "$(pwd)/${binary_name}.py" "/usr/local/bin/${binary_name}"
      sudo chmod +x "$(pwd)/${binary_name}.py"
      echo "${script_name} installed at: $(which ${binary_name})"

      if command -v python3 &> /dev/null; then
        echo "python3 is already installed, Great!"
      else
        echo -e "python3 is not installed\nInstalling python3..."
        if command -v pacman &> /dev/null; then
          sudo pacman -S python3 --needed --noconfirm
        elif command -v apt &> /dev/null; then
          sudo apt install python3 -y
        elif command -v yum &> /dev/null; then
          sudo yum install python3 -y
        elif command -v dnf &> /dev/null; then
          sudo dnf install python3 -y
        elif command -v zypper &> /dev/null; then
          sudo zypper --non-interactive install python3
        else
          echo -e "Distribution not supported!\nPlease install python3 manually."
        fi
      fi
    else
      echo "${binary_name}.py not found in the current directory!"
    fi
    ;;
  2)
    if command -v "${binary_name}" &> /dev/null; then
      echo "Uninstalling ${script_name}..."
      sudo rm -f "$(command -v "${binary_name}")"
      echo "${script_name} has been deleted!"
    else
      echo "${script_name} is not installed!"
    fi
    ;;
  3)
    echo "Cancelling."
    exit 0
    ;;
  *)
    echo "Invalid option!"
    exit 1
    ;;
esac

exit 0
