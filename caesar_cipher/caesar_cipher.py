
from cryptography.fernet import Fernet
import cryptography


def encrypt(plain, key):
    encrypted_text = ""

    for char in plain:

        if (char.isupper()):
            if char.isalpha() == False:
                encrypted_text +=" "
            else:
                encrypted_text += chr((ord(char) + key-65) % 26 + 65)
  
        else:
            if char.isalpha()== False:
                encrypted_text +=" "
            else:
                encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
      

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)

def crack(message):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    print("original string: ", message)
    print("encrypted string: ", encMessage)
    decMessage = fernet.decrypt(encMessage).decode()
  
    return( decMessage )


