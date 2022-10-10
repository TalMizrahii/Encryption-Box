from tkinter import *
from tkinter import scrolledtext
from src import StartScreen

# Using the standard English alphabet.
alphabet = "abcdefghigklmnopqrstuvwxyz "


def deciphered_screen(root, key, message):
    # Clearing this frame and setting the "Start" screen.
    def back_to_menu():
        deciphered_message_frame.destroy()
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

    # Decrypting the ciphertext using vigenere cipher.
    def decipher_character(key_char, message_char):
        if message_char == ' ':
            message_num = 26
        else:
            message_num = ord(message_char) - ord('a')
        if key_char == ' ':
            key_num = 26
        else:
            key_num = ord(key_char) - ord('a')
        return alphabet[(message_num - key_num) % 27]

    # Creating a padded key and sending it and the ciphertext to be decrypted.
    def decipher():
        padded_key = key_process()
        deciphered_message = ""
        for i in range(0, len(message)):
            deciphered_message = deciphered_message + str(decipher_character(padded_key[i], message[i]))
        return deciphered_message

    # Creating the frame for this screen.
    deciphered_message_frame = Frame(root, bg="#c9c9c9")
    # Headline of the system.
    headline_label = Label(deciphered_message_frame, text="DECIPHERED MESSAGE", font=(None, 30), width=60, bg="#c9c9c9")
    headline_label.pack(pady=30)
    # The description label
    description_label = Label(deciphered_message_frame, text="The DECIPHERED message is:", font=(None, 25),
                              bg="#c9c9c9")
    description_label.pack(pady=30)
    # Creating an entry scrolled text for the message.
    entry_message_widget = scrolledtext.ScrolledText(deciphered_message_frame,
                                                     wrap=WORD,
                                                     width=45, height=5,
                                                     font=("David", 15),
                                                     borderwidth=5)
    entry_message_widget.insert(INSERT, decipher())
    entry_message_widget.pack()
    # Creating an instruction label.
    instruction_label = Label(deciphered_message_frame, text="copy the deciphered message above",
                              font=(None, 20),
                              bg="#c9c9c9")
    instruction_label.pack()
    # Creating "back to menu" button.
    back_to_menu_button = Button(deciphered_message_frame, text="Back", command=back_to_menu, font=(None, 15))
    back_to_menu_button.pack(pady=25)
    # Packing this screen's frame.
    deciphered_message_frame.pack()
