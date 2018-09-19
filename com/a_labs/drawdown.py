"""
    __author__ = "Nidhi Kushwah"
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
            Finds drawdowns, sorts them and returns number of drawdowns
        """
        drawdown_list = list()
        i=0
        # To begin with set high
        if array[i] < array [i+1]:
            high = array[i+1]
        else:
            high = array[i]

        # Iterate
        trough_location = i+1
        while trough_location < len(array)-1:
            high, peak_location = self.__find_peaks_along_the_way(array, high, trough_location)
            low, new_high, trough_location = self.__find_troughs_along_the_way(array, high, peak_location)
            drawdown_list.append(high-low)
            # print("Drawdown: ", high - low)
            high = new_high
            if high == low:
                print("Drawdown doesn't exist ", high - low)
        drawdown_list.sort(reverse=True)
        return drawdown_list[:number_of_drawdowns]

    def __find_highest_along_the_way(self, array, current, tracker):
        """
            Finds highest value index untile the next fall happens
        """
        for index in range(tracker + 1, len(array)):
            element = array[index]
            if element >= current:
                current = element
            else:
                return current, tracker
        return current, tracker

    def __find_troughs_along_the_way(self,array, current, current_loc):
        """
            Finds lowest value index until the next rise happens
        """
        list_of_elements = list()
        for tracker in range(current_loc + 1, len(array)):
            element = array[tracker]
            if element < current:
                list_of_elements.append(element)
            elif element > current:
                current, loc = self.__find_highest_along_the_way(array, element, tracker)
                minimum = self.__get_minimum(list_of_elements)
                return minimum, current, loc
        return current, current, current_loc


    def __find_peaks_along_the_way(self, array, high, current_loc):
        """
            Tries to progressively find the peaks until the index starts to fall
        """   
        for tracker in range(current_loc + 1, len(array)):
            element = array[tracker]
            if element > high:
                high = array[tracker]
            else:
                return high, tracker-1
            position = tracker
        return high, position

    def __get_minimum(self, indiceslist):
        """
            Returns minimum in the list
        """
        lowest = indiceslist[0]
        for element in indiceslist:
            if lowest > element:
                lowest = element
        return lowest

    # def __get_maximum(self, indiceslist):
    #     highest = indiceslist[0]
    #     for element in indiceslist:
    #         if highest < element:
    #             highest = element
    #     return highest
