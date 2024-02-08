while True:
    a, b, c = map(int, input().split())

    if a + b + c == 0:
        break
    if a == b == c:
        print("Equilateral")
    elif a + b <= c or b + c <= a or a + c <= b:
        print("Invalid")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")