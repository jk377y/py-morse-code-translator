# needed a key:value dictionary to translate morse code < == > text
morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/' }

# because I like colors
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

# functions to translate text to morse code
def text_to_morse(text, morse_code_dict): # will accept user input and dictionary values
    morse_code = [] # list to store morse code
    for char in text.upper(): # convert text to uppercase
        morse_char = morse_code_dict.get(char) # get morse code for character from dictionary
        if morse_char: # if morse code exists
            morse_code.append(morse_char) # append morse code to list
    return ' '.join(morse_code) # join morse code list to return a string

# function to translate morse code to text
def morse_to_text(morse_code, morse_code_dict): # will accept user input and dictionary values
    text = [] # list to store text
    morse_code_words = morse_code.split('/') # split morse code into words using '/' as delimiter
    for word in morse_code_words: # iterate through words
        morse_code_chars = word.split(' ') # split words into characters using ' ' as delimiter
        word_text = '' # variable to store text for word
        for morse_char in morse_code_chars: # iterate through characters
            if morse_char == '': # if character is empty
                continue # skip to next character; this is to handle double spaces between words
            char = next((key for key, value in morse_code_dict.items() if value == morse_char), None) # get character for morse code from dictionary if it exists else None
            if char: # if character exists
                word_text += char # append character to word text
        text.append(word_text) # append word text to text list
    return ' '.join(text) # join text list to return a string

while True: # loop to display menu and accept user input until user exits
    print("\n==== Morse Code Translator ====")
    print("1. Text to Morse code")
    print("2. Morse code to Text")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ") # accept user input

    if choice == "1":
        text = input("Enter the text to translate: ") # accept user input
        morse_code = text_to_morse(text, morse_code_dict) # call function to translate text to morse code
        print(f"{GREEN}Morse Code Value:{RESET} {BLUE}{morse_code}{RESET}") # print morse code value

    elif choice == "2":
        morse_code = input("Enter the Morse code to translate: ") # accept user input
        text = morse_to_text(morse_code, morse_code_dict) # call function to translate morse code to text
        print(f"{GREEN}Text Value:{RESET} {BLUE}{text}{RESET}") # print text value
    
    elif choice == "3":
        print(f"Thank you for using the {RED}Morse Code Translator{RESET}. Goodbye!") # print exit message
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.") # print error message if user enters invalid choice