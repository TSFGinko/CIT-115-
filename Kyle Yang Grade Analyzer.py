#Kyle Yang
#CIT-115/115L
#Grade Analyzer

sStudentName = input("Name of the person that we are calculating the grades for?:   ")
iTestScoreOne = int(input("Input Grade for Test 1:  "))
iTestScoreTwo = int(input("Input Grade for Test 2:  "))
iTestScoreThree = int(input("Input Grade for Test 3:  "))
iTestScoreFour = int(input("Input Grade for Test 4:  "))

if 0 >= iTestScoreOne or 0 >= iTestScoreTwo or 0 >= iTestScoreThree or 0 >= iTestScoreFour:
    exit("Test scores must bea GREATER than 0!")

sDropGrade = input("Do you wish to Drop the Lowest Grade? Y/N    ")

fScoreAverage = iTestScoreOne + iTestScoreTwo + iTestScoreThree + iTestScoreFour

if sDropGrade == "N" or sDropGrade == "n":
    fScoreAverage /= 4

elif sDropGrade == "Y" or sDropGrade == "y":
    if iTestScoreOne <= iTestScoreTwo and iTestScoreOne <= iTestScoreThree and iTestScoreOne <= iTestScoreFour:
        fScoreAverage -= iTestScoreOne

    elif iTestScoreTwo <= iTestScoreOne and iTestScoreTwo <= iTestScoreThree and iTestScoreTwo <= iTestScoreFour:
        fScoreAverage -= iTestScoreTwo

    elif iTestScoreThree <= iTestScoreOne and iTestScoreThree <= iTestScoreOne and iTestScoreThree <= iTestScoreFour:
        fScoreAverage -= iTestScoreThree

    elif iTestScoreFour <= iTestScoreOne and iTestScoreFour <= iTestScoreTwo and iTestScoreFour <= iTestScoreThree:
        fScoreAverage -= iTestScoreFour
    
    fScoreAverage /= 3
    
else:
    exit(f"You Enter Y or N to Drop the Lowest Grade! {sDropGrade} is not valid!")

if fScoreAverage < 60:
    cLetterGrade = "F"
elif fScoreAverage <= 69.9:
    cLetterGrade = "D"
elif fScoreAverage <= 79.9:
    cLetterGrade = "C"
elif fScoreAverage <= 89.9:
    cLetterGrade = "B"
elif fScoreAverage <= 99.9:
    cLetterGrade = "A"


print(f"{sStudentName}'s test average is:   {fScoreAverage:.1f}")
print(f"Letter Grade for the test is:   {cLetterGrade}")