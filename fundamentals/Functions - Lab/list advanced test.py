#1. What is the correct way to create a list from a set of numbers in Python?
#A: my_list = set(1, 2, 3)
#B: my_list = list({1, 2, 3})
#C: my_list = {1, 2, 3}
#D: my_list = (1, 2, 3)
# my answer is b correct is b

#2. What is the output of the following Python code that squares all even numbers in a list?
#numbers = [1, 2, 3, 4, 5]
##result = sum(squared)
#A: 20
#B: 30
#C: 10
#D: 15
# my answer 20 correct is 20

#. Which list method is used to remove and return the last element from a list?
#A: my_list.remove()
#B: my_list.pop()
#C: my_list.extract()
#D: my_list.delete()
# answer is pop

#7. Which list comprehension would create a list of squares of numbers from 1 to 5?
#A: squares = [x^2 for x in range(1, 6)]
#B: squares = [x**2 for x in range(1, 6)]
#C: squares = [pow(x, 2) for x in 1..5]
#D: squares = [x*2 for x in range(1, 6)]
#Answer

#Correct Answer -> B: squares = [x**2 for x in range(1, 6)]

#8. How do you reverse the elements of a list in Python?
#A: my_list.reverse()
#B: my_list = my_list[::-1]
#C: reversed(my_list)
#D: All of the above
#Answer

#Correct Answer -> D: All of the above

#10. What will be the output of the following list comprehension?
#result = [x + y for x in [10, 20] for y in [30, 40]]
#A: [10, 30, 20, 40]
#B: [40, 50, 50, 60]
#C: [40, 50, 50, 60, 70]
#D: [40, 50, 60]
#Answer

#Correct Answer -> B: [40, 50, 50, 60]


#11. BONUS QUESTION -> What is the output of the following Python code using set() on a list?
#my_list = [1, 2, 2, 3, 3, 3, 4]
#unique_items = set(my_list)
#print(len(unique_items))
#A: 7
#B: 4
#C: 3
#D: 6
#Answer

#Correct Answer -> B: 4

#12. BONUS QUESTION -> What is the output of the following Python code?
#numbers = [1, 2, 3, 4, 5]
#result = filter(lambda x: x % 2 == 0, numbers)
#print(list(result))
#A: [1, 2, 3, 4, 5]
#B: [2, 4]
#C: [2, 3, 5]
#D: [1, 3, 5]
#Answer

#Correct Answer -> B: [2, 4]

#13. Additional QUESTION
#numbers = [1, 2, 3, 4]
#result = [x**2 for x in numbers if x % 2 == 0]
#A: [1, 4, 9, 16]
#B: [4, 16]
#C: [1, 9]
#D: []
#Answer

#Correct Answer -> B: [4, 16]

#14. Additional QUESTION
#umbers = [2, 4, 6, 8, 10]
#result = reduce(lambda x, y: x + y, numbers)
#A: 30
#B: 20
#C: 50
#D: 40
#Answer

#Correct Answer -> A: 30

