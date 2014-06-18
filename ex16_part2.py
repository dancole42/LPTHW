from sys import argv
script, filename = argv

ex15test = open(filename)

print ex15test.read()
print script
print filename

ex15test.close()