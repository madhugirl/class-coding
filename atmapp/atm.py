import sys
import fire
import questionary



from utils import load_accounts

from utils import validate_pin
    
from action.make_deposit import make_deposit
from action.make_withdrawal import make_withdrawal

def login():
    # prompt user to enter their pin
    pin = questionary.text("Enter PIN:").ask()

    # validate the pin provided
    if not validate_pin(pin):
        sys.exit("PIN not valid")


    # if pin validates, load the accounts
    accounts = load_accounts()

    # find the specific account based on the pin provided
    for account in accounts:
        if int(pin) == account["pin"]:
            return account


    # if there's a problem, exit the app
    sys.exit("Login was not successful.  Check your PIN and try again.")

#questionary has all these functions inside it and you must study it
def main_menu():
    action = questionary.select(
        "Do you want to check your balance, mnake a deposit, or make a withdrawal?",
        choices=["check balance", "deposit", "withdrawal", "done"]
    ).ask()

    return action
#def run function runs function login 

#def run():
    # login and if the pin is valid, return validated account
account = login()
    # show main menu where you can take action like check balance, deposit or withdrawal
action = main_menu()

# while loop to run throuh list to run all the fucntions != is not equal
while action != "done":

    # do the action selecetd like check balance
    if action == "check balance":
         print(f"Current account balance is {account['balance']: .2f}")
         action = main_menu()
         if action == "done":
          sys.exit("Have a great day, please spend your money with us again")

    #or make the deposit
    elif action == "deposit":
        account = make_deposit(account)
        action = main_menu()
        if action == "done":
         sys.exit("Have a great day, please spend your money with us again")

    # or make the withdrawal
    else:
        account = make_withdrawal(account)
        action = main_menu()
        if action == "done":
         sys.exit("Have a great day, please spend your money with us again")
    
    if action == "done":
        sys.exit("Have a great day, please spend your money with us again")



if __name__ == "__main__":
    fire.Fire()

