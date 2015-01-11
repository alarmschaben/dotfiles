#!/bin/bash
xrandr --output DVI-I-3 --mode 1280x1024 --right-of DVI-I-2 --rotate left

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

# Composting for smooth scrolling
compton --backend xrender --vsync opengl --paint-on-overlay -b

# start MQTT listener for weather info
~/.i3/feeder.rb &

exec i3
