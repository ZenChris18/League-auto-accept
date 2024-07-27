# lcu_gui.py
from tkinter import *
from tkinter import messagebox
import threading
import main as connector

#active/inactive
def update_status(status):
    status_label.config(text=status)

def start_connector():
    try:
        threading.Thread(target=connector.start_connector).start()
        update_status("Active")
        messagebox.showinfo("Info", "Connector started successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start connector: {e}")

def stop_connector():
    try:
        connector.stop_connector()
        update_status("Inactive")
        messagebox.showinfo("Info", "Connector stopped successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop connector: {e}")

# Create the main Tkinter window
root = Tk()
root.title("LCU Connector")
root.geometry("300x200")

# Create and place the Start button
start_button = Button(root, text="Start Auto Accept", command=start_connector)
start_button.pack(pady=20)

# Create and place the Stop button
stop_button = Button(root, text="Stop Program", command=stop_connector)
stop_button.pack(pady=20)

# Create and place the Status label
status_label = Label(root, text="Inactive", fg="red")
status_label.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
