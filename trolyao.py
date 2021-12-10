import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("robot: i'm listening")
	audio = robot_ear.listen(mic)

try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""
print("you:"+you)



if you == "":
	robot_brain = "i cant hear you"
elif you == "hello":
	robot_brain = "hello hoang long"
elif you == "today":
	robot_brain = "thu 5"	
else:
	robot_brain = "i'm fine thank u, and you"

print(robot_brain)