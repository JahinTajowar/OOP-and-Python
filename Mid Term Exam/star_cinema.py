class Hall:
    def __init__(self, hall_no, rows, cols):
        self.__hall_no = hall_no
        self.rows = rows
        self.cols = cols
        self.__seats = {}  # Empty dictionary for seats
        self.__show_list = []  # Empty list for shows

    def entry_show(self, show_id, movie_name, show_time):
        self.__seats[show_id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        show_info = (show_id, movie_name, show_time)
        self.__show_list.append(show_info)

    def book_seats(self, show_id, seats_to_book):
        booked_seats = []
        for row, col in seats_to_book:
            # Check if show ID exists and seat is within valid range
            if (show_id in self.__seats and
                    0 <= row < self.rows and 0 <= col < self.cols):
                if self.__seats[show_id][row][col] == 0:  # Check if seat is available
                    self.__seats[show_id][row][col] = 1  # Book the seat
                    booked_seats.append((row, col))
                else:
                    print(f"Seat ({row}, {col}) is already booked for show {show_id}")
            else:
                print(f"Invalid seat ({row}, {col}) or show ID {show_id}")
        return booked_seats

    def view_show_list(self):
        for show_id, movie_name, time in self.__show_list:
            print(f"{show_id}, {movie_name}, {time}")

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            print(f"Available seats for show {show_id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.__seats[show_id][row][col] == 0:
                        print(f"Seat ({row + 1}, {col + 1})")
            print("In matrix :")
            for row in range(self.rows):
                print(self.__seats[show_id][row])
        else:
            print(f"Show ID {show_id} not found.")


class Star_cinema(Hall):
    __hall_list = []

    def __init__(self):
        super().__init__(hall_no=0, rows=0, cols=0)

    def entry_hall(self, hall):
        self.__hall_list.insert(0, hall)


def main():
    cinema = Hall(1, 5, 5)
    cinema.entry_show("111", "War", "08:00 PM")
    cinema.entry_show("112", "Jawan", "12:00 PM")
    cinema.entry_show("113", "Heropanti", "1:00 PM")
    star_cinema = Star_cinema()
    star_cinema.entry_hall(cinema)

    while True:
        print("\nReplica System Menu:")
        print("1. View All Shows")
        print("2. View Available Seats")
        print("3. Book Tickets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            cinema.view_show_list()
        elif choice == '2':
            show_id = input("Enter show ID: ")
            cinema.view_available_seats(show_id)
        elif choice == '3':
            show_id = input("Enter show ID: ")
            num_seats = int(input("Enter number of seats to book: "))
            seats_to_book = []
            for i in range(num_seats):
                while True:
                    try:
                        row = int(input(f"Enter row for seat {i + 1}: ")) - 1
                        col = int(input(f"Enter column for seat {i + 1}: ")) - 1
                        if 0 <= row < cinema.rows and 0 <= col < cinema.cols:
                            seats_to_book.append((row, col))
                            break
                        else:
                            print("Invalid seat. Please enter a valid row and column.")
                    except ValueError:
                        print("Invalid input. Please enter integers for row and column.")
            booked_seats = cinema.book_seats(show_id, seats_to_book)
            if booked_seats:
                print(f"\nSuccessfully booked seats: {booked_seats}")
            else:
                print("No seats booked.")
        elif choice == '4':
            print("Exiting Replica System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
