# Kyle Yang
# CIT-115/115L
#Compound Iinterest Loop 

#Obtain user input, assign to variable, and check if it is valid for initial deposit, interest rate, number of months, and goal

fDeposit = input("What is your Original Deposit amount?(POSITIVE VALUE):    ") #Get value for fDeposit, will be converted to float
while not isinstance(fDeposit, (int, float)): #Check if fDeposit is a int or float and close loop if it is
    try:
        fDeposit = float(fDeposit)
        if fDeposit <= 0: #Check if value is negative
            fDeposit = input("You need to enter a POSITIVE numeric value that is GREATER than 0!:  ")
    except ValueError: #Prompt user for new value
        fDeposit = input("You need to enter a positive NUMERIC value!:  ")

fInterestRate = input("What is the Interest Rate?(POSITIVE VALUE):  ")
while not isinstance(fInterestRate, (int, float)): #Check if fDeposit is a int or float and close loop if it is
    try:
        fInterestRate = float(fInterestRate)
        if fInterestRate <= 0: #Check if value is negative
            fInterestRate = input("You need to enter a POSITIVE numeric value that is GREATER than 0!:  ")
    except ValueError: #Prompt user for new value
        fInterestRate = input("You need to enter a positive NUMERIC value!:  ")

iNumOfMonths = input("What is the Number of Months?(POSITIVE VALUE):    ")
while not isinstance(iNumOfMonths, (int, float)): #Check if fDeposit is a int or float and close loop if it is
    try:
        iNumOfMonths = int(iNumOfMonths)
        if iNumOfMonths <= 0: #Check if value is negative
            iNumOfMonths = input("You need to enter a POSITIVE numeric value that is GREATER than 0!:  ")
    except ValueError: #Prompt user for new value
        iNumOfMonths = input("You need to enter a positive NUMERIC value!:  ")

fGoalAmount = input("What is the Goal Amount?(can enter 0 but NOT negative):    ")
while not isinstance(fGoalAmount, (int, float)): #Check if fDeposit is a int or float and close loop if it is
    try:
        fGoalAmount = float(fGoalAmount)
        if fGoalAmount < 0: #Check if value is negative
            fGoalAmount = input("You need to enter a POSITIVE numeric value(Can enter 0 but NOT negative)!:  ")
    except ValueError: #Prompt user for new value
        fGoalAmount = input("You need to enter a positive NUMERIC value!:  ")

fInterestRate = (fInterestRate / 100) / 12

for iGoalMonth in range(iNumOfMonths): #Set variable for the goal month to be used in next loop, run loop for number of months input by user
    fDeposit += (fDeposit * fInterestRate) #Perform calculation and add to fDeposit
    print(f"Month:  {iGoalMonth+1}   Account Balance is: ${fDeposit:,.2f}") #Print this essage each time loop is ran, format to second decimal place for money


while fDeposit < fGoalAmount: #Run loop while fDeposit is more than the goal
    fDeposit += (fDeposit * fInterestRate) # Same calculation as above
    iGoalMonth += 1 #Add +1 to goal month to keep track of number of months to goal

#Print final message with the number of months it will take to get to goal and the original goal amount.
print(f"It will take:   {iGoalMonth+1} months to reach the goal of ${fGoalAmount:,.2f}")
