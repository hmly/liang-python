# Mid-term II - Q9

class MySet:
    def __init__(self):
        self.__storage = []

    def insert(self, item):
        if item not in self.__storage:
            self.__storage.append(item)

    def has(self, item):
        return item in self.__storage

    def __add__(self, item):
        if item not in self.__storage:
            self.__storage.append(item)

    def __contains__(self, item):
        return item in self.__storage

def main():
    mySet = MySet()
    item = ['Time', 8]
    print ('The item %s is in mySet: %s' % (item[0], str(mySet.has('Time'))))
    mySet.insert('Time')
    print ('The item %s is in mySet: %s' % (item[0], str(mySet.has('Time'))))

    print ('The item %d is in mySet: %s' % (item[1], str(mySet.__contains__(8))))
    mySet.__add__(8)
    print ('The item %d is in mySet: %s' % (item[1], str(mySet.__contains__(8))))

if __name__ == '__main__':
    main()
