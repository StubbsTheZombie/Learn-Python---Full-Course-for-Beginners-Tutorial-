
lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]

print(friends)

#extend function append a list to the end of another list

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.extend(lucky_numbers)
print(friends)

#append function adds another element

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.append("Creed")
print(friends)

#insert takes two parameters in order to add new element to a specific position

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.insert(1, "Kelly")
print(friends)

#remove function removes elements

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.remove("Jim")
print(friends)

#clear deletes the entire list

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.clear()
print(friends)

#pop pops an item off the list, removing the last element

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.pop()
print(friends)

#index tells u which position the element is in

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
print(friends.index("Toby"))

#count counts the number of elements in a list

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Toby", "Angela"]

print(friends.count("Jim"))

#sort function puts the list in order

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.sort()
print(friends)

#reverse function puts the list in reverse order

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends.reverse()
print(friends)

#copy function copies the elements of a list

lucky_numbers = [4,8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Toby", "Angela"]
friends2 = friends.copy()
print(friends2)


