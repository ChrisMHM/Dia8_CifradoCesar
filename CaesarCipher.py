alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    alphabetSize = len(alphabet)
    encryptedText = ""

    for letter in text:
        if not letter in alphabet:
            encryptedText += letter
        else:    
            newIndex = alphabet.index(letter) + shift

            if newIndex >= alphabetSize:
                newIndex = newIndex % alphabetSize

            newLetter = alphabet[newIndex]
            encryptedText += newLetter

    return encryptedText

encryptedText = encrypt(text, shift)
print(encryptedText)