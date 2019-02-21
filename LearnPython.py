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
	
# import sys


# #Get 3 number from user during program invocation. Write a script which points 1 if the sequence is a trimax number.
    # #A sequence is a trimax number if the third input is a number between first two inputs
    # # sc2.py 10 15 11
    # #Output : 1
	
# a=int(sys.argv[1])
# b=int(sys.argv[2])
# c=int(sys.argv[3])

# if(c>a and c<b):
	# print(1)

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


## Exceptions

try:
	print("Enter Num1:")
	a=int(input())
	print("Enter Num2:")
	b=int(input())
	c=a+b
	
	print(c)
	
except ValueError:
	print("Enter a number")
except ZeroDivisionError:
	print("Division by zero incorrect. Enter number greater than zero")
except:
	print("Something went wrong")


### whatever happens in code finally block will be executed



## Functions

def fn_name():
	return value
	
	
def sum1(a,b):
	c=a+b
	return c  ## If we remove the return stmt, the output will be None
	
result= sum1(5,6)
print(result)

###File Handling


file1=open("new1.txt","w") ## will search for the file, if it is present then overwrite else will create a new file.
file1.write("123") ##Content overwritten
file1.close()

##Apart from write there are two more modes, read and append

file1=open("new1.txt","a")
file1.write("Welcome");
file1.close()

## Open the file for reading

file1=open("new1.txt","r")
text=file1.read()
print(text)
file1.close()

l1=[123,456,789]

file1=open("data.xls","w")
for i in l1:
	print(i)
	file1.write(str(i)))
file1.close()


l1=[123,456,789]

file1=open("data.xls","w")
for i in l1:
	print(i)
	file1.write(str(i)+"\n"))
file1.close()

l1=[123,456,789]

file1=open("data.xls","w")
for i in l1:
	print(i)
	file1.write(str(i)+"\t"))
file1.close()




l1=[123,456,789]
l2=["Jack","Peter","Mark"]

file1=open("data.xls","w")
for i in range(0,len(l1)):
	print(i)
	file1.write(str(l1[i])+"\t"+l2[i]+"\n")
file1.close()



	
## mysql -h 192.168.5.1 -D python_database -U test1 -p  


## Connection to a database

import mysql.connector as maria_db

con = maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
cur = con.cursor()

cur.execute('Insert into computer values(1011,"Acer",59000)')

print("Connection Established Successfully")
cur.close()
con.commit()
con.close()


## Update
import mysql.connector as maria_db

con = maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
cur = con.cursor()

cur.execute('Update computer set Name='ACER' where CID=1001')

print("Connection Established Successfully")
cur.close()
con.commit()
con.close()
	
## Delete 

import mysql.connector as maria_db

con = maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
cur = con.cursor()

cur.execute('Delete from computer where CID=1003')
print(cur.rowcount)
print("Connection Established Successfully")
cur.close()
con.commit()
con.close()
	
	
## Select

import mysql.connector as maria_db

con = maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
cur = con.cursor()

cur.execute('select * from computer')

for row in cur:
	print(row)

print("Connection Established Successfully")
cur.close()
con.commit()
con.close()

## Count

## Select

import mysql.connector as maria_db

con = maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
cur = con.cursor()

cur.execute('select * from computer')

for row in cur:
	pass
	#print(row)

print(cur.rowcount)
print("Connection Established Successfully")
cur.close()
con.commit()
con.close()

## Insert into db with input values
import mysql.connector as maria_db

con = maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
cur = con.cursor()

print("Enter CID")
cid=input()
print("Enter name")
name=input()
print("Enter Cost")
cost=input()

cur.execute('Insert into computer values('+cid+',"'+name+'",'+cost+')')

print("Connection Established Successfully")
cur.close()
con.commit()
con.close()

### 

# import mysql.connector as maria_db

# con=maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
# print("Connection Established Successfully!!")
# con.close()

def submit():
	window.destroy()
	exit()

from tkinter import *

window=Tk()
window.title("My App")
window.geometry("500x500")

label1=Label(window,text="Welcome Page", width=20, font=("bold",20))
label1.place(x=80,y=80)

label2=Label(window,text="CID", width=20, font=("bold",10))
label2.place(x=80,y=120)
textbox2=Entry(window,width=20,bg="white")
textbox2.place(x=180,y=120)

label3=Label(window,text="Name", width=20, font=("bold",10))
label3.place(x=80,y=140)
textbox3=Entry(window,width=20,bg="white")
textbox3.place(x=180,y=140)

label4=Label(window,text="Cost", width=20, font=("bold",10))
label4.place(x=80,y=160)
textbox4=Entry(window,width=20,bg="white")
textbox4.place(x=180,y=160)

submit=Button(window,bg="sky blue",text="Close",command=submit)  #, command=submit
submit.place(x=180,y=200)

output=text(window,width=40,bg="white")
textbox4.place(x=180,y=160)

window.mainloop()


### GUI to add data in a table in database

import mysql.connector as maria_db

# con=maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
# print("Connection Established Successfully!!")
# con.close()

def submit():
	con=maria_db.connect(host='192.168.5.1', user='user1', password='infy@123', database='python_database')
	cur=con.cursor()
	cid=textbox2.get()
	cname=textbox3.get()
	cost=textbox4.get()
	
	cur.execute('Insert into computer values('+cid+',"'+cname+'",'+cost+')')
	
	cur.close()
	con.commit()
	con.close()

from tkinter import *

window=Tk()
window.title("My App")
window.geometry("500x500")

label1=Label(window,text="Welcome Page", width=20, font=("bold",20))
label1.place(x=80,y=80)

label2=Label(window,text="CID", width=20, font=("bold",10))
label2.place(x=80,y=120)
textbox2=Entry(window,width=20,bg="white")
textbox2.place(x=180,y=120)

label3=Label(window,text="Name", width=20, font=("bold",10))
label3.place(x=80,y=140)
textbox3=Entry(window,width=20,bg="white")
textbox3.place(x=180,y=140)

label4=Label(window,text="Cost", width=20, font=("bold",10))
label4.place(x=80,y=160)
textbox4=Entry(window,width=20,bg="white")
textbox4.place(x=180,y=160)

submit=Button(window,bg="sky blue",text="Close",command=submit)  #, command=submit
submit.place(x=180,y=200)

output=text(window,width=40,bg="white",height=5,wrap=word)
output.place(x=250,y=250)

window.mainloop()



### FTP

from ftplib import ftp

ftp=FTP('192.169.5.1')  ## Connect to the FTP Server
ftp.login(user='admin',passwd='infy@123') 

print("Logged in")
print(ftp.pwd())
ftp.quit()


## FTP login as anonymous

from ftplib import ftp

ftp=FTP('192.169.5.1')  ## Connect to the FTP Server
ftp.login('anonymous') ##or ftp.login()

print("Logged in")
print(ftp.pwd())  ## / refers to /var/ftp

ftp.dir()  ## to list files and folders in current working dir

ftp.cwd('pub') ## Change working directory
ftp.dir()

###ftp.dir('/path') or ftp.retrlines('list /path')

ftp.mkd('/path/dir_name') ## make directory
ftp.delete('/path/file_name') ## remove file
ftp.rmd('/path/dir_name') ## remove directory
ftp.rename('from_name','to_name') #rename file not works in anonymous


ftp.quit()


### Upload the file from client to server

from ftplib import ftp

ftp=FTP('192.169.5.1')  ## Connect to the FTP Server
ftp.login(user='admin',passwd='infy@123')
##ftp.cwd('/pub')
file_name=input("Enter the filename")
file=open('f11','rb')
ftp.storbinary('STOR f11', file1)
file1.close()
ftp.quit()


## download a file

from ftplib import ftp

ftp=FTP('192.169.5.1')  ## Connect to the FTP Server
ftp.login(user='admin',passwd='infy@123')
##ftp.cwd('/pub')
file_name=input("Enter the filename")
file=open('f22','wb')
ftp.retrbinary('RETR f22',file.write)
file.close()
ftp.quit()


## Paramiko

## Python implementation of secure shell


import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.5.1',username='sshuser',password='infy@123')

print("Connection Established Successfully")
stdin,stdout,stderr = ssh.exec_command('touch abcd')
stdin,stdout,stderr = ssh.exec_command('ls')

for i in stdout:
	print(i)
	
for file in stderr:
	print(file)

ssh.close()


### GenerateTicket

#total_Num_of_Ticket=180

file1=open("C:/Users/shresth_gupta01/Desktop/Tickets_Data.txt","r")
tickets=int(file1.read())

print("Enter Movie Name:")
movie_Name = input()
print("Enter number of tickets:")
number_Of_Tickets=int(input())

for i in range(0,number_Of_Tickets):
	t_no=tickets-i
	print("1M"+str(t_no))
	
available_tickets=tickets-number_Of_Tickets
file1=open("C:/Users/shresth_gupta01/Desktop/Tickets_Data.txt","w")
file1.write(str(available_tickets))
file1.close()

# while(total_Num_of_Ticket!=0):
	# if(number_Of_Tickets>0):
		# #total_Num_of_Ticket-=number_Of_Tickets
		# print(number_Of_Tickets," Tickets booked Successfully")
		# print("Your tickets are:")
		# for i in range(total_Num_of_Ticket,(total_Num_of_Ticket-number_Of_Tickets+1)):
			# print("1M"+str(i))
			# file1.write("1M"+str(i)+"\n")
			# break
	
# total_Num_of_Ticket-=number_Of_Tickets
			
# file1.close()












































































    



















