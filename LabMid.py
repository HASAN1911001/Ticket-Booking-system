"""--------------------------------------------------------------------------------------------------------------------------

1. Make a class named Star_Cinema which will have one class attribute named hall_list which is an empty list initially.
Make a method named entry_hall() to insert an object of class Hall (Described below) inside its hall_list. 		(5)

2. Make a class named Hall which will have 5 instance attributes given below	

    i.   seats which is an dictionary of seats information
    ii.  show_list which is an list of tuples
    iii. rows which is the row of the seats in that hall
    iv.  cols which is the column of the seats in that hall
    v.   hall_no which is the unique no. of that hall

  Initialize an object of class Hall with rows, cols and hall_no. And insert that object to the Star_Cinema class attribute
  named hall_list inside the initializer using inheritance. seats and show_list will be empty initially.			(20)

3. Make a method in Hall class named entry_show() which will take id, movie_name and time in string format. Make a tuple with 
all of the information and append it to the show_list attribute. Allocate seats with rows and cols using 2d list, initially all 
seats will be free. Make a key with id to the attribute seats and value will be the 2d list. (10)

4. Make a method in Hall class named book_seats() which will take the customer name, phone number, an id of the show and list of
 tuples where every tuple contains the row and col of the seat. You need to check the id of the show, and book the seats. 	(10)

5. Make a method in Hall class named view_show_list() which will view all the shows running.			(5)

6. Make a method in Hall class named view_available_seats() which will take an id of show, and view the seats that are available in
 that show		                                                                                        	(10)

7. Make a replica system so that the counter can view all shows that are running, view available seats in a show and can book tickets in a show. (20)

8. You need to handle the errors, for example-				                                        		(10)
 If someone gives a wrong id of a show
 If someone tries to book a seat that is invalid
 If someone tries to book a seat that is already booked


9. Make the information of the classes as protected/private as you can so that the attributes can't be accessed outside the class. +(10)

-------------------------------------------------------------------------------------------------"""

class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.entry_hall(vars(self))
        
    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))
        self.seats[id] = [[True for i in range(self.rows)] for i in range(self.cols)]


    def book_seats(self, name, phone, id, seats):
        for s in seats:
            if s[0] >= self.rows or s[1] >= self.cols:
                print(f"Invaldi Seat Number ({s[0], s[1]}) - Try Again")

            elif self.seats[id][s[0]][s[1]] == 'X':
                print("This seat is already booked")
            
            else:
                self.seats[id][s[0]][s[1]] = 'X'

    def view_show_list(self):
        for show in self.show_list:
            print(f"MOVIE NAME:{show[1]}                               SHOW ID:{show[0]}                    TIME:{show[2]}")

    def view_available_seats(self, id):
        try:
            show = self.seats[id]

            for row in range(self.rows):
                for col in range(self.cols):
                    print(show[row][col], end=" ")
                print("\n")
        except:
            print("Id didn't match with any show!")

        
hall = Hall(5, 5, 1)
hall.entry_show('ae123', "Black Adam", "October 26 2022 10:00 PM")
hall.entry_show('ae50', "Superman", "October 25 2022 8:00 PM")


while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    choice = input("ENTER OPTION: ")

    if choice == '1':
        print("-------------------------------------------------------------------------------------------------------------------------")
        hall.view_show_list()
        print("-------------------------------------------------------------------------------------------------------------------------")
    if choice == '2':
        id = input("ENTER SHOW ID: ")
        print("True for available seat and False for booked seat")
        print("\n")
        hall.view_available_seats(id)
    if choice == '3':
        name = input("CUSTOMER NAME: ")
        phone = input("Phone Number: ")
        id = input("Show Id: ")
        ticket_number = input("Enter Number of Ticket: ")
        seats = []
        for i in range(int(ticket_number)):
            row = int(input("Enter Seat Row: "))
            col = int(input("Enter Seat Col: "))
            seats.append((row, col))
            hall.book_seats(name, phone, id, seats)
        
        

            


    





"""
6. Make a method in Hall class named view_available_seats() which will take an id of show, and view the seats that are available in
 that show	"""