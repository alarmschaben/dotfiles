import psutil
import os.path
from time import time

class Py3status:

    def mqtt_temperature(self, i3status_output_json, i3status_config):
        tempfilename = '/tmp/mqtemps.txt'

        response = {'full_text': '', 'name': 'mqtt_temperature'}

        if os.path.isfile(tempfilename):
            tempsfile = open(tempfilename,'r')
            filecontent = tempsfile.read().strip()
            tempsfile.close()

        else:
            filecontent = "ERROR"

        response['full_text'] = filecontent

#        if (filecontent != ""):
#            response['color'] = i3status_config['color_degraded']
#        else:
#            response['color'] = i3status_config['color_bad']

        response['cached_until'] = time() + 5

        return (5, response)
