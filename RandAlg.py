import random
import time
import sys
from datetime import datetime
import os

#time adjustment (seconds)
adjust = 10

#shuffler algorithm
def shuffler():
    tst = random.random()
    strForm = str(tst)
    length = len(strForm)
    thisList = []
    x = 0
    #Randomizer Shuffler
    while x < length:
        if strForm[x] == ".":
            x+=1
            continue
        thisList.insert(x, strForm[x])
        x+=1

    random.shuffle(thisList)
    number = "".join(map(str,thisList))
    conv = int(number)
    return conv

#clear console function
def clear_console():
    # Clear console based on the operating system
    if os.name == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For Unix/Linux/Mac

def output():
    tick = 0 
    while tick != adjust:
        # Get the current time and format it as a string
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
        fin = shuffler()

        # Use '\r' to return the cursor to the start of the line
        # Use 'end=""' to prevent a new line after the print statement
        clear_console()
        tick += 1
        prompt = f"\rCurrent Time: {current_time} \nRandom Output: {fin} \nTick: {tick}"
        print(f"{prompt}",end="", flush=True)
    
        # Wait for one second before updating the time again
        time.sleep(1)

output()