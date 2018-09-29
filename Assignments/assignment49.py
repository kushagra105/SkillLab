#Assignment 49 : Use of _init__() method & Static members – Observations from Retail Application

class retail:
    def __init__(self, id=100, name="Null", ):
        self.id = id
        self.name = name

    def add_person(self,id,name):
        self.id = self.id + 1
        self.name = name
        print("Succeefully added")
    def print_person(self):
        print(self.id)
        print(self.name)
p1=retail(1002,"Kushagra")
p1.add_person(1002,"Kushagra")
p1.print_person()
p2=retail(1003,"Madhav")
p2.add_person(1003,"Madhav")
p2.print_person()

# ===================OUTPUT====================
# Succeefully added
# 1003
# Kushagra
# Succeefully added
# 1004
# Madhav