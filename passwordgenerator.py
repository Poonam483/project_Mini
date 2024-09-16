import random
import string
print("HELLO WELCOME TO RANDOM PASSWORD GENERATOR!")
def gen(length):
    p=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    password=random.sample(p,length)
    return("".join(password))
length=int(input("Enter the length of password you want:"))
password=gen(length) 
print("Your Password is ",password)   