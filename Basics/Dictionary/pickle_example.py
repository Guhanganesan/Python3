import pickle
 
# Define a Python object
# dont use file name pickle.py as we are imported pickle module from library
person = {
    "name": "Alice",
    "age": 30,
    "gender": "female"
}
 
# Pickle the object to a binary file
with open("person.pickle", "wb") as file:
    pickle.dump(person, file)
 
print("Pickling completed")
