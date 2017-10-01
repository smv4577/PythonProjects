# Sydney Vernatter
# November 28, 2016
# Program 3: Mad Libs
# Collaboration Statement:
# Algorithm: Ask user for input file and output file. Error handle. If error, ask user for file name again. Read input
# file line by line, looking for the special characters "<" or ">". Ask user for the specifiv word in between the <>.
# After asking for all special words, output text to the file. Ask user if they want to see the story
# they created. Ask if they want to write another MadLibs.

import madLibsFunctions


def main():
    done = False
    print("Welcome to the game of Mad Libs.")
    print("I will ask you to provide several words and phrases to fill in a mad lib story.")
    print("The result will be written to an output file.")

    while done == False:
        input_file, output_file, output_f = madLibsFunctions.getFile()
        madLibsFunctions.readFile(input_file, output_file)
        madLibsFunctions.closeFile(input_file, output_file)
        madLibsFunctions.writeStory(output_f)
        done = madLibsFunctions.anotherStory()

main()
