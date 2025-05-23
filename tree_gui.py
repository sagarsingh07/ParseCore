import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import uuid
from parser import parse_with_error
import graphviz

def build_tree(tree, dot=None, parent=None, count=[0]):
    if dot is None:
        dot = graphviz.Digraph()

    node_id = f'node{count[0]}'
    count[0] += 1

    if isinstance(tree, tuple):
        label = str(tree[0])
        dot.node(node_id, label)
        if parent:
            dot.edge(parent, node_id)
        for child in tree[1:]:
            build_tree(child, dot, node_id, count)
    else:
        label = str(tree)
        dot.node(node_id, label)
        if parent:
            dot.edge(parent, node_id)

    return dot

def parse_input():
    expr = entry.get()
    if not expr.strip():
        output_label.config(text="Please enter an expression.", foreground="orange")
        image_label.config(image='')
        return

    try:
        result, error = parse_with_error(expr)

        if error:
            output_label.config(text=error, foreground="red")
            image_label.config(image='')
            return

        if not result:
            output_label.config(text="Parse Error: Invalid syntax.", foreground="red")
            image_label.config(image='')
            return

        output_label.config(text="Parsed Successfully", foreground="green")
        dot = build_tree(result)

        filename = f"parse_tree_{uuid.uuid4().hex}"
        dot.render(filename, format="png", cleanup=True)

        img = Image.open(filename + ".png")
        img = img.resize((700, 450), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

    except Exception as e:
        output_label.config(text=f"Error: {str(e)}", foreground="red")
        image_label.config(image='')

# Setup main window
root = tk.Tk()
root.title("Parse Tree Visualizer")
root.geometry("800x650")
root.configure(bg="#f0f0f0")

# Style configuration for ttk widgets
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=6)
style.configure("TEntry", font=("Segoe UI", 14))
style.configure("TLabel", background="#f0f0f0", font=("Segoe UI", 12))

# Container frame with padding
frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# Input label and entry
input_label = ttk.Label(frame, text="Enter Expression:", font=("Segoe UI", 14, "bold"))
input_label.pack(anchor=tk.W, pady=(0, 5))

entry = ttk.Entry(frame, width=50)
entry.pack(fill=tk.X, pady=(0, 15))
entry.focus()

# Parse button
parse_button = ttk.Button(frame, text="Parse Expression", command=parse_input)
parse_button.pack(pady=(0, 20))

# Output label for errors or success
output_label = ttk.Label(frame, text="", font=("Segoe UI", 12, "italic"))
output_label.pack(pady=(0, 10))

# Image label for parse tree display
image_label = ttk.Label(frame)
image_label.pack(fill=tk.BOTH, expand=True)

root.mainloop()
