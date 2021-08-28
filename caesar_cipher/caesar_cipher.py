import nltk
import re

def encrypt( plain_text, key ):
    encrypted_msg = ""
    for letter in plain_text:
        if letter.isupper():  
            new_letter = chr((ord( letter ) - ord( 'A' )+ key) % 26 + ord( 'A' ))
            encrypted_msg = encrypted_msg + new_letter
        elif letter.islower(): 
            new_letter = chr((ord( letter ) - ord( 'a' )+ key) % 26 + ord( 'a' ))
            encrypted_msg = encrypted_msg + new_letter
        elif letter.isdigit():
            new_numb = ( int( letter ) + key ) % 10
            encrypted_msg = encrypted_msg + str( new_numb )
        else:
            encrypted_msg = encrypted_msg + letter

    return encrypted_msg

def decrypt( encrypted_msg, key ):
    return encrypt( encrypted_msg, -key )


nltk.download('names')
nltk.download('words')
from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()

def count_words(text):
    candidate_words = text.split()
    word_count = 0
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
             # print("english word", word)
            word_count += 1
        else:
            pass
    return word_count

def crack( encrypted_msg_msg ):
    decrypted_msg = ''
    for key in range(26):
        expected = decrypt(encrypted_msg_msg, key)
        word_count = count_words(expected)
        percent = int(word_count / len(expected.split()) * 100)
    if not decrypted_msg :
        decrypted_msg = "Not an English text."
        if percent > 50:
            decrypted_msg = expected

    return decrypted_msg


