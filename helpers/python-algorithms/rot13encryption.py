def rot13(text):
    """
    Rot13 encryption
    """
    encrypted = ''
    for ch in text:
        if not ch.isalpha():
            encrypted += ch
        else:
            rotatedLetterOrdinal = ord(character) + 13
            # If adding 13 pushes the letter past Z, subtract 26: 
            if character.islower() and rotatedLetterOrdinal > 122:
                rotatedLetterOrdinal -= 26
            if character.isupper() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26
            # Add the encrypted letter to encryptedText:
            encryptedText += chr(rotatedLetterOrdinal)
    return encryptedText