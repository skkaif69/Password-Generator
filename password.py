import tkinter as tk
import random
import string


# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())

    # Define character sets for password complexity
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user's choice
    all_chars = ""
    if lowercase_var.get():
        all_chars += lowercase
    if uppercase_var.get():
        all_chars += uppercase
    if digits_var.get():
        all_chars += digits
    if special_var.get():
        all_chars += special_chars

    if not all_chars:
        result_label.config(text="Select at least one character set")
        return

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(password_length))
    result_label.config(text="Generated Password: " + password)


# Create the main application window
app = tk.Tk()
app.title("Password Generator using python")

# Label for password length
length_label = tk.Label(app, text="Password Length:")
length_label.pack()

# Entry for password length
length_entry = tk.Entry(app)
length_entry.pack()

# Checkbox options for character sets
lowercase_var = tk.IntVar()
lowercase_checkbox = tk.Checkbutton(app, text="Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.pack()

uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(app, text="Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

digits_var = tk.IntVar()
digits_checkbox = tk.Checkbutton(app, text="Digits", variable=digits_var)
digits_checkbox.pack()

special_var = tk.IntVar()
special_checkbox = tk.Checkbutton(app, text="Special Characters", variable=special_var)
special_checkbox.pack()

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
