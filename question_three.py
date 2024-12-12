#3(i) code snippet to ask user for age and check for eligibility

print('ELIGIBILITY CHECK')
age = int(input('Please enter your age: '))

if age >= 18:
    print('You are eligible.')
else:
    print('You are not eligible.')


#3(ii) Grading function

def grade_students(mark):

    if mark >= 90:
        print('A')
    elif mark >=80:
        print('B')
    elif mark >= 70:
        print('C')
    elif mark >= 60:
        print('D')
    else:
        print('F')

#3(iii) Function test with the mark of 85
grade_students(85)




#3(iv)FUNCTION MODIFICATION
#using python error handling concept

def grade_students(mark):
    try:
        mark = float(mark)  # Ensuring the number is valid.
        if mark >= 90:
            print('A') 
        elif mark >= 80:
            print('B')
        elif mark >= 70:
            print('C')
        elif mark >= 60:
            print('D')
        elif mark >= 0:
            print('F')
        else:
            return 'Invalid Input'  
    except ValueError:
        return 'Invalid Input'


#function test with both a valid and an invalid input.

print(grade_students(85))  # valid input

print(grade_students('hello'))  # invalid input


#3(v) FUNCTION ENHANCEMENT TO PROVIDE A MESSAGE ALONG WITH GRADE

def grade_students(mark):
    try:
        mark = float(mark)  # Ensure the number is valid.
        if mark >= 90:
            print('A:', 'Excellent') 
        elif mark >= 80:
            print('B:', 'Excellent')
        elif mark >= 70:
            print('C:', 'Good')
        elif mark >= 60:
            print('D:', 'Satisfactory')
        elif mark >= 0:
            print('F:', 'Needs improvement')
        else:
            return 'Invalid Input'  
    except ValueError:
        return 'Invalid Input'
    

#3(vi) MODIFIED FUNCTION TEST
grade_students(78)
  
