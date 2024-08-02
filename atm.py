class ATM:
    def __init__(self):
        # Dictionary to store user information
        self.users = {
            "suresh": {"password": "8118", "balance": 1000},
            "manoj": {"password": "9750", "balance": 500},
          "rani": {"password": "8338", "balance": 105000},
            "vengat": {"password": "3132", "balance": 59000},
        }
        self.current_user = None

    def authenticate(self):
        user_id = input("Enter your user ID: ")
        password = input("Enter your password: ")

        if user_id in self.users and self.users[user_id]["password"] == password:
            self.current_user = user_id
            print("Authentication successful.")
            return True
        else:
            print("Invalid user ID or password.")
            return False
    def check_balance(self):
        if self.current_user:
            balance = self.users[self.current_user]["balance"]
            print(f"Your current balance is: ${balance:.2f}")
        else:
            print("You need to authenticate first.")
    def deposit(self):
        if self.current_user:
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    self.users[self.current_user]["balance"] += amount
                    print(f"Deposited ${amount:.2f}. New balance is ${self.users[self.current_user]['balance']:.2f}.")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print("You need to authenticate first.")

    def withdraw(self):
        if self.current_user:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if amount <= self.users[self.current_user]["balance"]:
                        self.users[self.current_user]["balance"] -= amount
                        print(f"Withdrew ${amount:.2f}. New balance is ${self.users[self.current_user]['balance']:.2f}.")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print("You need to authenticate first.")
    def main_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose again.")
def main():
    atm = ATM()
    if atm.authenticate():
        atm.main_menu()
    else:
        print("Authentication failed. Exiting...")
if __name__ == "__main__":
    main()
