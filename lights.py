import subprocess
import time
from datetime import datetime

def main():
    lights_on = True
    while True:
        daily()

def daily():
    now = datetime.now()
    if 7 <= int(now.strftime("%H")) <= 21:
        if lights_on == True:
            return
        else:
            subprocess.run(["uhubctl", "-l", "1-1", "-a", "on"])
            lights_on = True
            return
    else:
        if lights_on == False:
            return
        else:
            subprocess.run(["uhubctl", "-l", "1-1", "-a", "off"])
            lights_on = False

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