import sys
import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic

form_class = uic.loadUiType("ui/googleTrans.ui")[0]

class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("구글 한줄 번역기")
        self.setWindowIcon(QIcon("img/google.png"))

        self.statusBar().showMessage("Google Trans App v1.0 made by LIM_Company")

app = QApplication(sys.argv)
win = GoogleTrans()  # 이렇게 하면 화면에 나타났다가 사라짐. 아래를 해주면 나타났다가 엑스를 누를 때 까지 실행 됨
win.show()  # 이 문장의 위치가 손으로 만든 것 하고 차이.
sys.exit(app.exec_())

