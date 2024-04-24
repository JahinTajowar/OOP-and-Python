class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.allocate_seats()

    def allocate_seats(self):
        self.seats[self.hall_no] = [
            [0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [
            [0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
hall_obj = Hall(rows=3, cols=4, hall_no=1)
hall_obj.entry_show(id='S1', movie_name='Avengers', time='15:00')

print(hall_obj.show_list)
print(hall_obj.seats)
