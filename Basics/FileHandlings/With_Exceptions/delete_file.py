import os 
try:
    file_path = "Test\\test.txt"
    os.remove(file_path)

except Exception as err:
    print("Url not found!", err)