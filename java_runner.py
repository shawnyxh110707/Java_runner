import os
import tkinter as tk
from tkinter import filedialog
class __init__():
    window = tk.Tk()
    window.title("JAVA_PROGRAM_RUNNER")
    window.geometry("500x500")
    window.resizable(width=True,height = True)

file_addition = ""

def running(file = ''):
    a = os.system(f'java -jar "{file}"')
    

def button_clicked():
    global file_addition
    print(entry.get())
    file_addition = entry.get()
    running(file_addition)

def browse_file():
    global file_addition
    file_addition = filedialog.askopenfilename()
    entry.delete(0,-1)
    entry.insert(0,file_addition)

main = __init__()
label_text = tk.Label(main.window,text = "输入文件地址",font=("黑体",20))
label_text.place(x=180,y=150)

entry = tk.Entry(main.window,insertwidth=1)
entry.insert(0,'')
entry.place(x=180,y=200)

button_sure = tk.Button(main.window,text="确认",font=("黑体",15),command=button_clicked)
button_sure.place(x= 350,y=200)

button_find_file = tk.Button(main.window,text="浏览文件",font=("黑体",15),command=browse_file)
button_find_file.place(x= 200,y=230)

main.window.mainloop()

