def Reverse_Check(n):
    num_string = str(n)
    
    reverse_str = num_string[::-1]
    
    if num_string == reverse_str:
        print("Yes")
    else:
        print("No")

n = int(input())

Reverse_Check(n)
