# Creates exercise .py files for Learn Python the Hard Way

for i in range(1,53):
	f = open('ex' + str(i) + '.py', 'w+')
	f.write ("# Learn Python the Hard Way - Exercise No. %s\n" % str(i))
	if f.closed != True:
		f.close()