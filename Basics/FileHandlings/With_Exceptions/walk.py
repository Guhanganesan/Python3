import os 
try:
    file_path = r"F:\Periyar_Payilagam_Courses\Core_Python\Python\May-2023\Foundations\FileHandlings"
    # os.remove(file_path)
    for dir, sub_dir, file in os.walk(file_path): # 1ngle, [], []
        print("dir: ", dir)
        print("sub_dir: ", sub_dir)
        print("file: ", file)

except Exception as err:
    print("Url not found!", err)