# TODO: Finish the class Movie.
class Movie:
    """A movie contains a title, a release year, an actor, budget and revenue.
    """

    def __init__(self):
        pass


# TODO: Adjust bubble_sort to become movie_sort.
def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort.

    Args:
        numbers: a list of numbers.

    Returns:
        A sorted list of numbers.
    """
    sorted_numbers = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i, number in enumerate(sorted_numbers[:-1]):
            if number > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = \
                    sorted_numbers[i + 1], sorted_numbers[i]
                swapped = True
    return sorted_numbers


def read_movies(filename):
    """Reads a csv file and returns a list of movies.

    Args:
        filename: The file to read.

    Returns:
        A list of movies.
    """
    movies = []
    # TODO: Read the file correctly and instantiate movie objects to store them
    # inside the movies list.
    return movies


def print_movies(movies):
    """Prints a list of movies.

    Args:
        A list of movies.
    """
    for movie in movies:
        print(movie)


def bonus(movies):
    """This function tries to solve the bonus exercise on a list of movies.

    You can safely ignore it if you didn't try to solve that!

    Args:
        movies: The movie list to sort.
    """
    try:
        def actor_selector(movie):
            """Flips first and last name of an actor."""
            return ' '.join(movie.actor.split(' ')[::-1])

        sorted_by_actor = movie_sort(movies, key=actor_selector)
        print('\nSorted list (by actor, first 10):')
        print_movies(sorted_by_actor[:10])

        sorted_by_income = movie_sort(movies, key=lambda movie: movie.income())
        print('\nSorted list (by income, first 10):')
        print_movies(sorted_by_income[:10])
    except TypeError:
        pass


def main():
    """Reads a list of movies from bond.csv and sorts it."""
    movies = read_movies('bond.csv')

    print('Original list (first 10):')
    print_movies(movies[:10])

    sorted_movies = movie_sort(movies)
    print('\nSorted list (by year, first 10):')
    print_movies(sorted_movies[:10])

    bonus(movies)


if __name__ == '__main__':
    main()
