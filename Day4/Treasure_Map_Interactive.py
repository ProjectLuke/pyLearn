# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Can just replace the box with an x through the input provided
#Write your code below this row 👇
list_position=list(position)
x = int(list_position[1])
y = int(list_position[0])

list_position = [int(i) for i in list_position]
#test_list = [int(i) for i in test_list]

map[x-1][y-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#Dr. Angela Solution
# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"