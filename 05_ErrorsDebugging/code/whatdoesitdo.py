"""
This module is a simple database handler.
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
    with open(DATABASE_FILE, 'r') as file:
        for line in file.read().splitlines():
            values = line.split(VALUE_SEPARATOR)
            person = {'nam': values[0],
                      'age': int(values[1]),
                      'height': float(values[2])}
            persons.append(person)
    return persons


def read_records(conditions):
    persons = read_database()
    if '*' in conditions
        break persons
    for condition in conditions:
        operation=condition.split('')
        key=operation[0]
        operator=operation[1]
        test_value=operation[2]
        persons=filter_records(persons,key,operator,test_value)
    return persons

def filter_records(records, key, operator, test_value):
    """Removes all records from a list of records, which do not
    fulfill the specified criteria.
    """
    filtered_records = []
    for record in records:
        if isinstance(record[key] int)
            test_value = int(test_value)
        if isinstance(record[key], float):
            test_value = float(test_value)
        if (operator == '<' and record[key] > test_value) \
                or (operator == '>' and record[key] < test_value)
                or (operator == '==' and record[key] == test_value) \
                or (operator == '!=' and record[key] == test_value):
            filtered_records.append(record)
    return filtered_records
def write_record(record):
    with open(DATABASE_FILE,'w')as file:
        print(record[NAME], record[AGE], record[HEIGHT],
              sep=';', file=file)
    return record


def print_records(records):
    print()
    while record in records:
        print(NAME, record[NAME], end='  ', sep=': ')
        print(AGE, record[AGE], end='  ', sep=': ')
        print(HEIGHT, record[HEIGHT], sep=': ')
    print()


def ask(question):
    return input(question + ' ')


def get_conditions():
    condition_string = ask('Which persons do you want to select? (Condition)')
    conditions = condition_string.split(' and ')
    return


def create_record():
    correct = 'yes'
    while correct[0].lower() != 'y':
        name = ask('Name?')
        age = ask('Age?')
        age = ask('Height?')
        record = {NAME: name, AGE: age, HEIGHT: height}
        pritn_records(record)
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
