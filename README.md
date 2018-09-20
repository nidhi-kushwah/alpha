# Alpha-> # Drawdown & # Broadcaster

# Drawdown

Here we try to find patterns of Falling & Rising like letter V and patterns like Rising, Falling & Rising like letter N.
In both cases the numbers of interest are highest and lowest which the functions find_highest_peak_until_next_fall and find_lowest_trough_until_next_rise try to accomplish


# Broadcaster

I am using Dask dataframe as the dataset is quite large so to make use of all cores of the CPU dask is one of the best option.
The task could also have been accomplished by using a csv reader to read bothe the csv files and populate the data into a table in sqlite which integrates easily with python3.
Once in DB the sorting operation could have been easily done and then all that is required is to iterate through the table and publish the records to ZMQ by checking the time
delay.

