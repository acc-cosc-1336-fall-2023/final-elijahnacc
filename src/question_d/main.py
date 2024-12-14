from d_functions import create_multiplication_table, display_multiplication_table

def main():
    selection = 0
    while True:
        print("\nMenu\n1 - Display Multiplication Table\n2 - Exit")
        selection = int(input("Please enter selection: "))
        if selection == 2:
            exit()
        if selection == 1:
            table = create_multiplication_table()
            display_multiplication_table(table)

if __name__ == "__main__":
    main()