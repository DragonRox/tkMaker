import Tkinter as tk
from Tkinter import RIGHT

global verify_larg, verify_alt
verify_larg = False
verify_alt = False

def drawPos(event):
    global l
    try:
        l.destroy()
    except NameError: pass
    lt = "X = %i, Y = %i" % (event.x, event.y)
    setX, setY = 0, 0
    l = tk.Label(root, text = lt, bd = 5, bg = "white")
    setY = event.y + 20
    setX = event.x - ((len(lt) * 5) / 2)
    if event.y < 10: setY = 30
    elif event.y > C.winfo_height(): setY = event.y - 30
    if event.x < 25: setX = 30
    elif event.x > C.winfo_width(): setX = event.x - 30


    l.place(x = setX, y = setY)

def buildModf(event):
    global verify_larg, verify_alt
    if verify_larg == True:
        Build.configure(width = event.x, cursor = "arrow")
        verify_larg = False
    if verify_alt == True:
        Build.configure(height = event.y, cursor = "arrow")
        verify_alt = False
    l.destroy()
        
def checkPos(event):
    global verify_larg, verify_alt
    if event.x <= C.winfo_width() and event.x >= (C.winfo_width() - 5):
        Build.configure(cursor = "fleur")
        verify_larg = True
    if event.y <= C.winfo_height() and event.y >= (C.winfo_height() - 5):
        Build.configure(cursor = "fleur")
        verify_alt = True
    print "clicked at", event.x, event.y
    
root = tk.Tk()
root.geometry("1280x800")

f = tk.Frame(root, bg = 'red')
f.pack()

Build = tk.Canvas(root, bg = "blue", height = 500, width = 500, bd = 5)
Build.place(x = 10, y = 10)

Build.bind("<Button-1>", checkPos)
Build.bind("<ButtonRelease-1>", buildModf)
Build.bind("<B1-Motion>", drawPos)

MenuWidget = tk.Canvas(root, bg = "red", height = 512, width = 340)
MenuWidget.pack(anchor = "e")
















root.mainloop()