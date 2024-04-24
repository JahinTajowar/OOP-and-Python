class Hall:
    def _init_(self, name, capacity):
        self.name = name
        self.capacity = capacity

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)