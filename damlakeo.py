from random import randint

player = input()
computer = randint(0,2)

if computer == 0:
	computer = "dam"
if computer == 1:
	computer = ("keo")
if computer == 2:
	computer = ("la")
print(computer)
if player == computer:
	print("hoa")

else:
	if player == "keo":
		
		if computer == "la":
			print("win")
		else:
			print("lose")
	if player == "la":
		if computer == "keo":
			print("lose")
		
		else:
			print("win")
	if player == "dam":
		if computer == "keo":
			print("win")
		else:
			print("lose")
		