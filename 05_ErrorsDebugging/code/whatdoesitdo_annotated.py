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
    # @shoeffner: missing creation of persons = []
    with open(DATABASE_FILE, 'r') as file:
        for line in file.read().splitlines():
            values = line.split(VALUE_SEPARATOR)
            # @shoeffner: nam is wrong, better: NAME
            # @shoeffner: better: AGE
            # @shoeffner: better: HEIGHT
            person = {'nam': values[0],
                      'age': int(values[1]),
                      'height': float(values[2])}
            persons.append(person)
    return persons


def read_records(conditions):
    persons = read_database()
    # @shoeffner: Missing :
    if '*' in conditions :
        # @shoeffner: break is wrong, must be return
        break persons
    for condition in conditions:
        # @shoeffner: no whitespace in the next rows
        operation=condition.split(' ')
        key=operation[0]
        operator=operation[1]
        test_value=operation[2]
        persons=filter_records(persons,key,operator,test_value)
    return persons
# @shoeffner: not enough empty lines
def filter_records(records, key, operator, test_value):
    """Removes all records from a list of records, which do not
    fulfill the specified criteria.
    """
    filtered_records = []
    for record in records:
        # @shoeffner: missing , and :
        if isinstance(record[key] int)
            test_value = int(test_value)
        if isinstance(record[key], float):
            test_value = float(test_value)
        # @shoeffner: swapped operators
        if (operator == '<' and record[key] > test_value) \
                # @shoeffner: swapped operators, missing \
                or (operator == '>' and record[key] < test_value)
                or (operator == '==' and record[key] == test_value) \
                # @shoeffner: == is wrong here - copy/paste?
                or (operator == '!=' and record[key] == test_value):
            filtered_records.append(record)
    return filtered_records
# @shoeffner: not enough empty lines
def write_record(record):
    # @shoeffner: no whitespace + file mode must be 'a' not 'w'
    with open(DATABASE_FILE,'w')as file:
        print(record[NAME], record[AGE], record[HEIGHT],
              # @shoeffner: separator has to be , not ;. Use VALUE_SEPARATOR
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
    # @shoeffner: return value is missing! return conditions
    return


def create_record():
    # @shoeffner: will never enter loop, use e.g. 'no'
    correct = 'yes'
    while correct[0].lower() != 'y':
        name = ask('Name?')
        age = ask('Age?')
        age = ask('Height?')
        record = {NAME: name, AGE: age, HEIGHT: height}
        # @shoeffner: print_records: wrong spelling + takes list
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
    # @shoeffner: indentation level wrong
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
