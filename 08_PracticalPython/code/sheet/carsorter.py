class Car:

    def __init__(self, cost, maintenance, doors, seats, luggage, safety):
        self.cost = cost
        self.maintenance = maintenance
        try:
            self.doors = int(doors)
        except ValueError:
            self.doors = doors
        try:
            self.seats = int(seats)
        except ValueError:
            self.seats = seats
        self.luggage = luggage
        self.safety = safety

    def __repr__(self):
        return 'Car({}, {}, {}, {}, {}, {})'.format(self.cost,
                                                    self.maintenance,
                                                    self.doors,
                                                    self.seats,
                                                    self.luggage,
                                                    self.safety)

    def __str__(self):
        return 'Car: {} seats, {} luggage, {} doors'.format(self.seats,
                                                            self.luggage,
                                                            self.doors)


def read_cars(filename):
    """Reads cars and creates car instances.

    Drops the evaluation column.

    Args:
        filename: the name of the file containing the car data
    """
    with open(filename, 'r') as carfile:
        return [Car(*(car.split(',')[:-1]))
                for car in carfile.read().splitlines()]


def comfort_evaluation(car):
    """Returns 0."""
    # TODO: change this function to calculate a comfort value. Change the
    # docstring.
    return 0


def main():
    """Reads the cars and sorts them. Prints sorted cars."""
    cars = read_cars('car.data')

    # TODO: Sort the cars.

    # Hint: It might be cool to just check every 100th car or so. There are
    # many many similar cars.
    print(*cars[::], sep='\n')


if __name__ == '__main__':
    main()
