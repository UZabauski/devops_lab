def year(y):
    while 1900 <= y <= 10 ** 5:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            print("True - year is leap")
            break
        else:
            print("False - year isn't leap")
            break
    else:
        print(r"Wrong year, input correct year 1900<=y<=10**5")
        y = int(input("Input year: "))
        year(y)
    return year


y = int(input("Input year: "))
year(y)
