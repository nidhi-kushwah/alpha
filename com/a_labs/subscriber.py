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

class Subscriber():
    def __init__(self):
        """
        Initialize ports & sockets
        """
        self.port = "5556"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.number_of_messages = 0

    def get_number_of_messages(self):
        return self.number_of_messages

    def reset_number_of_messages(self):
        self.number_of_messages = 0

    def wait_on_topic(self, iterations=None):
        """
        Wait indefinitely or for a specified number of iterations.
        :param iterations:
        :return:
        """
        print("Waiting for data broadcast from exchange...")
        self.socket.connect("tcp://localhost:%s" % self.port)

        topicfilter = "Sample_Topic"
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

        if(iterations is not None):
            for update_nbr in range(iterations):
                string = self.socket.recv()
                print("Message received:{}".format(string))
                self.number_of_messages+=1
                print("self.number_of_messages: ",self.number_of_messages)
        else:
            while True:
                string = self.socket.recv()
                print("Message received:{}".format(string))

# if __name__ == '__main__':
#     sub = Subscriber()
#     sub.wait_on_topic(50)
#     print(sub.get_number_of_messages())