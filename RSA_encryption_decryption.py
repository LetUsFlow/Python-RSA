def encrypt(msg_plaintext, pubic):
    e, n = pubic
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext


def decrypt(msg_ciphertext, private):
    d, n = private
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    return ''.join(msg_plaintext)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    e = int(input("Enter the public key (e): "))
    d = int(input("Enter the private key (d): "))

    msg = input("Enter the message: ")
    print([ord(c) for c in msg])
    encrypted_msg = encrypt(msg, (e, n))
    print("Encrypted msg: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, (d, n)))
