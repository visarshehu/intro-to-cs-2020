import random
number=random.randint(0,5)
print "I guessed a number from 0 to 5. What was my guess?"
answer=input()
if answer==number:
	print "Congratulations, you won!"
else:
	print "Sorry, you guessed incorrectly!"
