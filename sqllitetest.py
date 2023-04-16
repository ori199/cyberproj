import sqlite3
from sqlite3 import Error
import hashlib
import tkinter as tk

database = r"D:\orir\Git\pythonsqlite.db"


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def trylogin(user,password):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name=? And password = ?", (user,hash_password(password)))

    rows = cur.fetchall()
    conn.close
    if len(rows) == 1:
        start_window()
    else:
        loginfail(conn)


def create_user(conn, user,password):
    conn = create_connection(database)
    """
    Create a new project into the projects table
    :param password:
    :param user:
    :param conn:
    :return: project id
    """
    sql = ''' INSERT INTO users(name,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql,(user,hash_password(password)))
    conn.commit()
    return cur.lastrowid


def start_window():
    root = tk.Tk()
    root.title("start_window")

    # create the username label and entry
    headerlabel = tk.Label(root, text="you are signed in ")
    headerlabel.pack()
    root.mainloop()


def loginfail():
    root = tk.Tk()
    root.title("failed login")

    # create the username label and entry
    headerlabel = tk.Label(root, text="the password or the username is wrong")
    headerlabel.pack()
    blogin_button = tk.Button(root, text="back to login ", command=window())
    blogin_button.pack()
    root.mainloop()





def window():
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
    login_button = tk.Button(root, text="Login", command=trylogin(username_entry.get(), password_entry.get()))
    login_button.pack()

    # create the signup button
    signup_button = tk.Button(root, text="SignUp", command=create_user(username_entry.get(), password_entry.get()))
    signup_button.pack()

    # start the main event loop
    root.mainloop()

def hash_password(data):
    # Create a hash object for SHA256
    hash_object = hashlib.sha256()
    datab = bytes(data, 'utf-8')
    hash_object.update(datab)
    # Get the hash value as a hexadecimal string
    hex_dig = hash_object.hexdigest()
    return hex_dig





def main():
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS users (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                password text NOT NULL
                                            ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        conn.close()
        window()
    else:
        print("Error")



if __name__ == '__main__':
    main()