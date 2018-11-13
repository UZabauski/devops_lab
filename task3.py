def number(n):
    if n < 10:
        print(n + 10)
        return
    res = []
    for i in range(9, 1, -1):
        while n % i == 0:
            n = n / i
            res.append(i)

    if n > 10:
        print("-1")
        return
    n = res[len(res) - 1]
    for i in range(len(res) - 2, - 1, - 1):
        n = 10 * n + res[i]
    print(n)


n = int(input("Input number:"))
number(n)
