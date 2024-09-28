#we have to use if else condition for decision making in python
#check you are eligible for voting or not
#get the age from user
userAge = int(input("Enter your age"))
#to check the user is eligible for voting then check age must be greater than 18

# if userAge > 18:
#      print("You are eligible for voting")
# else: 
#      print("You are not eligible for voting ")
      
#check the user is elegible for vote and super vote
#check vote age should be greater than 55
#vote age should be greater than 18 and less than 55

if userAge > 18 and userAge < 55:
    print("You are elegible for voting")
elif userAge > 55:
    print("You are not elegible for super vote")
else:
    print("You are not eligible for voting")
