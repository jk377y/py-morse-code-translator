# for simplicity in code, just going to define this here for now, instead of importing the json file
morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/' }

# i like color in the terminal window so i'll start with that
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

# need 2 functions to translate from text to morse, and from morse to text

def text_to_morse(text, morse_code_dict):
    morse_code = [] # empty list to store morse code values when translated
    for char in text: # loop through each character in the text
        morse_char = morse_code_dict.get(char) # get the morse code value for each character
        if morse_char: # if the character is in the dictionary
            morse_code.append(morse_char) # add the morse code value to the list
    return (morse_code) # return the list of morse code values




def morse_to_text(morse_code, mmorse_code_dict):
    text = [] # empty list to store text values when translated

    return (text)


# need menu and it should loop until user chooses to exit

while True:
    print("\n==== Morse Code Translator ====")
    print("1. Text to Morse code")
    print("2. Morse code to Text")
    print("3. Exit")

    # get the user's choice
    choice = input("\nEnter your choice (1-3): ")


    if choice == "1":
        text = input("Enter the text to translate: ") # input
        morse_code = text_to_morse(text, morse_code_dict) # call function
        print(f"{GREEN}Morse Code Value:{RESET} {BLUE}{morse_code}{RESET}") # output

    elif choice == "2":
        morse_code = input("Enter the Morse code to translate: ") # input
        text = morse_to_text(morse_code, morse_code_dict) # call function
        print(f"{GREEN}Text Value:{RESET} {BLUE}{text}{RESET}") # output
    
    elif choice == "3":
        print(f"Thank you for using the {RED}Morse Code Translator{RESET}. Goodbye!") # exit
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.") # error message