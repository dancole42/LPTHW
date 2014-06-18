# Learn Python the Hard Way - Exercise No. 15
from sys import argv

#Assigns the script and file name to argv.
script, filename = argv

#Open the supplied filename as an object called txt.
txt = open(filename)

#Intro txt and prints the contents of the txt object.
print "Here's your file %r:" % filename
print txt.read()

#Prompts the user to re-enter a file name, which
#it then opens as an object called txt_again.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()