import tkinter as tk # importing the tk-inter module
from tkinter import ttk #another module of tkinter for using buttons and lables

# initializing the tkinter with object name "root"
root = tk.Tk() # Tk is the constructor
#giving title to the app
root.title("GUI")

# creating the labels
name_label = ttk.Label(root,text = "Enter your name : ")
name_label.grid(row = 0,column = 0,sticky =tk.W ) # stick the label in the west direction/position
age_label= ttk.Label(root,text = "Enter your age : ")
age_label.grid(row=1,column=0,sticky=tk.W)
email_label = ttk.Label(root,text= "Enter email address : ")
email_label.grid(row=2,column=0,sticky=tk.W)

# create entry box for name 
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root,width = 16,textvariable = name_var)
name_entrybox.grid(row=0,column=1)
# create entry box for age 
age_var = tk.StringVar()
age_entrybox = ttk.Entry(root,width = 16,textvariable = age_var)
age_entrybox.grid(row=1,column=1)


# create entry box for email 
email_var = tk.StringVar()
email_entrybox = ttk.Entry(root,width = 16,textvariable = email_var)
email_entrybox.grid(row=2,column=1)

# create button
submit_button = ttk.Button(root,text="Submit")
submit_button.grid(row=3,column=0)


root.mainloop()