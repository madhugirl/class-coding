import sys
import questionary

def make_withdrawal(account):
    amount = questionary.text("How much would you like to withdrawal?").ask()
    amount = float(amount)

    if amount <= 0.0:
       sys.exit("Not a valid withdrawal amount.  Try again")

    if amount <= account ["balance"]:
        account["balance"] = account["balance"] - amount
        print("Withdrawal was successful")
        return(account)

    else:
        sys.exit("Insufficent funds.")
