# import morse_code.json to get key-value pairs of morse code characters and their corresponding text characters

# i like color in the terminal window so i'll start with that
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

# need 2 functions to translate from text to morse, and from morse to text

def text_to_morse(text, morse_dict)


    return (morse_code)




def morse_to_text(morse_code, morse_dict):


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