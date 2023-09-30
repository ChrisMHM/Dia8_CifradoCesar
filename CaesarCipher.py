import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarCipher(text, shift, direction):
    alphabetSize = len(alphabet)
    message = ""

    for letter in text:
        if not letter in alphabet:
            message += letter
        else:
            shift %= alphabetSize
            if direction == "encode":
                newIndex = alphabet.index(letter) + shift
                if newIndex > alphabetSize:
                    newIndex -= alphabetSize
            else:
                newIndex = alphabet.index(letter) - shift
                if newIndex < 0:
                    newIndex += alphabetSize
            newLetter = alphabet[newIndex]
            message += newLetter

    print(f"Here's the {direction}d result: {message}")

print(logo.logoList)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if not (direction == "encode" or direction == "decode"):
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesarCipher(text, shift, direction)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if again == "no":
        break

    print("")