class Pet:
    def __init__(self, foodName, foodAmount, petName):
        self.__foodName = foodName
        self.__foodAmount = foodAmount
        self.__petName = petName

    @property
    def foodName(self):
        return self.__foodName

    @property
    def foodAmount(self):
        return self.__foodAmount

    @property
    def petName(self):
        return self.__petName

    @foodName.setter
    def foodName(self, new_foodName):
        self.__foodName = new_foodName

    @foodAmount.setter
    def foodAmount(self, new_foodAmount):
        self.__foodAmount = new_foodAmount

    @petName.setter
    def petName(self,new_petName):
        self.__petName = new_petName
