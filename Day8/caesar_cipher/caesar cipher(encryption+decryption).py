import art
print(art.logo)

def cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    d=0
    if direction == 'encode':
        d=1
        def encrypt(text, shift):
            original_text = ""
            for letter in text:
                shifted_position = alphabet.index(letter) + shift
                cipher_text = alphabet[shifted_position]
                original_text += cipher_text
            print(original_text)

        encrypt(text, shift)
    elif direction == 'decode':
        d=1
        def decrypt(text, shift):
            original_text = ""
            for letter in text:
                shifted_position = alphabet.index(letter) - shift
                cipher_text = alphabet[shifted_position]
                original_text += cipher_text
            print(original_text)

        decrypt(text, shift)
    else:
        print("please enter valid direction \nType 'encode' to encrypt, type 'decode' to decrypt:\n")
        d=1
    while d>0:
        restart=input("Type 'yes' if you want to go again. Otherwise, type 'no': \n").lower()
        if restart == "no":
                print("Goodbye")
                break
        else:
            cipher()
cipher()