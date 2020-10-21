from selenium import webdriver
import time as t
import pyautogui as p
import random as r
def sec(z=0):
    p=0.9-z
    k = r.randint(0,100)/1000
    q = p+k
    t.sleep(q)
def openPage():
    p.moveTo(25, 240+48)
    t.sleep(5)
    location = p.locateOnScreen("play.png", confidence=0.9)
    p.click(location)
    t.sleep(2)
    location = p.locateOnScreen("gWorld.png", confidence=0.9)
    p.click(location)
    t.sleep(20)
    p.moveTo(25, 240+48)
    p.click()
    t.sleep(3)
    p.click(25,240+48)
    t.sleep(0.1)
    p.click(300,336+48)
    t.sleep(0.1)
    p.click(300,389+48)
    t.sleep(0.1)
    p.click(563,298+48)
    print("just so you know")
def findRQ(quests):
    for i in quests:
        if i['type'] == 'generic':
            return i
def getQuests(driver):
    quests = driver.execute_script(r"return MainParser.Quests")
    return quests
def getRQ(driver):
    return(findRQ(getQuests(driver)))
def pay():
    sec(0.8)
    p.click(465,555)
    sec(0.8)
    p.click(465,625)
class QClass:
    def __init__(self,QuestDict):
        self.title = QuestDict['title']
        self.abortLocation = (300,619+55*int("Meat Skewers and Cheese Wheels" in self.title or "Unbirthday" in self.title))
        self.isUBQ = "Unbirthday" in self.title
        self.Quest = QuestDict
        self.rewards = QuestDict['rewards'][0]
        if 'iconType' in self.rewards.keys():
            self.iconType = self.rewards['iconType']
        else:
            self.iconType = None
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(r"C:\Users\Dell\Desktop\chromedriver.exe", options = chrome_options)
driver.get('https://us7.forgeofempires.com/game/index?')
t.sleep(15)
bp_failsafe = False
for i in range(45000):
    K = QClass(getRQ(driver))
    if K.isUBQ:
        pay()
        sec()
        K = QClass(getRQ(driver))
        #print(K.iconType,K.rewards,K.Quest)
        p.click(565,539+48)
        if K.iconType == 'blueprint':
            t.sleep(1.5)
            p.click(43,625)
            bp_failsafe = True
    else:
        p.click(K.abortLocation)
        if bp_failsafe:
            p.click(43,625)
    bp_failsafe = False
    sec(0.05)