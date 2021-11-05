#Import the systems OS
import os

#Checks whether directory is true or false
def Directory():
    check = 'yes'
    while check == 'yes':
        path = input("What directory would you like to add a file to? ")
        #If directory is true
        if os.path.isfile(path) == True:
            file = input("Would you like to change your file?\n(Please type 'yes' or 'no') ")
            #Edit the file input
            if file == 'yes' or file == 'y':
                myFile = open(path, "w")
                #Write on the file
                myFile.write(input("Please enter your name. "))
                myFile.write("\n")
                myFile.write(input("Please enter your address. "))
                myFile.write("\n")
                myFile.write(input("Please enter your phone number. "))

                again = input("Do you need to make changes to your input?\n(Please type 'yes' or 'no') ")
                if again == 'yes' or again == 'y':
                    file = 'yes'
                else:
                    file = 'no'
                    check = 'no'
                    #Prints the text added to the document
                    print("Here is the text you added to your document...\n")
                    myFile = open(path)
                    content = myFile.read()
                    print(content)
                    myFile.close()
            else:
                print("Okay. Have a good day!")
                file = 'no'
                check = 'no'
        else:
            print("You have input a wrong directory, please try again.")
            check = 'yes'

run = 'yes'
while run == 'yes' or run == 'y':
    Directory()
    run = input("\nWould you like to change another directory?\n(Please type 'yes' or 'no') ")
    if run == 'no':
        print("Have a good day!")