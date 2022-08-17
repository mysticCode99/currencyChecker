import sys

from PyQt5.QtWidgets import ( 
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QHBoxLayout, QLabel
)
from PyQt5.QtCore import Qt

from kurs_parser import collect_banks

class RateMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print(1)
        self.setCentralWidget()
        print(2)

    def setCentralWidget(self):
        ''''''
        centralWidget = QWidget()
        self.setGeometry(2500, 500, 1000, 500)
        self.vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()
        nHeaderLabel = QLabel('Bank Name')
        usdLabel = QLabel('USD to AMD')
        eurLabel = QLabel('EUR to AMD')
        rubLabel = QLabel('RUB to AMD')
        hbox.addWidget(nHeaderLabel)
        hbox.addWidget(usdLabel)
        hbox.addWidget(eurLabel)
        hbox.addWidget(rubLabel)
        self.vbox.addLayout(hbox)
        content = Content()
        self.vbox.addWidget(content)
        centralWidget.setLayout(self.vbox)
        super().setCentralWidget(centralWidget)

class Content(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        ''''''
        vbox = QVBoxLayout()
        banks = collect_banks()
        for bank in banks:
            bnLabel = QLabel()
            usdLabel = QLabel()
            eurLabel = QLabel()
            rubLabel = QLabel()
            bnLabel.setAlignment(Qt.AlignCenter)
            usdLabel.setAlignment(Qt.AlignCenter)
            eurLabel.setAlignment(Qt.AlignCenter)
            rubLabel.setAlignment(Qt.AlignCenter)
            hbox = QHBoxLayout()
            bnLabel.setText(bank.name)
            usdLabel.setText(bank.get_currence_sell_value('usd'))
            eurLabel.setText(bank.get_currence_sell_value('eur'))
            rubLabel.setText(bank.get_currence_sell_value('rub'))

            # adding labels
            hbox.addWidget(bnLabel)
            hbox.addWidget(usdLabel)
            hbox.addWidget(eurLabel)
            hbox.addWidget(rubLabel)
            vbox.addLayout(hbox)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RateMainWindow()
    win.show()
    sys.exit(app.exec_())