class SmartSet:
    def __init__(self):
        self.__items = {}

    def __len__(self):
        return len(self.__items)

    def __items__(self):
        return list(self.__items.keys())

    def __getItem__(self, item):
        if item in self.__items:
            return self.__items[item]
        else:
            raise RuntimeError('Item ' + item + ' not in the set')

    def __contains__(self, item):
        return item in self.__items

    def __add__(self, item):
        if item in self.__items:
            self.__items[item] += 1
        else:
            self.__items[item] = 1

    def __sub__(self, item):
        if item in self.__items:
            self.__items[item] -= 1
            if self.__items[item] == 0:
                del self.__items[item]
        else:
            raise RuntimeError('Item ' + item + ' not in the set')

    def __str__(self):
        return 'SmartSet has length of %d' % len(self.__items)

# [fd + w for w in 'Hello World'.split()]
