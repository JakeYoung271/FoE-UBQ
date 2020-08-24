import pyautogui as p
import time
import random as r

def sec(p=0.93):
    k = r.randint(-100,100)/1000
    t = p+k
    time.sleep(t)
# Replace the below code with "l = [....]" after completing the code once and putting in the printed list
######################################################
print("To begin, open FoE and put it in a place on the screen that you will be able to go to again (fullscreen, halfscreen, etc.)")
print("Open this program and run it. You can make this a window which hides behind the fullscreen FoE window when you start running it")
print("Or you can run them both in splitscreen, but again make sure that the location of the buttons on the screen will stay in the")
print("The same place so you can run the program again at a later time. When you run this program for the first time, get the quest after UBQ up first ")
print("I think its the produce meat skewers. Run this program and then place you mouse over the abort button. Wait for it to click")
print("Every time it clicks, you have 3.5 seconds to move the mouse to the next position or leave it if it doesn't need to move.")
print("The abort button should stay in the same place for first five quests, but if not thats fine. Just each time, put your mouse over the abort")
print("button and wait for it to click. Once you get to the UBQ, place your mouse over the pay buttons and then the collect button.")
print("Last of all, put your mouse over to the far left of the quest window in FoE, this is to reset it if a blueprint is won and the")
print("window pops up. wait 3 or 4 seconds after moving you mouse there to be sure it collected your position. If you do happen to win a bp")
print("It should clear the window. Last of All, it will print out a list to the console. Copy that and replace all of this code with ")
print("\"l=[.....]\"  --- then uncomment the code below the second line of hashtags")
print("When running this code, if you need to stop it, quickly move the mouse to the top left of the screen")
input("--When you are ready and understand type anything and hit enter to run the code.-- \n")
l = []
for i in range(11):
    sec(3.5)
    j,z = p.position()
    l.append((j,z))
    p.click()
    print("clicked")
print(l)
######################################################
"""for i in range(2): #put how many times you want it to run UBQ
    for q,w in l:
        sec()
        p.click(q,w)"""
