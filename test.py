import tkinter as tk
from tkinter import ttk

def on_tree_select(event):
    # check the number of rows in the tree
    rows = tree.get_children()
    if len(rows) > height:
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)
    else:
        ysb.pack_forget()
        xsb.pack_forget()

root = tk.Tk()
root.geometry("700x350")

tree = ttk.Treeview(root, columns=("c1", "c2"), show='headings', height=5)
tree.heading("c1", text="Course")
tree.heading("c2", text="Grade")
tree.column("c1", width=300, minwidth=100, anchor='center')
tree.column("c2", width=50, minwidth=50, anchor='center')
tree.insert('', 'end', text="1", values=('math', 'A'))
tree.insert('', 'end', text="2", values=('science', 'B'))
tree.insert('', 'end', text="3", values=('history', 'C'))

ysb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
xsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)

tree.bind("oaicite:{"index":0,"invalid_reason":"Malformed citation <<TreeviewSelect>>"}", on_tree_select)

tree.pack()
root.mainloop()
