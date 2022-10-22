from tkinter import *
from tkinter import messagebox, scrolledtext
from src import StartScreen, DecipherMessageScreen


def decipher_screen(root):
    # Clearing this frame and setting the "Start" screen.
    def back_to_start():
        decipher_frame.destroy()
        StartScreen.front_page(root)

    # If the key is not valid, raising an error message box.
    def key_validation(key, message):
        if len(key) < 2:
            messagebox.showerror("KEY ERROR", "Key must contain at least 2 letters!")
            return False
        elif not all(x.isalpha() or x.isspace() for x in key):
            messagebox.showerror("KEY ERROR", "Key must contain letters or spaces only!")
            return False
        elif len(key) > len(message):
            messagebox.showerror("KEY ERROR", "Key can not be shorter then the ciphertext!")
            return False
        return True

    # If the ciphertext is not valid, raising an error message box.
    def message_validation(message):
        if len(message) <= 0:
            messagebox.showerror("MESSAGE ERROR", "Ciphertext must contain at least one letter!")
            return False
        elif not all(x.isalpha() or x.isspace() for x in message):
            messagebox.showerror("MESSAGE ERROR", "Ciphertext must contain letters and spaces only!")
            return False
        return True

    # Checking the key and ciphertext and sending it to be decrypted.
    def decipher_message():
        # Asking the user if he is sure about the key.
        if messagebox.askquestion("ATTENTION", "are you sure you entered the correct key?") == "yes":
            key = entry_key_widget.get().lower()
            message = entry_message_widget.get("1.0", "end -1c").lower()
            if key_validation(key, message) and message_validation(message):
                # clearing this screen and decrypting the message in the "Decrypt" screen.
                decipher_frame.destroy()
                DecipherMessageScreen.deciphered_screen(root, key=key, message=message)

    # Creating the frame for this screen.
    decipher_frame = Frame(root, bg="#c9c9c9")
    # Creating the headline of the key screen.
    headline_label = Label(decipher_frame,
                           text="ENCRYPTION BOX - DECRYPT",
                           font=(None, 27),
                           width=60,
                           bg="#c9c9c9")
    headline_label.pack(pady=30, padx=5)
    # Creating a key instruction.
    key_instruction_lbl = Label(decipher_frame,
                                text="Enter key (at least 2 characters)",
                                font=(None, 20),
                                bg="#c9c9c9")
    key_instruction_lbl.pack(pady=5)
    # Creating an entry label for the key.
    entry_key_widget = Entry(decipher_frame, width=20, borderwidth=5, font=("David", 22))
    entry_key_widget.pack()
    # Space label.
    space_lbl = Label(decipher_frame, bg="#c9c9c9")
    space_lbl.pack(pady=1)
    # Creating "Enter a message" instruction.
    entry_message_lbl = Label(decipher_frame,
                              text="Enter ciphertext",
                              font=(None, 20),
                              bg="#c9c9c9")
    entry_message_lbl.pack(pady=5)
    # Creating an entry scrolled text for the message.
    entry_message_widget = scrolledtext.ScrolledText(decipher_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.pack()
    # Creating an ENCRYPT command button.
    decipher_button = Button(decipher_frame, text="DECIPHER",
                             font=(None, 20),
                             bg="#c9c9c9",
                             fg="#DC143C",
                             command=decipher_message,
                             borderwidth=3)
    decipher_button.pack(pady=5)
    # Creating the "Back" button.
    back_button = Button(decipher_frame,
                         text="Back",
                         command=back_to_start,
                         font=(None, 15))
    back_button.pack(pady=15)
    # Packing the screen's frame.
    decipher_frame.pack()
