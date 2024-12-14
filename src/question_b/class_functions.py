#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self._symbol = symbol
        self._company_name = company_name

    def __str__(self):
        return f"{self._company_name} {self._symbol}"

    def get_symbol(self):
        return self._symbol
    
    def get_company_name(self):
        return self._company_name
    
def stock_purchase_history():
    
    stock_dictionary = {}

    with open(r"/workspaces/final-elijahnacc/src/stock_file.dat", "r") as stock_data:
        for line in stock_data:
            stripped_line = line.rstrip()
            stock = stripped_line.split(" ", 1)
            stock_dictionary[stock[0]] = stock[1]
        print("\nSymbol | Company Name")
        for symbol, name in stock_dictionary.items():
            print(f"{symbol}:     {name}")