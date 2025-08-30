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
            choice = -1
        
        match choice:
            case 1:
                inputARRAY()
            case 2:
                printARRAY()
            case 3:
                exitARRAY()
                return
            case _:
                print("\n[ENTER A VALID INPUT]")

def inputARRAY():
    while True:
        print("\nwhat data type do you want for inputing values to your array?")
        print("1. -- Integer")
        print("2. -- String")
        print("3. -- Float")
        print("4. -- return to menu")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            choice = -1
        match choice:
            case 1:
                inputINT()
            case 2:
                inputSTR()
            case 3:
                inputFLOAT()
            case 4:
                break
            case _:
                print("\n[ENTER A VALID INPUT]")

def inputINT():
    value = int(input("\nEnter integer value: "))
    listed_value = my_array(value)
    arrayHANDLING.append(listed_value)

def inputSTR():
    value = input("\nEnter string value: ")
    listed_value = my_array(value)
    arrayHANDLING.append(listed_value)

def inputFLOAT():
    value = float(input("\nEnter float value: "))
    listed_value = my_array(value)
    arrayHANDLING.append(listed_value)

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
            choice = -1

        if choice == 1:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                for values in arrayHANDLING:
                    print(f"\n{values.array}")
        elif choice == 2:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                complete_array = [values.array for values in arrayHANDLING]
                print(f"\n{complete_array}")
        elif choice == 3:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                for values in reversed(arrayHANDLING):
                    print(f"\n{values.array}")
        elif choice == 4:
            if not arrayHANDLING:
                print("\n[LIST IS EMPTY]")
            else:
                complete_set = [values.array for values in reversed(arrayHANDLING)]
                print(f"\n{complete_set}")
        elif choice == 5:
            break
        else:
            print("\n[ENTER A VALID INPUT]")

def exitARRAY():
    for i in range(3):
        print("\n[THANK YOU]")

if __name__ == "__main__":
    main()