class Room:
    def __init__(self, room_number, capacity, status='Available'):
        self.room_number = room_number
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"Room {self.room_number} - Capacity: {self.capacity}, Status: {self.status}")


class Guest:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Guest: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Booking:
    def __init__(self, room, guest, check_in_date, check_out_date):
        self.room = room
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def display_info(self):
        print("Booking Information:")
        self.room.display_info()
        self.guest.display_info()
        print(f"Check-in Date: {self.check_in_date}")
        print(f"Check-out Date: {self.check_out_date}")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room, guest, check_in_date, check_out_date):
        if room.status == 'Available':
            room.status = 'Booked'
            booking = Booking(room, guest, check_in_date, check_out_date)
            self.bookings.append(booking)
            print("Booking successful!")
        else:
            print("Room not available for the specified dates.")

    def display_rooms(self):
        print(f"{self.name} Rooms:")
        for room in self.rooms:
            room.display_info()

    def display_bookings(self):
        print(f"{self.name} Bookings:")
        for booking in self.bookings:
            booking.display_info()


# Example usage:
if __name__ == "__main__":
    hotel = Hotel("Grand Hotel")

    room1 = Room(101, 2)
    room2 = Room(102, 4)
    room3 = Room(103, 3)

    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    guest1 = Guest("John Doe", 30, "Male")
    guest2 = Guest("Jane Doe", 25, "Female")

    hotel.display_rooms()

    hotel.book_room(room1, guest1, "2023-01-01", "2023-01-05")
    hotel.book_room(room2, guest2, "2023-01-02", "2023-01-07")

    hotel.display_bookings()