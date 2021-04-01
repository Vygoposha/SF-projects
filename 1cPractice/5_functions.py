# def linear_solve(a, b):
#     if a:
#         return b / a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
# print(linear_solve(10,5))
# print(linear_solve(0, 9))
# print(linear_solve(0, 0))

def D(a,b,c):
    return b**2 - 4*a*c

def quadratic_solve(a, b, c):
    if D(a,b,c,)<0:
        return "Нет вещественных корней"
    elif D(a,b,c)==0:
        return -b/(2*a)
    elif D(a,b,c)>0:
        return (-b - D(a,b,c)**0.5)/(2*a), (-b + D(a,b,c)**0.5)/(2*a)

L = list(map(float, input().split()))
print(L)
print(quadratic_solve(L[0], L[1], L[2]))
print(quadratic_solve(a,b,c))