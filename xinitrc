xrdb ~/.Xresources

feh --bg-scale /home/armin/Bilder/wallpaper/wallpaper-2886666.jpg

xset +fp /usr/share/fonts/local
xset fp rehash

setxkbmap -option caps:none
setxkbmap -option grp:shift_caps_toggle us,de
setxkbmap -option grp_led:caps   

exec fbxkb &
exec i3

