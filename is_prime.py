# условие
#-------------------------------------------------------------------------------------------------------------------------

# создаю функцию с именем is_prime(она принемает значене а)
# а число которое будет проверятся на четность
def is_prime(a):          
    if a % 2 == 0:              # идет проверка делится ли а на 2 без остатка. Если остаток 0, то число четное 
        b = True                # b (если число четное) присваеивается значение True
        return(b)               # возвращается значение b(в данном случае это True(если число четное))
    else:                       # если условие не выполняется(число оказывается нечетным)
        b = False               # b присваивается значение False(значит число не четное)
        return(b)               # возвращается значение  b(в данном случае это False(если число нечетное))
    
#main fuction
def main():
    user_number = float(input("Введите число  "))
    TF = is_prime(user_number)    
    TF = is_prime(user_number)              # вызывается функция с переданным в неё числом number (результат проверки сохраняется в переменную TF)
    if TF == True:                     # если значение TF = True
        print(user_number," четное")        # выводится, что число четное 
    else:                              # если значение TF = False
        print(user_number," нечетное")      # выводится, что число нечетно


main()








