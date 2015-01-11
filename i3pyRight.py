# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Date and Clock without seconds display
status.register("clock",
    format="%a %-d %b %H:%M",)

# Show output of script that fetches temperatures from home automation
status.register("shell",
    command="cat /tmp/mqtemps.txt",
)

status.run()
