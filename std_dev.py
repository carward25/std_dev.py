#name: Cassidy Ward
#date: 11/3/2021
#description: this program takes as a parameter a
#list of Person objects and returns the standard deviation of all their ages (

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def std_dev(person_list):
    m = 0
    for person in person_list:
        m += person.age
    m /= len(person_list)
    total = 0
    for person in person_list:
        total += (person.age - m) ** 2
    return (total / (len(person_list) - 1)) ** 0.5
