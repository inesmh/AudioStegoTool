<h1>Audio Stego Tool</h1>

<h3>Objective</h3>
Hide text messages in .wav audio files. In the folder there is an example audio to try the functionality. The file to be executed is stegocode.py
<br /> <br />
<h3>Skills Learned</h3>
● How Steganography works <br />
● Python coding <br />

<br />
<h3>Tools Used</h3>
● Python <br />
● Sample audio <br />

<br />
<h3>Steps</h3>
To hide a message the interface will ask for:  <br />
● Audio file: path of the file in which the text will be hidden.  <br />
● Output file name: name of the file that will be created with the hidden message. The path in which it will be saved is the same as where the audio file is saved.  <br />
● Numeric password: it will allow to hide and unhide messages so it is more protected.  <br />
● Message: secret text we want to hide in the audio. The messages should only include text, numbers and spaces.  <br />
Once complited, press Hide. A .wav file will be generated with the hidden message.
<br />
<img width="251" alt="stego1" src="https://github.com/user-attachments/assets/e6b88fa7-3889-4742-a3bd-c8a0277f1dfc">
<br />
*Ref 1: Hide a message*
<br />
<br />
To unhide a message the interface will ask for:  <br />
● Audio file: path of the file in which the hidden text is.  <br />
● Numeric password: the one introduced before.  <br />
Once complited, press Unhide. The secret message will be shown in the interface, as well as a txt file with the hidden message with the same name as the file with the hidden message.
<br />
<img width="266" alt="stego2" src="https://github.com/user-attachments/assets/1f3de99b-40ee-4f7c-a6f9-705a7c44463b">
<br />
*Ref 2: Unhide a message*
<br />
