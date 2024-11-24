# num1 = int(input("enter number: "), 2)
# num2 = int(input("enter number: "), 2)

# print(f"{num1 * num2 : b}")
# print(f'{num1}{num2}')

#--------------------- 
import string

s = string.punctuation
print(s) 

text = 'hello!there'

for char in text:
    if not char in s:
        print(char, end='')
    
    else:
        print(' ', end='')

print('\n')
# ------------------
s2 = string.digits
print(s2, type(s2))

s2 = string.ascii_uppercase
print(s2)

s2 = string.ascii_letters
print(s2)

text = 'hello world how are you?'
s2 = string.capwords(text) # this is a helper Function
print(s2)