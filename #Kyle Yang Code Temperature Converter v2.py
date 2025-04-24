#Kyle Yang Code Temperature Converter
#CIT-115

print("Kyle Yang's Temperature Converter")

nTempurature = float(input("Enter a tempurature:    "))
cScale = input("Is the temp F for Fahrenheit or C for Celsius?: ")

while cScale not in ['F', 'f', 'C', 'c']:
    print("You must enter a F or a C")
    cScale = input("Is the Temp F for Fahrenheit or C for Celsius?: ")

while cScale in ['F', 'f']:
    if nTempurature < 100:
        print("Temp cannot be > 100°")
        break

    else:
        nCelsius = format(((5.0 / 9) * (nTempurature - 32)), ',.1f')
        print(f"The Celsius equivlent is: {nCelsius} °C")
        break 


while cScale in ['C', 'c']:
    if nTempurature > 212:
        print("Temp cannot be > 212°")
        break
    else:
        nFahrenheit = format(((9.0 / 5.0) * nTempurature) + 32, ',.1f')
        print(f"The Fahrenheit equivlent is: {nFahrenheit} °F")
        #print("test")
        break