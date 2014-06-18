# Learn Python the Hard Way - Exercise No. 5
name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

def metric(n, u):
	if u == 'lbs':
		return n * 0.453592
	elif u == 'inches':
		return n * 2.52
	else:
		return n

height = metric(height, 'inches')
weight = metric(weight, 'lbs')

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try and get it exactly right
print "If I add %d, %d, and %r, I get %r." % (
	age, height, weight, age + height + weight)
