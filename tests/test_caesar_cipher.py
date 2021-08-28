
from caesar_cipher import __version__

from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_string():
    assert encrypt("abc", 1) =="bcd"

def test_decrypt_previously_encrypted_string_same_shift():
    encrypt_text=encrypt('abc', 1)
    decrypt_test=decrypt(encrypt_text, 1)
    assert 'abc' == decrypt_test

def test_handle_upper_and_lower_case_letters():
     assert encrypt("AbC", 1) =="BcD"

def test_allow_non_alpha_characters_but_ignore():
    assert encrypt("ab c", 1)=="bc d"
    assert encrypt("ab##c", 1)=="bc##d"

def test_crack_not_50per_english_text():
    encrypt_text = encrypt( "maram", 1 )
    actual = crack( encrypt_text )
    assert actual == "Not an English text."