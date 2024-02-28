my_list = []

#append 10,20,30,40 to the empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# insert 15 to the second position in the list
my_list.insert(1, 15)
print(my_list)
# extend the list with 50,60,70
my_list.extend([50, 60, 70])
print(my_list)
# remove the last element from the list
del my_list[-1]
print(my_list)
# sort the list in ascending order
my_list.sort()
print(my_list)
# find and print the index of value 30
index_of_30 = my_list.index(30)
print("index_of_30:", index_of_30)

