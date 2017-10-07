print()
print("Welcome to the text dungeon :) ")
print("Do you go through the door 1 or 2?")

door = input("> ")

if door == '1':
	print("There is a nice vampire asking you if you enjoy your life.")
	print("What do you do ?")
	print("1. Tell a joke and try it to be funny")
	print("2. Say you're going to come again later because you forgot to make yourself a tea.")

	vampire = input("> ")

	if vampire == "1":
		print("Congrats, the vampire is bored and just want to chat.")
	elif vampire == "2":
		print("Sorry, the vampire wants to have some fun and keeps you here forever...")
	else:
		print("You really have only door 1 and 2 only. Type it correctly ;-) ")

