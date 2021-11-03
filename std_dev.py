#name: Cassidy Ward
#date: 11/3/2021
#description: this program takes as a parameter a
#list of Person objects and returns the standard deviation of all their ages (

class Person:
def __init__(self,name,age):
self.name = name
self.age = age
  
def std_dev(persons):
ages = []
for p in persons:
ages.append(p.age)
  
total = sum(ages)
mean = total/len(ages)
  
total = 0
for a in ages:
total += (a-mean)**2;
  
total /=len(ages)
  
dev = total**.5
return dev

if __name__ == '__main__':
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
answer = std_dev(person_list)
print("Standard deviation is : ",answer)
