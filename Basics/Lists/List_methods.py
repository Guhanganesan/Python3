#List Methods
L=[]
# List Slicing 
L=["A","B","C","D","E"]
print(L[0]) # A
print(L[0:3]) # ['A', 'B', 'C']
print(L[-3:-1]) # ['C', 'D']
print(L[::-1])#reverse ['E', 'D', 'C', 'B', 'A']
print(L[2:]) # ['C', 'D', 'E']
print(L[:4]) # ['A', 'B', 'C', 'D']
print(L[::]) # ['A', 'B', 'C', 'D', 'E']
print(L[:]) # ['A', 'B', 'C', 'D', 'E']
print(L[-5::1]) # ['A', 'B', 'C', 'D', 'E']
# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13]
print(List[1:12:2]) # [2, 4, 6, 8, 10, 12]
print(List[::2]) # [1, 3, 5, 7, 9, 11, 13]
print(List[::]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(List[::-2]) # [13, 11, 9, 7, 5, 3, 1]
print(List[::-3]) # [13, 10, 7, 4, 1]
print(List[:5:-2]) # [13, 11, 9, 7]
print(List[10::2]) # [11, 13]
print(List[1:1:1]) # []
print(List[-1:-1:-1]) # []
print(List[:0:]) # []

L=["A","B","C","D","E"]
print(len(L)) # 5
L.pop() # ['A', 'B', 'C', 'D'] Remove Last
L.append("F") # ['A', 'B', 'C', 'D', 'F'] Add Last
L.pop(1) # ['A', 'C', 'D', 'F'] Remove by index
L.insert(1,"K") # ['A', 'K', 'C', 'D', 'F'] Insert by index
del(L[0]) # ['K', 'C', 'D', 'F'] Delete by index
L.extend(["L","M","N"]) # ['K', 'C', 'D', 'F', 'L', 'M', 'N'] Extend new
L.remove("K") # ['C', 'D', 'F', 'L', 'M', 'N'] Remove by element
L.reverse() # ['N', 'M', 'L', 'F', 'D', 'C'] 
print(L.count("M")) # 1
copy=L.copy() # ['N', 'M', 'L', 'F', 'D', 'C']
clear=copy.clear() # None
L.sort() # ['C', 'D', 'F', 'L', 'M', 'N']
print(L.__contains__("D")) # True
L.__delitem__(0)  # # ['D', 'F', 'L', 'M', 'N']
item=L.__getitem__(0) # D
L[1]="Z" # ['D', 'Z', 'L', 'M', 'N'] Update

"""
random.shuffle(list1)
L =  [1, 3, 2]
print(L*2) # [1, 3, 2, 1, 3, 2]
list1 = [11, 2, 23]
list2 = [11, 2, 2]
print(list1<list2) # False Elements are compared one by one.

s="a@b@c@d"
a=list(s.partition("@"))
print(a)
b=list(s.split("@",3))
print(b)
['a', '@', 'b@c@d']
['a', 'b', 'c', 'd']

a=[14,52,7]
b=a.copy()
print(b is a) False

a=[[]]*3
print(a) # [[], [], []]
a[1].append(7)
print(a) # [[7], [7], [7]]

lst=[3,4,6,1,2]
lst[1:2]=[7,8]
print(lst) # [3, 7, 8, 6, 1, 2]

lst=[[1,2],[3,4]]
print(sum(lst,[])) # [1, 2, 3, 4]

word1="Apple"
word2="Apple"
list1=[1,2,3]
list2=[1,2,3]
print(word1 is word2) True
print(list1 is list2) False

x=[[1],[2]]
print(" ".join(list(map(str,x)))) # [1] [2]

a=165
b=sum(list(map(int,str(a))))
print(b) # 12
"""