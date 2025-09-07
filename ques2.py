"""
Movie Ticket Booking


1. Data Setup
	o Create a list called theaters. Each element is a dictionary with keys:
 "name" (theater name)
 "screens" (a nested list of screen dictionaries)
	o Each screen dictionary has:
 "screen_number" (int)
 "seats" (dict mapping seat IDs like "A1" to True/False for booked status)

2. Print Theaters
	o Print the full theaters list.

3. Show Availability
	o For a given theater and screen, list all unbooked seats.

4. Book a Seat
	o Write a function that takes theater name, screen number, and seat ID and marks
it booked.

5. Cancel a Screen
    o Remove one screen dictionary from a selected theater.
"""


# 1. list containing all theaters details
theaters = [
    {
        "name": "Theater 1",
        "screens": [
            {
                "screen_number": 1,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            },
            {
                "screen_number": 2,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            },
            {
                "screen_number": 3,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            }
        ]
    },
    {
        "name": "Theater 2",
        "screens": [
            {
                "screen_number": 1,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            },
            {
                "screen_number": 2,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            },
            {
                "screen_number": 3,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            }
        ]
    },
    {
        "name": "Theater 3",
        "screens": [
            {
                "screen_number": 1,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            },
            {
                "screen_number": 2,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            },
            {
                "screen_number": 3,
                "seats": {
                    "A1" : True,
                    "A2" : False,
                    "B1" : True,
                    "B2" : False
                }
            }
        ]
    }  
]


# 2. Print the full theaters list
print(theaters)


# 3. For a given theater and screen, list all unbooked seats
def findAvailableSeat(theater_name,screen_no):
    for theater in theaters:
        if theater["name"]==theater_name:
            for screen in theater["screens"]:
                if screen["screen_number"]==screen_no:
                    print("\nUnbooked Seats : ")
                    for seat,status in screen["seats"].items():
                        if status==False:
                            print(seat)

findAvailableSeat("Theater 1",2)


# 4. Write a function that takes theater name, screen number, and seat ID and marks it booked
def bookSeats(given_theater,given_screen,given_seat):
    for theater in theaters:
        if theater["name"]==given_theater:
            for screen in theater["screens"]:
                if screen["screen_number"]==given_screen and screen["seats"][given_seat]==False:
                    screen["seats"][given_seat]=True
                    print("Seat Booked: ",given_seat)
                elif screen["screen_number"]==given_screen and screen["seats"][given_seat]==True:
                    print("Seat Already Booked")

bookSeats("Theater 1",2,"A1")
bookSeats("Theater 2",1,"A2")
bookSeats("Theater 3",3,"B2")
print("After Booking:",theaters)


# 5. Remove one screen dictionary from a selected theater.
def removeScreen(theater_name,screen_no):
    for theater in theaters:
        if theater["name"]==theater_name:
            for screen in theater["screens"]:
                if screen["screen_number"]==screen_no:
                    theater["screens"].remove(screen)
                    print("\n",theater_name,"Screen",screen_no,"removed successfully")

removeScreen("Theater 1",3)
print("\nAfter removing Screen :",theaters)