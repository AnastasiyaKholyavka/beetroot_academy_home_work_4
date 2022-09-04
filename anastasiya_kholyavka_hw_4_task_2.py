'''
anastasiya_kholyavka
HW_4_task_2

The valid phone number program.

Make a program that checks if a string is in the right format for 
a phone number. The program should check that the string contains 
only numerical characters and is only 10 characters long. 
Print a suitable message depending on the outcome of the string evaluation.

'''
phone_number = 'ftdcjgddfg'

if 'phone_number'.isdigit and len(phone_number) == 10 :
    print('Дякую, ваш номер передано службі підтримки')
    
elif len(phone_number) > 10 :
    print('Номер має містити десять цифр')
    
elif len(phone_number) < 10 :
    print ('Номер має містити десять цифр')
    
elif 'phone_number'.isdigit == False: # Це не працює
    print('Номер телефону має містити лише цифри')
    