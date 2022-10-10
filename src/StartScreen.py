import tkinter
from tkinter import *
from src import EncryptScreen
from src import DicipherScreen


def front_page(root):

    # Clearing this frame and setting the "Encrypt" frame.
    def encrypt_key():
        start_frame.destroy()
        EncryptScreen.encrypt_screen(root)

    # Clearing this frame and setting the "Decipher" frame.
    def decipher_key():
        start_frame.destroy()
        DicipherScreen.decipher_screen(root)

    # The frame of the start screen.
    start_frame = Frame(root, bg="#c9c9c9")
    # Headline of the system.
    headline_label = Label(start_frame, text="ENCRYPTION BOX", font=(None, 35), width=60, bg="#c9c9c9")
    headline_label.pack(pady=12)
    # The description label
    description_label = Label(start_frame, text="Create a cryptographic key\n and encrypt plaintext using the key.",
                              font=(None, 20),
                              bg="#c9c9c9")
    description_label.pack(pady=30)
    # Creating the "encrypt" button and its frame.
    encrypt_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    encrypt_frame.pack(pady=10, padx=20)
    encrypt_button = Button(encrypt_frame, text="Encrypt plaintext", font=(None, 18), command=encrypt_key, width=60,
                            height=3)
    encrypt_button.pack(pady=0, padx=0)
    # Creating the "decipher" button and its frame.
    decipher_frame = tkinter.Frame(start_frame, highlightbackground="black", highlightthickness=2, bd=0)
    decipher_frame.pack(pady=10, padx=20)
    decipher_button = Button(decipher_frame, text="Decrypt Ciphertext", font=(None, 18), command=decipher_key, width=60,
                             height=3)
    decipher_button.pack(pady=0, padx=0)
    credit = Label(start_frame, text="Made by Tal Mizrahi", bg="#c9c9c9")
    credit.pack(pady=20)
    # Packing the screen's frame to the root.
    start_frame.pack()
