import zmq
"""
    __author__ = "Nidhi Kushwah"
    __date   : 16-09-2018
    __copyright__ = "Copyright 2007, The AL Assignment"
    __license__ = "Free Usage"
    __version__ = "1.0.0"
    __maintainer__ = "Nidhi Kushwah"
    __email__ = "nidhikushwah_it@rediffmail.com"
    __status__ = "Production"
"""

class Publisher():

    def __init__(self):
        # TODO: Read from config
        self.port = "5556"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://*:%s" % self.port)

    def publish_message(self, topic, record):
        self.socket.send_string("%s %s" % (topic, str(record)))