"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE

def encode(text):
    """
    Encodes the given text into Morse code.
    Words are separated by a pipe (|) and letters by a space.
    """
    ## her kelimeyi ayrı ayrı dön
    ## her kelimenin morse karşılığını bul çağır
    ## kelimeleri depola sakla
    ##sonra joinle returnle
    words = text.split()
    encoded_text = []
    
    for word in words:
        print(word)
        morse = encode_word(word)
        encoded_text.append(morse)
    return "|".join(encoded_text)


def encode_word(word):
    """
    Encodes a single word into Morse code.
    Letters are separated by a space.
    """
    # her harfi morse koduna dönüştür. 
    # sonra tek tek baralarında boşluk kullanarak birleştirip return etmem gerekir.
    
    ## split ile parçalara ayırabilirim -- for döngü kullanarak buna ihtiyaç kalmadan her harfte dolaşabilirim
    ## döngü ile her parçayı dolaş
    ## her parçanın karşılığını mors olarak bul çağır
    ## yeni listede saklayalım
    ## sonra da aralarında boşluk bırakarak birleştirelim
    encoded = []
    for char in word:
        morse = MORSE[char.upper()]
        encoded.append(morse)
    
    return " ".join(encoded)
    
    

if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_TEXT = "abc"
    ENCODED_TEXT = encode_word(EXAMPLE_TEXT)
    print(f"Encoded word '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")

    # Example usage for a sentence
    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
