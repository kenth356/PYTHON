class bank_account:
    def __init__(self, balance):
        self.balance = balance
        
    def actions(self, choice, amount):
        if choice.lower() == "deposit":
            self.balance += amount
            print(f"\nAMOUNT DEPOSITED --{amount}--")
            print(f"\nNEW BALANCE: {self.balance}")
        elif choice.lower() == "withdraw":
            if amount <= self.balance:
                self.balance -= amount
                print(f"\nAMOUNT WITHDRAWED --{amount}--")
                print(f"\nNEW BALANCE: {self.balance}")
            else:
                for i in range(1, 4):
                    print("\n[INSUFFICIENT FUNDS]")
        else:
            for i in range(1, 4):
                print("]\n[PLEASE ENTER A VALID INPUT]")


def main():
    account = bank_account(1000)
    print("\n[WELCOME TO BDO]")
    print("\nWHAT KIND OF ACTION DO YOU WANT TO DO IN YOUR ACCOUNT?")
    choice = input("Enter: ")
    amount = float(input("\nEnter amount: "))
    account.actions(choice, amount)

if __name__ == "__main__":
    main()