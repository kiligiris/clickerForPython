import threading
import keyboard

class funcKey():
    def __init__(self,funcb):
        self.started = threading.Event()
        self.finished = threading.Event()
        self.thread = threading.Thread(target=self.func,args=(funcb,))
        self.thread.start()

    def func(self,funcb):
        keyboard.add_hotkey(funcb,lambda: self.end())

    def begin(self):
        self.started.set()
        self.finished.clear()

    def end(self):
        if self.started.is_set():
            self.started.clear()
            self.finished.set()
        
    def kill(self):
        self.thread.join()
