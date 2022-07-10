
import urllib.request
import re, json
from pprint import pprint

from bank_parsers import Bank

def collect_banks():
    '''Collects Bamks information and returns banks object list'''
    with open('bank_list.json', 'r') as f:
        banks_data = json.load(f)
    # pprint(banks_data)
    banks = []
    for bank_data in banks_data['banks']:
        bank = Bank(bank_data["name"])
        bank.set_data(bank_data)
        banks.append(bank)
        print(bank)
        bank.parse_page()

def parse_rate_page():
    '''
    Parses http://rate.am/ page
    Collects and writes table in txt format file
    '''
    home_page_link = 'https://rate.am'
    exchanges_table_link = 'http://rate.am/am/armenian-dram-exchange-rates/exchange-points/cash'
    req = urllib.request.Request(home_page_link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    tr_reg_res = re.findall(r'<tr\s*id\s*=\s*[^>]*>(.*?)</tr>', str(html))
    with open('pageInfo', 'w') as f:
        start_str = '+' + '-' * 79
        print(start_str)
        f.write(start_str + "\n")
        for tr in tr_reg_res:
            res = re.search(r'<img.*?alt\s*=\s*[\'"\\]*([^\'"\\]*)', tr)
            bank_name = res.group(1)
            del res
            res = re.findall(r'<td>.*?([\d\.]+).*?<\/td>', tr)
            if res:
                res_str = '|{:^25}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|'.format(
                    bank_name, res[3], res[4], res[5], res[6], res[7], res[8]
                )
                print(res_str)
                f.write(res_str + "\n")
        print(start_str)
        f.write(start_str + "\n")

def main():
    ''' Collects and writes table in txt format file'''
    # parse_rate_page()
    collect_banks()

if __name__ == '__main__':
    main()