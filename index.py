
friends = ['Hanna', 'Oliver', 'Jama', 'Dan']
print(friends) # we print the LIST of friends 

# to access the list you can add index

print(friends[1], friends[2])
# index starts with 0

print(friends[3], friends[1])

print(friends[-2])

# first from the end
print(friends[-1])

# slicing method with :
print(friends[1:3]) # will print #1 and 2 excluding 3

# slicing method with :
print(friends[1:4]) # will print #1 to 3 excluding 4

# slicing method with :
print(friends[:]) # will print the whole list

print(len(friends))
print(friends.index('Oliver'))

