class Hall:
    def __init__(self, rows, cols, hall_no):
        """
        Initializes a Hall object with the specified rows, columns, and hall number.
        Args:
            rows (int): Number of rows in the hall.
            cols (int): Number of columns in the hall.
            hall_no (int): Unique hall number.
        """
        self.seats = {}  
        self.show_list = [] 
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, show_id, movie_name, show_time):
        """
        Adds a show to the show_list and initializes seats as a 2D list.
        Args:
            show_id (str): Unique show identifier.
            movie_name (str): Name of the movie.
            show_time (str): Show time in string format.
        """
        show_tuple = (show_id, movie_name, show_time)
        self.show_list.append(show_tuple)

        
        self.seats[show_id] = [['free'] * self.cols for _ in range(self.rows)]

    def book_seats(self, show_id, seat_tuples):
        """
        Books the specified seats for a show.
        Args:
            show_id (str): Unique show identifier.
            seat_tuples (list of tuples): Each tuple contains (row, col) of the seat to be booked.
        Returns:
            bool: True if seats were successfully booked, False otherwise.
        """
        if show_id not in self.seats:
            print(f"Show with ID '{show_id}' does not exist.")
            return False

        for row, col in seat_tuples:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[show_id][row][col] == '0':
                    self.seats[show_id][row][col] = '1'
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            else:
                print(f"Invalid seat coordinates: ({row}, {col}).")
                return False

        print(f"Seats booked successfully for show '{show_id}'.")
        return True

    def view_available_seats(self, show_id):
        """
        Displays the available seats for a specific show.
        Args:
            show_id (str): Unique show identifier.
        """
        if show_id not in self.seats:
            print(f"Show with ID '{show_id}' does not exist.")
            return

        print(f"Available seats for show '{show_id}':")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[show_id][row][col] == '0':
                    print(f"Row {row}, Seat {col}")

# Example usage:
if __name__ == "__main__":
    cinema = Hall(rows=10, cols=8, hall_no=1)
    cinema.entry_show("S123", "Avengers: Endgame", "18:00")
    cinema.book_seats("S123", [(2, 3), (4, 5), (6, 7)])
    cinema.view_available_seats("S123")
