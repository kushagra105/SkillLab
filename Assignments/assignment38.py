# Assignmnet 38: Write a program to show pass by refrence method
def compare(phoenix_to_slc , phoenix_to_tampa):
    if phoenix_to_slc > phoenix_to_tampa:
        print ("SLC is far from Phoenix as compared to Tampa, Florida")
    elif (phoenix_to_slc < phoenix_to_tampa):
        print ("Tampa,Florida is far from Phoenix compared to SLC")
    else :
        print ("Both locations are equidistance from Phoenix")
compare (1790, 506)
compare (phoenix_to_tampa = 506, phoenix_to_slc = 1790)

# ===================OUTPUT====================
# SLC is far from Phoenix as compared to Tampa, Florida
# SLC is far from Phoenix as compared to Tampa, Florida