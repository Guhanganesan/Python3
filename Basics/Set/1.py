a={1,4,2,5,7,9,7}
a.add(10)
print(a)
a.update({12,11})
print(a)

a.remove(11)
print(a)

#a.remove(100) #rise the key error if it is not presented

#a.discard(100) #cannot get any error

a.pop() #does not takes any argument
print(a)#remove from first

a.pop()
print(a)
a.discard(7) 
print(a)




