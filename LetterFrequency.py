#LetterFrequency.py
#Name:Nomaan Ahmed 
#Date:2/22/25
#Assignment:Lab 5 

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter
    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1
    for char in message:
        #find the position in the alphabet
        if char in alpha:
            position = alpha.find(char)
            #Increase the frequency at that position
            freq[position] += 1

        msg = msg.lower()  # Convert the message to lowercase for case-insensitive counting
    for char in msg:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            freq[char] += 1
    
    return freq
            
    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.
    def createOutput(freq, alpha):
     output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Hello World")
    countLetters(msg)


if __name__ == '__main__':
  main()
