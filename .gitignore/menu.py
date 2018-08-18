from tkinter import * 


root = Tk()
root.geometry("100x100")
def newgame():
    import animation
B = Button(root, text = "new game", command = newgame)
B.place(x = 50, y=50)
root.mainloop()
