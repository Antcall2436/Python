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