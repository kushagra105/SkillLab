"""
Wrong Code
class Customer:
    def setcustomerid(self, customerid):
        customerid = customerid
        def settelephoneno(self, teleno):
            telephoneno = teleno
        def getcustomerid(self):
            return customerid
        def gettelephoneno(self):
            return telephoneno
custobj = Customer() custobj.setcustomerid(1001)
custobj.settelephoneno(9201861311)
print("Customer Id : ", custobj.getcustomerid())
print("Telephone No : ", custobj.gettelephoneno())
"""
class Customer:
    def setcustomerid(self, customerid):
        self.customerid = customerid
    def settelephoneno(self, telephoneno):
        self.telephoneno = telephoneno
    def getcustomerid(self):
        return self.customerid
    def gettelephoneno(self):
        return self.telephoneno
custobj = Customer()
custobj.setcustomerid(1001)
custobj.settelephoneno(9201861311)
print("Customer Id : ", custobj.getcustomerid())
print("Telephone No : ", custobj.gettelephoneno())