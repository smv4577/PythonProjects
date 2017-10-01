# Sydney Vernatter
# November 28, 2016
# Program 3: Mad Libs
# Collaboration Statement: http://anh.cs.luc.edu/ ;


def getFile():
    """
    :return: input_file, output_file, output_f

    Purpose: To ask user for input and output file names. Afterwards, opening those files.
    """
    file = False
    while file == False:
        try:
            input_f = input("Input file name: ")
            input_file = open(input_f, "r")
            file = True
            output_f = input("Output file name: ")
            output_file = open(output_f, "w")
        except FileNotFoundError:
            print("File not found.")
    return input_file, output_file, output_f


def readFile(input_file, output_file):
    """
    Purpose: To read each line in the input file. When seeing the <>, ask the user for the special word. Print the lines
    in the output file.
    """
    line = input_file.readline()
        
    while line != "":
        words = line.split(" ")
        for i in range(len(words)):
            if "<" in words[i] and ">" in words[i]:
                start = words[i].find("<")
                stop = words[i].find(">")
                word = words[i][start+1:stop]
                if word[0] in ("a", "e", "i", "o", "u"):
                    userPick = input("Enter an " + word.replace("-", " ") + ": ")
                else:
                    userPick = input("Enter a " + word.replace("-", " ") + ": ")
                words[i] = userPick
            #words[i].lstrip()
            #'{:10}'.format(output_file.write(words[i] + " "))
            if "\n" in words[i]:
                output_file.write(words[i])
            else:
                output_file.write(words[i] + " ")
        line = input_file.readline()


def closeFile(input_file, output_file):
    """
    :param input_file, output_file

    Purpose: To close the input and output files.
    """
    input_file.close()
    output_file.close()


def writeStory(output_f):
    """
    :param output_f:

    Purpose: To ask user if they want to see the final story. If yes, prints out story.
    """
    print("Your MadLib story has been created.")
    write_story = input("Do you want to see the final story? (Y or N): ").upper()
    if write_story == "Y":
        story = open(output_f, "r")
        for line in story:
            print(line)
        story.close()


def anotherStory():
    """
    :return: done

    Purpose: To ask user if they want to process another MadLab. If yes, repeat. If no, finish.
    """
    again = input("Do you want to process another MadLib? (Y or N): ").upper()
    if again == "Y":
        done = False
    else:
        done = True
        print("Have a good day!")
    return done

