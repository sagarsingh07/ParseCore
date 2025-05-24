import tkinter as tk
from tkinter import messagebox, Scrollbar, Canvas
from PIL import Image, ImageTk
from parser import parser
import graphviz
import os

def build_graph(tree, dot=None, count=[0]):
    if dot is None:
        dot = graphviz.Digraph()
    node_id = str(count[0])
    count[0] += 1

    if isinstance(tree, tuple):
        label = tree[0]
        dot.node(node_id, label)
        for child in tree[1:]:
            child_id = build_graph(child, dot, count)
            dot.edge(node_id, child_id)
    else:
        dot.node(node_id, str(tree))
    return node_id

def parse_input():
    expr = entry.get()
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    try:
        tree = parser.parse(expr)
        status_label.config(text=f"Parsed successfully:\n{tree}", fg="green")

        dot = graphviz.Digraph()
        build_graph(tree, dot)

        dot.render("parse_tree", format="png", cleanup=False)
        img = Image.open("parse_tree.png")
        img = img.resize((img.width, img.height))
        img_tk = ImageTk.PhotoImage(img)

        label_img = tk.Label(canvas_frame, image=img_tk)
        label_img.image = img_tk
        label_img.pack()

    except SyntaxError as e:
        status_label.config(text=str(e), fg="red")

root = tk.Tk()
root.title("Expression Parse Tree")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Enter expression:")
label.grid(row=0, column=0, sticky='w')

entry = tk.Entry(frame, width=60)
entry.grid(row=0, column=1, padx=5)

parse_button = tk.Button(frame, text="Parse", command=parse_input)
parse_button.grid(row=0, column=2, padx=5)

status_label = tk.Label(frame, text="", justify="left", font=("Courier", 10))
status_label.grid(row=1, column=0, columnspan=3, sticky='w', pady=(10, 5))

canvas = Canvas(frame, width=800, height=500)
canvas.grid(row=2, column=0, columnspan=3)

scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=2, column=3, sticky='ns')

canvas.configure(yscrollcommand=scrollbar.set)

canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

canvas_frame.bind('<Configure>', on_configure)

root.mainloop()
