#list is used to store multiple data
#list store different type of data like int string float
#list can store the duplicate data

#create list and store your friends name
friendsName = ["ivan", "anshu", "anjali", "vani"]

#to access the data from list
#to get the single data from list -> listVariableName[indexNo]
# print(friendsName[3])

#to print the complete list
# for name in friendsName:
#     print(name)

#operation on list -> append will add data in end of the list
# friendsName.append("Sam")
#insert will add the data based on the index no
# friendsName.insert(0, "Sanya")
# friendsName.insert(14, "Sanya")

#to remove the data from list
# friendsName.remove("ivan")
# friendsName.remove("Sanya")

#to remove the data using pop
# friendsName.pop(0)

#to reverse the list
# friendsName.reverse()
#to delete the complete list
# friendsName.clear()

#to print the complete list
friendsName.append("rahul")
friendsName.append("rohit")
friendsName.append("Manik")

#for name in friendsName[1:3]: #starting index, 3 endindex-1
    #[ivan 0, anjali 1, anshu 2, vani 3]
    #print(name)

# for name in friendsName[2:6]
#     print(name)
# print(friendsName)
# for name in friendsName[:-1]:
#     print(name)

friendsName[0]= "ivan sharma"
friendsName.sort()

for name in friendsName[:]:
    print(name)

#WAP to add 10 student name in list, remove last value,
#reverse the list 
#sorting the name
