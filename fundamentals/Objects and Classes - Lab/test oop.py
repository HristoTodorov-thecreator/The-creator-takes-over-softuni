#1. What is the correct way to define a simple class Person in Python?
#A: class Person: pass
#B: def Person: pass
#C: Person(): pass
#D: class Person(): def __init__(self): pass

# correcft is a my answer a

#3. What is the correct way to inherit from a base class in Python?
#A: class Child extends Parent:
#B: class Child inherits Parent:
#C: class Child(Parent):
#D: class Child.Parent:
# correct c my answer c
#5. Which of the following defines a class attribute in Python?
#A: self.attribute = 5
#B: attribute = 5
#C: def __init__(self): self.attribute = 5
#D: cls.attribute = 5

#B: attribute = 5 corr my naswer b

#7. Which of the following correctly represents encapsulation in Python?
#A: Private methods and attributes are defined with a single leading underscore _
#B: Private methods and attributes are defined with double leading underscores __
#C: Methods and attributes defined with self
#D: All methods and attributes are public by default
# corr b my answ b

#8. Which of the following best represents polymorphism in Python?
#A: The ability to define a function with the same name in multiple classes
#B: Using inheritance to reuse code
#C: Encapsulating data in classes
#D: A class with only one method
# my answ a corr a

#9. How do you create a static method in Python?
#A: By using the @classmethod decorator
#B: By using the @staticmethod decorator
#C: By using def staticmethod(self)
#D: Static methods are not supported in Python
# i searched for this its b

#11. BONUS QUESTION -> What is method overriding in Python?
#A: When a subclass provides a new implementation of a method defined in its parent class
#B: When a method is defined multiple times in the same class
#C: When multiple methods are combined into one method
#D: When a method calls another method within the same class
#Answer
#
#Correct Answer -> A: When a subclass provides a new implementation of a method defined in its parent class
# 13. quest
#class Animal:
  #  def sound(self):
  #      return "Some sound"


#class Dog(Animal):
   # def sound(self):
       # return "Bark"


#a = Animal()
#d = Dog()
#print(a.sound(), d.sound())
# answer Some sound Bark
#quest 14
#class A:
  #  def f(self):
     #   return "A's f"
#

#class B(A):
    #def f(self):
       # return "B's f"
#

#class C(B):
   # pass


#c = C()
#print(c.f())
# answer is B's f

