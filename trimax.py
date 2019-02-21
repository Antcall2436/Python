import sys


#Get 3 number from user during program invocation. Write a script which points 1 if the sequence is a trimax number.
    #A sequence is a trimax number if the third input is a number between first two inputs
    # sc2.py 10 15 11
    #Output : 1
	
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

if(c>a and c<b):
	print(1)