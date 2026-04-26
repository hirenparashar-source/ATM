

balance = 5000  
transactions = []  


def display_balance():
    print(f"\n  Your Current Balance : Rs. {balance}")


def deposit(amount):
    global balance
    if amount <= 0:
        print("\n  [ERROR] Amount must be greater than 0.")
        return
    balance += amount
    transactions.append(f"Deposited  : Rs. {amount:.2f}  |  Balance after: Rs. {balance:.2f}")
    print(f"\n  Rs. {amount:.2f} deposited successfully!")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("\n  [ERROR] Amount must be greater than 0.")
        return
    if amount > balance:
        print("\n  [ERROR] Insufficient balance!")
        return
    balance -= amount
    transactions.append(f"Withdrawn  : Rs. {amount:.2f}  |  Balance after: Rs. {balance:.2f}")
    print(f"\n  Rs. {amount:.2f} withdrawn successfully!")


def show_statement():
    print("\n  ========== Transaction Statement ==========")
    if not transactions:
        print("  No transactions found.")
    else:
        for i, record in enumerate(transactions, start=1):
            print(f"  {i}. {record}")
    print(f"\n  Current Balance : Rs. {balance:.2f}")
    print("  ===========================================")
