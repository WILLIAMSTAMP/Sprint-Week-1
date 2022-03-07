import datetime
from datetime import date
import math

# Written by: William Stamp, Chris Pinto and Terrance Power
# Date: 2022-03-02

# NL Chocolate Company Function

# Constants
DAILY_RATE = 85.00
RENT_PER_DAY_RATE = 65.00
BONUS = 100.00
HST_RATE = .15
PER_KM_RATE = .17
EXT_DAYS_BONUS = 100.00
BONUS_KM_RATE = .04
DAILY_BONUS = 45
HOLIDAY_BONUS = 50.00
EXECUTIVE = 45.00
HOLIDAY_START = "2022-12-15"
HOLIDAY_END = "2022-12-22"
global NumDays, TotKmCost, TotKmDsp, Exec_Bonus_Dsp, KmBonusDsp, TotKmCostDsp


# Math Program
def monthly_claims():
    import matplotlib.pyplot as plt
    x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y = []
    for i in range(1):
        tot = print("Monthly Total Claim in $ (Jan-Dec):")
        jan = float(input("January: "))
        feb = float(input("February: "))
        mar = float(input("March: "))
        apr = float(input("April: "))
        may = float(input("May: "))
        jun = float(input("June: "))
        jul = float(input("July: "))
        aug = float(input("August: "))
        sep = float(input("September: "))
        octo = float(input("October: "))
        nov = float(input("November: "))
        dec = float(input("December: "))
        y.append(jan)
        y.append(feb)
        y.append(mar)
        y.append(apr)
        y.append(may)
        y.append(jun)
        y.append(jul)
        y.append(aug)
        y.append(sep)
        y.append(octo)
        y.append(nov)
        y.append(dec)

    plt.title("Monthly Claims Total")
    plt.xlabel("Months (Jan-Dec)")
    plt.ylabel("Monthly Totals ($)")
    plt.grid(True)
    plt.plot(x, y, color='cyan')
    plt.show()
    AnyKey = input("Press Any Key To Continue: ")


# Fun With Strings Code
def FizzBuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 8 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 8 == 0:
            print("Buzz")
        else:
            print(str(i))
    print()
    AnyKey = input("Press AnyKey To Continue: ")


# Chocolate Company Code
# User Inputs
def ChocolateCompany():
    HST = .15
    DeliveryFee = 4.99
    import datetime
    import datetime as datetime
    while True:
        while True:
            allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwqyz-' "
            FirstNam = input("Welcome to the Newfoundland Chocolate Factory, Enter The Employees First Name: ").title()
            if FirstNam == "":
                print("Name Cannot Be Blank - Please Re-Enter")
            elif set(FirstNam).issubset(allowed_char) == False:
                print("Last name contains invalid characters - Please re-enter last name: ")
            else:
                break
        while True:
            allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwqyz-' "
            LastNam = input("Enter the employees last name: ").title()
            if LastNam == "":
                print("Name Cannot Be Blank - Please Re-Enter")
            elif set(LastNam).issubset(allowed_char) == False:
                print("Last name contains invalid characters - Please re-enter last name: ")
            else:
                break
        while True:
            PhoneNum = input("Please enter Employees phone number (10 Digits): ")
            if not PhoneNum.isdigit():
                print("")
            elif len(PhoneNum) != 10:
                print("Cell Phone number must include area code and should be 10 digits - please try again: ")
            else:
                break

        while True:
            try:
                allowed_char = set("1234567890-")
                StartDate = input("Please enter the start date:  (YYYY-MM-DD): ")
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
            except:
                print("Date format is not a valid format - Please re-enter. ")
            else:
                break
        while True:
            try:
                allowed_char = set("1234567890-")
                BirthDate = input("Please enter the Employees Birthdate:  (YYYY-MM-DD): ")
            except:
                print("Date format is not a valid format - Please re-enter. ")
            else:
                break
        # Newfoundland Chocolate Company Menu
        print("      Welcome to NL Chocolate Company - Here Is The Most Updated Menu       ")
        print(" __________________________________________________________________________")
        print("|  141 Torbay Road,                                  Hours - 10AM - 2AM    |")
        print("|     NL A1A 2H1               NL Chocolate          Phone - (709)-420-4200|")
        print("|__________________________________________________________________________|")
        print("|       CAKES                                           SNACKS             |")
        print("|   ______________                                  ______________         |")
        print("|   1. Chocolate           2. Oreo                18. Mini Cake     $3.99  |")
        print("|   Small:  $15.99         Small:  $13.99         19. Muffins       $2.99  |")
        print("|   Medium: $18.99         Medium: $16.99         20. Strawberry    $3.99  |")
        print("|   Large:  $20.99         Large:  $18.99         21. Cookies       $1.99  |")
        print("|                                                 22. Caramel       $4.99  |")
        print("|   3. Supreme             4. Peanut Butter       23. Banana        $2.99  |")
        print("|   Small:  $15.99         Small:  $15.99         24. Whipped Creme $1.00  |")
        print("|   Medium: $18.99         Medium: $16.99         25. Cheesecake    $9.99  |")
        print("|   Large:  $20.99         Large:  $18.99         26. Scones        $3.99  |")
        print("|                                                 27. Brownie       $4.99  |")
        print("|   SANDWICHES                                                             |")
        print("|   __________                                                             |")
        print("|   5. Turkey ----------------------------------  $8.99                    |")
        print("|   6. Chicken ---------------------------------  $7.99                    |")
        print("|   7. Veggie ----------------------------------  $5.99                    |")
        print("|__________________________________________________________________________|")
        print("|   DRINKS                      PRICE             HOT DRINKS               |")
        print("|   _____                       _____             ___________              |")
        print("|   8. Diet Pepsi   355mL       $2.99         15. Hot Chocolate   $2.99    |")
        print("|   9. Mtn Dew      355mL       $2.99         16. Espresso        $4.99    |")
        print("|   10. Fruitopia   355mL       $2.99         17. Brewed Coffee   $2.99    |")
        print("|   11. Root Beer   355mL       $2.99                                      |")
        print("|   12. Diet Pepsi     2L       $4.49                                      |")
        print("|   13. Mountain Dew   2L       $4.99                                      |")
        print("|   14. Root Beer      2L       $4.99                                      |")
        print("|                                                    NL Chocolate Company  |")
        print("|                                                    --------------------  |")
        print("|__________________________________________________________________________|")
        print()
        # Assigning Values to a Variable
        while True:
            Choose = input("Welcome to the Newfoundland Chocolate Factory, Please Choose from our menu: ")
            if Choose == "1":
                Chocolate = Choose
                Size = input("Please Choose a Size (S,M,L): ").upper()
                if Size == "S":
                    Size = "Small"
                    Price = 15.99
                elif Size == "M":
                    Size = "Medium"
                    Price = 18.99
                elif Size == "L":
                    Size = "Large"
                    Price = 20.99
                else:
                    break
            elif Choose == "2":
                Oreo = Choose
                Size = input("Please Choose a Size (S,M,L): ").upper()
                if Size == "S":
                    Size = "Small"
                    Price = 13.99
                elif Size == "M":
                    Size = "Medium"
                    Price = 16.99
                elif Size == "L":
                    Size = "Large"
                    Price = 18.99
                else:
                    break
            elif Choose == "3":
                Supreme = Choose
                Size = input("Please Choose a Size (S,M,L): ").upper()
                if Size == "S":
                    Size = "Small"
                    Price = 15.99
                elif Size == "M":
                    Size = "Medium"
                    Price = 18.99
                elif Size == "L":
                    Size = "Large"
                    Price = 20.99
                else:
                    break
            elif Choose == "4":
                PeanutButter = Choose
                Size = input("Please Choose a Size (S,M,L): ").upper()
                if Size == "S":
                    Size = "Small"
                    Price = 15.99
                elif Size == "M":
                    Size = "Medium"
                    Price = 16.99
                elif Size == "L":
                    Size = "Large"
                    Price = 18.99
                else:
                    break
            elif Choose == "5":
                Turkey = Choose
                Price = 8.99
            elif Choose == "6":
                Chicken = Choose
                Price = 8.99
            elif Choose == "7":
                Veggie = Choose
                Price = 5.99
            elif Choose == "8":
                DietPepsi = Choose
                Price = 2.99
            elif Choose == "9":
                MtDew = Choose
                Price = 2.99
            elif Choose == "10":
                Fruitopia = Choose
                Price = 2.99
            elif Choose == "11":
                RootBeer = Choose
                Price = 2.99
            elif Choose == "12":
                DietPepsi2L = Choose
                Price = 4.99
            elif Choose == "13":
                MtDew2L = Choose
                Price = 4.99
            elif Choose == "14":
                RootBeer2L = Choose
                Price = 4.99
            elif Choose == "15":
                HotChoco = Choose
                Price = 2.99
            elif Choose == "16":
                Expresso = Choose
                Price = 4.99
            elif Choose == "17":
                BrewedCoffee = Choose
                Price = 2.99
            elif Choose == "18":
                MiniCake = Choose
                Price = 3.99
            elif Choose == "19":
                Muffins = Choose
                Price = 2.99
            elif Choose == "20":
                Strawberry = Choose
                Price = 3.99
            elif Choose == "21":
                Cookies = Choose
                Price = 1.99
            elif Choose == "22":
                Caramel = Choose
                Price = 4.99
            elif Choose == "23":
                Banana = Choose
                Price = 2.99
            elif Choose == "24":
                WhippedCreme = Choose
                Price = 1.00
            elif Choose == "25":
                CheeseCake = Choose
                Price = 9.99
            elif Choose == "26":
                Scones = Choose
                Price = 3.99
            elif Choose == "27":
                Brownie = Choose
                Price = 4.99
            else:
                break
            break
        # Calculations
        SubTotal = float(Price) + float(DeliveryFee)
        Tax = (SubTotal * HST)
        TaxDsp = "${:.2f}".format(Tax)
        FirstOptionDsp = "${:.2f}".format(Price)
        Total = (SubTotal + Tax)
        DeliveryFeeDsp = "${:.2f}".format(DeliveryFee)
        TotalDsp = "${:.2f}".format(Total)
        SubTotalDsp = "${:.2f}".format(SubTotal)
        ReceiptDsp = FirstNam[0] + "." + LastNam[0] + "-" + BirthDate[0:4] + "-" + PhoneNum[6:10]
        TrackingNumDsp = PhoneNum[0:3] + "-" + LastNam + "-" + PhoneNum[6:10] + "-" + FirstNam[0:3]
        CurDate = datetime.datetime.today()
        Date = CurDate.strftime("%B-%d-%Y")
        # Print the Receipt
        print()
        print("-----------------------------------------")
        print("            Newfoundland    ")
        print("          Chocolate Company   ")
        print("-----------------------------------------")
        print("Today's Date: ", Date)
        print("Receipt No: ", ReceiptDsp.upper())
        print()
        print("Sold to: ")
        print("    "f"{FirstNam.upper()[0]}.", LastNam.title())
        print("Tracking Number: ", TrackingNumDsp.upper())
        print()
        print("Cost Details")
        print("-----------------------------------------")
        print("Option Price: ", "{:>26}".format(FirstOptionDsp))
        print("Delivery Fee: ", "{:>26}".format(DeliveryFeeDsp))
        print("-----------------------------------------")
        print("HST:", "{:>36}".format(TaxDsp))
        print("SubTotal: {:>31}".format(SubTotalDsp))
        print("Total: {:>34}".format(TotalDsp))
        print("-----------------------------------------")
        print("     Newfoundland Chocolate Company  ")
        print(" 141 Torbay Road, St. John's, NL A1A 2H1 ")
        print("==========================================")
        AnyKey = input("Press AnyKey To Continue: ")
        break

# Main Menu
# Invoice Code
def EmpTravForm():
    global TotKmCost, TotKmDsp, Exec_Bonus_Dsp, KmBonusDsp, TotKmCostDsp
    while True:
        print("                                Travel Claims Program")
        print("----------------------------------------------------------------------------------------")
        print()
        while True:
            # Employee Number
            EmployeeNum = input("Enter your employee number: ")
            if not EmployeeNum.isdigit():
                print("Invalid characters - Please Re-Enter. ")
            elif EmployeeNum == "":
                print("Employee Number cannot be blank - Please re-enter. ")
            elif len(EmployeeNum) != 5:
                print("Employee Number Must Be Five Digits - Please Re-Enter. ")
            else:
                break
        # Employees First Name
        while True:
            allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwqyz-' "
            FirstName = "william"  # input("Enter the employees name: ").title()
            if FirstName == "":
                print("Name Cannot Be Blank - Please Re-Enter. ")
            elif not set(FirstName).issubset(allowed_char):
                print("Last name contains invalid characters - Please re-enter last name: ")
            else:
                break
        # Employees Last Name
        while True:
            allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwqyz-' "
            LastName = "Stamp"  # input("Enter the employees last name: ").title()
            if LastName == "":
                print("Name Cannot Be Blank - Please Re-Enter. ")
            elif not set(LastName).issubset(allowed_char):
                print("Last name contains invalid characters - Please re-enter last name: ")
            else:
                break
        # Travel Location
        while True:
            allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwqyz.-' "
            Location = "St. Johns"  # input("Enter the employees location: ").capitalize()
            if Location == "":
                print("Location Cannot Be Blank - Please Re-enter. ")
            elif not set(Location).issubset(allowed_char):
                print("Customers name cannot contain invalid characters - Please re-enter your name. ")
            else:
                break
        # Start Date
        while True:
            try:
                date_format = "%Y-%m-%d"
                StartDate = input("Enter The Start Date (YYYY-MM-DD): ").upper()
                StartDate = datetime.datetime.strptime(StartDate, date_format)
            except:
                print("Start Date is not a valid format - please re-enter.")
            else:
                break
        while True:
            try:
                date_format = "%Y-%m-%d"
                EndDate = input("Enter the end date (YYYY-MM-DD): ")
                EndDate = datetime.datetime.strptime(EndDate, date_format)
            except:
                print("End Date is not a valid format - please re-enter.")
            else:
                if EndDate < StartDate:
                    print("End Date cannot be before start date - Please re-enter. ")
                elif EndDate > StartDate + datetime.timedelta(days=7):
                    print("End date of trip cannot exceed 7 days from start date")
                else:
                    break
        # Transportation Type
        while True:
            allowed_char = "OoRr"
            Transport_Type = input(
                "Did the employee use their Car own or a rented Vehicle? (O - Own Vehicle, R - Rented): ").upper()
            if not set(Transport_Type).issubset(allowed_char):
                print("Invalid input - Please re-enter  (O - Own Vehicle, R - Rented): ")
            elif Transport_Type == "":
                print("Transportation type cannot be blank - Please try again. ")
            else:
                break
        # Total Kilometers
        if Transport_Type == "O":
            while True:
                try:
                    TotKm = int(input("Enter the total Kilometers traveled rounded to nearest Km. (Max 2000Km): "))
                except:
                    print("Invalid input - Please try again.")
                else:
                    if TotKm > 2000:
                        print("Total kilometers cannot exceed 2000Km. Please re-enter. ")
                    else:
                        break
        # Claim Type
        while True:
            allowed_char = "EeSs"
            ClaimType = input("Enter the Claim Type (S - Standard, E - Executive): ").upper()
            if ClaimType == "":
                print("Claim Type Cannot Be Blank - Please Re-Enter. ")
            elif not set(ClaimType).issubset(allowed_char):
                print("Invalid input. Please enter claim type. ")
            else:
                break
        # Holiday Bonus
        while True:
            Holiday_Bonus = 0
            delta = EndDate - StartDate
            NumDays = delta.days
            if StartDate >= datetime.datetime.strptime(HOLIDAY_START,
                                                       "%Y-%m-%d") and EndDate <= datetime.datetime.strptime(
                HOLIDAY_END, "%Y-%m-%d"):
                Holiday_Bonus = HOLIDAY_BONUS * NumDays
            else:
                break
            break
            # ---------------Calculations for Transportation Type " Owners Vehicle "--------------#
        while True:

            ClaimAmt = 0
            ExtendTripBonus = 0
            KmBonus = 0
            if Transport_Type == "O":
                delta = EndDate - StartDate
                NumDays = delta.days

                if TotKm > 1000:
                    KmBonus = TotKm * BONUS_KM_RATE
                    KmBonusDsp = "${:.2f}".format(KmBonus)

                if NumDays > 3:
                    ExtendTripBonus = EXT_DAYS_BONUS
                Transport_TypeDsp = "Owners vehicle"
                PerDiemAmt = DAILY_RATE * NumDays
                TotBonus = KmBonus + ExtendTripBonus + ClaimAmt + Holiday_Bonus

                if ClaimType == "E":
                    ClaimAmt = EXECUTIVE * NumDays
                    TotBonus = ClaimAmt + ExtendTripBonus + KmBonus + Holiday_Bonus

                TotKmCost = TotKm * PER_KM_RATE
                ClaimAmt = PerDiemAmt + TotBonus + TotKmCost
                Taxes = PerDiemAmt * HST_RATE
                TotClaim = ClaimAmt + Taxes
            # --------------Calculations for  Transportation Type " Rented Vehicle " ---------------#
            elif Transport_Type == "R":
                Transport_TypeDsp = "Rented Vehicle"
                delta = EndDate - StartDate
                NumDays = delta.days
                ClaimAmt = 0
                if ClaimType == "E":
                    Exec_Bonus_Dsp = "${:.2f}".format(EXECUTIVE * NumDays)
                    ClaimAmt = EXECUTIVE * NumDays

                ExtendTripBonus = 0
                if NumDays > 3:
                    ExtendTripBonus = EXT_DAYS_BONUS

                TotBonus = ClaimAmt + ExtendTripBonus + Holiday_Bonus
                PerDiemAmt = RENT_PER_DAY_RATE * NumDays
                ClaimAmt = PerDiemAmt + TotBonus
                Taxes = PerDiemAmt * HST_RATE
                TotClaim = ClaimAmt + Taxes
            else:
                break
            # ------------------------------- DISPLAY -------------------------------------#
            while True:
                Holiday_BonusDsp = "${:.2f}".format(Holiday_Bonus)
                ClaimTypeDsp = "{}".format(ClaimType)
                TaxesDsp = "${:.2f}".format(Taxes)
                PerDiemAmtDsp = "${:.2f}".format(PerDiemAmt)
                ClaimAmtDsp = "${:.2f}".format(ClaimAmt)
                TotClaimDsp = "${:.2f}".format(TotClaim)
                TripBonusDsp = "${:.2f}".format(TotBonus)
                if Transport_Type == "O":
                    TotKmCostDsp = "${:.2f}".format(TotKmCost)

                if ClaimType == "E":
                    ClaimTypeDsp = "Executive"
                    Exec_Bonus_Dsp = "${:.2f}".format(EXECUTIVE * NumDays)
                if NumDays > 3:
                    ExtendTripBonus = "${:.2f}".format(EXT_DAYS_BONUS)
                if ClaimType == "S":
                    ClaimTypeDsp = "Standard"
                if Transport_Type == "O":
                    TotKmDsp = "{}".format(TotKm)
                if Transport_Type == "R":
                    pass
                today = date.today()
                d1 = today.strftime("%b %d, %Y")
                d1Dsp = d1

                # -------------------------------------DISPLAY------------------------------------#
                print()
                print()
                print("         --NL Chocolate Company-- ")
                print("              Travel Claims ")
                print()
                print("Employee Travel Claim         ", d1Dsp)
                print("-------------------------------------------")
                print("Employee Number:", EmployeeNum)
                print("Employee Name:", FirstName, LastName)
                print("Travel Location:", Location)
                print()
                print("Start Date:                  ", StartDate.strftime("%b %d, %Y "))
                print("End Date:                    ", EndDate.strftime("%b %d, %Y "))
                print("Number Of Days: {:>21} {:>1}".format(NumDays, "Days"))
                print()
                print("Claim type: ", "{:>29}".format(ClaimTypeDsp))
                print("Vehicle Status: ", "{:>25}".format(Transport_TypeDsp))
                if Transport_Type == "O":
                    print("Total Km Traveled:", "{:>21}Km".format(TotKmDsp))
                    print("Total Mileage Amount:", "{:>20}".format(TotKmCostDsp))
                    print("------------------------------------------")
                else:
                    print("------------------------------------------")
                if ClaimType == "E":
                    print("Executive Bonus:", "{:>25}".format(Exec_Bonus_Dsp))
                if NumDays < 3:
                    pass
                else:
                    print("Extended Trip Bonus:", "{:>21}".format(ExtendTripBonus))
                if Transport_Type == "O" and TotKm > 1000:
                    print("Extended Travel Bonus: ", "{:>18}".format(KmBonusDsp))
                else:
                    pass
                if StartDate >= datetime.datetime.strptime(HOLIDAY_START,
                                                           "%Y-%m-%d") and EndDate <= datetime.datetime.strptime(
                    HOLIDAY_END, "%Y-%m-%d"):
                    print("Holiday Bonus:", "{:>27}".format(Holiday_BonusDsp))
                    print("------------------------------------------")
                else:
                    pass

                if TotBonus > 0:
                    print("Total Bonus: ", "{:>28}".format(TripBonusDsp))
                else:
                    pass
                print("------------------------------------------")
                print("Per Diem Amount:", "{:>25}".format(PerDiemAmtDsp))
                print("Claim Amount: ", "{:>27}".format(ClaimAmtDsp))
                print("HST", "{:>38}".format(TaxesDsp))
                print("------------------------------------------")
                print("Total Claim: ", "{:>28}".format(TotClaimDsp))
                print()
                print()
                break
            break

        while True:
            allowed_char = "YyNn"
            Cont = input(
                "Would you like to process another claim?  (Y = Yes / N = No: ").capitalize()
            if Cont == "Y":
                if set(Cont).issubset(allowed_char) == False:
                    print("Invalid response - Please re-enter. ")
                print()
                print()
                exit(EmpTravForm())
            else:
                if Cont == "N":
                    if set(Cont).issubset(allowed_char) == False:
                        print("Invalid response - Please re-enter. ")
            break
        break

while True:
    print(" _______________________________________ ")
    print("| NL Chocolate Company - Main Menu      |")
    print("|_______________________________________|")
    print("| 1. Enter an Employee Travel Claim.    |")
    print("|                                       |")
    print("| 2. Fun Interview Question.            |")
    print("|                                       |")
    print("| 3. Cool Stuff With Strings and Dates  |")
    print("|                                       |")
    print("| 4. Graph Monthly Claim Totals.        |")
    print("|                                       |")
    print("| 5. Quit                               |")
    print("|                                       |")
    print("|_______________________________________|")
    allowed_char = "12345"
    Choice = input("   Enter choice (1-5): ")
    if not set(Choice).issubset(allowed_char):
        print("Input is invalid - Please Choose an option between (1-6): ")
    elif Choice == "":
        print("choice cannot be blank - Please re-enter:")
    elif Choice == "1":
        EmpTravForm()
    elif Choice == "2":
        FizzBuzz()
    elif Choice == "3":
        ChocolateCompany()
    elif Choice == "4":
        monthly_claims()
    elif Choice == "5":
        print("Thanks For Using The Employee Travel Claim Menu")

