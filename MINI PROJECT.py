import tkinter as tk
import sqlite3
from tkinter import messagebox

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect("event_database.db")
cursor = conn.cursor()

# Create the events table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        location TEXT,
        description TEXT
    )
''')
conn.commit()

def add_event():
    title = title_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    location = location_entry.get()
    description = description_text.get("1.0", "end-1c")

    cursor.execute('''
        INSERT INTO events (title, date, time, location, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, date, time, location, description))

    conn.commit()
    clear_fields()
    messagebox.showinfo("Event Added", "Event has been added successfully.")

def clear_fields():
    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    description_text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Event Scheduler Wizard")

# Create and pack GUI components
title_label = tk.Label(root, text="Event Title:")
title_entry = tk.Entry(root)
date_label = tk.Label(root, text="Date:")
date_entry = tk.Entry(root)
time_label = tk.Label(root, text="Time:")
time_entry = tk.Entry(root)
location_label = tk.Label(root, text="Location:")
location_entry = tk.Entry(root)
description_label = tk.Label(root, text="Description:")
description_text = tk.Text(root, height=5, width=40)

add_button = tk.Button(root, text="Add Event", command=add_event)
clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)

title_label.pack()
title_entry.pack()
date_label.pack()
date_entry.pack()
time_label.pack()
time_entry.pack()
location_label.pack()
location_entry.pack()
description_label.pack()
description_text.pack()
add_button.pack()
clear_button.pack()

root.mainloop()

# Close the database connection when the GUI is closed
conn.close()