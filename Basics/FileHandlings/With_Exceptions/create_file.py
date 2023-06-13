try:
    # path relative path, absolute path
    # Relative current location => Test\\test.txt
    # Absolute => upto drive "F:\\Test\\test.txt"
    file = open("Test\\test.txt", 'w')
    if file:
        print("File Created Successfully!")

except Exception as err:
    print("Url not found!", err)