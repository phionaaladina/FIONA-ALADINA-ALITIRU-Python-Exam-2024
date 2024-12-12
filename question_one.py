#1.(i)

#import the math function
import math

#defining the function
def circle_area():
    radius = float(input('Please enter a circle radius: ')) #making the radius a user input
    area = math.pi * radius ** 2  #defining the formula to calculate the area
    print(f'The area of the circle of radius {radius} cm is {area:.2f} cm') #printing the area formatted to two decimal places

#calling the function
circle_area()




#1(ii)

numbers = [4, 7, 2, 9, 12, 15] # integer list

sum_odd_numbers = 0  #initializing the sum of odd numbers to 0

#for loop to iterate through the integer list
for number in numbers:
    if number % 2 != 0:
       sum_odd_numbers += number #suming up the odd numbers in each iteration

print("The sum of all odd numbers is:", sum_odd_numbers)   #out of sum of odd numbers



#1(iii)
#function creation
def num_operations():
    print('Please enter two numbers as follows:')
    first_num = int(input('Please enter the first number: ')) #user input
    second_num = int(input('Please enter the second number: '))  #user input

    sum = first_num + second_num  #sum of numbers

    difference = first_num - second_num # difference of numbers

    product = first_num * second_num  #product of numbers

    quotient = first_num // second_num #quotient of numbers

    #printing out the sum, difference, product and quotient of the numbers
    print(f'Sum of {first_num} and {second_num} is {sum}')
    print(f'Difference of {first_num} and {second_num} is {difference}')
    print(f'Product of {first_num} and {second_num} is {product}')
    print(f'Quotient of {first_num} and {second_num} is {quotient}')

num_operations() #function call




#1(iv)
#creating the dictionary

student_info = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}


#updating the value of age to 26
student_info['age'] = 26

#adding a new key-value pair
student_info['city'] = 'Kampala'

#printing the final dictionary
print(student_info)  
