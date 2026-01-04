# 1.       	Write a Python program to check whether the no is even and odd.	 	 	

def evenorodd():
   # do only this code
  n = int(input("Enter a number"))
  if n%2 == 0:
    print("even")
  else:
    print("odd")
    



# 2.       	Write a Python program to display Greater no between 3 inputs.	 	

def greaterno():
   # do only this code
  a= int(input("enter first number: "))
  b= int(input("enter seccond number: "))
  c= int(input("enter third number: "))
  
  if(a > b and a > c):
    print(a, "is gratest")
  elif(b > a and b > c ):
    print(b," is greatest")
  elif(a==b and b==c):
    print("all numbers are equal")
  elif(a==b and b > c):
    print(f'{a} & {b} are equal and greater than {c}')
  elif(a==c and c > b):
    print(f"{a} & {c} are equal and greater than {b}")
  else:
    print(c," is greatest")
    
# greaterno()
 	
# 3.       	Write a Python program to print prime no between n and m using Recursion.
def is_prime(n,i=2):
  if n < 2:
    return False
  if i*i > n:
   return True
  if n%i == 0:
    return False
  return is_prime(n, i+1)

  

def printPrime(start, end):
  if start > end:
    return
  if is_prime(start):
    print(start)
  return printPrime(start + 1, end)

# s = int(input("Enter Start "))
# e = int(input("Enter End "))

# printPrime(s,e)
  

# 4.       	Write a Python program to display Fibonacci series using Recursion. 

def display_fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return display_fib(n-1) + display_fib(n-2)

# for i in range(0, 8):
#   print(display_fib(i))
    
    	 	 	
# 5.       	Write a Python program factorial of no.	 	 	

def factorial(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  return n * factorial(n-1)

# print(factorial(6))
# 6.       	Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form 
# (x, x*x).	 	 	
# 	Sample Dictionary ( n = 5) :			
# 	Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}	

def dictPract():
  # do only this code
  newdict = {}
  n = int(input("Enter a number "))
  for i in range(1, n+1):
      newdict[i] = i*i
  print(newdict)
  
  
# 7.       	Create a Dictionary antaining 5 elements in the form of key value pair, and write python code to perform the following operation on it:
# 1.	To display all the keys.
# 2.	Add new Key Value Pair.
# 3.	Delete specific element from the Dictionary.
# 4.	To modify value of particular key. 

def pract7():
  # do only this code
  newdict = {
    "name" : "Sourabh",
    "age": 26,
    "class": "Middle",
    "Married": True,
    "spouse": "alisha"
  }
  
  print(newdict.keys())
  newdict["child"] = "salish"
  newdict.pop("class")
  newdict["age"] = 28
  
  print(newdict)
  
# pract7()

	 	 	
# 8.       	Write a program to create a set by accepting n elements (1-9 or A-Z or a-z) input from the users. 
# i.	Display Set Elements 
# ii.	Display Length of Set 
# iii.	Count number of digits, Lowercase letter and uppercase letter in a set.	 

def pract8():
  # do only this code
  newset = set()
  n = input("Enter number between 0-9, A-Z, a-z ")

  for i in n:
    newset.add(i)
  
  print(newset)
  print(f"length of set:- {len(newset)}")
  digit = 0
  upper = 0
  lower = 0
  for i in newset:
    if i.isdigit():
      digit += 1
    elif i.isupper():
      upper +=1
    elif i.islower():
      lower += 1
  print(f"digits = {digit},\nUppercasr Letters = {upper}\nLowercase Letter = {lower}")


  
# 9.       	Write a python program to create a separate list of digit from original list which contains digit and alphabets using list comprehension.
# (Input List – [‘a’, ‘b’, 2 , 5,’Hi’, 500, 900, ‘pqr’] )
# (Output List – [2,5,500,900] 	 	 	

def pract9():
  List = ['a','b', 2, 5, 'Hi', 500, 900, 'pqr']
  digits = [x for x in List if isinstance(x, int)]
  print(digits)


# Sr. No.	Title of Program	Page no	Date  	Sign
# 1.       	Write a Python program to check whether the no is even and odd.	 	 	
# 2.       	Write a Python program to display Greater no between 3 inputs.	 	 	
# 3.       	Write a Python program to print prime no between n and m using Recursion.	 	 	
# 4.       	Write a Python program to display Fibonacci series using Recursion. 	 	 	
# 5.       	Write a Python program factorial of no.	 	 	
# 6.       	Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form 
# (x, x*x).	 	 	
# 	Sample Dictionary ( n = 5) :			
# 	Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}			
# 7.       	Create a Dictionary antaining 5 elements in the form of key value pair, and write python code to perform the following operation on it:
# 1.	To display all the keys.
# 2.	Add new Key Value Pair.
# 3.	Delete specific element from the Dictionary.
# 4.	To modify value of particular key. 	 	 	
# 8.       	Write a program to create a set by accepting n elements (1-9 or A-Z or a-z) input from the users. 
# i.	Display Set Elements 
# ii.	Display Length of Set 
# iii.	Count number of digits, Lowercase letter and uppercase letter in a set.	 	 	
# 9.       	Write a python program to create a separate list of digit from original list which contains digit and alphabets using list comprehension.
# (Input List – [‘a’, ‘b’, 2 , 5,’Hi’, 500, 900, ‘pqr’] )
# (Output List – [2,5,500,900] 	 	 	


# 10.   	
# Write a Python program to construct the following pattern, using a nested loop number.	 	 	
# 	687954231			
# 	87954231			
# 	7954231			
# 	954231			
# 	54231			
# 	4231			
# 	231			
# 	31			
# 	1			  
# 13	Write a program to add Two matrices using List, accept elements for the matrices from the user.	 	 	
# 14	Write a Python program to remove the characters which have odd index values of a given string	 	 	
# 15	Write a python Code for List;
# i.	Create a list of animal consisting of following animals – Loin, Tiger, cow, ship, elephant, zebra 
# ii.	Delete zebra from the list.
# iii.	Print all alternative elements from the list.
# iv.	Sort the list in descending order.
# v.	Add horse to the list.	 	 	
# 16	Write a Python program to get the factorial of a non-negative integer using recursion.	 	 	
# 17	Write a generator function which will generate the next prime no from the number passed. For example if the numbers 14 then the next prime no is 17. 	 	 	
# 18	Write a program for Decorator.			
# 19	Write a program in which you need to calculate size of rectangle, square, circle and Triangle.(Separate Package need to be created for the same)	 	 	
# 20	Write a program that ask for an integer number. Accepted number should be in between 1 to 10 and break the loop if not then generate the exception and print an error message.	 	 	
# 21	Write a user defined exception program in python which will except age as input from the user and check whether the user is eligible for voting or not. If age< 18 it should raise the exception as ‘Not eligible to Vote. ’.	 	 	
# 22	Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.	 	 	
# 23	Write a python Program to create a class of bankdemo having attributes bank_Acc_No, Name, Balance write methods to_deposit, Withdraw and Check balance of Account. 	 	 	
# 24	Write Code to perform different types of Inheritance.	 	 	
# 25	Write a program to validate URL using regular expression. 	 	 	
# 26	Write a program to validate email using regular expression.	 	 	
# 27	Write a program to validate Password using regular expression.	 	 	
# 28	Write a Python Program to perform synchronized Multi-threading.	 	 	
# 29	Write a Program using Mongodb to create “Books” collection having fields: Title, Author, Publisher Price. Write a code to perform following operation
# 1.	Insert 5 documents into books collection
# 2.	Retrieve books whose publisher is “Person”. 
# 3.	Retrieve books whose price is between 400 to 600.
# 4.	Retrieve books in descending order of the price. 
# 5.	Update the price of book by 10% whose title is “Python”.
# 6.	Update the title of a book whose author is ‘Guido’ and publisher is “BPB”.	 	 	
# 30	Write a python Program using MongoDB to create “movies” collection with field (title, writer, year, actor, director) write a code to perform following operations:
# 1.	Insert 5 documents.
# 2.	Get all movies released before 2010
# 3.	Sort the movies according to directors.
# 4.	Get all the movies with actor set to “Rajniskant”.
# 5.	Get all document where director include “R. Kapoor”.
# 6.	Update writer of the movie “Devra”.
# 7.	Delete Movie is “Devra”.	 	 	
# 31	Create a Django project named StudentPortal and an app records. Define a model Student with fields: name, email, course, admission_date.
# Write programs to:
# 1.	Migrate the model
# 2.	Add new student records using Django shell
# 3.	Display all students using a view & template
# 4.	Update and delete a student record	 	 	
# 32	Create a Django form for adding a new Course with fields: course_name, duration, fees.Write:
# 1.	The forms.py code
# 2.	A view to handle GET (show form) and POST (save form data)
# 3.	A template to display the form
# 4.	Validation to ensure fees cannot be negative	 	 	
# 33.	Build a simple authentication module:
# 1.	Create a Register page to create a Django user
# 2.	Create a Login and Logout system
# 3.	Restrict a page /dashboard/ so only logged-in users can access it
# Write the code for:
# 4.	URL patterns
# 5.	Views
# 6.	Templates
# 7.	Using Django’s @login_required decorator			
# 34	Using Django Rest Framework:
# 1.	Create an API for the Student model
# 2.	Implement:
# o	List all students (GET)
# o	Create a student (POST)
# o	Update a student (PUT)
# o	Delete a student (DELETE)
# Write code for:
# 3.	Serializer
# 4.	API View / ViewSet
# 5.	URL routing using DefaultRouter			
# 35.	Create a WebSocket-based real-time notification feature.
# Tasks:
# 1.	Install & configure Django Channels
# 2.	Create a consumer that sends real-time messages
# 3.	Add a template that listens for WebSocket messages and displays them dynamically
# 4.	Write routing for channels
# Example: When a new student is added, a WebSocket message “New student added!” should appear instantly on the frontend.
			