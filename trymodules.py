import modules #modules.py in the same directory
modules.f1()
from win10toast import ToastNotifier
import time
from datetime import datetime

from modules import f2
f2()

def f3():
    print('calling f3()')
    #"ctypes.windll.user32.MessageBoxW(0, "The number generated is less than 10", "ALERT", 1)
    toaster=ToastNotifier()
    try:
        currenttime = datetime.now().strftime("%H%M%S")
        title=f'time{currenttime}'
        content=f'''line1
hi bary
{currenttime}
its a nice day to go out
'''

        toaster.show_toast(title,content,duration=6)
    except NameError as err:
        print(err)
f3()


