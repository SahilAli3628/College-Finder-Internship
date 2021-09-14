#
#Project 3: Simple Multiplucation Table
#

#input part
num = int(input("Enter the number that you want the multiplication table of: "))
limit = int(input("Upto which number you want the tables to go? "))

#logic and printing output
print(" ")
#Printing the Heading
print(" Simple Multiplication Table ".center(50,"#"))

multiple = 1

while(multiple < limit+1):
    print(f"{num} x {multiple} = {num*multiple}")
    multiple += 1

print(" END ".center(50,"#"))
