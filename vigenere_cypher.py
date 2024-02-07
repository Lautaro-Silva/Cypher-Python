## Add Vigenere encryption method, where each character of my text is encypted using a different shift in the alphabet given by a custom_key

def vigenere_v1(message, key):
    key_index = 0 # key_index keeps track of which character from the key is being used
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            key_char = key[key_index % len(key)] # This line selects the character from the key to use for encoding and %len(key) ensures that if the message is longer than the key, the key characters will be repeated cyclically.
            key_index += 1

            offset = alphabet.index(key_char) # Similarly to fixed shift method, the offset here is determined by the placement on the alphabet of the currect character of the key
            index = alphabet.find(char) # Current position of the character to be encypted
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

text = 'Hello Zaira'
custom_key = 'python'

encryption = vigenere(text, custom_key)
print(encryption)


## Also i can implement a decryption method using the same cypher

def vigenere_en_de(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

## Solve the error of wrong encyption and decryption of special symbols and add default functions for en and decryption for clarity

def vigenere_v2_with_decryption(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]  
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
    
encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)

## Note that here as well as the other encyption methods i can using add numerical and ASCII symbols to my alphabet and that may solve the need for the if/else clause
