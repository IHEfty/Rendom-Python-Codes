# Author: IHEfty

import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

root = tk.Tk()
root.title("Wooh Note")
root.geometry("515x515")

style = Style(theme="darkly")  
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

root.configure(bg="#333333")

notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass 

def toggle_theme():
    if style.theme_use() == "darkly":
        style.theme_use("journal")  
        root.configure(bg="#ffffff")
        style.configure("TNotebook", background="#ffffff", foreground="#000000")
        style.configure("TButton", background="#e0e0e0", foreground="#000000")
    else:
        style.theme_use("darkly")  
        root.configure(bg="#333333")
        style.configure("TNotebook", background="#333333", foreground="#ffffff")
        style.configure("TButton", background="#444444", foreground="#ffffff")

def add_note():
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")

    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)

    def save_note():
        title = title_entry.get().strip()
        content = content_entry.get("1.0", tk.END).strip()
        if title:
            notes[title] = content
            with open("notes.json", "w") as f:
                json.dump(notes, f)

            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.forget(notebook.select())
            notebook.add(note_content, text=title)
        else:
            messagebox.showwarning("Warning", "Wooh > Title cannot be empty.")

    save_button = ttk.Button(note_frame, text="Save", command=save_note)
    save_button.grid(row=2, column=0, padx=10, pady=10)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        pass

load_notes()

def delete_note():
    current_tab = notebook.index(notebook.select())
    note_title = notebook.tab(current_tab, "text")

    confirm = messagebox.askyesno("Delete Note", f"Wooh > Are you sure you want to delete '{note_title}'?")
    if confirm:
        notebook.forget(current_tab)
        notes.pop(note_title, None)
        with open("notes.python main.pyjson", "w") as f:
            json.dump(notes, f)

new_button = ttk.Button(root, text="New", command=add_note, style="dark.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", command=delete_note, style="dark.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

theme_button = ttk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
