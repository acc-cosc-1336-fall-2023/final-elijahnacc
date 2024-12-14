#write functions here, don't add input('') statements here!
def create_multiplication_table():
    table = [[] for i in range(5)]
    for m in range(5):
        for n in range(10):
            product = (m+1) * (n+1)
            table[m].append(product)
    return table

def display_multiplication_table(table):
    for m in range(5):
        row = ""
        for n in range(10):
            row = row + f"{table[m][n]} "
        print(row)