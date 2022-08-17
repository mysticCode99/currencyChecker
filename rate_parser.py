import urllib.request
import re, json
from pprint import pprint

RATE_AM_BANKS_LINK = 'https://rate.am'
RATE_AM_EXCHANGES_LINK = 'http://rate.am/am/armenian-dram-exchange-rates/exchange-points/cash'

class Bank:
    def __init__(self) -> None:
        self.name = ''
        self.cont_page_link = ''
        self.link = ''
        self.rates = []

def parse_rate_page():
    '''
    Parses http://rate.am/ page
    Collects and writes table in txt format file
    '''
    req = urllib.request.Request(RATE_AM_BANKS_LINK, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    tr_reg_res = re.findall(r'<tr\s*id\s*=\s*[^>]*>(.*?)</tr>', str(html))
    banks = []
    for tr in tr_reg_res:
        bank_name = re.search(r'<img.*?alt\s*=\s*[\'"\\]*([^\'"\\]*)', tr).group(1)
        read_link_reg = r'''.*<a.*?href\s*=\s*(?:\\'|\\")(.*?)(?:\\'|\\").*?>'''
        read_link_reg = r'.*<a.*?href\s*=\s*[\'"\\]*([^\'"\\]*)'
        cont_link = re.search(read_link_reg, tr).group(1)
        res = re.findall(r'<td>.*?([\d\.]+).*?<\/td>', tr)
#         print(f'''{bank_name} --- {RATE_AM_BANKS_LINK + cont_link}
# {res[3]:<8}{res[4]:<8}{res[5]:<8}{res[6]:<8}{res[7]:<8}{res[8]:<8}''')
        banks.append(Bank())
        banks[-1].name = bank_name
        banks[-1].cont_page_link = RATE_AM_BANKS_LINK + cont_link
        banks[-1].rates = res
    
    for bank in banks:
        parse_bank_cont_page(bank)
        parse_bank_page(bank)
        print()

def parse_bank_page(bank):
    req = urllib.request.Request(RATE_AM_BANKS_LINK, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    exchange_table_reg = r'''<\s*table.*?class\s*=\s*["'].*?exchange__table.*?["']\S*?>([\S\s]*?)<\s*\/table\s*>'''
    exchange_table_reg = r'''(<\s*table.*?class\s*=\s*["'].*?exchange.*?>([\S\s]*?)<\s*\/table\s*>)'''
    res = re.search(exchange_table_reg, str(html))
    if res:
        print(bank.name, res)
        print(res.group())

def parse_bank_cont_page(bank):
    '''
    Parses rate.am banks contact page
    '''
    req = urllib.request.Request(bank.cont_page_link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    data_table_regex = r'''<\s*table.*class="bankpagebankcontact">([\S\s]*?)<\/table>'''
    data_table = re.search(data_table_regex, str(html)).group(1)
    with open('res', 'w') as o:
        o.write(data_table)
    # print(data_table)
    read_link_reg = r'.*<a.*?href\s*=\s*[\'"\\]*([^\'"\\]*)'
    link = re.search(read_link_reg, data_table).group(1)
    print(f'''{bank.name} --- {bank.cont_page_link}
{link}''')
    del html
    bank.link = link

def main():
    ''' Collects and writes table in txt format file'''
    parse_rate_page()

if __name__ == '__main__':
    main()