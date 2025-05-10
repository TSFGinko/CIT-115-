#Kyle Yang
#Real Estate Analyzer
#CIT-115-D80

#Define Main funtion
def main():
    #Define variable for list
    lPropertyValues = []
    #Create While loop to get property values until user inputs N or n 
    while True:
        fSalesPrice = getFloatInput(input("Enter a number: "))
        #Put user input into list and reprompt
        lPropertyValues.append(fSalesPrice)
        sAnswer = input("Would you like to enter another number? (y/n): ")
        #Check user input for valid response and reprompt
        while sAnswer not in ["y", "Y", "n", "N"]:
            sAnswer = input("Answer must be 'y' or 'n'. Input an answer. (y/n): ")
        #Brek loop if user inputs n or N
        if sAnswer in ["n", "N"]:
            break
            
    #Sort list
    lPropertyValues.sort()

    #Print message for each item in list
    for value in range(len(lPropertyValues)):
        #Add 1 so property does not say 0
        iPlace = value + 1
        print(f"Property {iPlace}  $     {lPropertyValues[value]:.2f}")
    
    #Get total, minimum, maximum, median, average, and commission values
    fTotal = sum(lPropertyValues)
    fMinimum = min(lPropertyValues)
    fMaximum = max(lPropertyValues)
    fMedian = getMedian(lPropertyValues)
    fAverage = fTotal / len(lPropertyValues)
    fCommission = fTotal * 0.03

    #DIsplay results
    print(f"Minimum:    $   {fMinimum:.2f}")
    print(f"Maximum:    $   {fMaximum:.2f}")
    print(f"Total:      $   {fTotal:.2f}")
    print(f"Average:    $   {fAverage:.2f}")
    print(f"Median:     $   {fMedian:.2f}")
    print(f"COmmission: $   {fCommission:.2f}")
          

#Define getFloatInput function
def getFloatInput(val):
    while True:
        try:
            #Attempt to convert input to float
            val = float(val)
            if val <= 0:
                #Reprompt for input if input or equal to or less than 0
                val = input("Property sales value needs to be GREATER than 0!: ")
            else:
                return val
        except ValueError:
            #Reprompt for input if value is not number
            val = input("Property sales value to be a NUMBER!: ")

#Define getMedian function
def getMedian(lPropertyValues):
    #Get length of list value
    iListLength = len(lPropertyValues)
    #Get the value in the middle of list for median
    iMedian = iListLength // 2
    #Check if list is even number
    if iListLength % 2 == 0:
        #Average middle two values and return result
        iMedianOdd = (lPropertyValues[iMedian - 1] + lPropertyValues[iMedian]) / 2
        return iMedianOdd
    else:
        #Return median
        return lPropertyValues[iMedian]


#Call main funtion
main()