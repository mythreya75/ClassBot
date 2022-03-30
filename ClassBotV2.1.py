import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#browser = webdriver.Chrome(ChromeDriverManager().install())
'''
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("bruh")
        
'''


class Window(QWidget):
    def __init__(self, buttonList):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QPushButton("bruh", 1, 1))
        self.setWindowTitle("ClassBot v2.1")
        self.setGeometry(650, 360, 500, 350)
        self.show()




# The input list is a list of lists, where the string at index 0 
# is the button label and the string at index 1 is the URL

btnList = [["YouTube", "https://youtube.com"],["Google", "https://google.com"],["NJIT Portal", "https://portal.njit.edu"]]

#if __name__ == '__main__':
app = QApplication(sys.argv)
ex = Window(btnList)
sys.exit(app.exec_())