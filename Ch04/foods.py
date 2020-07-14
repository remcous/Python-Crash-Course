my_foods = ['pizza', 'falafel', 'carrot cake']
# copies the list by producing a sublist slice including the entire list
friend_foods = my_foods[:]
# friend_foods = my_foods would not work as friend_foods will point to the same list as my_foods

# prove that the lists are independent
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are: ")
print(my_foods)

print("\nMy friends favorite foods are: ")
print(friend_foods)