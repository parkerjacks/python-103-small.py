#Create a square of astericks made up of a NxN characters decided by user
#Set it Up
square_length = int(input("Enter a number for the length of your square: "))
square_is_made_of = '*'  
count = 0

#Work it Out 
while count < square_length: 
    print (square_is_made_of * square_length) 
    count = count + 1


#Finish
