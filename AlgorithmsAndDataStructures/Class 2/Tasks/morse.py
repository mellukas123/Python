MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def morse_to_text(morse_code):
    # Split the input Morse code by spaces
    words = morse_code.split('   ')  # Splitting by 3 spaces to separate words
    translated_words = []

    for word in words:
        letters = word.split(' ')  # Splitting by single space to separate letters
        translated_word = ''.join(MORSE_CODE[letter] for letter in letters)
        translated_words.append(translated_word)

    return ' '.join(translated_words)


# Example usage
print(morse_to_text('.... . -.--   .--- ..- -.. .'))  # Output: HEY JUDE
print(morse_to_text('... --- ...'))  # Output: SOS
print(morse_to_text('.-'))  # Output: A
