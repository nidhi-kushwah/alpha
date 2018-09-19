from com.a_labs.data_broadcaster import DataBroadcaster
from com.a_labs.subscriber import Subscriber
import unittest
import time
import threading
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

class TestDataBroadcaster(unittest.TestCase):

    def setUp(self):
        self.broadcaster = DataBroadcaster()
        self.book_path = "resources/orderbook.csv"
        self.trade_path = "resources/executed_trade.csv"
        self.subscriber = Subscriber()

    def subscribe(self):
        time.sleep(2)
        d = threading.Thread(name='daemon', target=self.daemon)
        d.setDaemon(True)
        d.start()

    def daemon(self):
        self.subscriber.wait_on_topic(50)  ## Give any number greater than 50

    def publish(self):
        self.broadcaster.broadcast_data(book_path=self.book_path, trade_path=self.trade_path)

    def test_broadcast(self):
        from multiprocessing import Process
        p1 = Process(target=self.subscribe())
        p1.start()


        p2 = Process(target=self.publish())
        p2.start()

        # from concurrent.futures import ProcessPoolExecutor
        # process_pool = ProcessPoolExecutor(
        #     max_workers=2)
        # process_pool.submit(self.subscribe, None)
        # process_pool.submit(self.publish, None)

        print("Sleeping for 5 seconds before checking the count of messages published")
        time.sleep(5)
        print("self.subscriber.get_number_of_messages(): ",self.subscriber.get_number_of_messages())
        # self.assertTrue(self.subscriber.get_number_of_messages() == 50)

if __name__ == '__main__':
    unittest.main()