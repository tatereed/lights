import subprocess
import time
from datetime import datetime

def main():
    test()

def daily():
    lights_on = True
    while True:
        now = datetime.now()
        if 7 <= int(now.strftime("%H")) <= 21:
            if lights_on == False:
                subprocess.run(["uhubctl", "-l", "1-1", "-a", "on"])
                lights_on = True
                print(now.strftime("%H:%M:%S"))
        else:
            if lights_on == True:
                subprocess.run(["uhubctl", "-l", "1-1", "-a", "off"])
                lights_on = False
                print(now.strftime("%H:%M:%S"))
            
                

def test():
    lights_on = True
    while True:
        time.sleep(5)
        if lights_on == True:
            subprocess.run(["uhubctl", "-l", "1-1", "-a", "off"])
            lights_on = False
        else:
            subprocess.run(["uhubctl", "-l", "1-1", "-a", "on"])
            lights_on = True

if __name__=="__main__":
    main()