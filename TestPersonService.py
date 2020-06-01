import unittest
from parameterized import parameterized
from personService import PersonService
from person import Person
from repository import Repository


class TestPersonService(unittest.TestCase):
    @parameterized.expand([
        ("federico", "gonzales", 20, 0),
        ("claudio", "pico", 33, 1)
    ])
    def test_add_person(self, name, surname, age, key):
        persona1 = Person(name, surname, age)
        listPerson = PersonService()
        listPerson.add_person(persona1)
        self.assertEqual(Repository.personDict[key], persona1.__dict__)


if __name__ == '__main__':
    unittest.main()
