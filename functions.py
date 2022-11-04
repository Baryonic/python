from win10toast import ToastNotifier
import time
from datetime import datetime


class Function:
    def f0():
        print('f0() in functions.py works')
    def startnotification():
        print('calling f0()---')
        toaster=ToastNotifier()
        try:
            currenttime = datetime.now().strftime("%H%M%S")
            title=f'time{currenttime}'
            content=f'''hi bary
{currenttime}
its a nice day to go out
%H : %M : %S
'''
            toaster.show_toast(title,content,duration=10)
        except NameError as err:
            print(f'error in starter.py f0(){err}')
