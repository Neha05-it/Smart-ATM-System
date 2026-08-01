print("==================")
print("   SMART ATM SYSTEM  ")
print("===================")

correct_pin = 1234
balance = 5000

pin = int(input("Enter your 4-digit PIN: "))
if pin == correct_pin:
    print("\nLogin Successful!")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("Your Balance is Rs.", balance)

    elif choice  == 2:
        print = float(input("Enter amount to deposit: Rs."))
        balance = balance = amount
        print("Money Deposited Successfully!")
        print("Updated Balance: Rs.",balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: Rs."))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Remaining Balance: Rs.", balance)
        else:
            print("Insufficient Balance!")
    elif choice == 4:
        print("Thank you for using Smart ATM!")

    else:
        print("Invalid Choice!")

else:
    print("Incorrect PIN! Access Denied")
