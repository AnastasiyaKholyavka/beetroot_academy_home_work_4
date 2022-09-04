'''
anastasiya_kholyavka
HW_4_task_1

String manipulation

Write a Python program to get a string made of 
the first 2 and the last 2 chars from a given string. 
If the string length is less than 2, return instead of the empty string.

1. Sample String: 'helloworld'

Expected Result : 'held'

2. Sample String: 'my'

Expected Result : 'mymy'

3. Sample String: 'x'

Expected Result: Empty String

'''
# 1. Підозрюю, то має робитися більш просто. 

l_h = 'helloworld'[0]
l_e = 'helloworld'[1]
l_l = 'helloworld'[2]
l_d = 'helloworld'[-1]
print(f'{l_h}{l_e}{l_l}{l_d}')

# 2. 

print('my'*2)

# 3.

ryadok = 'x'
if len(ryadok) < 2:
    print('')