# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Date and Clock without seconds display
status.register("clock",
    format="%a %-d %b %H:%M",)

# Load display
status.register("load")

# CPU temperature
status.register("temp",
    format="Ç {temp:.0f}°C",)

# CPU usage
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
status.register("alsa",
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
