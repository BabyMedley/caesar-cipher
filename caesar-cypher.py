import random

# chr(1), ord("a")

def make_key():
    global key
    key = random.randint(-10,10)

mode = input("Encrypt or Decrypt: ").lower()

#-------------------------------------------------------------------------------

if mode == "encrypt":
    make_key()
    message = list(input("Message: ").lower())
    new_message = ""
    for character in message:
        if ord(character) >= ord("a") and ord(character) <= ord("z"):
            replace = chr(ord(character) + key)
            if replace > "z":
                replace = chr(ord(character) - 26 + key)
            new_message += replace
        else:
            replace = character
            new_message += replace
    print("Encrypted Text: " + new_message)
    print("Key: " + str(key))
#-------------------------------------------------------------------------------

if mode == "decrypt":

    message = list(input("Encrypted Message: ").lower())
    new_message = ""
    key = int(input("Key: "))
    for character in message:
        if ord(character) >= ord("a") and ord(character) <= ord("z"):
            replace = chr(ord(character) - key)
            if replace < "a":
                replace = chr(ord(character) + 26 - key)
            new_message += replace
        else:
            replace = character
            new_message += replace
    print("Decrypted Text: " + new_message)
