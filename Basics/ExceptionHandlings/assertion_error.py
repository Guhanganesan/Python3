try:
    user = int(input("Enter Value"))
    assert(user>0)
    print(user+100)

except AssertionError:
    print("Ur data is not suitable for this process")
