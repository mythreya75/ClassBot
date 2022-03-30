from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

course = input("What class would you like to join?: ")

if __name__ == '__main__':
    print('Foo')
    
course = course.lower()

browser = webdriver.Chrome(ChromeDriverManager().install())

def click(xpath):
    button = browser.find_element_by_xpath(xpath)
    button.click()

def typing(xpath, message):
    box = browser.find_element_by_xpath(xpath)
    box.send_keys(message)

def enter(xpath):
    box = browser.find_element_by_xpath(xpath)
    box.send_keys(Keys.RETURN)


#MATH
if course == "mathlect" or course == 'calclect':
    #MATH LECTURE
    browser.get("https://njit.webex.com/njit/j.php?MTID=m0ac743f920cbda8729e01936286c2fdb")
elif course == "mathRec" or course == "calcRec":
    #MATH RECITATION
    browser.get("https://njit.webex.com/webappng/sites/njit/meeting/download/4872fd8e085547b4a1c68be486c38554")
    
#HUMANITIES
elif course == "hum":
    #HUMANITIES
    browser.get("https://njit.instructure.com/courses/12754/external_tools/411")
    
    #From here, we have to sign into NJIT login
    typing("//*[@id=\"username\"]", "mv379") #Username
    #And the password
    typing("//*[@id=\"password\"]", "1_Gangaraju") #Password
    #then click "login"
    click("/html/body/div/div[2]/div/div[1]/form/div[3]/button") #login

    #Click through the useless COVID agreement page
    click("//*[@id=\"accept\"]") #checkbox
    click("//*[@id=\"submitbtn\"]") #submit 

#PHYSICS    
elif course == 'physlect':
    #PHYSICS LECTURE
    browser.get("https://njit.webex.com/njit/j.php?MTID=mb9ab96d149ff8fff2bbc577b6ff30ecd")
elif course == 'physlab':
    #PHYSICS LAB
    browser.get("https://njit.webex.com/njit/j.php?MTID=mba00c19fcf03e1c51d9573eea45a4b39")

#CS
elif course == 'cs':
    browser.get("https://njit.webex.com/njit/j.php?MTID=mc74342470298aaff25df9d4aeb1ee89c")


