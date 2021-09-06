import threading
import time
import pyautogui
from decimal import Decimal

class clicker():

    def __init__(self,sb,eb,EditBox):
        sb.begin()
        self.sbFinished = sb.finished
        self.ebFinished = eb.finished
        self.EditBox = EditBox
        self.alive = True
        self.thread1 = threading.Thread(target=self.clicker,args=(eb,))
        self.thread2 = threading.Thread(target=self.begin,args=(sb,))
        self.inter = 0.01
        self.thread1.start()
        self.thread2.start()
    
    def clicker(self,eb):
        self.sbFinished.wait()
        while self.alive:
            eb.begin()
            self.inter = self.intercheck()
            while self.sbFinished.is_set():
                pyautogui.click()
                time.sleep(self.inter)
            self.sbFinished.wait()

    def begin(self,sb):
        self.ebFinished.wait()
        while self.alive:
            sb.begin()
            self.sbFinished.wait()
            self.ebFinished.wait()

    def intercheck(self):
        inter = self.EditBox.get()
        if inter.isdecimal():
            inter = Decimal(inter) / 1000
            print(inter)
            if inter >= 0.001:
                return inter
        return 0.01

    def kill(self,sb,eb):
        self.alive = False
        self.sbFinished.set()
        self.ebFinished.set()
        self.thread1.join()
        self.thread2.join()
        print("clicker.end")