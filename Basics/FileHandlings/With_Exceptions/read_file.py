try:
    file = open("Test\\test.txt", 'r')
    # data = file.read() # All data
    # data = file.readline() # First Line
    data = file.readlines()
    """
    ['hello vathithra how are you\n', 'Where are you going\n', 'Where are you going']
    """
    print(data)
except Exception as err:
    print("Url not found!", err)