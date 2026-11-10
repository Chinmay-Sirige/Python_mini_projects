def show_balance(balance):
    print("****************************")
    print(f"Your current balance is {balance:.2f} rupees.")

def deposit():
    print("****************************")
    amount = float(input("Enter amount to deposited: "))

    if amount < 0:
        print("Sorry! That's not a valid amount to deposit.")
        return 0
    else:
        return amount

def withdraw(balance):
    print("****************************")
    amount = float(input("Enter amount to withdrawn: "))

    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************************")
        print("      Banking program.      ")
        print("****************************")
        print("1.Show Balance.")
        print("2.Deposit.")
        print("3.Withdraw.")
        print("4.Exit")
        print("**********************************")
        choice = input("Enter your choice (1-4): ")
        print("**********************************")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************")
            print("That is not a valid choice.")
            print("***************************")

    print("***************************")
    print("Thank you! Have a nice day!")
    print("***************************")

if __name__ == "__main__":
    main()