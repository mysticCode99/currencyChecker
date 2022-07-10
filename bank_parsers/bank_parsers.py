
from urllib import request
import re

from . import HEADER_DICT

def id_bank_parser(link):
    ''''''
    r = request.Request(link, headers=HEADER_DICT)
    r_res = request.urlopen(r)
    if r_res.getcode() != 200:
        print("Code is", r_res.getcode())
        return
    print("Start of Parsing", r_res.getcode())
    print('Bank link is', r_res.geturl())
    html = str(r_res.read())
    html = html.replace('\\n', '\n')
    html = html.replace('\\t', '\t')
    with open('id_bank.html', 'w') as html_file:
        html_file.write(html)