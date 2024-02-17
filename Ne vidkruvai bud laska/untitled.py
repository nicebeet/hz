import sys
from PyQt5  import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('bambim.ui',self)
        self.pushButton.clicked.connect(self.plus)



    def plus(self):
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_2.text())
        self.label.setText(str(a+b))





if  __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())