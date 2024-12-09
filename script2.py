import sys
from PyQt5.QtWidgets import QApplication,   QMainWindow,QLabel
from PyQt5.QtGui import  QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setGeometry(700,300,500,500)
        label = QLabel("This is my name",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0, 500,100)
        label.setStyleSheet("color: blue;background-color:red;")
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

def main():
    app = QApplication(sys.argv) # app object
    window =  MainWindow() #window object
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()