#!/bin/bash
INSTALL_DIR=${1:-/usr/local/bin}
ICON_DIR=${2:-/usr/share/icons/hicolor/48x48/apps}
DESKTOP_DIR=${3:-$HOME/.local/share/applications}
SOUND_DIR=${4:-/usr/local/share/smalltimer/sounds}
if [ ! -d "$ICON_DIR" ]; then
    sudo mkdir -p "$ICON_DIR"
fi
if [ ! -d "$DESKTOP_DIR" ]; then
    mkdir -p "$DESKTOP_DIR"
fi
if [ ! -d "$SOUND_DIR" ]; then
    sudo mkdir -p "$SOUND_DIR"
fi
sudo cp SmallTimer "$INSTALL_DIR/"
sudo cp img/icon.png "$ICON_DIR/smalltimer.png"
sudo cp sounds/end.wav "$SOUND_DIR/"
sed -e "s|Exec=.*|Exec=$INSTALL_DIR/SmallTimer|" \
    -e "s|Icon=.*|Icon=smalltimer|" \
    SmallTimer.desktop > "$DESKTOP_DIR/SmallTimer.desktop"
if [ -f "$INSTALL_DIR/SmallTimer" ] && [ -f "$DESKTOP_DIR/SmallTimer.desktop" ]; then
    echo "Installation complete. You can now launch SmallTimer from your application menu."
else
    echo "Installation failed. Please check your paths and try again."
fi
