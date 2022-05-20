import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates payments.")

parser.add_argument("-t", "--type", choices=["diff", "annuity"],
                    help='Choices are "diff" and "annuity".')
parser.add_argument("-pr", "--principal",
                    help="Input the principal total of the loan.")
parser.add_argument("-per", "--periods",
                    help="Input number of periods.")
parser.add_argument("-pay", "--payment",
                    help="Input monthly payment amount.")
parser.add_argument("-i", "--interest",
                    help="Input interest percentage.")
args = parser.parse_args()


def differential_payment(loan_principal, number_of_payments, nominal, current_month):
    return (loan_principal / number_of_payments) + nominal * (
            loan_principal - ((loan_principal * (current_month - 1)) / number_of_payments))


if args.type == "annuity" and args.interest:
    interest = float(args.interest) / 100
    nominal_rate = interest / 12
    if args.payment and args.principal:
        payment = float(args.payment)
        principal = float(args.principal)
        months = math.ceil(math.log(payment / (payment - nominal_rate * principal), nominal_rate + 1))
        years = months // 12
        print(f"It will take {years} years"
              + (f" and {months - (years * 12)} months" if months % 12 != 0 else "")
              + " to repay this loan!" + (f"\nOverpayment = {math.ceil(months * payment - principal)}"
                                          if math.ceil(months * payment) > principal else ""))
    elif args.periods and args.principal:
        principal = float(args.principal)
        number_of_periods = int(args.periods)
        monthly_payment = principal \
                          * (nominal_rate
                             * (1 + nominal_rate) ** number_of_periods) / ((1 + nominal_rate) ** number_of_periods - 1)
        print(f"Your annuity payment = {math.ceil(monthly_payment)}!"
              + (f"\nOverpayment = {math.ceil(math.ceil(monthly_payment) * number_of_periods - principal)}"
                 if principal < monthly_payment * number_of_periods else ""))
    elif args.payment and args.periods:
        payment = float(args.payment)
        number_of_periods = int(args.periods)
        principal = payment / ((nominal_rate * (1 + nominal_rate)
                                ** number_of_periods) / ((1 + nominal_rate) ** number_of_periods - 1))
        print(f"Your loan principal = {math.floor(principal)}!"
              + (f"\nOverpayment = {math.ceil(payment * number_of_periods - principal)}"
                 if principal < payment * number_of_periods else ""))
    else:
        print("Incorrect parameters")

elif args.type == "diff" and args.interest and args.periods and args.principal and not args.payment:
    interest = float(args.interest) / 100
    nominal_rate = interest / 12
    periods = int(args.periods)
    principal = float(args.principal)
    current_period = 1
    total = 0
    while current_period <= periods:
        payment = math.ceil(differential_payment(principal, periods, nominal_rate, current_period))
        total += payment
        print(f"Month {current_period}: payment is {payment}")
        current_period += 1
    if total > principal:
        print(f"\nOverpayment = {math.ceil(total - principal)}")
else:
    print("Incorrect parameters")
