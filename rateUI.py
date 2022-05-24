import sys

from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel
)

from kurs_parser import collect_banks

class RateMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        ''''''
        self.setGeometry(2500, 500, 1000, 500)
        self.vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Bank Name'))
        hbox.addWidget(QLabel('USD to AMD'))
        hbox.addWidget(QLabel('EUR to AMD'))
        hbox.addWidget(QLabel('RUB to AMD'))
        self.vbox.addLayout(hbox)
        self.addBanksInfo()
        self.setLayout(self.vbox)
    
    def addBanksInfo(self):
        ''''''
        banks = collect_banks()
        for bank in banks:
            print(bank.name, bank.currences)
            print(bank.get_currence('usd'))
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(bank.name))
            hbox.addWidget(QLabel(bank.get_currence_sell_value('usd')))
            hbox.addWidget(QLabel(bank.get_currence_sell_value('eur')))
            hbox.addWidget(QLabel(bank.get_currence_sell_value('rub')))
            self.vbox.addLayout(hbox)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RateMainWindow()
    win.show()
    sys.exit(app.exec_())