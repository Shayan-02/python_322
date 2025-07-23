num = int(input("enter a number: "))

# if num == 0: # 0
#     print("zero")
# elif num % 2 == 0: # zoj
#     print("even")
# elif num % 2 == 1: # fard
#     print("odd")

if num == 0:
    print(num ,"is zero")
else:
    if num % 2 == 0:
        print(f"{num} is even")
    elif num % 2 == 1:
        print(f"{num} is odd")