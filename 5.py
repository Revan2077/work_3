def print_smaller():
    num1, num2 = map(int, input().split())
    
    if num1 < num2:
        print(num1)
    else:
        print(num2)

print_smaller()
