# Morse code dictionary
char_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

# Reverse dictionary for decoding
morse_to_char = {}  
for char, morse in char_to_morse.items(): 
    morse_to_char[morse] = char  

def encode(text):
    #Converting text to Morse code.
    result = []
    for ch in text.upper():
        if ch == " ":
            result.append("/")  # word gap
        elif ch in char_to_morse:
            result.append(char_to_morse[ch])
        else:
            result.append("?")  # unknown character that is not in our dictionary

    return " ".join(result)


def decode(morse_code):
    #Converting Morse code to text.
    result = []
    parts = morse_code.split(" ")
    for code in parts:
        if code == "/":
            result.append(" ")
        elif code in morse_to_char:
            result.append(morse_to_char[code])
        else:
            result.append("?")  # unknown morse sequence
    return "".join(result)


def customize_dictionary():
    #In order to customise the morse dictionary
    while True:
        print("\n--- Customize Morse Dictionary ---") # Menu for customisations to be made
        print("1. Add New Mapping")
        print("2. Edit Existing Mapping")
        print("3. Delete Mapping")
        print("4. View Dictionary")
        print("5. Go Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            char = input("Enter character to add: ")
            char=char.upper()
            if char in char_to_morse: #checking if already exists
                print(" Character already exists! Use Edit option instead.")
            else:
                morse = input("Enter Morse code for it: ")
                char_to_morse[char] = morse
                morse_to_char[morse] = char
                print("Mapping Added Successfully!")

        elif choice == "2":
            char = input("Enter character to edit: ")
            char=char.upper()
            if char not in char_to_morse: #checking if does not exists
                print("Character not found in dictionary!")
            else:
                morse = input(f"Enter new Morse code for {char}: ")
                old_morse = char_to_morse[char]
                del morse_to_char[old_morse] #removing old data and adding new
                char_to_morse[char] = morse
                morse_to_char[morse] = char
                print("Mapping Updated Successfully!")

        elif choice == "3":
            char = input("Enter character to delete: ")
            char=char.upper()
            if char in char_to_morse:
                morse = char_to_morse[char]
                del char_to_morse[char]
                del morse_to_char[morse] #removing from both thse dictionaries
                print(" Mapping Deleted Successfully!")
            else:
                print("Character not found!")

        elif choice == "4":
            print("\n--- Current Morse Dictionary ---")
            for char, morse in char_to_morse.items():
                print(f"{char} : {morse}") #displaying one by one

        elif choice == "5":
            break

        else:
            print("Invalid option! Try again.")


text=input("Enter your String: ")
print(f"Encoding {text}")
encoded = encode(text)
print(encoded)

print("\nDecoding back:")
decoded = decode(encoded)
print(decoded)

while True:
    print("\n" + "=" * 40)
    print("      MORSE CODE TRANSLATOR")
    print("=" * 40)
    print("1. Encode Text to Morse")
    print("2. Decode Morse to Text")
    print("3. Show Morse Dictionary")
    print("4. Edit Morse Dictionary")
    print("5. Exit")
    print("=" * 40)
    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("\nEnter text to encode: ")
        print("Morse Code:", encode(text))

    elif choice == "2":
        morse = input("\nEnter Morse code to decode: ")
        print("Text:", decode(morse))

    elif choice == "3":
        print("\nMORSE CODE REFERENCE TABLE")
        for char, morse in char_to_morse.items():
            print(f"{char} : {morse}")
    
    elif choice =="4":
        customize_dictionary()

    elif choice == "5":
        print("\nExiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")