# Liang 2.9

def computeWindChill(temp, velc):
    return (35.74 + 0.6215*temp - 35.75*velc**0.16 + 0.4275*temp*velc**0.16)

def main():
    temperature = float(input('Enter the temperature in Fahrenheit between -58 and 41: '))
    windSpeed = int(input('Enter the wind speed in miles per hour (greater than or equal to 2): '))
    
    print ('The wind chill index is ', computeWindChill(temperature, windSpeed))

main()
