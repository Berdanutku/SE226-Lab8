from abc import ABC


class a(ABC):
    def __init__(self, address):
        self.address = address

    def calculate_freqs(self, address):
        pass


class ListCount(a):
    def __init__(self, address):
        a.__init__(self, address)

    def calculate_freqs(self, address):
        list = []
        file = open(address)
        read = file.readline().split()
        for x in read:
            if x not in list:
                list.append(x)
        for x in range(0, len(list)):
            print(read.count(list[x]), " - ", list[x])


class DictCount(a):
    def __init__(self, address):
        a.__init__(self, address)

    def calculate_freqs(self, address):
        dict = {}
        file = open(address)
        read = file.readline()
        for x in read.split():
            dict[x] = dict.get(x, 0) + 1
        for x in dict:
            print(x,":",dict[x])

address = 'strange.txt'
list = ListCount(address)
list.calculate_freqs(address)
dict = DictCount(address)
dict.calculate_freqs(address)