from pathlib import Path
import csv
import sys

def load_accounts():
    accounts = []
    csv_path = Path("./data/accounts.csv")

    with open(csv_path, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)

        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)

        return accounts


def validate_pin(pin):
    if len(pin) == 6:
       print("PIN is valid")
       return True
    else:
        return False


