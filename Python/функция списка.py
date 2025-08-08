"""numb = [1, 5, 3, 4, 3]
numb.append(6)
numb.insert(0, 0)
numb.remove(3)
numb.extend([3, 4, 2])
numb.sort()
numb.reverse()
print("length:", len (numb))
"""

n = int(input("Enter number: "))

user_list =[]

b = 0 
while b < n:
    user_list.append(int(input("Enter another number: ")))
    b += 1
print("Your list:", user_list)