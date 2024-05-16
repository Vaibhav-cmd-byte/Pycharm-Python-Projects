import hashlib


class User:
    def __init__(self, account_number, hashed_pin, balance=0):
        self.account_number = account_number
        self.hashed_pin = hashed_pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
            print(f"Deposit of {amount} successfully made.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(f"Withdrawal: -{amount}")
                print(f"Withdrawal of {amount} successfully processed.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def view_statement(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def verify_pin(self, pin):
        hashed_input = hashlib.sha256(pin.encode()).hexdigest()
        return hashed_input == self.hashed_pin


class Bank:
    def __init__(self):
        self.users = {}
        self.admin_pin = hashlib.sha256("1234".encode()).hexdigest()  # Example admin PIN hash

    def create_account(self, account_number, pin):
        if account_number not in self.users:
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
            self.users[account_number] = User(account_number, hashed_pin)
            print("Account created successfully.")
        else:
            print("Account already exists.")

    def login(self, account_number, pin):
        user = self.users.get(account_number)
        if user and user.verify_pin(pin):
            return user
        else:
            print("Invalid account number or PIN.")
            return None

    def admin_login(self, admin_pin):
        hashed_input = hashlib.sha256(admin_pin.encode()).hexdigest()
        return hashed_input == self.admin_pin

    def get_user_accounts(self):
        return self.users.keys()


def user_menu(user):
    while True:
        print("\nUser Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Statement")
        print("4. Change PIN")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "3":
            user.view_statement()
        elif choice == "4":
            new_pin = input("Enter new PIN: ")
            user.pin = new_pin
            print("PIN changed successfully.")
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


def admin_menu(bank):
    while True:
        print("\nAdmin Menu:")
        print("1. View All Accounts")
        print("2. View Transactions")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            accounts = bank.get_user_accounts()
            if accounts:
                print("All User Accounts:")
                for account_number in accounts:
                    print(f"Account Number: {account_number}")
            else:
                print("No user accounts found.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in bank.users:
                user = bank.users[account_number]
                user.view_statement()
            else:
                print("Account not found.")
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank!")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Create Account")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            user = bank.login(account_number, pin)
            if user:
                user_menu(user)
            else:
                print("Login failed. Invalid account number or PIN.")
        elif choice == "2":
            admin_pin = input("Enter admin PIN: ")
            if bank.admin_login(admin_pin):
                admin_menu(bank)
            else:
                print("Invalid admin PIN.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            pin = input("Set your PIN: ")
            bank.create_account(account_number, pin)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
