import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.master.config(menu=self.create_menu())
        self.text_area = tk.Text(self.master, font=("Helvetica", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

    def create_menu(self):
        menu = tk.Menu(self.master)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu.add_cascade(label="File", menu=file_menu)
        return menu

    def new_file(self):
        if self.text_area.get("1.0", tk.END) == "\n":
            self.text_area.delete("1.0", tk.END)
            self.master.title("Untitled")
        else:
            if messagebox.askyesno("Save?", "Do you want to save?"):
                self.save_file()
                self.text_area.delete("1.0", tk.END)
                self.master.title("Untitled")
            else:
                self.text_area.delete("1.0", tk.END)
                self.master.title("Untitled")

    def open_file(self):
        file = filedialog.askopenfile(mode="r", filetypes=[("Text Files", "*.txt")])
        if file is not None:
            self.master.title(file.name)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if self.master.title() == "Untitled":
            self.save_as_file()
        else:
            file = open(self.master.title(), mode="w")
            file.write(self.text_area.get("1.0", tk.END))
            file.close()

    def save_as_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file is not None:
            file.write(self.text_area.get("1.0", tk.END))
            file.close()
            self.master.title(file.name)

def main():
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
