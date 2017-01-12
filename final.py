import random 
import os
check='y'
i=0
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
sop=sop-1
for num in range(0,sop):
	print "Hello %s, Are you ready to see the name of the person? Your screen will self-destruct in 10 seconds."% people[num]
	print people
	if sol== 1:
		lucky=0
	else:
		while True:
			lucky=random.randint(0,sol)
			if people[num] == lot[lucky]:
				break
	print "You are the secret santa of %s"% lot[lucky]
	print people
	lot.pop(lucky)

	sol=sol-1