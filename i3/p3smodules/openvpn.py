import psutil
import os.path
from time import time

class Py3status:

    def openvpn(self, i3status_output_json, i3status_config):
        pidfilename = '/tmp/nepo.pid'

        response = {'full_text': '', 'name': 'openpvn'}
        response['full_text'] = "VPN"

        if os.path.isfile(pidfilename):
            pidfile = open(pidfilename,'r')
            pid = int(pidfile.read().strip())
            pidfile.close()

        else:
            pid=0


        if (pid != 0 and psutil.pid_exists(pid) and
            psutil.Process(pid).name == "openvpn"):
                response['color'] = i3status_config['color_good']
        else:
            response['color'] = i3status_config['color_bad']

        response['cached_until'] = time() + 5

        return (5, response)
