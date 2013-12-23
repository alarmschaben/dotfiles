#!/bin/bash

xrdb ~/.Xresources
xrdb -merge ~/dotfiles/solarized

feh --bg-scale /home/armin/Bilder/wallpaper/wallpaper.jpg

xset +fp /usr/share/fonts/local
xset fp rehash

setxkbmap -option caps:none
setxkbmap -option grp:shift_caps_toggle us,de
setxkbmap -option grp_led:caps

# Start a D-Bus session
source /etc/X11/xinit/xinitrc.d/30-dbus

# Start GNOME Keyring
eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)
export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK

exec i3
