# Creates exercise .py files for Learn Python the Hard Way

for i in range(1, 53):
	with open('ex' + str(i) + '.py', 'w+') as f:
		f.write ("# Learn Python the Hard Way - Exercise No. %s\n" % str(i))
