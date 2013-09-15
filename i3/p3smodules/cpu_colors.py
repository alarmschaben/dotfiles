import psutil
from time import time

class Py3status:
    def CPUinfo(self, json, i3status_config):

        response = {'full_text' : '', 'name' : 'CPUinfo'}
        cpu_percent = psutil.cpu_percent(interval=0)

        if cpu_percent <= 50:
            response['color'] = i3status_config['color_good']
        elif cpu_percent <= 75:
            response['color'] = i3status_config['color_degraded']
        else:
            response['color'] = i3status_config['color_bad']

        response['full_text'] = 'Ñ {}%'.format(cpu_percent)

        response['cached_until'] = time() + 5

        return(0, response)
