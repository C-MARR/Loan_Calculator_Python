import math

loan_principal = int(input("Enter the loan principal: \n"))
print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
option = input()
if option == "m":
    monthly_payment = int(input("Enter the monthly payment: \n"))
    months = math.ceil(loan_principal / monthly_payment)
    print("It will take " + str(months)
          + (" months to repay the loan" if months != 1 else " month to repay loan"))
elif option == "p":
    months = int(input("Enter the number of months: \n"))
    monthly_payment = math.ceil(loan_principal / months)
    last_payment = loan_principal - ((months - 1) * monthly_payment)
    if last_payment == 0:
        print("Your monthly payment = " + str(monthly_payment))
    else:
        print("Your monthly payment = " + str(monthly_payment)
              + " and the last payment = " + str(math.ceil(last_payment)) + ".")

