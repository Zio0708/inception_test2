class Pet:
    def __init__(self, petName, foodName, foodAmount, foodTime):
        self.__foodName = foodName
        self.__foodAmount = foodAmount
        self.__petName = petName
        self.__foodTime = foodTime

    @property
    def foodName(self):
        return self.__foodName

    @property
    def foodAmount(self):
        return self.__foodAmount

    @property
    def petName(self):
        return self.__petName

    @property
    def foodTime(self):
        return self.__foodTime

    @foodName.setter
    def foodName(self, new_foodName):
        self.__foodName = new_foodName

    @foodAmount.setter
    def foodAmount(self, new_foodAmount):
        self.__foodAmount = new_foodAmount

    @petName.setter
    def petName(self,new_petName):
        self.__petName = new_petName

    @foodTime.setter
    def foodTime(self,new_foodTime):
        self.__foodTime = new_foodTime