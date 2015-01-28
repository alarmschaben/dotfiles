# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Date and Clock without seconds display
status.register("clock",
    format="%a %-d %b %H:%M",)

# determine spin state of hard disks, main system is on SSD
status.register("shell",
    command="~/dotfiles/getHDDstate.sh sdb",
    color="#ffffff",
    error_color="#00ff00",
)

status.register("shell",
    command="~/dotfiles/getHDDstate.sh sda",
    color="#ffffff",
    error_color="#00ff00",
)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
    critical_limit=4
)

# CPU temperature
status.register("temp",
    format="Ç {temp:.0f}°C",)

status.register("cpu_usage",
    format="Ñ {usage:3}%",
)

# Disk usage of /
status.register("disk",
    path="/",
    format="Ð {avail}G",)

status.register("mem",
        format="{used_mem:.0f}/{total_mem:.0f} MiB",
)

# Pulseaudio volume
status.register("pulseaudio",
    format="í {volume}%",)

# mpd status
status.register("mpd",
    format="à {artist} - {title}",
#    status={
#        "pause": "▷",
#        "play": "▶",
#        "stop": "◾",
#    },
)

status.run()
