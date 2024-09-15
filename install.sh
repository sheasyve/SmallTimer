#!/bin/bash
INSTALL_DIR=${1:-/usr/local/bin}
ICON_DIR=${2:-/usr/share/icons/hicolor/48x48/apps}
DESKTOP_DIR=${3:-$HOME/.local/share/applications}
SOUND_DIR=${4:-/usr/local/share/teenytinytimer/sounds}

if [ ! -d "$ICON_DIR" ]; then
    sudo mkdir -p "$ICON_DIR"
fi
if [ ! -d "$DESKTOP_DIR" ]; then
    mkdir -p "$DESKTOP_DIR"
fi
if [ ! -d "$SOUND_DIR" ]; then
    sudo mkdir -p "$SOUND_DIR"
fi

sudo cp TeenyTinyTimer "$INSTALL_DIR/"
sudo cp img/icon.png "$ICON_DIR/teenytinytimer.png"
sudo cp sounds/end.wav "$SOUND_DIR/"

sed -e "s|Exec=.*|Exec=$INSTALL_DIR/TeenyTinyTimer|" \
    -e "s|Icon=.*|Icon=teenytinytimer|" \
    TeenyTinyTimer.desktop > "$DESKTOP_DIR/TeenyTinyTimer.desktop"

if [ -f "$INSTALL_DIR/TeenyTinyTimer" ] && [ -f "$DESKTOP_DIR/TeenyTinyTimer.desktop" ]; then
    echo "Installation complete. You can now launch TeenyTinyTimer from your application menu."
else
    echo "Installation failed. Files could not be copied."
fi
sudo gtk-update-icon-cache /usr/share/icons/hicolor
