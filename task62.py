def year(y):
    while 1900 <= y <= 10 ** 5:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            print("True - year is leap")
            break
        else:
            print("False - year isn't leap")
            break
    return year


if __name__ == "__main__":
    y = int(input("Input year: "))
    year(y)
