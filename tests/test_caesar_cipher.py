
from caesar_cipher import __version__

from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_string_with_given():

    assert encrypt("abc", 1) =="bcd"


def test_decrypt_previously_encrypted_string_same_shift():
    orginal_text="abc"
    encrypt_text=encrypt(orginal_text, 1)
    decrypt_test=decrypt(encrypt_text, 1)

    assert orginal_text == decrypt_test

def test_encryption_should_handle_upper_and_lower_case_letters():

     assert encrypt("AbC", 1) =="BcD"


def test_encryption_should_allow_non_alpha_characters_but_ignore():

    assert encrypt("a@bc", 1)=="b cd"



def test_decrypt_encrypted_version():

    original_text="Maram"
    crack_test=(crack(original_text))
    
    assert crack_test == original_text