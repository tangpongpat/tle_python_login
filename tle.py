import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "admin":
        message_label.config(text="Login successful!")
        # Create the menu page
        create_menu_page()
    else:
        message_label.config(text="Incorrect username or password.")

def create_menu_page():
    # Destroy the login page
    username_label.destroy()
    username_entry.destroy()
    password_label.destroy()
    password_entry.destroy()
    login_button.destroy()
    message_label.destroy()

    # Create the menu page
    menu_label = tk.Label(window, text="Select a class:")
    menu_label.pack()

    differential_button = tk.Button(window, text="Differential", command=show_differential_page)
    differential_button.pack()

    type_button = tk.Button(window, text="Type", command=show_type_page)
    type_button.pack()

    disassembly_button = tk.Button(window, text="Disassembly", command=show_disassembly_page)
    disassembly_button.pack()

    warning_button = tk.Button(window, text="Warning", command=show_warning_page)
    warning_button.pack()

def show_differential_page():
    # Create the differential page
    differential_label = tk.Label(window, text="Differential class page")
    differential_label.pack()

def show_type_page():
    # Create the type page
    type_label = tk.Label(window, text="Type class page")
    type_label.pack()

def show_disassembly_page():
    # Create the disassembly page
    disassembly_label = tk.Label(window, text="Disassembly class page")
    disassembly_label.pack()

def show_warning_page():
    # Create the warning page
    warning_label = tk.Label(window, text="Warning class page")
    warning_label.pack()

# Create the main window
window = tk.Tk()
window.title("Login Page")

# Create the username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Create the password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Create the message label
message_label = tk.Label(window, text="")
message_label.pack()

# Start the main event loop
window.mainloop()
