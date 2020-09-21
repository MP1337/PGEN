#PGEN Simple Password Generator
#Version: 1.0
#Author: Peter Mazela
#Contact: info@elix-it.de
"""Generator for strong passwords"""
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator, QPixmap
import pgen as pg

WORKING_DIR = os.getcwd() + '/'
GUI = WORKING_DIR + '/data/gui.ui'
ICON = WORKING_DIR + '/data/pgen.png'

class PGen(QMainWindow):
    """Qt GUI MainWindow class"""
    def __init__(self):
        """Init UI, clipboard and genereate random
        passwords on start"""
        super().__init__()

        uic.loadUi(GUI, self)

        #Logo
        pixmap = QPixmap(ICON).scaled(150,150)
        self.logoLabel.setPixmap(pixmap)

        #Clipboard
        self.clipboard = QApplication.clipboard()

        # Buttons
        self.generateButton.clicked.connect(self.generate_password)
        self.copyButton.clicked.connect(self.button_cliboard)
        self.listWidget.itemClicked.connect(self.list_clicked)
        self.actionAbout.triggered.connect(self.button_about)
        self.actionClose.triggered.connect(self.close)

        #Integer Validation
        self.validator = QIntValidator()
        self.lenText.setValidator(self.validator)

        self.generate_password()
        self.lineStrongness.setText(self.listWidget.item(0).text())

    def generate_password(self):
        """Generating passwords and filling listWidget"""
        self.listWidget.clear()
        letters = self.checkLetters.isChecked()
        digits = self.checkDigits.isChecked()
        special = self.checkSpecial.isChecked()

        try:
            password_length = int(self.lenText.text())
        except ValueError:
            password_length = 10
            self.lenText.setText(str(password_length))

        for _i in range(17):
            self.listWidget.addItem(
                pg.generate_password(password_length,letters,digits,special))

        color = "red" if password_length < 8 else "orange" if password_length < 10 else "lime"
        self.lineStrongness.setStyleSheet(f"background-color: {color};")

    #####################################################################

    def button_cliboard(self):
        """Copy password to clipboard """
        try:
            self.clipboard.setText(self.listWidget.currentItem().text())
        except (AttributeError, ValueError):
            pass

    def button_about(self):
        """Show 'About' information window"""
        QMessageBox.information(self, "Info",\
        "PGEN Simple Password Generator v1\nCreated by Peter Mazela\ninfo@elix-it.de\n\
https://github.com/MP1337/PGEN_Simple_Password_Generator")

    def list_clicked(self):
        """Copy current item to textbox"""
        self.lineStrongness.setText(self.listWidget.currentItem().text())

def main():
    """No need to describe =)"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = PGen()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
