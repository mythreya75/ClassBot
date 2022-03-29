# ClassBot

## Inspiration
During the COVID-19 pandemic the process to log into Cisco Webex room for online classes was unnecessarily complicated and the link for the website would be in inconsistent locations. The solution I created was ClassBot, a bot that would automatically direct me to the meeting room I need to be in.

## Description
The primary package used for this project was Selenium Webdriver, which automates the process of manuevering through Chrome. I used PyQt5 for the widgets to display the user interface. The script works by first building a class App which contains all the visuals and logic for the program. By creating an instance of Chrome's Webdriver, the program opens a tab to manuever through Chrome

## Version 1
The initial version of ClassBot took an input from terminal that accepted a few different keywords such as "math" or "physics" to sign me into the classes. This was quicker than going through to the rooms manually, but it still used Selenium to fill in my passcode entry for my college's sign-in page. I knew there was still room for improvement

## Version 2
I improved on the original by introducing PyQt5 Widgets, namely QApplication, QWidget, QInputDialog, QLineEdit, and QIcon.
