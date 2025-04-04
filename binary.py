import os
import time
import sys

def binary_to_text_soosun(binary_str_mhto):

    binary_values_mhto = binary_str_mhto.split()
    try:
        ascii_characters_soosun = [chr(int(b, 2)) for b in binary_values_mhto]
        return ''.join(ascii_characters_soosun)
    except ValueError:
        return "Invalid binary input!"

def text_to_binary_01(text):
    return ' '.join(format(ord(char), '08b') for char in text)

class color:
        r = '\x1b[;33m'
        g = '\x1b[;32m'

def susan(s):
  for a in s + '\n':
      sys.stdout.write(a)
      sys.stdout.flush()
      time.sleep(1./12)

susan(color.r + "Program By Sushant Mahato")
susan("Devlop By Nepal")
time.sleep(1)
os.system('clear')

# Main interaction
print("Choose an option:")
print("1. Text to Binary")
print("2. Binary to Text")

choice = input("Enter 1 or 2: ")
time.sleep(1.12)

os.system('clear')


class color:
        r = '\x1b[;33m'
        g = '\x1b[;32m'


if choice == '1':
    user_text = input("Enter text to convert to binary: ")
    print("Binary:", color.g + text_to_binary_01(user_text))
elif choice == '2':
    user_binary = input("Enter binary (space-separated 8-bit values): ")
    print("Text:", color.r +  binary_to_text_soosun(user_binary))

else:
    print("Invalid choice.")
