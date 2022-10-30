class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        self.entry_hall(self)

    #helper methode
    def __stage(self, row, col):
        stage =  [[True for i in range(self.__cols)] for i in range(self.__rows)]
        for r in range(row):
            for c in range(col):
                stage[r][c] = chr(65+r)+str(c)
        return stage
    
    def check_id(self, id):
        for show in self.__show_list:
            if show[0] == id:
                return True
        return False
        
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = self.__stage(self.__rows, self.__cols)


    def book_seats(self, name, phone, id, seats):
        self.__name = name
        self.__phone = phone

        for s in seats:
            if s[0] >= self.__rows or s[1] >= self.__cols:
                print("\n")
                print("---------------------------------------------------")
                print("\n")
                print(f"Invalid Seat Number {self.number_to_string(s)} - Try Again")
                print("\n")
                print("---------------------------------------------------")
                print("\n")
                return

            elif self.__seats[id][s[0]][s[1]] == 'X':
                print("\n")
                print("-----------------------------")
                print("\n")
                print(f"This Seat is  already booked - {self.number_to_string(s)}")
                print("\n")
                print("-----------------------------")
                print("\n")
                return
            
            else:
                self.__seats[id][s[0]][s[1]] = 'X'
        
        #showing information of booking
        print("\n")
        print("###### TICKET BOOKED SUCCESSSFULLY! ######")
        print("-----------------------------------------------")
        print("\n")
        print(f"Name: {self.__name}")
        print(f"Phone Number: {self.__phone}")
        print("\n")
        for show in self.__show_list:
            if(show[0] == id):
                print(f"Movie Name: {show[1]}      Time: {show[2]}")
        tickets = []
        for s in seats:
            tickets.append(chr(65+s[0])+str(s[1]))
        print("TICKETS: ", end="")
        for t in tickets:
            print(t, end=" ") 
        print("\n")
        print(f"HALL: {self._hall_list[0].__hall_no}")
        print("\n")
        print("-----------------------------------------------")
        print("\n")

    def view_show_list(self):
        for show in self.__show_list:
            print("MOVIE NAME: ",show[1], "                   SHOW ID: ", show[0], "              TIME: ", show[2])

    def view_available_seats(self, id):
        for show in self.__show_list:
            if(show[0] == id):
                print(f"Movie Name: {show[1]}      Time: {show[2]}")
                print("X for already booked seats")

        show = self.__seats[id]
        print("\n")
        print("--------------------------------")
        print("\n")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(show[row][col], end="     ")
            print("\n")
        print("--------------------------------")


    def string_to_number(self, s):
        return (ord(s[0])-65, int(s[1:]))
    def number_to_string(self, n):
        return chr(65+n[0])+str(n[1])

        
hall = Hall(3, 5, "A10")
hall.entry_show('ae123', "Black Adam", "October 26 2022 10:00 PM")
hall.entry_show('ae50', "Superman", "October 25 2022 8:00 PM")


while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    choice = input("ENTER OPTION: ")

    if choice == '1':
        print("\n")
        print("-------------------------------------------------------------------")
        print("\n")
        hall.view_show_list()
        print("\n")
        print("-------------------------------------------------------------------")
        print("\n")

    if choice == '2':
        id = input("ENTER SHOW ID: ")
        if hall.check_id(id) == False:
            print("\n")
            print("---------------------------------")
            print("\n")
            print(f"There is no show with id {id}")
            print("\n")
            print("---------------------------------")
            print("\n")
            
        else:
            print("\n")
            hall.view_available_seats(id)
            print("\n")
           
    if choice == '3':
        name = input("CUSTOMER NAME: ")
        phone = input("Phone Number: ")
        id = input("ENTER SHOW ID: ")
        if hall.check_id(id) == False:
            print("\n")
            print("--------------------------------")
            print("\n")
            print(f"There is no show with id {id}")
            print("\n")
            print("--------------------------------")
            print("\n")
            
        
        else: 
            ticket_number = input("Enter Number of Ticket: ")
            seats = []
            for i in range(int(ticket_number)):
                s = input("Enter Seat Number: ")
                seats.append(hall.string_to_number(s))
            hall.book_seats(name, phone, id, seats)
            
        