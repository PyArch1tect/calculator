"""
Age and Basic Calculator.
"""

print("Welcome to \"Basic Calculator\" and \"Age Calculator\".")

calculator_choice = input("Please choose calculator type (Basic\Age)... ").upper().strip()

while True :

    if calculator_choice == "Basic".upper() :
        print("Basic Calculator".center(50,"_"))

        num1 = float(input().strip())
        arthmetic_operator = input().strip()
        num2 = float(input().strip())

        if arthmetic_operator == "+" : #Addition
            Result = num1 + num2
            print(f"{num1} + {num2} = {Result:0.2f}")

        elif arthmetic_operator == "-" : #Substartion
            Result = num1 - num2
            print(f"{num1} - {num2} = {Result}")

        elif arthmetic_operator == "*" : #Multiply
            Result = num1 * num2
            print(f"{num1} * {num2} = {Result}")

        elif arthmetic_operator == "/" : #Subdivision
            Result = num1 / num2
            print(f"{num1} / {num2} = {Result}")

        elif arthmetic_operator == "//" : #Floor division
            Result = num1 // num2
            print(f"{num1} // {num2} = {Result:0.2f}")

        elif arthmetic_operator == "**" : #Exponentiation
            Result = num1 ** num2
            print(f"{num1} ** {num2} = {Result}")

        elif arthmetic_operator == "%" : #Modulus
            Result = num1 % num2
            print(f"{num1} % {num2} = {Result}")

    if calculator_choice == "Age".upper() :
        print("Age Calculator".center(50,"_"))

        Birth_day, Birth_month, Birth_year = map(int,input("Please enter your birth date (dd/mm/yyyy). ").split("/"))
        day, month, year = map(int,input("Please enter current day date (dd/mm/yyyy). ").split("/"))
        
        age_in_years = year - Birth_year
        age_in_monthes = age_in_years * 12
        age_in_days = age_in_years * 365
        age_in_hours = age_in_days * 24
        age_in_minuts = age_in_hours * 60
        age_in_seconds = age_in_minuts * 60
        
        print("you lived for: ")
        print(f"{age_in_years} years.")
        print(f"{age_in_monthes} monthes.")
        print(f"{age_in_days} days.")
        print(f"{age_in_hours} hours.")
        print(f"{age_in_minuts} minuts.")
        print(f"{age_in_seconds} secs.")

    Again = input("Do you want to calculate again? (Yes\\No)...")
    if Again in ["no","NO","n","N"]:
        break
    
    else:
        print("Erorr input")   

        