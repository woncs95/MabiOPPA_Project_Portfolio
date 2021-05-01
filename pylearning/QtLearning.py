from PyQt5.QtWidgets import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 200)
        self.setWindowTitle("PyQt")
        #self.setWindowIcon(QIcon="icon.png")

        btn = QPushButton("sex", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()