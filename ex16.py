# Learn Python the Hard Way - Exercise No. 16
from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
"""
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
"""

def openFile():
	print "Opening the file..."
	return open(filename, 'r+')

target = openFile()

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
"""
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
"""

line = "This is line 1 \n"
line += "This is line2 \n"
line += "line 3 \n"
print "I'm going to write those to the file."

nl = "\n"
"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
target.write(line)

print "And finally, we close it."
target.close()
target = openFile()
print target.read()
target.close()