import tkinter
from funcKey import funcKey
from clicker import clicker

#ウィンドウ生成
tki = tkinter.Tk()
tki.geometry('300x200')
tki.title(u'クリック連打君')

#ラベル生成
Static1 = tkinter.Label(text=u'クリック連打君！', foreground='#ff0000', background='#ffaacc')
Static1.pack()

#テキストボックス生成
EditBox = tkinter.Entry()
EditBox.insert(tkinter.END,"10")
EditBox.pack()


#スタート
sb = funcKey("F9")
eb = funcKey("F10")
main = clicker(sb,eb,EditBox)
objs = [sb,eb]

tki.mainloop()

main.kill(sb,eb)
for obj in objs:
    obj.kill()










