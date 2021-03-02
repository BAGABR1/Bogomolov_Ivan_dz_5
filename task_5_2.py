def ran_gen(n):
    ran_g = (i for i in range(1, int(n)+1))
    print(*ran_g)


ran_gen(input('Введите число n: '))
