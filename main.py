from tkinter import Tk, Button, Label
from generator import Generator
# TODO : add password lenght field

root = Tk()
root.title("PassGen")
root.resizable(0, 0)

password_object = Generator() # Create an object

def set_password_into_label(password, lbl_object):
	lbl_password['text'] = password

def generate_password():
	global password_object
	password = password_object.generate()
	set_password_into_label(password, lbl_password)

def set_copy_tag_into_lebel(lbl_object):
	lbl_object['text'] = lbl_object['text'] + ' - copied!'

def copy_password():
	password_object.copy_password()
	set_copy_tag_into_lebel(lbl_password)

btn_generate = Button(root, text="Generate", width=20, font=("Consolas", 17), command=generate_password)
btn_copy = Button(root, text="Copy", width=10, font=("Consolas", 17), command=copy_password)
lbl_password = Label(root, text="Password", font=("Consolas", 16), justify='center', anchor="center")
btn_generate.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))
btn_copy.grid(row=0, column=1, padx=(0, 15), pady=(15, 0))
lbl_password.grid(row=1, column=0,)
root.mainloop()