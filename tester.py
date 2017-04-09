import tkinter as tk
from rtree import rtree

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500)

tree = rtree(canvas)
tree.render()

canvas.pack()

root.mainloop()
