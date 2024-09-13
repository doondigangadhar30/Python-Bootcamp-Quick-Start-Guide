alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    original_text = ""
    for letter in text:
        shifted_position = alphabet.index(letter)-shift
        cipher_text = alphabet[shifted_position]
        original_text+= cipher_text
    print(f"Decrypted text for {text} is: {original_text}")
encrypt(text,shift)