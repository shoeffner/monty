class Movie:
    """A movie contains a title, a release year, an actor, budget and revenue.
    """

    def __init__(self, title, year, actor, budget, revenue):
        self.title = title
        self.year = year
        self.actor = actor
        self.budget = budget
        self.revenue = revenue

    def __str__(self):
        return self.title + ' (' + str(self.year) + ', ' + self.actor + ')'

    def income(self):
        """Returns the income of the movie.

        Returns:
            The income is the difference between the revenue and the budget.
        """
        return self.revenue - self.budget


def movie_sort(movies, key=lambda movie: movie.year):
    """Sorts a list of movies by their release date using bubble sort.

    Args:
        movies: a list of movies.
        key: the key to sort by.

    Returns:
        A sorted list of movies.
    """
    sorted_movies = movies.copy()
    swapped = True
    while swapped:
        swapped = False
        for i, movie in enumerate(sorted_movies[:-1]):
            if key(movie) > key(sorted_movies[i + 1]):
                sorted_movies[i], sorted_movies[i + 1] = \
                    sorted_movies[i + 1], sorted_movies[i]
                swapped = True
    return sorted_movies


def read_movies(filename):
    """Reads a csv file and returns a list of movies.

    Args:
        filename: The file to read.

    Returns:
        A list of movies.
    """
    movies = []
    with open(filename, 'r') as movie_file:
        for line in movie_file.read().splitlines()[1:]:
            title, year, actor, budget, revenue = line.split(',')
            movies.append(Movie(title, int(year), actor, float(budget) * 1e6,
                                float(revenue) * 1e6))
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
