from tkinter import *
from tkinter import scrolledtext
from src import StartScreen

# Using the standard English alphabet.
alphabet = "abcdefghigklmnopqrstuvwxyz "


def encrypted_screen(root, key, message):
    def back_to_menu():
        # Clearing this frame and setting the "Start" screen.
        encrypted_message_frame.destroy()
        StartScreen.front_page(root)

    # Processing the key to check if it's valid.
    def key_process():
        if len(key) == len(message):
            return key
        padded_key = key
        x = 0
        for i in range(0, len(message) - len(key)):
            padded_key = padded_key + str(key[x])
            x = (1 + x) % len(key)
        return padded_key

    # Encrypting the plaintext using vigenere cipher.
    def encrypt_character(key_char, message_char):
        key_num = ord(key_char) - ord('a')
        if message_char == ' ':
            message_num = 26
        else:
            message_num = ord(message_char) - ord('a')
        return alphabet[(key_num + message_num) % 27]

    # Creating a padded key and sending it and the plaintext to be encrypted.
    def encrypt():
        padded_key = key_process()
        encrypted_message = ""
        for i in range(0, len(message)):
            encrypted_message = encrypted_message + str(encrypt_character(padded_key[i], message[i]))
        return encrypted_message

    # Creating the frame for this screen.
    encrypted_message_frame = Frame(root, bg="#c9c9c9")
    # Headline of the system.
    headline_label = Label(encrypted_message_frame, text="ENCRYPTED MESSAGE", font=(None, 30), width=60, bg="#c9c9c9")
    headline_label.pack(pady=30)
    # The description label
    description_label = Label(encrypted_message_frame, text="The encrypted message is:", font=(None, 25), bg="#c9c9c9")
    description_label.pack(pady=30)
    # Creating an entry scrolled text for the message.
    entry_message_widget = scrolledtext.ScrolledText(encrypted_message_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.insert(INSERT, encrypt())
    entry_message_widget.pack()
    # Creating an instruction label.
    instruction_label = Label(encrypted_message_frame, text="copy the cipher above",
                              font=(None, 20),
                              bg="#c9c9c9")
    instruction_label.pack()
    # Creating "back to menu" button.
    back_to_menu_button = Button(encrypted_message_frame, text="Back", command=back_to_menu, font=(None, 15))
    back_to_menu_button.pack(pady=25)
    # Packing this screen's frame.
    encrypted_message_frame.pack()
