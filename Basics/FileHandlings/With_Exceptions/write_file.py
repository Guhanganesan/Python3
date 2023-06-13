try:
    # path relative path, absolute path
    # Relative current location => Test\\test.txt
    # Absolute => upto drive "F:\\Test\\test.txt"
    file = open("Test\\test.txt", 'w')
    file.write("hello vathithra how are you")
    # print(100)

except Exception as err:
    # raise
    print("Url not found!", err)