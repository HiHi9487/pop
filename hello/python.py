# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:05:55 2024

@author: user
"""

import tkinter as tk
def greet():
    user_name = entry.get()
    label.config(text=f"hello, {user_name}!")
window = tk.Tk()
window.title("hello,world")
window.geometry("400x200")
tk.Label(window, text="hello,Tkinter!", font=("Arial", 16)).pack()

   
label = tk.Label(window, text="請輸入名字:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="提交", command=greet)
button.pack()
window.mainloop()