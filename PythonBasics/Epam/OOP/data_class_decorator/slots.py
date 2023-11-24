import timeit
from dataclasses import dataclass
from functools import partial


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


def get_set_delete(person: Person | PersonSlots): # alt 124
    person.address = '123 main st'
    person.address
    del person.address


# slots breakes when uses multiple inharitance
class PesonEmployee(PersonSlots, Person):
    pass


def main():
    person = Person('Jhon', '123 Main St', 'jhon@doe.com')
    person_slots = PersonSlots('Jhon', '123 Main St', 'jhon@doe.com')
    no_slots = min(timeit.repeat(partial(get_set_delete, person),  number=1000000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots),  number=1000000))
    print(f'No slots: {no_slots}')#
    print(f'No slots: {slots}')
    print(f'No slots: {(no_slots-slots)/no_slots:.2%}')


if __name__ == "__main__":
    main()   
