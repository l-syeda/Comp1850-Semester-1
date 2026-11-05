#testing for rect.py
from rect import Rectangle

rectangle = Rectangle(10, 5)

print(rectangle.is_square())
print(rectangle.area())
print(rectangle.perimeter())


#testing for person.py
from datetime import date
from person import Person

person1 = Person("Roman Smith", date.today())
person2 = Person("Joseph Olly Edward Mike Anthony Matt Alex ", date(2007,11,6))

print(person1.initials())
print(person1.is_birthday())

print(person2.initials())
print(person2.is_birthday())