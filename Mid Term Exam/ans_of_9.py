class Show:
    def _init_(self, name, available_seats):
        self._name = name
        self._available_seats = available_seats

    def get_name(self):
        return self._name

    def get_available_seats(self):
        return self._available_seats

class ShowManagementSystem:
    def _init_(self):
        self._shows = {}

    def add_show(self, name, available_seats):
        self._shows[name] = Show(name, available_seats)

    def remove_show(self, name):
        if name in self._shows:
            del self._shows[name]
            print(f"{name} has been removed from the shows.")
        else:
            print(f"Show {name} not found.")

    def view_all_shows(self):
        if not self._shows:
            print("No shows available.")
            return
        for name, show in self._shows.items():
            print(f"{show.get_name()}: {show.get_available_seats()} seats available")

class SeatReservationSystem:
    def _init_(self):
        self._reservations = {}

    def reserve_seat(self, show_name, seats):
        if show_name in self._reservations:
            self._reservations[show_name] += seats
        else:
            self._reservations[show_name] = seats

    def cancel_reservation(self, show_name, seats):
        if show_name in self._reservations:
            if self._reservations[show_name] >= seats:
                self._reservations[show_name] -= seats
                print(f"{seats} seats canceled for {show_name}.")
            else:
                print(f"Not enough seats reserved for {show_name}.")
        else:
            print(f"No reservations found for {show_name}.")

class CounterInterface:
    def _init_(self, show_management_system, seat_reservation_system):
        self._show_management_system = show_management_system
        self._seat_reservation_system = seat_reservation_system

    def display_menu(self):
        print("1. View all shows")
        print("2. View available seats for a show")
        print("3. Book tickets for a show")
        print("4. Cancel ticket reservations")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self._show_management_system.view_all_shows()
            elif choice == '2':
                show_name = input("Enter the name of the show: ")
                if show_name in self._show_management_system._shows:
                    print(f"Available seats for {show_name}: {self._show_management_system._shows[show_name].get_available_seats()}")
                else:
                    print("Show not found.")
            elif choice == '3':
                show_name = input("Enter the name of the show: ")
                if show_name in self._show_management_system._shows:
                    try:
                        seats = int(input("Enter the number of seats to book: "))
                        if seats <= 0:
                            raise ValueError("Number of seats must be a positive integer.")
                        if seats > self._show_management_system._shows[show_name].get_available_seats():
                            print("Not enough seats available.")
                        else:
                            self._seat_reservation_system.reserve_seat(show_name, seats)
                            self._show_management_system._shows[show_name]._available_seats -= seats
                            print(f"{seats} seats booked for {show_name}.")
                    except ValueError as e:
                        print("Invalid input:", e)
                else:
                    print("Show not found.")
            elif choice == '4':
                show_name = input("Enter the name of the show: ")
                if show_name in self._show_management_system._shows:
                    try:
                        seats = int(input("Enter the number of seats to cancel: "))
                        if seats <= 0:
                            raise ValueError("Number of seats must be a positive integer.")
                        if seats > self._seat_reservation_system._reservations.get(show_name, 0):
                            print("Not enough seats reserved for cancellation.")
                        else:
                            self._seat_reservation_system.cancel_reservation(show_name, seats)
                            self._show_management_system._shows[show_name]._available_seats += seats
                    except ValueError as e:
                        print("Invalid input:", e)
                else:
                    print("Show not found.")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage:
show_management_system = ShowManagementSystem()
show_management_system.add_show("Show 1", 50)
show_management_system.add_show("Show 2", 30)

seat_reservation_system = SeatReservationSystem()

counter_interface = CounterInterface(show_management_system, seat_reservation_system)
counter_interface.run()