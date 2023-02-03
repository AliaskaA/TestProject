from tkinter import *
root = Tk()
root.title('окно')
c = Canvas(width = 1000, height = 700)
c.pack()
c.create_polygon(900, 505, 105, 150, 480, 655, fill = 'yellow', outline = 'pink')

root.mainloop()