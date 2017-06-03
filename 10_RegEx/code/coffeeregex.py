import re


def read_recipes(filename='coffeerecipes.txt'):
    """Reads the file and returns its content as a list of strings."""
    with open(filename, 'r') as file_handle:
        return file_handle.read().splitlines()


def test(recipe):
    """
    Tests if a coffee recipe is valid.

    Args:
        recipe: The coffee recipe.

    Returns:
        True if the recipe matches the regular expression for coffee
        recipes. False otherwise.
    """
    return bool(re.fullmatch(r'^C*((FC*P|PF)C|PC+F)C*BC*$', recipe))


def main():
    recipes = read_recipes()
    results = [(r, test(r)) for r in recipes]
    results = sorted(results, key=lambda x: x[1])
    print(*['{}: {}'.format(*r) for r in results], sep='\n')


if __name__ == '__main__':
    main()
