import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=12))


# Same as
# def __init__(self, name: str, adress: str):
#     self.name = name
#     self.adress = adress
    
# def __str__(self) -> str:
#     return f'{self.name}, {self.adress}'
# in data class is __repr__

# emain_adresses: list[str] = []
# if we have multiple instances they all have same reference to list

# field factory function with default_factory create a list when create 
# class call a functuin from field

# to exclude arguments from the initializer (not set id exclicitly)
# id: str = field(default_factory=generate_id) -> id: str = field(default_factory=generate_id)

# sometimes you need to inizialized values after creating and instanse  see __post_init__

# frozen = True = read_only after creation making data not mutable = good
# kw_only Person(name="Jhon", adress='Sina') not Person("Jhon", Sina')
@dataclass(frozen=True, kw_only=False)
class Person:
    # with @dataclass not class variable but instance
    name: str
    adress: str
    active: bool = True
    emain_adresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    search_string: str = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self.search_string = f'{self.name} {self.adress}'





def main() -> None:
    person = Person(name="Jhon", adress='Sina')
    person.name = 'Aaron'
    print(person)


if __name__ == "__main__":
    main()