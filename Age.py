import sys

name=sys.argv[1]
year_Of_Birth=int(sys.argv[2])
current_Year=int(sys.argv[3])

age=current_Year-year_Of_Birth;

print(name+" is ",age," years old."); 

