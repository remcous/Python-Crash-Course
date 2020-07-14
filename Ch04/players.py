players = ['charles', 'martina', 'michael', 'florence', 'eli']
# prints a sublist containing elements starting at index 0 not including final index 3
print(players[0:3])

# if you omit first index, python will start at beginning of the list
print(players[:4])

# similarly omiting the last index, python will include up to the end of the list
print(players[2:])

# negative index indicates nth element from the end
print(players[-3:])

print("Here are the first 3 players on my team:")
for player in players[:3]:
	print(player.title())