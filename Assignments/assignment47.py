# Assignment 47 : Implement the solution to the Problem using Object Oriented Language
class Customer:
    def setcustomerid(self, id):
        self.__customerid = id
    def settelephoneno(self, teleno):
        self.__telephoneno = teleno
    def getcustomerid (self):
        return self.__customerid
    def gettelephoneno(self):
        return self.__telephoneno
custobj = Customer()
custobj.setcustomerid(1001)
custobj.settelephoneno(123456789)
print ("Customer ID :",custobj.getcustomerid())
print ("Telephone No : ",custobj.gettelephoneno())

# ===================OUTPUT====================
# Customer ID : 1001
# Telephone No :  123456789