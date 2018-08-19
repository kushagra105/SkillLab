# Write a python program to find top 3 scorers and average of all students
student_details = {"John": 86.5,"Jack": 91.2,"Jill": 84.5,"Harry": 72.1,"Joe":80.5}
print ("Top three scorers are : ")
for i in range(3):
    print (sorted(student_details.values(),reverse = True)[i])
print ("Average marks of all students are :  ",sum(student_details.values())/len(student_details))