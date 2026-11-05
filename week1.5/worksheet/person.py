# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):


        if not isinstance (name,str):
                raise TypeError
        if name == "":
            raise ValueError

        if not isinstance(birth,date):
             raise TypeError

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """Returns uppercase initials of person's name
        """

        initials = ""

        for part in self.name.split():
            initials += part[0]

        return initials.upper()
    

    def is_birthday(self):
         """Result is True if today is person's birthday, and False if not.
         """
         
         today =  date.today()

         return today.day == self.birth.day and today.month == self.birth.month

         


