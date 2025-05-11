from morse_dict import MORSE_CODE_DICT

def text_to_morse(text):
    morse_output = ''
    for letter in text:
        morse_code = MORSE_CODE_DICT.get(letter.upper()) # Using .get to prevent KeyError
        if morse_code:
            morse_output += morse_code + ' '
        else:
            print(f"Warning: char '{letter}' not supported and it was ignored.")
    return morse_output.strip()

def main():
    print("Welcome to the Morse Code Converter!")
    user_input = input("Enter your message: ")
    output = text_to_morse(user_input)
    print("Morse code:", output)

if __name__ == "__main__":
    main()