__author__ = 'Pavel.Malko'
def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    return "???"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"