#условие задачи
#--------------------------------------------------------------------

#convertstion fuction
def to_fahrenheit(c):
    return 1.8 * c + 32

#main fuction
def main():
    user_temp = float(input("Введите в градусах Цельсия"))
    res_temp = to_fahrenheit(user_temp)
    print("Ваша темпиратура в Фаренгейтах:", res_temp)


if __name__ == '__main__':
    main()