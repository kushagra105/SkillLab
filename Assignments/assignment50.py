#assignment50:__init__() method (Constructors Equivalent)
class Customer:
    def __init__(self):
        self.__customerid=0
        self.__customername=None
        self.__telephoneno=[]

    def setcustomerid(self, id):
        self.__customerid = id

    def setcustomername(self, customername):
        self.__customername = customername

    def settelephoneno(self, teleno):
        self.__telephoneno = teleno

    def getcustomerid(self):
        return self.__customerid

    def gettelephoneno(self):
        return self.__telephoneno

    def getcustomername(self):
        return self.__customername

    def validatecustomername(self):
        if(len(self.__customername) >= 3 and len(self.__customername) <= 20):
            return True
        else:
            return False
custobj = Customer()
print("Customer Id : ", custobj.getcustomerid())
print("Telephone Nos : ", custobj.gettelephoneno())
print("Customer Name : ", custobj.getcustomername())

# =====================OUTPUT==========================
# Customer Id :  0
# Telephone Nos :  []
# Customer Name :  None