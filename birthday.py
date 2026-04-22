import tkinter as tk

#window create
root = tk.Tk()
root.title("Happy Birthday🎂")
root.geometry("400x300")
root.configure(bg="#ffccd5")

#label create
label = tk.Label(root, text="",font=("Arial",20),bg="#ffccd5")
label.pack(pady=20)

#function to show message
def show_message():
    label.config(text="🎉Happy birthday!🎂")

btn = tk.Button(root,text="Click Me🎁",
                command=show_message)
btn.pack(pady=20)

root.mainloop()