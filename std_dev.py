#name: Cassidy Ward
#date: 11/3/2021
#description: this program takes as a parameter a
#list of Person objects and returns the standard deviation of all their ages (


class Person:
def __init__(self, name, age):
self.name = name
self.age = age


def showPerson(personList):
for person in personList:
print("Name: ", person.name, "\t Age: ", person.age)


def standardDeviation(personList, length):
total, mean, sd = 0.0, 0.0, 0.0


for person in personList:

total += person.age


mean = total / length


for person in personList:
# Calculates standard deviation
sd += math.pow(person.age - mean, 2);
# Returns standard deviation
return math.sqrt(sd / length);


# Creaates an array of objects of class Person
personList = []
personList.append(Person("Pyari",40))
personList.append(Person("Mohan", 22))
personList.append(Person("Sasmita", 35))
personList.append(Person("Manvi", 12))
personList.append(Person("Tanvi", 10))

showPerson(personList)

# displays return value
print("\n Standard Deviation = ", standardDeviation(personList, 5))
