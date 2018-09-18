#assignment 35: Write a python program to satisfy below mentioned business requirements
java_course = {"John","Jack","Jill","Joe"}
python_course = {"Jake","John","Eric","Jill"}
print ("Number of students for python course are :",len(python_course))
print ("Students enrolled for java course only : ",java_course-python_course)
print ("Students enrolled for python course only : ",python_course-java_course)
print ("Number of students enroll for both java and python course : ",len(python_course & java_course))
print ("Students enroll for both java and python course : ",python_course & java_course)
print ("Number of Students enroll for either java or python course but not both : ",python_course ^ java_course)
print ("Students enroll for either java or python course but not both : ", python_course ^ java_course)
print ("Students enroll for either or python course : ",python_course | java_course)

# =========================OUTPUT========================
# Number of students for python course are : 4
# Students enrolled for java course only :  {'Jack', 'Joe'}
# Students enrolled for python course only :  {'Eric', 'Jake'}
# Number of students enroll for both java and python course :  2
# Students enroll for both java and python course :  {'Jill', 'John'}
# Number of Students enroll for either java or python course but not both :  {'Eric', 'Joe', 'Jake', 'Jack'}
# Students enroll for either java or python course but not both :  {'Eric', 'Joe', 'Jake', 'Jack'}
# Students enroll for either or python course :  {'Eric', 'Joe', 'Jake', 'Jill', 'John', 'Jack'}