import random
import string

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("Welcome to the Random Letter Generator!")
print("\nPlease Enter How Many Letters You Wish To Generate: ")
while True:
    number = int(input())
    if (number > 26):
        print("\nThat's Too Many Letters. Please Enter a Number less than 26.")
    else:
        word =  random.sample(letters, number)
        print("\nThank You. Here is Your Word: ", word)
        break
