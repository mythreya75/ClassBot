import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from tkinter import *

browser = webdriver.Chrome(ChromeDriverManager().install())

def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    grid = QGridLayout()



    '''
    Within the window we need to create
    button widgets for each class, label 
    them, and then connect each one to a 
    function that opens the specified WebEx
    room.
    '''

    #Physics
    physRecButton = QPushButton(widget)
    physLabButton = QPushButton(widget)
    physLectButton = QPushButton(widget)

    physRecButton.setText("Physics Recitation")
    physLabButton.setText("Physics Lab")
    physLectButton.setText("Physics Lecture")

    physRecButton.move(50,50)
    physLabButton.move(200,50)
    physLectButton.move(350, 50)

    physRecButton.clicked.connect(physRecButton_clicked)
    physLabButton.clicked.connect(physLabButton_clicked)
    physLectButton.clicked.connect(physLectButton_clicked)

    physRecButton.resize(150, 30)
    physLabButton.resize(150, 30)
    physLectButton.resize(150, 30)

    #Math
    mathRecButton = QPushButton(widget)
    mathLectButton = QPushButton(widget)

    mathRecButton.setText("Math Recitation")
    mathLectButton.setText("Math Lecture")

    mathRecButton.move(50, 95)
    mathLectButton.move(200, 95)

    mathRecButton.clicked.connect(mathRecButton_clicked)
    mathLectButton.clicked.connect(mathLectButton_clicked)

    mathRecButton.resize(150, 30)
    mathLectButton.resize(150, 30)
    
    
    #CS
    CSButton = QPushButton(widget)
    CSButton.setText("Computer Science")
    CSButton.move(350, 95)
    CSButton.clicked.connect(CSButton_clicked)
    CSButton.resize(150, 30)

    #Humanities
    humButton = QPushButton(widget)
    humButton.setText("Humanities")
    humButton.move(200, 140)
    humButton.clicked.connect(humButton_clicked)
    humButton.resize(150, 30)

    widget.setLayout(grid)
    widget.setGeometry(700, 360, 550, 220)
    widget.setWindowTitle("ClassBot v2")
    widget.show()
    sys.exit(app.exec_())

'''
The following two functions are 
going to be referenced in the other
link-opening functions
'''

def click(xpath):
    button = browser.find_element_by_xpath(xpath)
    button.click()

def typing(xpath, message):
    box = browser.find_element_by_xpath(xpath)
    box.send_keys(message)

# These are the link-opening functions

def physRecButton_clicked():
    browser.get('https://njit.webex.com/njit/j.php?MTID=mfc46c640175e637cf479736785d8c99a')
    

def physLabButton_clicked(widget):
    browser.get("https://njit.webex.com/njit/j.php?MTID=mba00c19fcf03e1c51d9573eea45a4b39")
    widget.close()
    
def physLectButton_clicked(widget):
    browser.get("https://njit.webex.com/njit/j.php?MTID=mb9ab96d149ff8fff2bbc577b6ff30ecd")
    widget.close()

def mathRecButton_clicked(widget):
    browser.get("https://njit.webex.com/webappng/sites/njit/meeting/download/4872fd8e085547b4a1c68be486c38554")
    widget.close()

def mathLectButton_clicked(widget):
    browser.get("https://njit.webex.com/njit/j.php?MTID=m0ac743f920cbda8729e01936286c2fdb")
    widget.close()

def CSButton_clicked(widget):
    browser.get("https://njit.webex.com/njit/j.php?MTID=mc74342470298aaff25df9d4aeb1ee89c")
    widget.close()

def humButton_clicked(widget):
    browser.get("https://njit.instructure.com/courses/12754/external_tools/411")
    
    # From here, we have to sign into NJIT login
    typing("//*[@id=\"username\"]", "mv379") #Username
    # And the password
    typing("//*[@id=\"password\"]", "1_Gangaraju") #Password
    # then click "login"
    click("/html/body/div/div[2]/div/div[1]/form/div[3]/button") #login

    # Click through the useless COVID agreement page
    click("//*[@id=\"accept\"]") #checkbox
    click("//*[@id=\"submitbtn\"]") #submit 
    
    widget.close()

window()