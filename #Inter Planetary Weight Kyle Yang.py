#Inter Planetary Weight Kyle Yang
#CIT-115-D80 2025SP2
import time

#Weight of factors of other planets
nMERCURY_FACTOR = 0.38
nVENUS_FACTOR = 0.91
nMOON_FACTOR = 0.165
nMARS_FACTOR = 0.38
nJUPITER_FACTOR = 2.34
nSATURN_FACTOR = 0.93
nURANUS_FACTOR = 0.92
nNEPTUNE_FACTOR = 1.12
nPLUTO_FACTOR = 0.066

sFirstName = input("What is your first name? ") #Assign string to firstName variable
nEarthWeight = float(input("Type in your weight?    ")) #Assign string to bodyWeight variable and convert it to float, hopefully it's a number

#Perform calculations and format to two decimal spaces
nMercury = format(0.38 * nEarthWeight, ',.2f')
nVenus = format(0.91 * nEarthWeight, ',.2f')
nMoon = format(0.165 * nEarthWeight, ',.2f')
nMars = format(0.38 * nEarthWeight, ',.2f')
nJupiter = format(2.34 * nEarthWeight, ',.2f')
nSaturn = format(0.93 * nEarthWeight, ',.2f')
nUranus = format(0.92 * nEarthWeight, ',.2f')
nNeptune = format(1.12 * nEarthWeight, ',.2f')
nPluto = format(0.066 * nEarthWeight, ',.2f')

#Print out message including input name and calculated weights
print(f"{sFirstName} here are you weight on our Solar System's planets:    ")
print(f"Weight on Mercury:                 {nMercury}")
print(f"Weight on Venus:                   {nVenus}") 
print(f"Weight on Earth's Moon:            {nMoon}")
print(f"Weight on Mars:                    {nMars}")
print(f"Weight on Jupiter:                 {nJupiter}")
print(f"Weight on Saturn:                  {nSaturn}")
print(f"Weight on Uranus:                  {nUranus}")
print(f"Weight on Neptune:                 {nNeptune}")
print(f"Weight on Pluto:                   {nPluto}")
time.sleep(5) #Wait 5 seconds before closing