# test
import random
from tkinter import *

root = Tk()
root.title("Password Generator")


def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbols = "@#&/"

    all_char = str(lower) + str(upper) + str(symbols) + str(num)

    password = "".join(random.sample(all_char, length_value))

    return password


def my_password():
    if 3 <= length_value <= 50:
        password = Label(root, text=f"Password : {generate_password()}")
        password.pack()
        # print(f"Password : {generatepassword()}")
    elif length_value < 3:
        error_1 = Label(root, text="Length is too short ! try again")
        error_1.pack()
        # print("Length is too short ! try again")
    elif length_value > 20:
        error_2 = Label(root, text="Length is higher than expected ! try again")
        error_2.pack()
        # print("Length is higher than expected ! try again")

if __name__ == '__main__':
    global length_value
    length = Entry(root)
    length.pack()
    length_value = int(length.get())
    generate_button = Button(root, text="Generate Password", command=my_password)
    generate_button.pack()
    # length = int(input("Enter the length of password : "))


root.mainloop()

