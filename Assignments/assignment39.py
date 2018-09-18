# Assignment 39: Write a program to Solve the given problem
def check_baggage(baggage_amount):
    if (baggage_amount >= 0):
        return True
    elif (baggage_amount <= 40):
        return True
    else:
        return False
def check_immigration(expiry_year):
    if (expiry_year >= 2001, expiry_year <= 2025):
        return True
    else : 
        return False
def check_security(noc_status):
    if (noc_status == True):
        return True
    else:
        return False
def traveler():
    traveler_id = 1001
    traveler_name = 'Jim'
    baggage_amount = 35
    expiry_year = 2019
    noc_status = True
    if (check_baggage(baggage_amount) == True, check_immigration(expiry_year) == True, check_security(noc_status) ==True):
        print ("Traveler id is : ",traveler_id)
        print ("Traveler name is : ", traveler_name)
        print ("Allow travaler to fly")
    else:
        print ("Traveler id is : ",traveler_id)
        print ("Traveler name is : ", traveler_name)
        print ("Detain Traveller for re-checking!")
traveler()

# ======================OUTPUT=========================
# Traveler id is :  1001
# Traveler name is :  Jim
# Allow travaler to fly