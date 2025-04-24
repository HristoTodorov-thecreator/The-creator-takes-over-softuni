#1. How do you declare a string variable in Python?
#A: By assigning a number directly to the variable.
#B: By enclosing the text in single or double quotes (e.g., name = "Alice").
#C: Using a dedicated string data type declaration.
#D: Using a container to store string data in your program
# my answer b correct answer is b

#2. What is the output of the following code?
#my_dict = {"fruit": "apple"}
#my_dict["fruit"] = "banana"
#print(my_dict["fruit"])
#A: An error, you cannot modify dictionaries.
#B: "apple" (original value)
#C: "banana" (modified value)
#D: It will print the entire dictionary.
# my answer c correct is c

#3. How can you check the data type of a variable in Python?
#A: By using a specific function to define the data type.
#B: There's no way to check the data type in Python.
#C: The data type is automatically determined at runtime.
#D: By using the type() function
# my answer is d correct is d

#4. What is the difference between mutable and immutable data types in Python?
#A: There's no such distinction in Python.
#B: Mutable data types can be changed after creation, while immutable ones cannot.
#C: Mutable data types are faster for performance reasons.
#D: Immutable data types are used for storing user input.
# my answer is b correct is b

#5. How can you convert a string containing comma-separated numbers into a list of integers?
#A: There's no built-in way to do this directly.
#B: Use a loop to split the string and convert each element to an integer.
#C: Use the split() method on the string and then int() on each element to create a list of integers.
#D: None of this
# here the answer is c

#6. How can you iterate over elements in a list while modifying them simultaneously?
#A: You cannot modify elements while iterating in Python.
#B: You need to create a separate loop for modification.
#C: Use a for i in range(len(list)) loop to access indices and modify elements.
#D: Use a for element in list loop. This iterates directly over the elements, allowing in-place modification.
# here the correct is d

#7. What happens when you try to access an element outside the list's index range?
#A: The element is automatically created at that index.
#B: The code silently ignores the out-of-range access.
#C: You will get an IndexError exception.
#D: The program crashes.
# correct is c my answer c

#8. What is the concept of type hinting in Python, and how is it beneficial?
#A: Type hinting is a way to force specific data types during variable declaration (not enforced).
#B: Type hinting is a way to provide optional type annotations for variables and function arguments, improving code readability and potential static type checking with external tools.
#C: It's a mandatory requirement for Python programs.
#D: It allows for faster code execution.
# correct is b my answer a

#9. How can you deep copy a nested data structure (list of dictionaries) in Python to avoid unintended modifications?
#A: Copying the reference is sufficient, as changes won't affect the original.
#B: Use a loop to manually copy each element and create a new structure.
#C: There's no built-in way to achieve a deep copy.
#D: Use the copy module's deepcopy() function to create a new, independent copy of the entire nested structure.
# correct is d my answer is d

#10. How can you convert a string representation of a number (e.g., "123") to an actual integer in Python?
#A: number = "123"
#B: number = int("123")
#C: number = number + 0
#D: number = number('123')
# correct is b my answer is b

#11. BONUS QUESTION -> What does the global keyword do in Python, and when should it be used
#A: It creates a new local variable in the current function.
#B: It declares that a variable inside a function refers to a global variable defined outside the function.
#C: It is used to import all global functions from the Python standard library.
#D: It makes all local variables global in scope.
# correct is b my answer is b


#def test_func(x, lst=[]):
  #  lst.append(x)
  #  return lst

#print(test_func(1))
#print(test_func(2))

#A: [1] and [2], because lst is initialized as an empty list each time the function is called.
#B: [1] and [1, 2], because the default mutable argument lst retains changes across function calls.
#C: [1] and an error, as the function does not handle multiple calls properly.
#D: An exception is raised due to appending elements inside a function.
# correct is b 


#12. BONUS QUESTION -> What is the output of the following Python code?
#original_list = [1, 2, 3, 4, 5]
#doubled = map(lambda x: x * 2, original_list)
#result = list(doubled)
#A: [2, 4, 6, 8, 10]
#B: [1, 2, 3, 4, 5, 2, 4, 6, 8, 10]
#C: [1, 2, 4, 8, 16]
#D: [2, 4, 8, 16, 32]


# otgovora e a za tova potursih v neta


#numbers = [2, 4, 6, 8, 10]
#result = [i for i in numbers if all(i % j != 0 for j in range(2, i))]
#A: [2, 4, 6, 8, 10]
#B: []
#C: [2]
#D: [10]
# tova sushto e 2 proverih go v neta

