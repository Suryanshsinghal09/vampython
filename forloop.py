#For loop is used to complete the iteration or repeating the task
# name= input("Enter your name")
# #Iteration my name using for loop
# # e.g. in c for(int i=0; i<10; i++)
# for i in name:
#     print(i)

# #print the no 1 to 10
# for x in range(1,11):
#     print(x)

# #print this pattern using for loop 1 3 5 7 9 11
# for x in range(1, 12,2):
#     print(x)

# print this pattern using for loop 1 3 5 7 9 11 solve
for x in range(1, 12):
    if x%2 != 0:
        print(x)

#print the even no and odd no using for loop from 1 to 20   {by range}
#for x in range(1, 21, 2):
#    print(x)
# for x in range(0, 21, 2):
#     print(x)

# by loop
for y in range(1, 21):
    if y%2 ==0:
        print("Even no", y)
    else :
        print("odd no", y)

