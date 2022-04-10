import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from ui.ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class MyConverter(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyConverter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # load interface
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Currency converter")
        self.setWindowIcon(QIcon("./ui/exchange.png"))
        self.ui.input_currency.setPlaceholderText("From: ")
        self.ui.input_amount.setPlaceholderText("I give: ")
        self.ui.output_currency.setPlaceholderText("To: ")
        self.ui.output_amount.setPlaceholderText("I get: ")
        self.ui.pushButton.clicked.connect(self.convert)

    def convert(self):
        conv = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())
        output_amount = round(conv.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        self.ui.output_amount.setText(str(output_amount))



def main():
    app = QtWidgets.QApplication([])
    application = MyConverter()
    application.show()

    sys.exit(app.exec()) # exit from app


if __name__ == "__main__":
    main()