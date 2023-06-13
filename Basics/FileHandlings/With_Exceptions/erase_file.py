try:
    file = open("Test\\test.txt", 'w')
    file.truncate()

except Exception as err:
    print("Url not found!", err)