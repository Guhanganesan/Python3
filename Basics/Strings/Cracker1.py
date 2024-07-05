S = "A BC CDE" # Input
# E DC CBA
un_index = [i for i in range(0, len(S)) if S[i] == ' ']
match_index = [i for i in range(0, len(S)) if S[i] != ' ']
print(un_index)
print(match_index)
R=S[::-1]
R_L=list(R)
print(R_L)
R_L_C = [d for d in R_L if d!=' ']
print(R_L_C)
R_L_J = "".join(R_L_C)
print(R_L_J)
my_size = [None]*len(S)
print(my_size)

count=0
for i in range(0, len(my_size)):
    if i in un_index:
        my_size[i]=' '
    if i in match_index:
        my_size[i]=R_L_J[count]
        count+=1
        
print("".join(my_size))

"""
Input : "A BC CDE" 
[1, 4]
[0, 2, 3, 5, 6, 7]
['E', 'D', 'C', ' ', 'C', 'B', ' ', 'A']
['E', 'D', 'C', 'C', 'B', 'A']
EDCCBA
[None, None, None, None, None, None, None, None]
E DC CBA
"""