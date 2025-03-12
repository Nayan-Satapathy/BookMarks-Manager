import tkinter as tk
from tkinter import ttk
import json
import webbrowser

memory = {}
def open_link(urll):
    webbrowser.open(urll)
def add_window():
    def Submit():
        Name = name.get()
        Link = link.get()
        memory[Name] = Link
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)        
        except:
            data = {}

        data[list(memory.keys())[0]] = list(memory.values())[0]
        tk.Label(new_window, text = "Submitted !", font=("Arial", 14)).place(x = 250, y = 600)
        name.delete(0, tk.END)
        link.delete(0, tk.END)
        memory.clear()
        

        with open("data.json", 'w') as file:
            json.dump(data, file, indent=4)



    new_window = tk.Toplevel(root)  # Creates a new top-level window
    new_window.title("Add a bookmark")
    new_window.geometry("1000x800")

    tk.Label(new_window, text="Add a book mark now: ", font=("Arial", 14)).pack(pady=20)
    tk.Label(new_window, text = "Name: ", font=("Arial", 14)).place(x = 200, y = 300)
    tk.Label(new_window, text = "Link: ", font=("Arial", 14)).place(x = 200, y = 400)
    name = tk.Entry(new_window, width=20)
    link = tk.Entry(new_window, width=50)
    name.place(x = 300, y = 300)
    link.place(x = 300, y = 400)
    submit = tk.Button(new_window, text = "Submit", font=("Arial", 14), command = Submit)
    submit.place(x = 250, y = 500)
def load_window():

    def search_that():
        nonlocal search, a 
        content = search.get()
        with open("data.json", 'r') as file:
            contents = json.load(file)
        for key, value in contents.items():
            if key == str(content):
                a.config(text = "")
                a.config(text = f"Link of {key} is: {value}")
                a.bind("<Button-1>", lambda e: open_link(value)) # Binds text with a function
                break
            else:
                a.config(text = "")
                a.config(text = "NOTHING FOUND !")

    new_window = tk.Toplevel(root)
    new_window.title("load all bookmarks")
    new_window.geometry("1000x800")
    a = tk.Label(new_window, text = "",font=("Arial", 14), fg = "blue",  cursor="hand2")
    a.place(x = 250, y = 300)
    text_widget = tk.Text(root, wrap="word", height=10, width=40)
    scrollbar = tk.Scrollbar(new_window, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    search = tk.Entry(new_window, width = 80)
    search.place(x = 150, y = 200)
    search_btn = tk.Button(new_window, text = "search", height = 1, width = 10, font=("Arial", 14), command = search_that).place(x = 800, y = 190)
    tk.Label(new_window, text = "Load a book mark: ", font=("Arial", 14),).place(x = 150, y = 100)
def all_window():
    new_window = tk.Toplevel(root)
    new_window.title("load all bookmarks")
    new_window.geometry("1000x800")

    text_widget1 = tk.Text(new_window, wrap="word", height=10, width=40, cursor="hand2")
    text_widget1.pack(side="left", fill="both", expand=True)
    scrollbar1 = tk.Scrollbar(new_window, command=text_widget1.yview)
    scrollbar1.pack(side="right", fill="y")
    text_widget1.config(yscrollcommand=scrollbar1.set)

    with open("data.json", 'r') as file:
        info = json.load(file)
    i = 1
    for key, values in info.items():
        text_widget1.insert(f"{i}.0", f"{key} --> ")
        start_index = text_widget1.index("end-1c")  # Get start index of URL
        text_widget1.insert("end", f"{values}\n")
        end_index = text_widget1.index("end-1c\n") # Get end index of URL
        text_widget1.tag_add(values, start_index, end_index)
        text_widget1.tag_config(values, foreground="blue", underline=True)
        text_widget1.tag_bind(values, "<Button-1>", lambda e, v = values: open_link(v))  
        i += 1
        
root = tk.Tk()  # Create the main window
root.title("Bookmark manager")  # Set window title
root.geometry("1200x1600")  # Set window size (Width x Height)
label = tk.Label(root, text="WELCOME TO BOOKMARKS MANAGER!",font=("Arial", 18, "bold"))
ADD = tk.Button(root, text="ADD A BOOKMARK", command = add_window, height = 3, width = 20, padx = 10, pady = 10, bg="#d8e0e8")
LOAD = tk.Button(root, text="LOAD A BOOKMARK", command = load_window, height = 3, width = 20, padx = 10, pady = 10, bg="#d8e0e8")
ALL_MARKS = tk.Button(root, text="SHOW ALL BOOKMARKS", command=all_window, height = 3, width = 20, padx = 10, pady = 10, bg="#d8e0e8")

label.pack()
ADD.place(x = 100, y = 200)
LOAD.place(x = 500, y = 200)
ALL_MARKS.place(x = 900, y = 200)

root.mainloop()  # Run the application