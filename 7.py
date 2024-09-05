def sum_numbers():
    
    a, b = map(int, input().split())
    
    if a < 1 or a > 100 or b < 1 or b > 100:
        return
    
    result = a + b
    print(result)

sum_numbers()
