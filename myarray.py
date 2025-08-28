class my_array:
    def __init__(self, array):
        self.array = array

arrayHANDLING = []

def main():
    while True:
        print("\nWhat kind of action do you want to do in your array?")
        print("1. -- Input")
        print("2. -- Print")
        print("3. -- Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            for i in range(3):
                print("\n[ENTER A VALID INPUT]")
        
        match choice:
            case 1:
                inputARRAY()
            case 2:
                printARRAY()
            case 3:
                exitARRAY()
                return
            case _:
                print("\n[THANK YOU FOR USING THIS PROGRAM]")

def inputARRAY():
    print("\nDo you want to enter a value for your array?")
    choice = input("Enter: ")
    
    while choice.lower() == "yes":
        value = int(input("\nEnter value for the array: "))
        new_value = my_array(value)
        arrayHANDLING.append(new_value)
        print("\nDo you want to enter another value for your array?")
        choice = input("Enter: ")

def printARRAY():
    while True:
        print("\nin what way do you want to print your array?")
        print("1. -- one by one")
        print("2. -- complete array")
        print("3. -- reversed one by one")
        print("4. -- reversed complete array")
        print("5. -- return to menu")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("\n[ENTER A VALID INPUT]")

        if choice == 1:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                for value in arrayHANDLING:
                    print(f"\n{value.array}")
        if choice == 2:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                complete_array = [value.array for value in arrayHANDLING]
                print(f"\n{complete_array}")
        if choice == 3:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                for value in reversed(arrayHANDLING):
                    print(f"\n{value.array}")
        if choice == 4:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                complete_set = [value.array for value in reversed(arrayHANDLING)]
                print(f"\n{complete_set}")
        if choice == 5:
            break

def exitARRAY():
    for i in range(3):
        print("\n[THANK YOU]")

if __name__ == "__main__":
    main()