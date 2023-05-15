import os
import time


class Event:
    def __init__(self, mode):
        self._object = None
        self._route = None
        if mode not in (1, 2, 3):
            raise Exception('Wrong mode')
        if mode == 1:
            self._mode = 1
        if mode == 2:
            self._mode = 2
        if mode == 3:
            self._mode = 3

    def __del__(self):
        del self

    def register(self):
        self._object = input('Object:')
        self._route = input('Route:')
        os.chdir(r'src/txt')
        with open('registry.log', mode='w') as rl:
            rl.write(str(time.time())+'Object:'+self._object+'\n')
            rl.write('Route:'+self._route)
        rl.close()


    