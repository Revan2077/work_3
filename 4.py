def nth_digit(n):
    big_number = ""
    for i in range(1, 5001):
        big_number += str(i)
    if x <= len(big_number):
        print(big_number[n-1])
    else:
        print()
        
x = int(input())
nth_digit(x)
