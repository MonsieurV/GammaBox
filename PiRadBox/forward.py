import json
import requests

class Forwarder(object):
    """Forward the Geiger Counter readings to miscellaneous external
    services.
    In a better world, this should be an independant application (like an Erlang one)
    that receives the readings through a broker (like ZeroMQ) and then dispatch them
    to the several ends. Here we may have threading issues, and it may not be totally
    reliable."""
    def __init__(self, configurationFileName):
        self.configurationFileName = configurationFileName
        self.configuration = None
        self.reloadConfiguration()

    def reloadConfiguration(self):
        with open(self.configurationFileName, 'rb') as f:
            self.configuration = json.load(f)

    def dispatch(self, readings):
        print(readings)
        pass
