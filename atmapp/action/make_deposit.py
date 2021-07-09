import sys
import questionary

def make_deposit(account):
    amount = questionary.text("How much would you like to deposit?").ask()
    amount = float(amount)

    if amount > 0.0:
        account["balance"] = account["balance"] + amount
        print("Deposit was successful")
        return(account)

    else:
        sys.exit("Not a valid depsosit amount.  Try again")
