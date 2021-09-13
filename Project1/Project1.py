#
#PROJECT 1: STUDENT PORTFOLIO/MARKSHEET
#

#taking in the details
name = input("Enter the name of the student: ")
std = int(input("Enter the standard: "))
div = input("Enter the division: ")
roll_no = int(input("Enter the roll number: "))
p_marks = int(input("Enter the marks for Physics (out of 100): "))
c_marks = int(input("Enter the marks for Chemistry (out of 100): "))
m_marks = int(input("Enter the marks for Mathematics (out of 100): "))

#calculating the percentage
percentage = ((p_marks + c_marks + m_marks)/300)*100

#Displaying:
print("\n")
print(" STUDENT PORTFOLIO ".center(50,"#"))     #To create a centered Heading
print("\n\tName:\t\t", name)                    #All those escape sequences just to display in an orderly format to make it look good
print("\tClass:\t\t", std, div)
print("\tRoll No.:\t", roll_no)
print("\n")
print(" SUBJECTS and MARKS ".center(50,"#"))    #To create a centered Heading
print("\n\tPhysics:\t", p_marks)
print("\tChemistry:\t",c_marks)
print("\tMathematics:\t",m_marks)
print("\nTotal Percentage = ",percentage)
