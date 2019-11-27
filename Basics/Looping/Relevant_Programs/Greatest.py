data=int(input("Enter Number how many numbers"))
mind=0
for i in range(1,data+1):
    print("Enter number",i)
    user_data=int(input())
    if user_data>mind:
        mind=user_data

print("Greatest number is ", mind)
     