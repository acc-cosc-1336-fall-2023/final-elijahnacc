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
    
def get_stock_list():
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")
    return [stock1, stock2, stock3, stock4, stock5]