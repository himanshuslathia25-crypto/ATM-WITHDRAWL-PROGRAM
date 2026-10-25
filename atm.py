# ATM Withdrawal Program
# Python Mini Project

balance = 10000
correct_pin = 1234


def check_balance():
    print("\n--------------------------------")
    print("Current Balance: ₹", balance)
    print("--------------------------------")


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print("Withdrawal successful.")
            print("Amount withdrawn: ₹", amount)
            print("Remaining balance: ₹", balance)

    except ValueError:
        print("Invalid input. Please enter a number.")


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Please enter a valid amount.")

        else:
            balance += amount
            print("Deposit successful.")
            print("Amount deposited: ₹", amount)
            print("Updated balance: ₹", balance)

    except ValueError:
        print("Invalid input. Please enter a number.")


# PIN Authentication

print("================================")
print("       WELCOME TO ATM")
print("================================")

try:
    entered_pin = int(input("Enter your 4-digit PIN: "))

    if entered_pin == correct_pin:

        print("\nLogin successful!")

        while True:

            print("\n================================")
            print("          ATM MENU")
            print("================================")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
            print("================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    check_balance()

                elif choice == 2:
                    withdraw()

                elif choice == 3:
                    deposit()

                elif choice == 4:
                    print("\nThank you for using the ATM.")
                    print("Please visit again!")
                    break

                else:
                    print("Invalid choice. Please select 1-4.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    else:
        print("Incorrect PIN. Access denied.")

except ValueError:
    print("Invalid PIN. Please enter numbers only.")
