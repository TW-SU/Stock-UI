import sys
import qdarkstyle
from PyQt5.QtWidgets import QDialog, QApplication
from MyFirstUI import Ui_Form    #MyFirstUI 是你的.py檔案名字

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
w = AppWindow()
w.show()
sys.exit(app.exec_())