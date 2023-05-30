# for simplicity in code, just going to define this here for now, instead of importing the json file
morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/' }

# i like color in the terminal window so i'll start with that
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

# need 2 functions to translate from text to morse, and from morse to text

def text_to_morse(text, morse_code_dict)


    return (morse_code)




def morse_to_text(morse_code, mmorse_code_dict):


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
        text_to_morse()

    elif choice == "2":
        morse_to_text()
    
    elif choice == "3":
        break

    else:
        print("Invalid choice!")