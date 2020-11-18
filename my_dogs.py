# -----------------
# my_dogs.py
# -----------------
from dog import Dog

# Instantiation of Dog
my_dog = Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

dog_2 = Dog("Matt", "SuperDog")
dog_2.bark()

dog_3 = Dog("Chris", "SuperDog")
dog_3.sit()

dog_4 = Dog("Alex", "SuperDog")
dog_4.roll_over()
