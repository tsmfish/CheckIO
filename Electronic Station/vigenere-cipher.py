__author__ = 'Pavel.Malko'
def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key = [chr((ord(old_encrypted[char]) - ord(old_decrypted[char]) + 26) % 26 + ord('A')) for char in range(len(old_encrypted))]
    keylength = len(key)
    for i in range(1, len(key)):
        for j in range(i, len(key)):
            if key[j] != key[j%i]: break
        else:
            keylength = i
            break
    return "".join([chr((ord(new_encrypted[char]) - ord(key[char % keylength]) + 26) % 26 + ord('A')) for char in range(len(new_encrypted))])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"

    assert decode_vigenere("ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT",
                           "PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI",
                           "XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL") \
                        == "IMALUMBERJACKANDIMOKISLEEPALLNIGHTANDIWO" \
                           "RKALLDAYICUTDOWNTREESISKIPANDJUMPILIKETOPRESSWILDFLOWERSIPUTONWOMENSCLOTHINGANDHANGAROUNDINBARS", 'NotOk'