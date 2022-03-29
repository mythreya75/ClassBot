# ClassBot

## Inspiration
During the COVID-19 pandemic the process to log into Cisco Webex room for online classes was unnecessarily complicated and the link for the meeting room would be in inconsistent locations for each of my classes. The solution I created was ClassBot, a Python script that would automatically direct me to the meeting room I need to be in using a package that retrieves the needed link for the specified meeting.

## Description
The primary package used for this project was Selenium Webdriver, which automates the process of manuevering through Chrome. I used PyQt5 for the widgets to display the user interface. The script works by first building a class App which contains all the visuals and logic for the program. By creating an instance of Chrome's Webdriver, the program opens a tab to manuever through Chrome

## Version 1
The initial version of ClassBot took an input from terminal that accepted a few different keywords such as "math" or "physics" to sign me into the classes. This was quicker than going through to the rooms manually, but it still used Selenium to fill in my passcode entry for my college's sign-in page. I knew there was still room for improvement

## Version 2
I improved on the original by introducing PyQt5 Widgets, namely QApplication, QWidget, QInputDialog, QLineEdit, and QIcon. These allowed me to create a pop-up screen with several buttons labeled with my respective classes. I also avoided having to input my sign-in information by retrieving the direct link to the meeting room. 

## Verstion 3
The ultimate version of ClassBot uses the same widgets but now displays a drop-down menu to select the designated class instead of the individual buttons. This greatly changed how efficient the script was as it allowed me to use my keyboard (arrow keys and the enter key) to manuever the menu and join my class. 
