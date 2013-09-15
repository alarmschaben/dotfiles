import psutil
from time import time

class Py3status:
    def RAMinfo(self, json, i3status_config):

        response = {'full_text' : '', 'name' : 'RAMinfo'}

        mem_total = int(psutil.virtual_memory().total / 1048576)
        mem_used = int(psutil.virtual_memory().used / 1048576)
        mem_buffers = int(psutil.virtual_memory().buffers / 1048576)
        mem_cached = int(psutil.virtual_memory().cached / 1048576)
        mem_real_used = mem_used - mem_buffers - mem_cached
        mem_percent = int(psutil.virtual_memory().percent)

        if mem_percent <= 50:
            response['color'] = i3status_config['color_good']
        elif mem_percent <= 75:
            response['color'] = i3status_config['color_degraded']
        else:
            response['color'] = i3status_config['color_bad']

        response['full_text'] = 'Î {}MB/{}MB'.format(mem_real_used, mem_total)

        response['cached_until'] = time() + 5

        return(1, response)
