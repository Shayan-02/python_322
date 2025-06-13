a = int(input("enter num1: "))
b = int(input("enter num2: "))
c = int(input("enter num3: "))
d = int(input("enter num4: "))
if 0 <= a <= 20:
    if 0 <= b <= 20:
        if 0 <= c <= 20:
            if 0 <= d <= 20:
                f = (a + b + c + d) / 4
                if f >= 18:
                    print("a")
                elif f >= 16:
                    print("b")
                elif f >= 14:
                    print("c")
                elif f >= 10:
                    print("d")
                else:
                    print("fail")
            else:
                print(f"nomre {d} ghalateh")
        else:
            print(f"nomre {c} ghalateh")
    else:
        print(f"nomre {b} ghalateh")
else:
    print(f"nomre {a} ghalateh")
