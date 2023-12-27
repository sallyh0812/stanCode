class Theater:
    def __init__(self, seats: int) -> None:
        self.seats = []
        for i in range(seats):
            # self.seats.append(1)
            self.seats.append(i + 1)
    
    # def reserve(self) -> int:
    #     for i in range(len(self.seats)):
    #         if self.seats[i]:
    #             self.seats[i] = 0
    #             return i + 1
    
    def reserve(self):
        return self.seats.pop(0)
    
    def unreserve(self, seat_number) -> None:
        # self.seats[seat_number - 1] = 1
        self.seats.append(seat_number)
        self.seats = sorted(self.seats)


def main():
    auditorium_a = Theater(5)
    print(auditorium_a.reserve())
    print(auditorium_a.reserve())
    print(auditorium_a.reserve())
    auditorium_a.unreserve(1)
    auditorium_a.unreserve(3)
    print(auditorium_a.reserve())
    print(auditorium_a.reserve())
    auditorium_a.unreserve(1)
    print(auditorium_a.reserve())
    print(auditorium_a.reserve())


if __name__ == '__main__':
    main()
