__author__ = 'hmly'


def cels_to_fahr(celsius):
    return (9/5) * celsius + 32

cels = input("Enter a degree in Celsius: ")
print("%d Celsius is %.1f Fahrenheit" % (cels, cels_to_fahr(cels)))