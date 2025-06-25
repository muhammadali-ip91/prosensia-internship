
full_name = input('enter your full name  :')

s = full_name.find(' ')

first_name = full_name[:s]
last_name = full_name [s:]

print(f'first name is {first_name}')
print(f'last name is {last_name}')

num1 = float(input('enter your first number : '))
num2 = float(input('enter your second number : '))

print (f'add the number ={num1 + num2}')
print (f'subtract the number ={num1 - num2}')
print (f'multiply the number ={num1 * num2}')
print (f'divide the number ={round (num1 / num2 , 3)}')