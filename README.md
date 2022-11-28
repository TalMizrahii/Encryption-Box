<h1 align="center">
  
  ![python-logo-glassy](https://user-images.githubusercontent.com/103560553/204082228-92a30920-ca99-4517-9b9d-c3ab44d42a0b.png)

  ENCRYPTION BOX
  <br>
</h1>

<h4 align="center"> An Encryption application to encrypt and decipher messages using Vigenere cipher.


<p align="center">
  <a href="#description">Description</a> •
  <a href="#implementation">Implementation</a> •
  <a href="#dependencies">Dependencies</a> •
  <a href="#installing-and-executing">Installing And Executing</a> •
  <a href="#author">Author</a> 
</p>

## Description
  
### About The Program
  
This program uses the Vigenere cipher to encrypt text messages using an encryption key determined by the user. 
From the main screen, The user can choose whether to encrypt or decrypt a message, enter his encryption key, and the program will present him the encrypted/decrypted message on a new textbox on the screen.
  
![ezgif com-gif-maker](https://user-images.githubusercontent.com/103560553/194914374-61e71a06-567b-4eef-9d30-62bbfd3d6073.gif)

### About The Cipher

The Vigenere cipher was issued in 1553. It is a polyalphabetic cipher, which uses a key to encrypt plaintext into ciphertext. The main advantage of it is that it is highly resistant to frequency analysis.

![vigenere-cipher](https://user-images.githubusercontent.com/103560553/196162003-5043af75-310f-4060-a373-97d39825fbbf.png)

If you wish to read about the Vigenere cipher or about Frequency Analysis you can visit:
* [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
* [Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis)
## Implementation

The GUI design is based on three screens:
* The menu screen - For the user to choose whether to encrypt or decipher a message.
* The Encrypt screen - Encrypting the user's message.
* The Decrypt screen - Decrypting the user message.

![123](https://user-images.githubusercontent.com/103560553/194918643-2680c671-374e-4327-9988-d483119c535e.PNG)

The program makes validation checks to determain if the user's input follows the key and message requirements. If any of the checks detect an error, a popup message apear on the screen.

![1](https://user-images.githubusercontent.com/103560553/204360871-fa35fff4-1ea2-4d64-82c7-a020510420e4.PNG)

The program also make sure the user saved the encryption key using a popup message.

![2](https://user-images.githubusercontent.com/103560553/204361110-0f577673-7a67-4253-9376-88b515953410.PNG)

## Dependencies

* I used the "Tkinter" library for the GUI.
* The Python version I used is Python 3.9.

## Installing And Executing

To install and run the program you can click on the [release](https://github.com/TalMizrahii/Encryption-Box/releases/tag/v1.0) button in this repository.
  
You can also use [Git](https://git-scm.com). From your command line:

```bash
# Clone this repository.
$ git clone https://github.com/TalMizrahii/Encryption-Box

# Go into the repository.
$ cd Encryption-Box

# Run the program
$ EncryptionBox
```
## Author

* [@Tal Mizrahi](https://github.com/TalMizrahii)
* Taltalon1927@gmail.com
