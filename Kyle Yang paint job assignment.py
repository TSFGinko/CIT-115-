#Kyle Yang
#CIT-115
#Paint Job Estimator
def main():
    #Get user input and assign to variables and use as arguments in getFloatInput function
    fWallSquareFt = getFloatInput(input("Enter wall space in square feet: "))
    fPaintPrice = getFloatInput(input("Enter paint price per gallon:    "))
    fFeetPerGallon = getFloatInput(input("Enter feet per gallon:           "))
    fLaborHours = getFloatInput(input("How many Labor hours per gallon: "))
    fLaborCharge = getFloatInput(input("Labor charge per hour:           "))
    #Use results from getFloatInput and use as arguments in functions to get totals. Then assign them to variables.
    iTotalGallons = getGallonsOfPaint(fWallSquareFt, fFeetPerGallon)
    fLaborHourTotal = getLaborHours(fLaborHours, iTotalGallons)
    fLaborChargeTotal = getLaborCost(fLaborHourTotal, fLaborCharge)
    fPaintChargeTotal = getPaintCost(iTotalGallons, fPaintPrice)
    sSalesTax = getSalesTax(input("State that the job is in:        "), fPaintChargeTotal, fLaborChargeTotal)
    sCustomerLastName = input("Customer Last Name:              ")#Get user input for name and assign to variable

    #Use results and feed into showCostEstimates function 
    showCostEstimates(iTotalGallons, fLaborHourTotal, fLaborChargeTotal, fPaintChargeTotal, sSalesTax, sCustomerLastName)
    

def getFloatInput(val):
    while not isinstance(val, (int, float)):
        try:
            val = float(val)
            if val <= 0:
                val = input("Value needs to be GREATER than 0!: ")
        except ValueError:
            val = input("Value needs to be a NUMBER GREATER than 0!: ")

    return val


def getGallonsOfPaint(fWallSquareFt, fFeetPerGallon):
    iTotal = int(round(fWallSquareFt / fFeetPerGallon))
    return iTotal

def getLaborHours(fLaborHours, iTotalGallons):
    fTotal = round((fLaborHours * iTotalGallons), 2)
    return fTotal

def getLaborCost(fLaborHours, fLaborCharge):
    fTotal = round((fLaborHours * fLaborCharge), 2)
    return fTotal

def getPaintCost(iTotalGallons, fPaintPrice):
    fTotal = round((iTotalGallons * fPaintPrice), 2)
    return fTotal

def getSalesTax(taxstate, fPaintChargeTotal, fLaborChargeTotal):
    try: 
        taxstate = taxstate.upper()
        while True:
            if taxstate == "CT":
                taxrate = 0.06
                break
            elif taxstate == "MA":
                taxrate = 0.0625
                break
            elif taxstate == "ME":
                taxrate = 0.85
                break
            elif taxstate == "NH":
                taxrate = 0.0
                break
            elif taxstate == "RI":
                taxrate = 0.07
                break
            elif taxstate == "VT":
                taxrate = 0.06
                break
            else:
                try:
                    taxstate = input("Enter a valid state!:            ").upper()
                except:
                    taxstate = input("Enter a CT, MA, ME, NH, RI, or, VT:  ")
    except:
        try:
            taxstate = input("Enter a valid state!:            ").upper()
        except:
            taxstate = input("Enter a CT, MA, ME, NH, RI, or, VT:  ")
    
    taxrate *= round((fPaintChargeTotal + fLaborChargeTotal), 2)
    
    return taxrate    
    
def showCostEstimates(iTotalGallons, fLaborHourTotal, fLaborChargeTotal, fPaintChargeTotal, sSalesTax, sCustomerLastName):
    fGrandTotal = round((sSalesTax + fPaintChargeTotal + fLaborChargeTotal), 2)
    sFileOutput = f"Gallons of paint:    {iTotalGallons}\nHours of Labor:      {fLaborHourTotal}\nPaint charges:       {fPaintChargeTotal}\nLabor charges:       {fLaborChargeTotal}\nTax:                 {sSalesTax:.2f}\nTotal cost:          {fGrandTotal}\n"
    file_CustomerEstimate = "output.txt"
    print(sFileOutput)
    with open(file_CustomerEstimate, "w") as file:
        file.write(sFileOutput)
        print("File:    " + sCustomerLastName + "_PaintJobOutput.txt was created.")


main()