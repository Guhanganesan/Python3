#To replace the ‘a’ to ‘A’ if it is followed by 4 numbers.
import re
flight_details="Flight Savana Airlines a2134"
print(re.sub(r"a(\d{4})",r"A\1",flight_details))

