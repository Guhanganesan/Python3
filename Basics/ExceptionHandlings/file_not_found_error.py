try:
    path='D:\\python\\myfile.text'
    data=open(path,'r')
    print(data)

except FileNotFoundError:
    print("The file is not found")

