def vigenere_v3(message, key, direction=1):
    key_index = 0
    ascii_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    final_message = ''

    for char in message:       
        # Find the right key character to encode/decode
        key_char = key[key_index % len(key)]
        key_index += 1

        # Define the offset and the encrypted/decrypted letter
        offset = ascii_characters.index(key_char)
        index = ascii_characters.find(char)
        new_index = (index + offset*direction) % len(ascii_characters)
        final_message += ascii_characters[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
