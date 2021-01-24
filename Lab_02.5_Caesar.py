charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numchars = len(charset)


def caesar_encrypt(message, key):
    """put an appropriate function doc string here"""

    message = message.upper()  # convert message to upper case
    result = ''  # initialise result as empty string

    for ch in message:
        if ch in charset:  # if is is actually a letter
            # find the corresponding result letter in the alphabet
            new = (charset.find(ch) + key) % len(charset)
            result = result + charset[new]
        else:
            result = result + ch

    return result  # returns result so it can be reused


def caeser_decrypt(message, key):
    """put an appropriate function doc string here"""

    message = message.upper()  # convert message to upper case
    result = ''

    for ch in message:
        if ch in charset:  # if is is actually a letter
            # find the corresponding result letter in the alphabet
            new = (charset.find(ch) - key) % len(charset)
            result = result + charset[new]
        else:
            result = result + ch

    return result


def caesar_crack(cipher):
    """put an appropriate function doc string here"""
    
    for key in range(len(charset)):
        translated = ''

        for symbol in cipher:
            if symbol in charset:
                num = charset.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(charset)

                translated = translated + charset[num]
            else:
                translated = translated + symbol
    
        print(f'Key {key}: {translated}')

def main():
    # test cases
    key = 2
    plaintext = 'Hello Suzanne'
    cipher = 'THIS IS MY SECRET MESSAGE'
    # crackme = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA'
    # call functions with text cases
    encrypted = caesar_encrypt(plaintext, key)
    decrypted = caeser_decrypt(encrypted, key)

    print(encrypted)
    print(decrypted)
    caesar_crack(cipher)
    # caesar_crack(crackme) # remove comment to test cracking

if __name__ == "__main__":
    main()
