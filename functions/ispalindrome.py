from Deque import Deque

def isPalindrome(string):
    charDeque = Deque()
    hasPairs = True
    
    for char in string:
        charDeque.addFront(char)

    while hasPairs and not charDeque.isEmpty():
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            return False
        if charDeque.size()%2 != 0:
            hasPairs = False
    return True
