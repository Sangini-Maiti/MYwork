#Genarate a dictionary where keys are numbers between 1 and n and values are their squares.

n=int(input("Enter the value of n in integer: ")) #To get inputs from user
square_dict={} #Creating a dictionary
square_dict={n:n**2 for n in range(1,1+n)}   #Implementing the logic
print(square_dict) #Printing the final result
