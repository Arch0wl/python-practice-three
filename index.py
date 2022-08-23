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

friendsgroup = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friendsgroup)

# sort
friendsgroup.sort()
print(friendsgroup)

friendsgroup.sort(reverse=True) #will print reverse
print(friendsgroup)

friendsgroup.reverse()
print(friendsgroup)

cars.reverse()
print(cars)
# print max number
print(max(cars))

# print min number
print(min(cars))

#statements, adding one more name to the list 
friendsgroup.append('Levie')
print(friendsgroup)

# insert statemnt 
friendsgroup.insert(1,'Melena')
print(friendsgroup)

# remove statemnt 
friendsgroup.remove('Melena')
print(friendsgroup)

del friendsgroup[2]
print(friendsgroup)

new_friends=friendsgroup[:]
print(friendsgroup)
print(new_friends)

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.insert(1,'TerryG')
print(friends) 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends[2]='TerryG'
print(friends)

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.extend(cars)
print(friends)

# remove 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.remove('Terry')
print(friends)

# pop, when you use pop by default it will grab the latest in array


friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.pop()
print(friends)

# or specify wht to remove: 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.pop(2)
print(friends) 

# or specify wht to remove: 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.pop(-1)
print(friends) 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.clear()
print(friends) 

# delete

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends
print(friends) # friends is not defined 

# delete

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends[2]
print(friends) 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends[2]
new_friends = friends[:]
print(friends)
print(new_friends)


#split and join 

msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list))


print(''.join(msg.split()))