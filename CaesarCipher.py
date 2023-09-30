alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesarCipher(text, shift, direction):
    alphabetSize = len(alphabet)
    message = ""

    for letter in text:
        if not letter in alphabet:
            message += letter
        else:
            shift = shift % alphabetSize
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

    print(message)