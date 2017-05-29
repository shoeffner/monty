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
    """Calculates a comfort value for a car.

    The comfort value is the sum of mapped doors, seats and luggage:

        map_to    door    seats   luggage
           1        2       2      small
           2        3       4       med
           3        4      more     big
           4      5more     --       --

    Args:
        car: The car to evaluate.

    Returns:
        A comfort value. For a car with three doors, four seats and a small
        luggage boot, this would be 2 + 2 + 1 = 5.
    """
    doors = [2, 3, 4, '5more'].index(car.doors) + 1
    seats = [2, 4, 'more'].index(car.seats) + 1
    luggage = ['small', 'med', 'big'].index(car.luggage) + 1
    return doors + seats + luggage


def main():
    """Reads the cars and sorts them. Prints sorted cars."""
    cars = read_cars('car.data')

    cars = sorted(cars, key=comfort_evaluation)

    print(*cars[::100], sep='\n')


if __name__ == '__main__':
    main()
