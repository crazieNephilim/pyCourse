import binascii

def main():
    test = 'Hello_World'
    print(test[4:])
    word = 'car'
    print binascii.hexlify(word)
    print binascii.hexlify(word).decode("hex")

    print type(word)

main()