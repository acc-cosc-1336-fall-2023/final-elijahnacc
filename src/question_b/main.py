from class_functions import stock_purchase_history

def main():
    selection = 0

    while True:
        print("\nMenu\n1 - Display Stock Purchase History\n2 - Exit")
        selection = int(input("Please Enter Selection: "))

        if selection == 2:
            exit()
        if selection == 1:
            stock_purchase_history()

if __name__ == "__main__":
    main()