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
        self.entry_hall(self)  
hall_obj = Hall(rows=10, cols=10, hall_no=1)
print(Star_Cinema.hall_list)  
