def main():
    print("\n===========================")
    print("    Warehouse Inventory    ")
    print("===========================")
    print("Item        item       item")
    print("Code      Description   Qty")

    with open("table.dat", "r") as dataIn:
        for _ in range(5):
            line = dataIn.readline()
            if not line:
                break
            code, description, quantity = line.split()
            print(f"\n{code:<11}{description:<12}{quantity:>4}")


if __name__ == "__main__":
    main()