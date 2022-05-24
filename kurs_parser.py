
import urllib.request
import re

req = urllib.request.Request('https://rate.am', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()

class Bank(object):
    def __init__(self, name) -> None:
        self.name = name
        self.currences = {}

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

def collect_banks():
    '''Collects Bamks information and returns banks object list'''
    banks = []
    tr_reg_res = re.findall(r'<tr\s*id\s*=\s*[^>]*>(.*?)</tr>', str(html))
    for tr in tr_reg_res:
        res = re.search(r'<img.*?alt\s*=\s*[\'"\\]*([^\'"\\]*)', tr)
        bank = Bank(res.group(1))
        del res
        res = re.findall(r'<td>.*?([\d\.]+).*?<\/td>', tr)
        if res:
            bank.set_currence('usd', (res[3], res[4]))
            bank.set_currence('eur', (res[5], res[6]))
            bank.set_currence('rub', (res[7], res[8]))
        banks.append(bank)
    return banks

def main():
    ''' Collects and writes table in txt format file'''
    tr_reg_res = re.findall(r'<tr\s*id\s*=\s*[^>]*>(.*?)</tr>', str(html))
    with open('pageInfo', 'w') as f:
        f.write('+' + '-' * 79 + '+\n')
        for tr in tr_reg_res:
            res = re.search(r'<img.*?alt\s*=\s*[\'"\\]*([^\'"\\]*)', tr)
            bank_name = res.group(1)
            del res
            res = re.findall(r'<td>.*?([\d\.]+).*?<\/td>', tr)
            if res:
                f.write(f'|{bank_name:^25}|{res[3]:^8}|{res[4]:^8}|{res[5]:^8}|{res[6]:^8}|{res[7]:^8}|{res[8]:^8}|\n')
        f.write('+' + '-' * 79 + '+')

if __name__ == '__main__':
    main()