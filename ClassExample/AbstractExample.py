from abc import ABC, abstractmethod


class Cricket(ABC):

    @abstractmethod
    def overs(self):
        pass


class T20(Cricket):

    def overs(self):
        print("Teams get 20 overs each")


class OneDay(Cricket):

    def overs(self):
        print("Teams get 50 overs each")




t20 = T20()
oneday = OneDay()

t20.overs()
oneday.overs()
