# Assignment 60 : Implementation of association relationship using a retail application scenario
class customer :
    counter = 1000 #class variable
    def __init__(self, telephoneno, customername, add):
        customer.counter += 1
        self.__customerid = customer.counter
        self.__customername = customername
        self.__telephoneno = telephoneno
        self.__address = add
    
    def setcustomerid(self, cid):
        self.__customerid = cid
    def settelephoneno(self, teleno):
        self.__telephoneno = teleno
    def getcustomerid(self):
        return self.__customerid
    def gettelephoneno(self):
        return self.__telephoneno
    def getcustomername(self):
        return self.__customername
    def getaddress(self):
        return self.__address
    @staticmethod
    def gettotalcustomer():
        return customer.counter-1000
class regularcustomer(customer):
    def __init__(self, telephoneno, customername, discount, add):
        # super to invoke base class init
        super().__init__(telephoneno, customername, add)
        self.__discount = discount
    def setdiscount(self, dis):
        self.__discount = dis
    def getdiscount(self):
        return self.__discount
class address:
    def __init__(self, add):
        self.__addressline = add
    def setaddress(self, add):
        self.__addressline = add
    def getaddress(self):
        return self.__addressline
regcustadd1 = address("No.22, Vijay Nagar Mysore Karnataka 570018")
teleno = [9201861311, 9201861321, 9201661311]
regcustobj1 = regularcustomer(teleno, "John", 12.5, regcustadd1)
#custobj1.setcustomerid(1001)
#custobj1.seltelephoneno(1234567890)
print ("Customer id: ",regcustobj1.getcustomerid())
print ("Telephone number: ",regcustobj1.gettelephoneno())
print ("Customer name: ",regcustobj1.getcustomername())
print ("Discount : ",regcustobj1.getdiscount())
#temp1 = regcustobj1.getaddress().getaddress()
print ("Customer's address: ",regcustobj1.getaddress().getaddress())
print ("\n")
regcustadd2 = address("NO.33, JP road Bangalore Karnataka 570011")
teleno1 = [1122334455,1199887766,2244668897]
regcustobj2 = regularcustomer(teleno1,"Mary", 15.6, regcustadd2)
print ("Customer id: ",regcustobj2.getcustomerid())
print ("Telephone number: ",regcustobj2.gettelephoneno())
print ("Customer name: ",regcustobj2.getcustomername())
print ("Discount : ",regcustobj2.getdiscount())
#temp1 = regcustobj1.getaddress().getaddress()
print ("Customer's address: ",regcustobj2.getaddress().getaddress())
print ("\n")
print ("Total customers registered: ", customer.gettotalcustomer())

# =========================OUTPUT=========================
# Customer id:  1001
# Telephone number:  [9201861311, 9201861321, 9201661311]
# Customer name:  John
# Discount :  12.5
# Customer's address:  No.22, Vijay Nagar Mysore Karnataka 570018

# Customer id:  1002
# Telephone number:  [1122334455, 1199887766, 2244668897]
# Customer name:  Mary
# Discount :  15.6
# Customer's address:  NO.33, JP road Bangalore Karnataka 570011

# Total customers registered:  2