# AND OR NOT
state = 2>3 or 2==2 # 0 1  => 1
print(state)
if state:
    print("A")  

state = 2<3 or 2==2 # 1 1 => 1
print(state)
if state:
    print("B")


state = 2>3 or 2>2 # 0 0 => 0
print(state)
if state:
    print("C")


state = 2<3 or 2>2 # 1 0 => 1
print(state)
if state:
    print("D")

