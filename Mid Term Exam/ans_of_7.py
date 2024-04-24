class Show:
    def __init__(self, name, available_seats):
        self.name = name
        self.available_seats = available_seats

class ShowManagementSystem:
    def __init__(self):
        self.shows = {}

    def add_show(self, name, available_seats):
        self.shows[name] = Show(name, available_seats)

    def remove_show(self, name):
        if name in self.shows:
            del self.shows[name]
            print(f"{name} has been removed from the shows.")
        else:
            print(f"Show {name} not found.")

    def view_all_shows(self):
        for name, show in self.shows.items():
            print(f"{name}: {show.available_seats} seats available")

class SeatReservationSystem:
    def __init__(self):
        self.reservations = {}

    def reserve_seat(self, show_name, seats):
        if show_name in self.reservations:
            self.reservations[show_name] += seats
        else:
            self.reservations[show_name] = seats

    def cancel_reservation(self, show_name, seats):
        if show_name in self.reservations:
            if self.reservations[show_name] >= seats:
                self.reservations[show_name] -= seats
                print(f"{seats} seats canceled for {show_name}.")
            else:
                print(f"Not enough seats reserved for {show_name}.")
        else:
            print(f"No reservations found for {show_name}.")

class CounterInterface:
    def __init__(self, show_management_system, seat_reservation_system):
        self.show_management_system = show_management_system
        self.seat_reservation_system = seat_reservation_system

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
                self.show_management_system.view_all_shows()
            elif choice == '2':
                show_name = input("Enter the name of the show: ")
                if show_name in self.show_management_system.shows:
                    print(f"Available seats for {show_name}: {self.show_management_system.shows[show_name].available_seats}")
                else:
                    print("Show not found.")
            elif choice == '3':
                show_name = input("Enter the name of the show: ")
                seats = int(input("Enter the number of seats to book: "))
                self.seat_reservation_system.reserve_seat(show_name, seats)
                print(f"{seats} seats booked for {show_name}.")
            elif choice == '4':
                show_name = input("Enter the name of the show: ")
                seats = int(input("Enter the number of seats to cancel: "))
                self.seat_reservation_system.cancel_reservation(show_name, seats)
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
