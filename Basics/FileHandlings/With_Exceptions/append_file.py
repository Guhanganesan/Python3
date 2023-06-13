try:
    file = open("Test\\test.txt", 'a')
    L =  ['hello vathithra how are you\n', 'Where are you going\n', 'Where are you going\n']
    # file.write("\nWhere are you going")

    for item in L:
        file.write(item)

except Exception as err:
    print("Url not found!", err)