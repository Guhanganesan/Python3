import logging
logging.basicConfig(filename="logdetails.log", level=logging.INFO)

count = 0
def increment_count_value():
    global count
    count = count+1

for i in range(0,5):
    logging.info("Count value is: {} ".format(count))
    increment_count_value()