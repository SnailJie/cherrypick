import subprocess
import base64

from cloudbench import constants
from cloudbench.util import Debug

class Cloud(object):
    def __init__(self, env):
        self._env = env

    def execute(self, command):
        Debug.cmd << (' '.join(filter(None, command))) << "\n"
        p = subprocess.Popen(' '.join(command), shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        (outdata, errdata) = p.communicate()

        if errdata: 
            Debug.err << errdata << "\n"

        if outdata:
            Debug.info << outdata << "\n"

        return (p.wait() == 0)

    @property
    def env(self):
        return self._env

    def unique(self, name):
        """ Generates a unique name based on the benchmark """
        if name is None:
            return None

        return self.env.benchmark_name() + str(name)


    def if_available(self, option, value):
        if value:
            return [option,'"' + str(value) + '"']
        return []

