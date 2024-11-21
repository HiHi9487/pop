# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:08:55 2024

@author: user
"""

import tkinter as tk 
from PIL import Image, ImageTk
#創建主視窗
window = tk.Tk()
window.title("PoP 點擊遊戲")
window.geometry("400x500")
window.resizable(False, False)

closed_mouth_image = ImageTk.PhotoImage(Image.open("close_mouth.png").resize((300, 250)))
open_mouth_image = ImageTk.PhotoImage(Image.open("open_mouth.png").resize((300, 250)))

cat_label = tk.Label(window, image=closed_mouth_image)
cat_label.pack(pady=20)

count_label = tk.Label(window, text="點擊次數: 0", font=("Arial", 18))
count_label.pack(pady=10)


def update_count():
    global click_count
    click_count += 1
    count_label.config(text=f"點擊次數: {click_count}")

def on_click(event):
    cat_label.config(image=open_mouth_image)
    window.after(200, lambda: cat_label.config(image=closed_mouth_image))
    update_count()
click_count = 0
cat_label.bind("<Button-1>", on_click)

def reset_count():
    global click_count
    click_count = 0
    count_label.config(text="點擊次數: 0")
reset_button = tk.Button(window, text="重製", command=reset_count, font=("Arial", 14), bg="lightblue")
reset_button.pack(pady=10)

window.mainloop()






