
# ***********************************
# Libraries to be imported & Random prime numbers to generate the sequence of bits
# ***********************************
import re
import wave
import math

#prime number constants
RANDOMPRIMENUMBER_1= 15485863
RANDOMPRIMENUMBER_2= 2038074743

# ***********************************
# Function to generate the sequence of bits
# ***********************************
def sequence_generator(byte_array_len,passw,message_len):
  #This function generates a sequence of bits, depending on the user message and password input
  bit_sequence = []
  passw = int(passw)


  for i in range(message_len):
    pos = (RANDOMPRIMENUMBER_1*passw + RANDOMPRIMENUMBER_2*i)%byte_array_len
    while(pos in range(0,33)):
      pos = (RANDOMPRIMENUMBER_1*passw + RANDOMPRIMENUMBER_2*i)%byte_array_len
      
    bit_sequence.append(pos)

  return bit_sequence


# ***********************************
# Function to hide message in byte_array
# ***********************************

def hide(byte_array,passw,msg):
    
    # Text data to bit array
    msg = [int(i) for i in ''.join([bin(ord(c)).lstrip('0b').rjust(8,'0') for c in msg])]

    # Get the length of the message
    msg_len = len(msg)

    # check if the message is too long to be hidden in the audio
    if msg_len > len(byte_array)*8:
      return "The message is too long to be hidden in the audio file"

    # Message length to a bit array
    msg_len_bin = bin(msg_len)[2:].zfill(32)
    msg_len_bin = list(msg_len_bin)
    
    # Hide message length message in the first 32 bits of the audio
    for i in range(0,32):
      byte_array[i] = ((byte_array[i] & 254) | int(msg_len_bin[i]))

    # Generate bits to hide the message
    positions = sequence_generator(len(byte_array),passw,msg_len)
    
    # Iterate text bits and hide them in the LSB of the audio
    for i in range(len(positions)):
        byte_array[positions[i]] = ((byte_array[positions[i]] & 254) | msg[i])

    return byte_array

#***********************************
# run_hide : Function to hide the message in the audio file
#***********************************
def run_hide(audio_path,passw,msg,outputfilename):
  # Open the audio file in read mode
  with wave.open(audio_path, "rb") as audio_file:
   
    # Read the frames of the audio file
    frames = audio_file.readframes(-1)
   
    # Convert the frames to a byte array
    byte_array = bytearray(frames)
    byte_array = hide(byte_array,passw,msg)
  
  #  Write the modified audio data to a new file in the same path as the original audio file ,
  #  the user has selected the name of the file
  # delete the last part of the path to get the path of the audio file
    path=audio_path.rsplit('/',1)[0] + '/'

    #concatenate path and name of the output file
    output_path = str(path) + str(outputfilename) + ".wav"

    # Write the modified audio data to a new file
    with wave.open(output_path, "wb") as hidden_audio:
        hidden_audio.setparams(audio_file.getparams())
        hidden_audio.writeframes(byte_array)
  
  return "The data has been hidden successfully"

#***********************************
# run_unhide : Function to find the message in the audio file
#***********************************
def run_unhide(audio_path,passw):
  with wave.open(audio_path, "rb") as audio_file:
    # Read the frames of the audio file
    frames = audio_file.readframes(-1)
    # Convert the frames to a byte array
    byte_array = bytearray(frames)

  msg_len_bin = ""

  # Extract the length of the message from the first 32 bits of the audio data
  for i in range(0,32):
    bit = bin(byte_array[i])[2:].zfill(8)
    msg_len_bin += str(bit[-1])

  msg_len = int(msg_len_bin,2)
  
  # Generate the sequence of bits to extract the text data
  positions = sequence_generator(len(byte_array),passw,msg_len)

  msg = []
  
  # Extract the text data from the audio data
  for i in range(len(positions)):
    msg.append(byte_array[positions[i]] & 1)
  
  text = ''.join([chr(int(i, 2)) for i in [''.join(map(str,msg[i:i+8])) for i in range(0, len(msg), 8)]])

  #checking password
  regex = re.compile(r'[\W_]')
  if ' ' not in text:
    if regex.search(text) is not None:
      text="Incorrect password"

  # Return a text file with  the extracted text data and save it in the same path as the audio file
  path=audio_path.rsplit('/',1)[0] + '/'

  #change the name of the file as the same number of the audio file
  output_path = str(path) + str(audio_path.rsplit('/',1)[1].split('.')[0]) + ".txt"

  with open(output_path, "w") as text_file:
    text_file.write(text)

  return text