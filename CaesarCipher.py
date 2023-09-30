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
            shift = shift % alphabetSize
            newIndex = alphabetSize - (alphabet.index(letter) + shift)
            newLetter = alphabet[newIndex]
            encryptedText += newLetter

    print(encryptedText)

encrypt(text, shift)

def decrypt(text, shift):
    alphabetSize = len(alphabet)
    decryptedText = ""

    for letter in text:
        if not letter in alphabet:
            decryptedText += letter
        else:
            shift = shift % alphabetSize
            newIndex = alphabet.index(letter) - shift
            newLetter = alphabet[newIndex]
            decryptedText += newLetter

    print(decryptedText)

decrypt(text, shift)