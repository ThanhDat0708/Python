class Person:
    # Định nghĩa class parameter "name"
    name = "Person"

    def __init__(self, name=None):
        # self.name là instance parameter
        self.name = name


jeffrey = Person("Jeffrey")

print("%s name is %s" % (Person.name, jeffrey.name))


nico = Person()
nico.name = "Nico"

print("%s name is %s" % (Person.name, nico.name))