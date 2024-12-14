from c_functions import get_most_likely_ancestor_consensus, verify_initial_strand, verify_second_strand, get_amt_of_positions

def main():
    selection = 0

    while True:
        print("\nMenu\n1 - Compare Strands\n2 - Exit")
        selection = int(input("Please enter selection: "))

        if selection == 2:
            exit()
        if selection == 1:
            valid = False
            while True:
                strand1 = str(input("Enter 1st strand (must be 8-16 characters): ")).upper()
                valid = verify_initial_strand(strand1)
                if valid == True:
                    break
            valid = False
            while True:
                strand2 = str(input("Enter 2nd strand (must be 4 characters): ")).upper()
                valid = verify_second_strand(strand2)
                if valid == True:
                    break
            amt_positions = get_amt_of_positions(str(strand1), str(strand2))
            if amt_positions == 0:
                print(f"Substring {strand2} not found in strand {strand1}")
            else:
                print(f"Substring {strand2} is present in strand {strand1} in positions:")
                for pos in get_most_likely_ancestor_consensus(strand1, strand2):
                    print(pos)
                
                
if __name__ == "__main__":
    main()