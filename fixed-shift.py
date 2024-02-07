## This is a text cypher using only a fixed shift in letters as key

def caesar_v1(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
    return encrypted_text


text = 'Hello World'
shift = 3

caesar(text, shift)
caesar(text, 13)

## This function can be made more complete if we add alphanumerical symbols or even all ASCII symbols

def caesar_v2(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'  # an example using alphanumiercal symbols
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
    return encrypted_text
