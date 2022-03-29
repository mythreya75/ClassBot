import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class App(QWidget):
    browser = webdriver.Chrome(ChromeDriverManager().install())

    def __init__(self):
        super().__init__()

        self.title = 'ClassBot V3'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()
        self.close()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getChoice()
        self.show()

    def getChoice(self):
        items = ("Physics", "Physics Lab", "Math", "Humanities",
                 "Sociology", "CS Lecture", "CS Lab")
        item, okPressed = QInputDialog.getItem(
            self, "ClassBot V3", "Class:", items, 0, False)
        if okPressed and item:
            self.goToClass(item)

    def goToClass(self, course):
        # PHYSICS
        if course == 'Physics':
            self.browser.get("https://njit.webex.com/meet")
        elif course == 'Physics Lab':
            # PHYSICS LAB
            self.browser.get("https://njit.webex.com/meet/physics")
        # MATH
        elif course == "Math":
            # MATH LECTURE
            self.browser.get("https://njit.webex.com/meet/math")
        # HUMANITIES
        elif course == 'Humanities':
            self.browser.get("https://njit.webex.com/meet/hum")
        # SOCIOLOGY
        elif course == 'Sociology':
            self.browser.get("https://njit.webex.com/meet/sociology")
        # CS
        elif course == 'CS Lecture':
            self.browser.get("https://njit.webex.com/meet/cslecture")
        elif course == 'CS Lab':
            self.browser.get("https://njit.webex.com/meet/cslab")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
