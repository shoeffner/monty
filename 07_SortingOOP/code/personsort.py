import peopledb
persons = peopledb.read('persons.data')
print(len(persons), 'Example:', persons[0])
persons = peopledb.bubblesort(persons)
for person in persons[:4]:
    print(person)
