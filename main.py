from string import printable
from random import choice

status = False

while status == False:
    size_password = int(input("Какой будет длина пароля? "))

    if size_password <= 7:
        print("Пароль слишком которкий, попробуйте еще раз")
    elif size_password > 20:
        print("Пароль слишком длинный, попробуйте еще раз")
    else:
        status = True

while status == True:
    password = ''.join([choice(list(printable)) \
               for symbol in range(size_password)])
    password = password.replace(' ', choice(list(printable)))
    password = password.replace('\n', choice(list(printable)))
    print("Пароль: {}".format(password))
    
    answer = input("Нравится полученный пароль? ")
    if answer == "нет" or answer == "Нет":
        status = True
    elif answer == "да" or answer == "Да":
        print("Отлично! Ваш новый пароль: ", password)
        status = False
    else:
        print("Ничего не понимаю! Попробуем в другой раз")
        break
        
