
from bank_parsers import bank_parsers

class Bank(object):
    def __init__(self, name=None) -> None:
        self.name = name
        self.link = ''
        self.currences = {}

    def __str__(self) -> str:
        return self.name

    def set_link(self, link, parser):
        '''Setup bank page link'''
        self.link = link
        self.page_parser = parser

    def set_data(self, data):
        '''Setup bank page link'''
        self.name = data["name"]
        self.link = data["link"]
        self.page_parser = getattr(bank_parsers, data["parser"])

    def set_currence(self, currence, values=()):
        '''Adding currence value to currences dict'''
        self.currences[currence] = values

    def get_currence_sell_value(self, currence):
        ''''''
        return self.currences[currence][0]

    def get_currence_buy_value(self, currence):
        ''''''
        return self.currences[currence][1]
    
    def get_currence(self, currence):
        '''Return all values for required currence'''
        if self.currences.get(currence):
            return self.currences[currence]
        else:
            return None

    def parse_page(self):
        '''
        Parses Bank's home page 
        where defined current currency
        '''
        if not self.page_parser:
            print("Warning : Parser doesn't exist")
            return
        print(self.page_parser)
        self.page_parser(self.link)
        pass