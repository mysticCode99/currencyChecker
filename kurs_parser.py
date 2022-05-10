
import urllib.request
import re

req = urllib.request.Request('https://rate.am', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()

class Bank(object):
    def __init__(self, name) -> None:
        self.name = name
        currences = {}

    def set_currence(self, currence, values):
        '''Adding currence value to currences dict'''
        # if not currence:
        #     print("ERROR: Currence didn't defined")
        #     return
        self.currences[currence] = values

    def get_currence_sell_value(self, currence):
        ''''''
        return self.currences[currence][0]

    def get_currence_buy_value(self, currence):
        ''''''
        return self.currences[currence][1]

tr_reg_res = re.findall(r'<tr\s*id\s*=\s*[^>]*>(.*?)</tr>', str(html))
with open('pageInfo', 'w') as f:
    f.write('+' + '-' * 79 + '+\n')
    # f.write(f'|{"Bank":^25}|{"":^53}|\n')
    for tr in tr_reg_res:
        res = re.search(r'<img.*?alt\s*=\s*[\'"\\]*([^\'"\\]*)', tr)
        bank_name = res.group(1)
        del res
        res = re.findall(r'<td>.*?([\d\.]+).*?<\/td>', tr)
        if res:
            # print(bank_name, res[3:11])
            f.write(f'|{bank_name:^25}|{res[3]:^8}|{res[4]:^8}|{res[5]:^8}|{res[6]:^8}|{res[7]:^8}|{res[8]:^8}|\n')
        # f.write(tr.replace('\\n', '\n'))
        # f.write('\n')
    f.write('+' + '-' * 79 + '+')