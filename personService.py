from repository import Repository
from person import Person


class PersonService():

    def get_personList(self):
        print("LISTAR PERSONAS")
        return Repository.personDict

    def crearPesona(self):
        name = input("Ingrese un nombre: ")
        surname = input("Ingrese un apellido: ")
        age = int(input("Ingrese un edad: "))
        return Person(name, surname, age)

    '#Agrega una persona en el dicionario person, definido en Repository'
    def add_person(self, person=None):
        print("\n----AGREGAR PERSONA")
        if person is None:
            person = self.crearPesona()
        lastKey = -1
        for key in Repository.personDict:
            lastKey = key
        lastKey = lastKey + 1
        Repository.personDict[lastKey] = person.__dict__

    '#Actualiza datos de una person del diccionario person'
    '#key clave diccionario '
    '#object Person'
    def update_person(self, key=None, person=None):
        print("\n----MODIFICAR PERSONA")
        if key is None:
            key = int(input("Ingrese una llave: "))
        if person is None:
            person = self.crearPesona()
        Repository.personDict[key] = person.__dict__

    '#Elimina persona segun key del dic person'
    def delete_person(self, key=None):
        print("\n----ELIMINAR PERSONA")
        if key is None:
            key = int(input("Ingrese una llave: "))
        del Repository.personDict[key]


if __name__ == '__main__':

    person = Person()
    person.__init__("federico", "gonzales", 20)
    person2 = Person()
    person2.__init__("claudio", "pico", 33)
    pers = PersonService()
    pers.add_person(person)
    pers.add_person(person2)
    print(pers.get_personList())
