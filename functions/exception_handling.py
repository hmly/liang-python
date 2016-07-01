def main():
    while True:
        try:
            print ("Enter a number: ")
            n = input()
        except IOError:
            print ("Please enter a correc number")
