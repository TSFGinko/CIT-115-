# Kyle Yang
# Compound Interest Code
# CIT-115/115L
import time #To sleep the program so that is doesn't close immediately after it's ran

#Get user input and convert it to float
principalInvestment = float(input("Enter the starting principal:  "))
interestRate = float(input("Enter the annual interest rate: "))
compounding = float(input("How many times per year is the interest compounded?    "))
numOfPeriods = float(input("For how many years will the account earn interest? "))

interestRate = interestRate / 100 #Convert interest rate from percent to decimal
#Perform calculations and assign to variable futureValue
futureValue = format(principalInvestment * (1 + (interestRate / compounding)) ** (compounding*numOfPeriods), '.2f')
#Print message referencing numOfPeriods and futureValue variabkes
print("At the end of", numOfPeriods, "years you will have $", futureValue)
time.sleep(5) #Sleep program for 5 seconds after displaying message