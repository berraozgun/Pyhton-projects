
print ("Welcome! You have $100 in your account.")
def withdraw_money(current_balance, amount):
    
    if (current_balance >= amount):
        current_balance = current_balance - amount
        print ("Your current balance is", current_balance)
   
    else:
        print ("Error. You do not have that much money in your account")
    
amount=int(input ("How much do you want to withdraw? "))

withdraw_money (100, amount)
    