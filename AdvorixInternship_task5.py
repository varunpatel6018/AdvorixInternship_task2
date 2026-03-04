import json
import os

DATA_FILE = "accounts.json"


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. Balance: ${self.balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: ${self.balance}"
        return "Insufficient funds"

    def apply_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        return f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}"


# ✅ Load data from file
def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            accounts = {}
            for name, balance in data.items():
                accounts[name] = Account(name, balance)
            return accounts
    return {}


# ✅ Save data to file
def save_accounts(accounts):
    data = {}
    for name, acc in accounts.items():
        data[name] = acc.balance

    with open(DATA_FILE, "w") as file:
        json.dump(data, file)


accounts = load_accounts()

while True:
    print("\n====== BANK MENU ======")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Apply Interest")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account holder name: ")

        if name in accounts:
            print("Account already exists!")
        else:
            balance = float(input("Enter opening balance: "))
            accounts[name] = Account(name, balance)
            save_accounts(accounts)
            print("Account created successfully!")

    elif choice == "2":
        if not accounts:
            print("No accounts available.")
        else:
            print("\n--- Account Records ---")
            for acc in accounts.values():
                print(f"Account owner: {acc.owner}")
                print(f"Account balance: ${acc.balance}")
                print("------------------------")

    elif choice == "3":
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = float(input("Enter amount to deposit: "))
            print(accounts[name].deposit(amount))
            save_accounts(accounts)
        else:
            print("Account not found.")

    elif choice == "4":
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = float(input("Enter amount to withdraw: "))
            print(accounts[name].withdraw(amount))
            save_accounts(accounts)
        else:
            print("Account not found.")

    elif choice == "5":
        name = input("Enter account holder name: ")
        if name in accounts:
            rate = float(input("Enter interest rate (%): "))
            print(accounts[name].apply_interest(rate))
            save_accounts(accounts)
        else:
            print("Account not found.")

    elif choice == "6":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice. Try again.")