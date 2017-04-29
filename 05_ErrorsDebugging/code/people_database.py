"""
This module is a simple database handler.
It allows to manage persons as dictionaries in a database file.

Each person is represented as a dictionary containing three values:
    a name (string), an age (integer), a height (float)

To read from the database, a very simple query language is implemented:

    query := '*' | key <space> operator <space> test
           | query <space> 'and' <space> query
    key := 'name' | 'age' | 'height'
    operator := '<' | '>' | '==' | '!='
    test := <string, float, or int value>

When the query contains '*', all records are returned. Otherwise, the records
are filtered by the specified query criteria, such that all must be fulfilled
for a record to be included in the result list.

The database represents records as comma seperated values and linebreak
separated rows. No escaping is done.
"""
DATABASE_FILE = 'recorded_persons'
NAME = 'name'
AGE = 'age'
HEIGHT = 'height'
VALUE_SEPARATOR = ','


def read_database():
    """Reads the database file.

    Reads the database file line by line. Each line is split at the
    value separator into three parts:
        name   a string
        age    an integer
        height a float
    A person-dictionary is created from the three values.

    Returns:
        A list of all persons.
    """
    persons = []
    with open(DATABASE_FILE, 'r') as file:
        for line in file.read().splitlines():
            values = line.split(VALUE_SEPARATOR)
            person = {NAME: values[0],
                      AGE: int(values[1]),
                      HEIGHT: float(values[2])}
            persons.append(person)
    return persons


def read_records(conditions):
    """Reads the records from the database which fulfill all conditions.

    If conditions includes '*', all records are returned.
    Otherwise only those records matching all conditions are returned.

    Args:
        conditions: A list of conditions to be fulfilled by a record.

    Returns:
        The list of matching records.
    """
    persons = read_database()
    if '*' in conditions:
        return persons
    for condition in conditions:
        operation = condition.split(' ')
        key = operation[0]
        operator = operation[1]
        test_value = operation[2]
        persons = filter_records(persons, key, operator, test_value)
    return persons


def filter_records(records, key, operator, test_value):
    """Removes all records from a list of records, which do not
    fulfill the specified criteria.

    The criteria are checked by applying the operator with the record's value
    for the specified key as the first and the test_value as the second
    operand.

    If the record's value is not a string, int and float casting are tried
    for the test_value.

    Args:
        records: The list of records.
        key: The key to select from the record.
        operator: The relation to test.
        test_value: The value to test against.

    Returns:
        A list of records for which all criteria are True.
    """
    filtered_records = []
    for record in records:
        if isinstance(record[key], int):
            test_value = int(test_value)
        if isinstance(record[key], float):
            test_value = float(test_value)
        if (operator == '<' and record[key] < test_value) \
                or (operator == '>' and record[key] > test_value) \
                or (operator == '==' and record[key] == test_value) \
                or (operator == '!=' and record[key] != test_value):
            filtered_records.append(record)
    return filtered_records


def write_record(record):
    """Writes a record to the database.

    Args:
        record: The record to write.

    Returns:
        The record that was written.
    """
    with open(DATABASE_FILE, 'a') as file:
        print(record[NAME], record[AGE], record[HEIGHT],
              sep=VALUE_SEPARATOR, file=file)
    return record


def print_records(records):
    """Prints a list of records.

    Args:
        records: The list of records.
    """
    print()
    for record in records:
        print(NAME, record[NAME], end='  ', sep=': ')
        print(AGE, record[AGE], end='  ', sep=': ')
        print(HEIGHT, record[HEIGHT], sep=': ')
    print()


def ask(question):
    """Asks a question.

    Appends a blank space after the question.

    Args:
        question: The question to prompt.

    Returns:
        The user input.
    """
    return input(question + ' ')


def get_conditions():
    """Asks for conditions and splits them into a list of conditions.

    The conditions are split around ' and '.

    Returns:
        A list containing conditions.
    """
    condition_string = ask('Which persons do you want to select? (Condition)')
    conditions = condition_string.split(' and ')
    return conditions


def create_record():
    """Creates a record from user input.

    Asks the user for name, age, and height. Then prints the possible record.
    Only if the user accepts with 'y' or 'Y', the record is returned.
    Otherwise, the user is asked again.

    Returns:
        A dictionary representing a person.
    """
    correct = 'no'
    while correct[0].lower() != 'y':
        name = ask('Name?')
        age = ask('Age?')
        height = ask('Height?')
        record = {NAME: name, AGE: age, HEIGHT: height}
        print_records([record])
        correct = ask('Correct? [yes/no]')
    return record


def main():
    """Runs the program.

    Until the users enters 'q' to exit, they can use the following commands
    to interact with the database:
        a: add a new entry
        r: read entries
        q: exit
        d (hidden): add example data
    """
    response = ''
    while response != 'q':
        response = ask('Do you want to add records, retrieve records, or ' +
                       'quit? [a, r, q]')
        if response == 'r':
            conditions = get_conditions()
            records = read_records(conditions)
            print_records(records)
        elif response == 'a':
            record = create_record()
            write_record(record)
        elif response == 'd':
            fill_with_example_data()


def fill_with_example_data():
    """Writes example data into the database."""
    records = [
        {NAME: 'Graham Chapman', AGE: 48, HEIGHT: 1.88},
        {NAME: 'John Cleese', AGE: 77, HEIGHT: 1.96},
        {NAME: 'Terry Gilliam', AGE: 76, HEIGHT: 1.75},
        {NAME: 'Eric Idle', AGE: 74, HEIGHT: 1.85},
        {NAME: 'Terry Jones', AGE: 75, HEIGHT: 1.73},
        {NAME: 'Michael Palin', AGE: 73, HEIGHT: 1.78}
    ]
    for record in records:
        write_record(record)


if __name__ == '__main__':
    main()
