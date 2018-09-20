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
class DrawDownCalculator():

    def find_drawdown(self, array, number_of_drawdowns):
        """
        Find drawdowns in the form of V, sorts them and returns drawdown start index, end index, duration and recovery time in addition to the n largest drawdowns.
        """
        drawdown_list = list()
        if sorted(array) == array:
            return []
        search_from_location = 0
        current_index = array[search_from_location]
        while search_from_location < len(array)-1:
            if array[search_from_location] > array[search_from_location+1]:
                ## It is Falling Rising type V->
                lowest_location_tuple = self.find_lowest_trough_until_next_rise(array, current_index, search_from_location)
                lowest = lowest_location_tuple[0]
                lowest_location = lowest_location_tuple[1]
                highest, highest_location = self.find_highest_until_next_fall(array, current_index, lowest_location)
                v_completed = True
                if v_completed:
                    drawdown_list.append((current_index-lowest,search_from_location, highest_location,highest_location-search_from_location, highest_location-lowest_location))
                    current_index = highest
                    search_from_location = highest_location
            else:
                ## It is Rising Falling Rising type N ->
                # find the peak
                highest_tuple = self.find_highest_until_next_fall(array, current_index, search_from_location)
                highest1 = highest_tuple[0]
                highest_location1 = highest_tuple[1]
                lowest, lowest_location = self.find_lowest_trough_until_next_rise(array, highest1, highest_location1)
                highest_tuple = self.find_highest_until_next_fall(array, current_index, lowest_location)
                highest2 = highest_tuple[0]
                highest_location2 = highest_tuple[1]
                v_completed = True
                if v_completed:
                    drawdown_list.append((highest1-lowest, highest_location1, highest_location2, highest_location2 -highest_location1, highest_location2-lowest_location))
                    current_index = highest2
                    search_from_location = highest_location2
        drawdown_list = sorted(drawdown_list, key=lambda x: x[0], reverse=True)
        return drawdown_list[:number_of_drawdowns]

    def find_highest_until_next_fall(self, array, current_high, search_from_location):
        list_of_highs = list()
        tracker = search_from_location+1
        for tracker in range(search_from_location+1, len(array)):
            if (tracker == len(array)):
                break
            element = array[tracker]
            if element > current_high:
                current_high = element
                list_of_highs.append((element, tracker))
            elif element < current_high:
                return self.__get_maximum(list_of_highs)
        if tracker+1 == len(array):
            print("{} is the final element".format(array[search_from_location+1]))
            return self.__get_maximum(list_of_highs)


    def find_lowest_trough_until_next_rise(self, array, current, search_from_location):
        list_of_lows = list()
        for tracker in range(search_from_location+1, len(array)):
            element = array[tracker]
            if element < current:
                list_of_lows.append((element,tracker))
            elif element > current:
                return self.__get_minimum(list_of_lows)

    def __get_minimum(self, indiceslist):
        """
            Returns minimum in the list
        """
        sorted_list = sorted(indiceslist, key=lambda x: x[0])
        lowest = sorted_list[0]
        return lowest

    def __get_maximum(self, indiceslist):
        """
            Returns maximum in the list
        """
        sorted_list = sorted(indiceslist, key=lambda x: x[0], reverse=True)
        highest = sorted_list[0]
        return highest