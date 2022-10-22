from tkinter import *
from src.StartScreen import front_page

# Create a root window.
root = Tk()
# Create a title for the window.
root.title("Tal's Encryption Box")
# Upload an icon to the window and set it.
img = PhotoImage(file='resources/lock1.png')
root.tk.call('wm', 'iconphoto', root._w, img)
# Set the size of the window.
root.geometry("550x550")
# Enable/Disable the resize option.
# root.resizable(width=False, height=False)
# Set the background color of the window.
root.configure(bg="#c9c9c9")
# Start the system in the first page.
front_page(root)
# The main loop.
root.mainloop()
