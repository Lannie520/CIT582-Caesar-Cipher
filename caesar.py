def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    list = []
    for character in plaintext:
        a = chr(ord(character) + key)
        list.append(a)
    ciphertext = list
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    list = []
    for character in ciphertext:
        b = chr(ord(character)- key)
        list.append(b)
    plaintext = list
    return plaintext

if __name__ == '__main__':
    print(encrypt(1, "WELL"))
    print(decrypt(1, "DONE"))

