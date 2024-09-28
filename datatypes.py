#data type is used to defined the data in which form

#int data is used to store the numeric type data
#Note in python we don't need to declare the datatypes
#we just assign the value in variable
#Variable can store any type of value which type of data
age= 19
name = "Suryansh Singhal"
salary = 3000.89

#how to pass the variables inside the print statement
#we have 3 ways to pass the variable in print statement
#print("My name is"+ name + "and salary" + salary+ " and age" + age)
#It generate the type error, bcz string only concatenate with string nor int 
#Solution 1:- replace + by , when data type is not string
print("My name is" + name + " and salary", salary, "and age", age)
#solution 2:- pass the variable in print statement with f{}
print(f"my name is {name} salary is {salary} and age {age}")
#Solution 3:- typecast the data into string
salaryString = str(salary)
ageString = str(age)
print("My name is" + name + " and salary " + salaryString + " and age" + ageString)

#to find the type of data we need to use type() function
print(type(name))
print(type(age))
print(type(salary))

