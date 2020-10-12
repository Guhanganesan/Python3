def outer_function(first_name):
    def inner_function(last_name):
        print(first_name, last_name)
    inner_function("Ganesan")

if __name__ == "__main__":
    outer_function("Guhan")
