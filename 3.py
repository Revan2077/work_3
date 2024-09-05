def triangle():
    
    ag1, ag2, ag3 = map(int, input().split())
    if ag1 + ag2 + ag3 == 180  and ag1 > 0 and ag2 > 0 and ag3 > 0 :
        print("Yes")
    else :
        print("No")
triangle()
