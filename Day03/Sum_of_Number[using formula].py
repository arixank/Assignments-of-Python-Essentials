print("################################# Sum_Of_Natural_Numbers #####################\n")

#taking input from the user
natural_Number = int(input("Enter a natural number: \n"))
# I have stored this to display the actual number !!
temp = natural_Number
sum = 0
# Actually While loop is not required !!
while (natural_Number > 0):
    sum = (natural_Number * (natural_Number + 1)//2) # Gauss Formula !! n*(n+1)\2
    print(natural_Number , "--->" , sum)
    break

print(f"\nSum of natural numbers for the number {temp} is found out to be : {sum}")
