#Inter Planetary Weight Kyle Yang
#CIT-115-D80 2025SP2
import time
firstName = input("What is your first name? ") #Assign string to firstName variable
bodyWeight = input("Type in your weight?    ") #Assign string to bodyWeight variable, hopefully it's a number

#Now to check if bodyWeight is a number so it can be converted to float
while bodyWeight.isalpha() == True: #Keeps asking for weight until integer or float is entered
    bodyWeight = input("You need to enter a number:  ")
else: #Now that a number is entered, time to do conversions
    bodyWeight = float(bodyWeight) #Convert string to float
    mercuryGrav = format(0.38 * bodyWeight, '.2f')
    venusGrav = format(0.91 * bodyWeight, '.2f')
    moonGrav = format(0.165 * bodyWeight, '.2f')
    marsGrav = format(0.38 * bodyWeight, '.2f')
    jupiterGrav = format(2.34 * bodyWeight, '.2f')
    saturnGrav = format(0.93 * bodyWeight, '.2f')
    uranusGrav = format(0.92 * bodyWeight, '.2f')
    neptuneGrav = format(1.12 * bodyWeight, '.2f')
    plutoGrav = format(0.066 * bodyWeight, '.2f')

if bodyWeight <= 0: #Check if number is 0 because nobody is 0 lbs
    print("You need to go eat something!")
    time.sleep(5) #Wait 5 seconds before closing

elif bodyWeight > 0: #Print out results
    print(firstName, ", you would weigh following on each planet on each our Solar System's planets:    ")
    print("Weight on Mercury:                 ", mercuryGrav, "lbs", "\nWeight on Venus:                   ", venusGrav, "lbs")
    #print("Weight on Venus:                   ", venusGrav) These were here so that I could test new line feature and test output formatting 
    print("Weight on Earth's Moon:            ", moonGrav, "lbs", "\nWeight on Mars:                    ", marsGrav, "lbs")
    #print("Weight on Mars:                    ", marsGrav)
    print("Weight on Jupiter:                 ", jupiterGrav, "lbs", "\nWeight on Saturn:                  ", saturnGrav, "lbs")
    #print("Weight on Saturn:                  ", saturnGrav)
    print("Weight on Uranus:                  ", uranusGrav, "lbs", "\nWeight on Neptune:                 ", neptuneGrav, 'lbs')
    #print("Weight on Neptune:                 ", neptuneGrav)
    print("Weight on Pluto:                   ", plutoGrav, "lbs")
    time.sleep(5) #Wait 5 seconds before closing