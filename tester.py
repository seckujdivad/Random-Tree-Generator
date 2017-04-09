import tkinter as tk
from rtree import rtree

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

tree = rtree(canvas)
tree.render()

root.mainloop()
