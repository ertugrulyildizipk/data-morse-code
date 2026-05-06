from morse.mapping import MORSE

ANTIMORSE = {
    
}
for key, value in MORSE.items():
    ANTIMORSE[value] = key


def decode(morse_text):
    morse_words = morse_text.split("|")
    
    decoded_words = []
    for word in morse_words:
        antimorse = decode_word(word)
        decoded_words.append(antimorse)
    return " ".join(decoded_words)

def decode_word(morse_word):
    ## '.- -... -.-.'
    
    ## adım 1 her karaktere parçala
    ## döngü yap 
    ## her karakterin antimors unu çağır
    ## çağırdıklarını depola list içine at
    ## joinle ve returnle
    morse_letters = morse_word.split()
    
    decoded_word = []
    for char in morse_letters:
        antimorse = ANTIMORSE[char]
        decoded_word.append(antimorse)
        
    return "".join(decoded_word)
    



if __name__ == "__main__":
    EXAMPLE_TEXT = '.- -... -.-.'
    ENCODED_TEXT = decode_word(EXAMPLE_TEXT)
    print(f"decoded_code '{EXAMPLE_TEXT}' to word: '{ENCODED_TEXT}'")

    # Example usage for a sentence
    EXAMPLE_TEXT = '.- -... -.-.|.- -... -.-.'
    ENCODED_TEXT = decode(EXAMPLE_TEXT)
    print(f"decoded_code '{EXAMPLE_TEXT}' to word: '{ENCODED_TEXT}'")