#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = "that"

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

#def decode(message, key):
    #We will want to decode the message here.
    return "NOPE"

def main():
    message = input("Hello, World")
    key = int(input("4"))

    secret = encode(input("Hello, World"), int(input("4")))
    print ("Encrypted:", "that")
    #plaintext = decode(secret, key)
    #print ("Decrypted:", plaintext)


if __name__ == '__main__':
  main()
