#4(i)
#(a)
'''Object-Oriented Programming (OOP) is a concept in programming which organizes data and behavior
 into reusable structures called objects that are created using classes. '''


#OOP significance in programming
'''
- It allows objects to take multiple forms through polymorphism.
- Keeps code organised and neat through the use of classes and objects.
- Inheritance in object oriented programming allows code reusability.
- Code encapsulation concept helps in maintabilbility.

'''

#(b) #difference between a class and object
'''
A class is a blueprint for creating objects, defining the structure, attributes, and behavior of objects
while an object is an instance of a class. 
 
'''

#4(ii)WORD COUNT
sentence = input("Enter a sentence: ") #making the program dynamic using the input function for user to input a function
words = sentence.split() #splitting the sentence into individual words using the inbuilt split function

word_count = {} #initializing an empty dictionary
for word in words: #for loop to iterate through the words
    word_count[word] = word_count.get(word, 0) + 1 #appending the words split from the sentence to the empty dictionary as a key-value pair alongside the word count

print(word_count) #printing the dictionary to display the word count



#4(iii) PROGRAM TO RETURN SUM

#defining a function, numbers that takes two parameters a and b and returns their sum
def numbers(a,b):
    return a + b

#function test
print(numbers(3,4))

 
 # 4(iv) Define a `Car` class and instantiate an object.

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

# Instantiate the object
my_dream_car = Car("Tesla", "Convertible", "White")

#print car atrributes
print(f"MY DREAM CAR:")
print(f"Brand: {my_dream_car.brand}")
print(f"Name: {my_dream_car.name}")
print(f"Color: {my_dream_car.color}")



#4(v)Adding a start_engine method to the Car class 

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
    
    #add start_engine method
    def start_engine(self):
        print(f'The engine of the {self.color} {self.brand} car has started.')

#creating a car instance 
car_2 = Car('Mazda','Toyota', 'Black')

 #calling the start_engine method
car_2.start_engine()






