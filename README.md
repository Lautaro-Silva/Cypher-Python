## Cypher-Python
I will test diferent types of password/text cyphers using Python. Firstly a Ceaser or fixed-shift of characters to encrypt the message and then using the Vigenere cypher, where given a custom key, each character of the text given for encyption is shifted a different ammount of characters (dependent of the key). In the final version i also add the posibility to decrypt messages as well as encrypt them.

After some research the main weakness of the Vigenere cypher is: '(...) the repeating nature of its key. If a cryptanalyst correctly guesses the key's length n, the cipher text can be treated as n interleaved Caesar ciphers, which can easily be broken individually. The key length may be discovered by brute force testing each possible value of n, or Kasiski examination and the Friedman test can help to determine the key length'

# Future modificactions:
Add the running key variant of the Vigenère cipher, where for the key this version uses a block of text as long as the plaintext. Since the key is as long as the message, the Friedman and Kasiski tests no longer work, as the key is not repeated.
