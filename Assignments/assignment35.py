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