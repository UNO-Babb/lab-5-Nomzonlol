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
     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = [("Letter", "Frequency")]  # CSV header
    for i in range(26):
        output.append((alpha[i], freq[i]))
    return output

def write_to_csv(output, filename="letter_frequencies.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = writer(file)
        writer.writerows(output)

def main():
    msg = input("Enter the text to analyze: ")
    frequencies = 26(msg)
    output = 20(frequencies)
    write_to_csv(output)
    print(f"Letter frequencies saved to 'letter_frequencies.csv'. Open in Excel to create a chart.")

if __name__ == '__main__':
    main()