from class_functions import get_stock_list

def main():
    selection = 0

    while True:
        print("Menu\n1 - Display Stock Purchase History\n2 - Exit")
        selection = int(input("Please enter selection: "))

        if selection == 2:
            exit()
        if selection == 1:
            stock_list = get_stock_list()
            for i in range(len(stock_list)):
                print(stock_list[i])

if __name__ == "__main__":
    main()