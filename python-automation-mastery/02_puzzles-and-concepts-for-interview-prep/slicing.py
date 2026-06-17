my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[0::])
print(my_list[3:6:])
print(my_list[2:6:2])
print(my_list[:6:2])
print(my_list[:6:])
print("-------------------")
print(my_list[::-1]) # Reversing the array using negative step value
print(my_list[:-2:]) # from start till second last item
print(my_list[-2::]) # returns last two elements
print(my_list[-4:-2:1][::-1]) # reversed list of the fourth and third last elements
