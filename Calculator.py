class Calculator:
    def __init__(self, initial_calculation=0):
        self.__last_calculation = initial_calculation

    def get_last_calculation(self):
        return self.__last_calculation

    def add(self, addend1, addend2=0):
        if not (isinstance(addend1, int) or isinstance(addend1, float)) or \
                not (isinstance(addend2, int) or isinstance(addend2, float)):
            return "INVALID INPUT"
        if not addend2 == 0:
            self.__last_calculation = addend1 + addend2
        else:
            self.__last_calculation += addend1
        return self.__last_calculation

    def subtract(self, sub1, sub2=0):
        if not (isinstance(sub1, int) or isinstance(sub1, float)) or \
                not (isinstance(sub2, int) or isinstance(sub2, float)):
            return "INVALID INPUT"
        if not sub2 == 0:
            self.__last_calculation = sub1 - sub2
        else:
            self.__last_calculation -= sub1
        return self.__last_calculation
