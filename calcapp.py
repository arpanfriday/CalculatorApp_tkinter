import pymsgbox
import tkinter as tk
from tkinter import *

root = tk.Tk()
hiddenmodule = ['pymsgbox']

tk.Label(root, text="SIMPLE CALCULATOR").grid(row=0, column=30)


def key(num):
    num = t.insert(END, num)
    root.mainloop()


def seven():
    t.insert(END, 7)
    root.mainloop()


def eight():
    t.insert(END, 8)
    root.mainloop()


def nine():
    t.insert(END, 9)
    root.mainloop()


def divide():
    t.insert(END, "/")
    root.mainloop()


def multiply():
    t.insert(END, "*")
    root.mainloop()


def ge():
    x = t.get()
    x = str(x)
    pymsgbox.alert("Result is : " + str(eval(x)))
    t.delete(0, END)


def clear():
    t.delete(0, END)


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black')
t = tk.Entry(root, bg='white')
t.grid(row=3, column=8)

#                HALF OF THE BUTTON COMMANDS ARE MADE USING A SEPARATE KEY() METHOD AND
#         REST HALF OF THE BUTTONS ARE MADE USING SEPARATE METHODS FOR EACH NUMBER OR KEY PRESSED
#                EITHER OF THE TWO CAN BE USED TO DEFINE ALL THE BUTTONS IN THE PROGRAM

# -----------------------------------------------------------------------------------------------------------------------#

tk.Button(root, text="0", command=lambda: key(0), height=1, width=6, bd=4).grid(row=3, column=1, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="1", command=lambda: key(1), height=1, width=6, bd=4).grid(row=3, column=2, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="2", command=lambda: key(2), height=1, width=6, bd=4).grid(row=3, column=3, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="3", command=lambda: key(3), height=1, width=6, bd=4).grid(row=4, column=1, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="4", command=lambda: key(4), height=1, width=6, bd=4).grid(row=4, column=2, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="5", command=lambda: key(5), height=1, width=6, bd=4).grid(row=4, column=3, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="6", command=lambda: key(6), height=1, width=6, bd=4).grid(row=5, column=1, sticky=tk.W, pady=20,
                                                                                padx=20)
tk.Button(root, text="7", command=seven, height=1, width=6, bd=4).grid(row=5, column=2, sticky=tk.W, pady=20, padx=20)
tk.Button(root, text="8", command=eight, height=1, width=6, bd=4).grid(row=5, column=3, sticky=tk.W, pady=20, padx=20)
tk.Button(root, text="9", command=nine, height=1, width=6, bd=4).grid(row=15, column=1, sticky=tk.W, pady=20, padx=20)
tk.Button(root, text="+", command=lambda: key("+"), height=1, width=6, bd=4).grid(row=15, column=3, sticky=tk.W,
                                                                                  pady=20, padx=20)
tk.Button(root, text="-", command=lambda: key("-"), height=1, width=6, bd=4).grid(row=15, column=2, sticky=tk.W,
                                                                                  pady=20, padx=20)
tk.Button(root, text="/", command=divide, height=1, width=6, bd=4).grid(row=15, column=1, sticky=tk.W, pady=20, padx=20)
tk.Button(root, text="*", command=multiply, height=1, width=6, bd=4).grid(row=16, column=1, sticky=tk.W, pady=20,
                                                                          padx=20)
tk.Button(root, text="%", command=lambda: key("%"), height=1, width=6, bd=4).grid(row=16, column=2, sticky=tk.W,
                                                                                  pady=20,
                                                                                  padx=20)
tk.Button(root, text=".", command=lambda: key("."), height=1, width=6, bd=4).grid(row=16, column=3, sticky=tk.W,
                                                                                  pady=20,
                                                                                  padx=20)
tk.Button(root, text="clear", command=clear, height=1, width=6, bd=4).grid(row=17, column=1, sticky=tk.W, pady=20,
                                                                           padx=20)
tk.Button(root, text="Quit", command=lambda: sys.exit(), height=1, width=6, bd=4).grid(row=17, column=2, sticky=tk.W,
                                                                                       pady=20, padx=20)
tk.Button(root, text="Submit", command=ge, height=1, width=6, bg='green2', bd=4).grid(row=17, column=3, sticky=tk.W,
                                                                                      pady=20, padx=20)
tk.mainloop()
