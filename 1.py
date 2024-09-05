def multi_table():
    x = int(input())

    if x < 1 or x > 100:
        return
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            print(a * b, end=" ")
        print()


multi_table()
