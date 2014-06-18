# Learn Python the Hard Way - Exercise No. 17
from sys import argv
from os.path import exists
open(argv[2], 'w').write(open(argv[1]).read())
open(argv[1]).close()
open(argv[2]).close()

"""
print argv[1]
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "Filesize: %d " % len(indata) + "File exists? %r" % exists(to_file)


#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
"""