import math as mth
import os
import random
#import sys
import re

print("Hello")

val2=4
var1="Hello"
print("This is value of variable var1: "+var1)
print("This is value of variable var1:",var1)

val="10"

print(val+"1")
print(int(val)+1)

print(type(var1))
#print(id(var1))

print(mth.sqrt(val2))

#os.mkdir("Python362")
#print("Folder Created")

#os.rmdir("Python362")
#print("Folder Deleted")

print(mth.ceil(24.2))
print(mth.floor(24.9))
print(random.randrange(2,5))

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])




#print("Hi, Enter your Name: ");
#name = input()
#print("Hi "+name+"!!")


##Regex

str="HelloEveryone H1*b0 H# H4 H*5 Hoi"
el = "EleCtRoNiCs"
test="Hello everyone H1234ABCD5678h Hiiii H11"

#H followed by Digit
if(re.search("H\d",str)!=None):
    print(re.search("H\d",str))
    print("Pattern Found")
#H followed by non-Digit
if(re.search("H\D",str)!=None):
    print(re.search("H\D",str))
    print("Pattern Found")
#H followed by Non-Alphanumeric(\W)
if(re.search("H\W",str)!=None):
    print(re.search("H\W",str))
    print("Pattern Found")
#H followed by number within range
if(re.search("H[1-4]",str)!=None):
    print(re.search("H[1-4]",str))
    print("Pattern Found")
#H followed by *(Since * is a wildcard, we need to use escape sequence \)
if(re.search("H\*",str)!=None):
    print(re.search("H\*",str))
    print("Pattern Found")
#H followed by . to check for a single alphabet
if(re.search("H.i",str)!=None):
    print(re.search("H.i",str))
    print("Pattern Found")
#How to perform case insensitive search
if(re.search("electronics",el,re.I)!=None):
    print(re.search("electronics",el,re.I))
    print("Pattern Found")
#How to perform substitution
if(re.sub(r"Hello",r"Hi",test)!=None):
    print(re.sub(r"Hello",r"Hi",test))
    print(test)
#How to perform substitution(Error)
if(re.sub(r"H(\d{4})[A-D](\d{4})",r"A(\1)(\D)(\2)H",test)!=None):
    print(re.sub(r"H(\d{4})[A-D](\d{4})",r"A(\1)(\D)(\2)H",test))
    #print(test)


##If-else stmts

runway="free"

if(runway == "free"):
    print("Land")

else:
    print("Circle in Air")

print("Outside If")


##Assignment

print("Please input age: ")
age = input()
Age=int(age)

if(Age>=18):
    print("Do you have VoterId(Y/N): ")
    hasVoterId=input()
    if(hasVoterId == 'Y' or hasVoterId == 'y'):
        print("You can Vote")
    else:
        print("You cannot vote")

else:
    print("You are not eligible for voting")


#Get 3 number from user during program invocation. Write a script which points 1 if the sequence is a trimax number.
    #A sequence is a trimax number if the third input is a number between first two inputs
    # sc2.py 10 15 11
    #Output : 1

# Python script to get the year of birth, current year and display <name> "is" <years> "old."
# Python script to get the year of birth, current year and display <name> "is" <years> "old." get input from user during program execution
# convert a date of yyyy-mm-dd to dd-mmm-yyyy format

#####String Manipulation#####

str1="Welcome to Pune"
# >>> print(str1[3].split(" "))
# ['c']
# >>> li = str1.split(" ")
# >>> li[2]
# 'Pune'
# >>> str1.length()
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'length'
# >>> str1.len()
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'len'
# >>> str1.len
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'len'
# >>> len(str1)
# 15
# >>>

print(len(str1))
#String Slicing
print(str1[0:7])
print(str1[0:7:2]) #step count 2
print(str1[-4:-1])   
print(str1[-1:-4]) #No output
print(str1[-1:-4:-1])    
print(str1[::-1]) #Reverse string
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
username="rahul singh"
u2="111"
print(username.isalpha()) ##Space is not considered in isalpha
print(u2.isdigit()) ##True

print(username[:4])
print(username[0:])
print(username[::-1])


print(username.count("h"))
print(username.count("r")) # if letter not present then output will be zero
print(username.count("abc")0 # Output: 0(case sensitive)

print(username.replace("rah","vip"))

## Tuple and String are immutable whereas List and dictionary are mutable(means you can make changes to it)
print(id(username))
username=username+" Rajaput"
print(id(username))

###Split

li=username.split(" ")
print(l1)

## List is a collection of any data type

li=[]
li.append("Hello")
li.append(1)
print(li)

print(li[1])

li[1]=4
print(li)


## To add an element in the beginning of the list
list2=[2,5,6]
list2 = [1]+list2

## Appending the list within a list
list2.append([7,8,9])
print(list2)

## Tuple

t1=(1,2,3)
print(t1)
print(t1[2])


t1=t1+4 
print(t1) ## Will give error cannot concatenate int

t2=(1,2,3)
t2=t2+(4,)
print(t2)


### Dictionary

d1=[] ## Empty Dictionary

d1["a"] = 1
print(d1)
d1["b"]=2
d1["a"]=3
## Values can have duplicates but keys cannot
print(d1)


print(d1["b"]) ## you can access values using keys but not keys using values


####Loops

for i in 1,2,3:
	print(i)
	
for i in "hello":
	print(i)
	
for i in "hello","abc":
	print(i)
	
##Error since integer is not iterable like string
for i in 1234:
	print(i)
	
	
for i in range(1,11):
	print(i)
	
for i in [1,2,3,4]:
	print(i)
	
for i in (1,2,3,4):
	print(i)
	
#2 is step count	
for i in range(0,6,2):
	print(i)
	
for i in range(0,6,-1):
	print(i) ##No Output
	
for i in range(0,-4,-1):
	print(i)
	
for i in range(-6,0):
	print(i)
	

lst=["abc","def","ghi","jkl"]

for i in lst:
	print(i)
	

for i in range(0,len(lst)):
	print(i)
	
## Iterating through index	
for i in range(0,len(lst)):
	print(lst[i])

## Print the even index value
for i in range(0,len(lst)):
	if(i%2==0):
		print(lst[i])
	


### While loop

wt_limit=150
while(wt_limit>0):
	print("Enter the weight of the bag:")
	wt=input()
	wt_limit=wt_limit-int(wt)
	print("available wt limit:", wt_limit)
	
print("The limit is over")


###Continue and break

for passenger in "A","FC","C","FA","SP","A":
	if(passenger =="FC" or passenger=="FA"):
		print("No Check reqd")
		continue
	if(passenger=="SP"):
		print("Declare Emergency")
		break
	if(passenger =="A" or passenger=="C"):
		print("Proceed with normal check")
	print("Check the person")
	
	
	
## Pass


	
	

	
	
































































































    



















