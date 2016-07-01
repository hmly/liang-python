from Stack import Stack

def decToBin(dec):
    remStack = Stack()
    bin = ''
    while dec > 0:
        remStack.push(dec % 2)
        dec //= 2
    while not remStack.isEmpty():
        bin += str(remStack.pop())
    return bin

print('Dec: %d -> Bin: %s' % (5672, decToBin(5674)))
