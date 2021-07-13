
from tkinter import *
import passGenModule

root = Tk()
root.title("Password Generator")
root.geometry("400x400")


def my_password(length):
    generated_password_entry.delete(0, END)
    if 3 <= length <= 50:
        password_module = passGenModule.Password(length)
        generated_password_entry.insert(0, password_module.true_random())
        # password_label = Label(root, text=f"Password = {generated_password(length)}")
        # password_label.pack()

    elif length < 3:
        generated_password_entry.insert(0, "Length is too short ! try again")
        # error_1 = Label(root, text="Length is too short ! try again")
        # error_1.pack()

    elif length > 20:
        generated_password_entry.insert(0, "Length is higher than expected ! try again")
        # error_2 = Label(root, text="Length is higher than expected ! try again")
        # error_2.pack()
    else:
        generated_password_entry.insert(0, "Enter the number in above field")


length_entry = Entry(root)
length_entry.pack()

generated_password_entry = Entry(root)
generated_password_entry.pack()


if len(length_entry.get()) == 0:
    generated_password_entry.delete(0, END)
    generated_password_entry.insert(0, "Enter the number in above field")

generate_button = Button(root, text="Generate Password", command=lambda: my_password(int(length_entry.get())))
generate_button.pack()

root.mainloop()
