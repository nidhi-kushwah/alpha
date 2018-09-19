import dask
import dask.dataframe as dd
import time
from com.a_labs.publisher import Publisher

"""
    __author__ = "Nidhi Kushwah"
    __date   : 19-09-2018
    __copyright__ = "Copyright 2007, The AL Assignment"
    __license__ = "Free Usage"
    __version__ = "1.0.0"
    __maintainer__ = "Nidhi Kushwah"
    __email__ = "nidhikushwah_it@rediffmail.com"
    __status__ = "Production"
"""

class DataBroadcaster:
    def __init__(self):
        self.port = "5556"
        self.publisher = Publisher()
        #TODO: Should be the exchange name
        self.topic = "Sample_Topic"

    def __read_merge_and_sort_data(self, book_path, trade_path) -> dask.dataframe:
        df_bu_book = dd.read_csv(book_path)
        print("Length of df_bu_book: {}".format(len(df_bu_book)))
        df_bu_trade = dd.read_csv(trade_path)
        print("length of df_bu_trade is {}".format(len(df_bu_trade)))
        merged = df_bu_book.merge(df_bu_trade, how='outer')
        delayed_df = dask.delayed(merged)
        result = delayed_df.sort_values(by='qs_send_time')
        final = dask.compute(result)
        print("length of merged is: {}".format(len(final[0])))
        return final[0]

    # def sort_based_on_time(self):
    #     import csv
    #     import operator
    #     merged = open("merged.csv", 'r')
    #     merged_data = csv.reader(merged, delimiter=',')
    #     sort = sorted(merged_data, key=operator.itemgetter(1))
    #     for each_record in sort:
    #         self.broadcast(each_record[1])


    def publish(self,record):
        if record is not None:
            self.publisher.publish_message(self.topic, record)

    def broadcast_data(self, book_path, trade_path):
        print("About to broadcast now...")
        merged_data_frame = self.__read_merge_and_sort_data(book_path,trade_path)
        for index in range(len(merged_data_frame.values) - 1):
            print("Index at: ", index)
            record = merged_data_frame.values[index]
            self.publish(record)
            time_to_sleep = (merged_data_frame.values[index + 1][1] - merged_data_frame.values[index][1]) / 1000
            print("Sleeping for {} seconds".format(time_to_sleep))
            time.sleep(time_to_sleep)
        print("Last message index {}".format(len(merged_data_frame.values) - 1))
        self.publish(merged_data_frame.values[len(merged_data_frame.values) - 1])

# if __name__ == '__main__':
#     b = DataBroadcaster()
#     b.broadcast_data(book_path="resources/orderbook.csv", trade_path="resources/executed_trade.csv")