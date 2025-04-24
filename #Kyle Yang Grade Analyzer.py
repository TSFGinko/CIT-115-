#Kyle Yang
#CIT-115/115L
#Grade Analyzer


#Obtain user input for calculations
sStudentName = input("Name of the person that we are calculating the grades for?:   ") #String
iTestScoreOne = int(input("Input Grade for Test 1:  "))   #Integer
iTestScoreTwo = int(input("Input Grade for Test 2:  "))   #Integer
iTestScoreThree = int(input("Input Grade for Test 3:  ")) #Integer
iTestScoreFour = int(input("Input Grade for Test 4:  "))  #Integer

#Check if user input for any of the variables is equal to 0 
if 0 >= iTestScoreOne or 0 >= iTestScoreTwo or 0 >= iTestScoreThree or 0 >= iTestScoreFour:
    exit("Test scores must be GREATER than 0!")

#Ask if user would like to drop grade and store answer in variable
sDropGrade = input("Do you wish to Drop the Lowest Grade? Y/N    ") #String

#Add scores
fScoreAverage = iTestScoreOne + iTestScoreTwo + iTestScoreThree + iTestScoreFour

if sDropGrade == "N" or sDropGrade == "n":
    fScoreAverage /= 4 #Divide by 4 to get average 

#Find lowest grade and remove it from equation
elif sDropGrade == "Y" or sDropGrade == "y":
    if iTestScoreOne <= iTestScoreTwo and iTestScoreOne <= iTestScoreThree and iTestScoreOne <= iTestScoreFour:
        fScoreAverage -= iTestScoreOne

    elif iTestScoreTwo <= iTestScoreOne and iTestScoreTwo <= iTestScoreThree and iTestScoreTwo <= iTestScoreFour:
        fScoreAverage -= iTestScoreTwo

    elif iTestScoreThree <= iTestScoreOne and iTestScoreThree <= iTestScoreOne and iTestScoreThree <= iTestScoreFour:
        fScoreAverage -= iTestScoreThree

    elif iTestScoreFour <= iTestScoreOne and iTestScoreFour <= iTestScoreTwo and iTestScoreFour <= iTestScoreThree:
        fScoreAverage -= iTestScoreFour
    
    fScoreAverage /= 3 #Divide by 3 to get average
    
else:
    exit(f"You Enter Y or N to Drop the Lowest Grade! {sDropGrade} is not valid!")#Exi program and display message.

#Use average score to get letter grade with the correct marking depending on the number and assign it to variable
if fScoreAverage < 60:
    cLetterGrade = "F"
elif fScoreAverage < 70: #Check is grade is lower than grade number
    if fScoreAverage < 64: #Check is grade is lower then - threshold
        cLetterGrade = "D -"
    elif fScoreAverage < 67: #Check if grade is lower than middle threshold
        cLetterGrade = "D"
    else: #If grade is higher than last two thresholds, apply + marking
        cLetterGrade = "D +"
elif fScoreAverage < 80:
    if fScoreAverage < 74:
        cLetterGrade = "C -"
    elif fScoreAverage < 77:
        cLetterGrade = "C"
    else:
        cLetterGrade = "C +"
elif fScoreAverage < 90:
    if fScoreAverage < 84:
        cLetterGrade = "B -"
    elif fScoreAverage < 87:
        cLetterGrade = "B"
    else:
        cLetterGrade = "B +"
elif fScoreAverage < 100:
    if fScoreAverage < 94:
        cLetterGrade = "A -"
    elif fScoreAverage < 97:
        cLetterGrade = "A"
    else:
        cLetterGrade = "A +"

print(f"{sStudentName}'s test average is:   {fScoreAverage:.1f}")#Display message with student name and average score formatted to one decimal point
print(f"Letter Grade for the test is:   {cLetterGrade}") #Print message with letter grade.