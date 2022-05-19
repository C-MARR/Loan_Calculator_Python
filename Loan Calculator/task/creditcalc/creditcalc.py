import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
option = input()
if option == "n":
    principal = int(input("Enter the loan principal: \n"))
    monthly_payment = int(input("Enter the monthly payment: \n"))
    interest = float(input("Enter the loan interest: \n")) / 100
    nominal_rate = interest / 12
    months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_rate * principal), nominal_rate + 1))
    years = months // 12
    print(f"It will take {years} years "
          + (f"and {months - (years * 12)} months" if months % 12 != 0 else "")
          + " to repay this loan!")
elif option == "a":
    principal = int(input("Enter the loan principal: \n"))
    number_of_periods = int(input("Enter the number of periods: \n"))
    interest = float(input("Enter the loan interest: \n")) / (12 * 100)
    monthly_payment = principal \
                      * (interest
                         * (1 + interest) ** number_of_periods) / ((1 + interest) ** number_of_periods - 1)
    print(f"Your monthly payment = {math.ceil(monthly_payment)}!")
elif option == "p":
    annuity_payment = float(input("Enter the annuity payment: \n"))
    number_of_periods = int(input("Enter the number of periods: \n"))
    interest = float(input("Enter the loan interest: \n")) / (12 * 100)
    principal = annuity_payment \
                / ((interest * (1 + interest) ** number_of_periods)
                   / ((1 + interest) ** number_of_periods - 1))
    print(f"Your loan principal = {math.floor(principal)}!")
