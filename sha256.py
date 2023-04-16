import tkinter as tk


def login():
    username = username_entry.get()
    password = password_entry.get()

    # TODO: add code to validate username and password

    print("Username:", username)
    print("Password:", password)


# create the main window
root = tk.Tk()
root.title("Login")

# create the username label and entry
headerlabel = tk.Label(root, text="Enter your details:")
headerlabel.pack()
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# create the password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# create the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# create the signup button
signup_button = tk.Button(root, text="SignUp", command=signup)
signup_button.pack()

# start the main event loop
root.mainloop()
