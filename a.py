from random import randint

player = input()
computer = randint(0,2)

if computer == 0:
	computer = "dam"
if computer == 1:
	computer = "la"
if computer == 2:
	computer = "keo"

print(computer)
if player == "dam":
	if computer == "dam":
		print("hoa")
	if computer == "la":
		print("thua")
	if computer == "keo":
		print("thang")
if player == "la":
	if computer == "dam":
		print("thang")
	if computer == "la":
		print("hoa")
	if computer == "keo":
		print("thua")
if player == "keo":
	if computer == "dam":
		print("thua")
	if computer == "la":
		print("thang")
	if computer == "keo":
		print("hoa")
