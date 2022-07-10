
from urllib import request
import re

HEAFER_DICT = {
    'User-Agent': 'Mozilla/5.0'
}

def main():
    r = request.Request(r'https://idbank.am', headers=HEAFER_DICT)
    # print(r.full_url)
    # print(r.type)
    # print(r.host)
    # print(dir(r))
    r_res = request.urlopen(r)
    print(r_res.geturl())
    # print(r_res.info())
    print(r_res.getcode())
    # print(dir(r_res))
    if r_res.getcode() != 200:
        print("Code is", r_res.getcode())
        return
    print("Start of Parsing")
    print(type(r_res))
    # print(type(r_res.read()))
    # html = str(r_res.read())
    # html = html.replace('\\n', '\n')
    # html = html.replace('\\t', '\t')
    # re.search(r'<div class="m-exchange__table-row">.*?</div>')
    # with open('id_bank.html', 'w') as html_file:
    #     html_file.write(html)
    with open('id_bank.html', 'r') as html_file:
        html = html_file.read()
        res = re.findall(
            r'<div\s+class\s*=\s*"m-exchange__table-cell"\s*>(.*)',
            html
        )
        if res:
            print(res)

if __name__ == '__main__':
    main()