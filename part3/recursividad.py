def factorial(num):
    if num == 1:
        return 1
    else:
        aux = num * factorial(num-1)
        return aux

print(factorial(5))    