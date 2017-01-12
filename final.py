import random 
import os
import time
check='y'
checkrdy ='n'
people=[]
while check == 'y':
	print "Hello, welcome to Secret Santa.Enter the names of the people, reply N when you want to stop to,\"Are there more people?\""
	name= raw_input("Your name:")
	check= raw_input("Are there more people?")
	people.append(name)
	os.system('clear')
lot=people[:]
sop=len(people)
sol=len(lot)
sol=sol-1
sop=sop
for num in range(0,sop):
	if sop/2 != 0 and sol+1==1:
		print "Hey we're sorry but the pool is already divided, better luck next time %s!"% people[num]
	else:
		while checkrdy == 'n':
			print "Hello %s, Are you ready to see the name of the person? Your screen will self-destruct in 5 seconds. Enter Y to see the name of the person"% people[num]
			checkrdy=raw_input()
		if sol+1 == 1:
			lucky=0
		else:
			while True:
				lucky=random.randint(0,sol)
				if people[num] != lot[lucky]:
					break
		os.system('clear')
		print "You are the secret santa of %s"% lot[lucky]
		time.sleep(5)
		lot.pop(lucky)
		checkrdy ='n'
		sol=sol-1