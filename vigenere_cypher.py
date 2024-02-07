def vigenere(message, key):
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
