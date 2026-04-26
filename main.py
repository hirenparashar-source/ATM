

import account  


def main():
    print("\n  ==============================")
    print("       Welcome to the ATM      ")
    print("  ==============================")

    while True:
        print("\n  -------- ATM Menu --------")
        print("  1. Display Balance")
        print("  2. Deposit Money")
        print("  3. Withdraw Money")
        print("  4. View Statement")
        print("  5. Exit")
        print("  --------------------------")
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == '1':
            account.display_balance()

        elif choice == '2':
            try:
                amount = float(input("\n  Enter amount to deposit: Rs. "))
                account.deposit(amount)
            except ValueError:
                print("\n  [ERROR] Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("\n  Enter amount to withdraw: Rs. "))
                account.withdraw(amount)
            except ValueError:
                print("\n  [ERROR] Please enter a valid number.")

        elif choice == '4':
            account.show_statement()

        elif choice == '5':
            print("\n  Thank you for using the ATM. Goodbye!\n")
            break

        else:
            print("\n  [ERROR] Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
