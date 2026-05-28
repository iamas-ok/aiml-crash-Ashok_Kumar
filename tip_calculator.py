#  print total bill using actual bill amount and tip given
def calculate_tip(bill, tip_percent):
    tip_amount = (bill*tip_percent)/100
    total_bill = bill + tip_amount
    return {'Tip Amount': tip_amount, 'Total Bill': total_bill}


print(calculate_tip(7800, 2))

print(calculate_tip(1000, 15))
print(calculate_tip(4785, 9))
