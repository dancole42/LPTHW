

def whiletest(x, t):
  i = 0
  numbers = []
  while i < x:
    print "At the top is %d" % i
    numbers.append(i)

    i = i + t
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
  return numbers
  
whiletest(30, 4)
  
print "The numbers: "

for num in numbers:
  print num