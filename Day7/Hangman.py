import random
word_list = ["aardvark", "baboon", "camel"]
rand_word=random.choice(word_list)
print(rand_word)
key=input("Enter a letter: ").lower()
print(key)
for letter in rand_word:
    if letter ==key:
        print("True")
    else:
        print("False")