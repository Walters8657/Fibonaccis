def fib(n):
    f1, f2, i = 0, 1, 1

    if (n < 1):
        return
    
    print(f1)

    while (i < n):
        print(f2)
        next = f1 + f2
        f1 = f2
        f2 = next
        i = i + 1

num = int(input('How many numbers do you want? '))

fib(num)