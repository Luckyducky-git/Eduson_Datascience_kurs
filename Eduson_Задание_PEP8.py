# Получение коэффициентов
first_coefficient = int(input('a = ', ))
second_coefficient = int(input('b = ', ))
third_coefficient = int(input('c = ', ))

# Решение по сокращенной формуле, т.к. b - четное
if first_coefficient != 0 and second_coefficient % 2 == 0 and third_coefficient != 0:
    k = second_coefficient / 2
    d1 = k ** 2 - first_coefficient * third_coefficient
    k1 = (-k + d1 ** 0.5) / first_coefficient
    k2 = (-k - d1 ** 0.5) / first_coefficient

    print('так как коэффициент b - четное число, решаем по сокращенной формуле')
    print(f'k1 = {k1}')
    print(f'k2 = {k2}')

# Решение уравнения при с = 0
if first_coefficient != 0 and third_coefficient== 0 and second_coefficient != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_coefficient / first_coefficient}')

# Решение уравнения при b = 0 и third_coefficient = 0
if first_coefficient != 0 and second_coefficient== 0 and third_coefficient == 0:
    print(f'корни уравнения равны нулю, first_coefficient * x ** 2 = 0')

# Решение полного уравнения
if first_coefficient != 0 and second_coefficient % 2 != 0 and third_coefficient != 0:
    d = second_coefficient ** 2 - 4 * first_coefficient * third_coefficient
    if d > 0:
        k1 = (-second_coefficient + d ** 0.5) / (2 * first_coefficient)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(k1, 2)}')
        k2 = (-second_coefficient - d ** 0.5) / (2 * first_coefficient)
        print(f'второй корень равен: {round(k2, 2)}')  
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет') 
    else:
        k = -second_coefficient / (2 * first_coefficient)
        print(f'уравнение имеет один корень: {k}')

        # решение уравнения при b = 0
        if first_coefficient != 0 and third_coefficient != 0 and second_coefficient == 0:        
            if (- third_coefficient / first_coefficient) >= 0:
                k1 = ( -third_coefficient / first_coefficient ) ** 0.5
                print(f'первый корень равен: {k1}')
                k2 = (-1) * (( -third_coefficient / first_coefficient ) ** 0.5)
                print(f'второй корень равен: {k2}')
        if ( - third_coefficient / first_coefficient ) < 0:
            print(
                f'-c/a = : {-third_coefficient / first_coefficient}, '
                f'т.е. < 0, поэтому действительных корней нет')
